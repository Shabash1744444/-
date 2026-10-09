from pathlib import Path
import json,hashlib
from multipath_native import infer
R=Path(__file__).resolve().parent
p=R/'D7_FRESH_ADVERSARIAL_FROZEN.json'; dataset=json.loads(p.read_text())
report={'dataset_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scientific_status':'assistant-authored unseen after hypothesis design, frozen before evaluation; NOT independent human study','summary':{},'cases':{}}
for k in (1,2,4,8,16,32):
    pos=[{'text':e['text'],'expected':e['ast'],'got':infer(e['text'],k)} for e in dataset['parse_positive']]
    neg=[{'text':e,'got':infer(e,k)} for e in dataset['should_abstain']]
    report['summary'][str(k)]={'positive_exact':sum(x['got']['ast']==x['expected'] for x in pos),'positive_total':len(pos),'negative_false_candidates':sum(x['got']['status']=='CANDIDATE' for x in neg),'negative_total':len(neg)}
    report['cases'][str(k)]={'positive':pos,'negative':neg}
(R/'D7_FRESH_REATTACK_RESULTS.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
print(json.dumps(report['summary'],indent=2,ensure_ascii=False))