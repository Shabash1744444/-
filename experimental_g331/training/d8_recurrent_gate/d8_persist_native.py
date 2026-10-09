"""Save trained D8 logit gate scalars as STRICT LANGUAGE_CONVENTION facts in real native C4Graph.
Original source .c4m is untouched. Reader accepts only exact D8 root and relation.
"""
from pathlib import Path
import sys,json,hashlib
from dataclasses import asdict
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'native_runtime'))
from c4child.checkpoint import load_c4m_compact,save_c4m_compact
from c4child.bootstrap import BootstrapTeacher
from c4child.scope import LANGUAGE_CONVENTION,fact_scope
PARENT=ROOT/'inputs'/'prior_d6'/'inputs'/'d5'/'C4_D5_LEARNED_EDGE_RESEARCH_ONLY.c4m'
CANDIDATE=ROOT/'C4_D8_LEARNED_CRITIC_NONCANONICAL.c4m'
PARAMS=ROOT/'D8_FROZEN_CRITIC_WEIGHTS.json'
REL='D8_CRITIC_WEIGHT'
TEACHER='curated:assistant-teacher:c4-d8-critic-2026-10-09'
assert hashlib.sha256(PARENT.read_bytes()).hexdigest()=='b7b2dd0f826bbc217f2a5499e53ba554a61c415817fe5d1f2c5313f2caa81036'

class C4NativeLearnedCritic:
    def __init__(self,graph):
        self.graph=graph;self.params=None
    def load(self):
        s={}
        for f in self.graph.facts.values():
            if f.relation!=REL or f.status!='ADMITTED' or f.source_group!=TEACHER or f.origin!='EXTERNAL_CORPUS' or f.authority!='TEACHER' or fact_scope(self.graph,f)!=LANGUAGE_CONVENTION:continue
            ent=self.graph.entities.get(f.subject)
            if ent and ent.label.startswith('d8critic|'):
                s[ent.label[len('d8critic|'):]]=float(f.object_value)
        self.params=s
        if set(s)!={f'{key}:{i}' for key in ('coef','mean','scale') for i in range(16)}|{'intercept','threshold'}:raise ValueError('Incomplete learned native critic')
        return self
    def prob(self,x):
        import math
        assert len(x)==16
        z=self.params['intercept']+sum(self.params[f'coef:{i}']*(v-self.params[f'mean:{i}'])/self.params[f'scale:{i}'] for i,v in enumerate(x))
        return 1/(1+math.exp(-z))
    def predict(self,candidates):
        if not candidates:return {'status':'ABSTAIN','ast':None}
        scores=[self.prob(c['features']) for c in candidates];k=max(range(len(scores)),key=lambda i:scores[i]);p=scores[k]
        if p<self.params['threshold']:return {'status':'ABSTAIN','ast':None,'confidence':p}
        return {'status':'CANDIDATE','ast':candidates[k]['ast'],'confidence':p}

def save():
    spec=json.loads(PARAMS.read_text())
    g,h,_=load_c4m_compact(PARENT,hydrate_cold=True)
    old={i:asdict(f) for i,f in g.facts.items()}
    scores={'intercept':spec['intercept'],'threshold':spec['threshold']}
    for name in ('coef','scale','mean'):
        for i,v in enumerate(spec[name]):scores[f'{name}:{i}']=v
    events=[]
    for i,(k,v) in enumerate(sorted(scores.items())):
        events.append({'schema':'C4_BOOTSTRAP_EVENT_V0.1','event_id':f'c4-d8critic:{i:05d}',
            'origin':'EXTERNAL_CORPUS','source_group':TEACHER,'authority':'TEACHER',
            'scope':{'principal':'USER','privacy':'LOCAL'},'constitutional_basis':'LANGUAGE_CONVENTION',
            'payload':{'kind':'CLAIM','subject':'d8critic|'+k,'relation':REL,'object':repr(float(v)),'object_kind':'literal'}})
    result=BootstrapTeacher(g).ingest(events)
    assert result.rejected==0 and result.admitted==len(events),(result,len(events))
    assert all(asdict(g.facts[k])==v for k,v in old.items())
    new=[f for k,f in g.facts.items() if k not in old]
    assert all(fact_scope(g,f)==LANGUAGE_CONVENTION and f.status=='ADMITTED' for f in new)
    save_c4m_compact(CANDIDATE,g,h,meta={'experimental_only':True,'parent_sha256':spec['model_sha256'],
        'critic_is_NOT_native_live_chat':True,'training_dependency':'single synthetic instructor family'})
    g2,_,_=load_c4m_compact(CANDIDATE,hydrate_cold=True)
    assert len(g2.facts)==len(old)+len(events)
    assert all(asdict(g2.facts[k])==v for k,v in old.items())
    reader=C4NativeLearnedCritic(g2).load()
    for k,v in scores.items():
        assert reader.params[k]==v,k
    report={'parent_sha256':hashlib.sha256(PARENT.read_bytes()).hexdigest(),'new_sha256':hashlib.sha256(CANDIDATE.read_bytes()).hexdigest(),
        'model_bytes':CANDIDATE.stat().st_size,'old_fact_count':len(old),'new_fact_count':len(g2.facts),
        'new_critic_weight_fact_count':len(events),'source_scoped_as_LANGUAGE_CONVENTION':True,
        'original_facts_unchanged':True,'critics_legacy_D5_weights_present':True,
        'root':TEACHER,'independence_note':'One dependent teacher-synthetic body, not independent evidence'}
    (ROOT/'D8_NATIVE_COLD_CHECK.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':save()