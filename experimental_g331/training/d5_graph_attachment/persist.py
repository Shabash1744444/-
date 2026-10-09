"""Persist actual learned pairwise graph-edge weights INSIDE original native C4Graph copy."""
import json,hashlib,sys,os
from dataclasses import asdict
from pathlib import Path
L=Path(__file__).parent;sys.path.insert(0,str(L/'native_runtime'))
import c4child  # Pin native experimental package before importing analysis tools.
from logistic import Model
from experiment import write_json
from c4child.d5_graph_attachment import GraphEdgeAttachment,ROOT,REL
from c4child.scope import LANGUAGE_CONVENTION,fact_scope
from c4child.checkpoint import load_c4m_compact,save_c4m_compact
from c4child.bootstrap import BootstrapTeacher
from c4child.d3_scoped import decode,train_weights,ScopedLearner
from c4child.d2_grounder import tokenize

src=Path('/mnt/data/c4_decisive_lab/original/C4_D2_P2C_RELBINDER_NEGATION_CANDIDATE.c4m');assert hashlib.sha256(src.read_bytes()).hexdigest()=='36e9fb9c54691d1ba7a0625e88d65d85017d60d4e4a021d320ecbd8a064ee385'
train=json.loads((L/'D5_TRAIN.json').read_text()); test=json.loads((L/'D5_HOLDOUT_FROZEN.json').read_text())['generated'];clf=Model(train);tw=train_weights(train,4)

g,handle,_=load_c4m_compact(src,hydrate_cold=True);old={k:asdict(f) for k,f in g.facts.items()}
# A cold C4M must own BOTH learned token tags and learned graph attachments.
tag_info=ScopedLearner.train(g,train,epochs=4)
assert tag_info['parameter_facts']>0
weights=[]
for rel,(vectorizer,model) in clf.r.items():
  weights.append((rel,'__intercept__',float(model.intercept_[0])))
  for key,number in zip(vectorizer.get_feature_names_out(),model.coef_[0]):
    if number:weights.append((rel,str(key),float(number)))
records=[]
for i,(rel,key,val) in enumerate(sorted(weights)):
  records.append({'schema':'C4_BOOTSTRAP_EVENT_V0.1','event_id':f'c4-d5edge:{i:06d}','origin':'EXTERNAL_CORPUS','source_group':ROOT,'authority':'TEACHER','scope':{'principal':'USER','privacy':'LOCAL'},'constitutional_basis':'LANGUAGE_CONVENTION','payload':{'kind':'CLAIM','subject':f'd5edge|{rel}|{key}','relation':REL,'object':repr(val),'object_kind':'literal'}})
res=BootstrapTeacher(g).ingest(records)
print('TRAIN GRAPH',len(records),res,flush=True)
assert res.rejected==0 and res.admitted+res.dedup==len(records)
added=[f for k,f in g.facts.items() if k not in old]
assert len(added)==len(records)+tag_info['parameter_facts']
assert all(f.origin=='EXTERNAL_CORPUS' and f.authority=='TEACHER' and fact_scope(g,f)==LANGUAGE_CONVENTION and f.status=='ADMITTED' for f in added)
assert all(asdict(g.facts[k])==v for k,v in old.items())
filename=L/'C4_D5_LEARNED_EDGE_RESEARCH_ONLY.c4m';save_c4m_compact(filename,g,handle,meta={'research_only':True,'no_promotion':True,'D5_edge_inference_not_main_dialogue':True})
g2,handle2,_=load_c4m_compact(filename,hydrate_cold=True)
assert all(asdict(g2.facts[k])==v for k,v in old.items())
reader=GraphEdgeAttachment(g2)
tagreader=ScopedLearner(g2);tagreader.load();assert tagreader.weights is not None and len(tagreader.weights)>0

def test_one(ex,tags):
    x=reader.parse(ex['text'],tags)
    return x.get('ast')==ex['ast'] and x['status']=='CANDIDATE'
checks={}
for name,cases in test.items():
    oracle=sum(test_one(e,e['tags']) for e in cases)
    learned=sum(test_one(e,decode(tokenize(e['text']),tagreader.weights)) for e in cases)
    checks[name]={'oracle_tags_correct':oracle,'learned_tags_correct':learned,'total':len(cases)}
for name,v in checks.items():print('COLD',name,v,flush=True)
record={'original_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'new_sha256':hashlib.sha256(filename.read_bytes()).hexdigest(),'model_bytes':filename.stat().st_size,'parent_fact_count':len(old),'trained_weight_facts':len(added),'edge_facts':len(records),'tag_facts':tag_info['parameter_facts'],'cold_total_facts':len(g2.facts),'original_facts_all_identical':True,'teacher_roots':[ROOT,tag_info['root']],'roots_share_one_synthetic_teacher':True,'language_only':True,'scores':checks,'not_native_chat':True}
write_json(L/'D5_COLD_INTEGRITY.json',record)
print('MODEL',record,flush=True)