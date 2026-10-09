"""Frozen D8 native C4M critic K=1..32; no fitting/tuning after D8 exam."""
from pathlib import Path
import sys,json,hashlib,time
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R))
import d8_persist_native as mod
import d8_gate as gate
from c4child.checkpoint import load_c4m_compact
f=R/'D8_FROZEN_EXAM.json'
assert hashlib.sha256(f.read_bytes()).hexdigest()==gate.REQUIRED_SHA
exam=json.loads(f.read_text());rows=[{'kind':'positive',**e} for e in exam['positive']]+[{'kind':'negative','text':t} for t in exam['negative']]
g,_,_=load_c4m_compact(mod.CANDIDATE,hydrate_cold=True)
critic=mod.C4NativeLearnedCritic(g).load()
report={'native_c4m_sha256':hashlib.sha256(mod.CANDIDATE.read_bytes()).hexdigest(),'exam_sha256':gate.REQUIRED_SHA,'runs':{}}
for k in (1,2,4,8,16,32):
    pred=[];elapsed=time.perf_counter()
    for e in rows:
        rs=critic.predict(gate.vectors(e['text'],k))
        pred.append({'text':e['text'],'kind':e['kind'],'expected':e.get('ast'),'predicted':rs['ast'],
            'accepted':rs['ast'] is not None,'correct':e['kind']=='positive' and rs['ast']==e.get('ast'),
            'false_accept':e['kind']=='negative' and rs['ast'] is not None})
    report['runs'][str(k)]={**gate.stat(pred),'seconds':round(time.perf_counter()-elapsed,4)}
(R/'D8_CRITIC_BUDGET_RESULTS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report['runs'],ensure_ascii=False,indent=2))