"""Additional simulated structural learning; NEVER world-grounded."""
import hashlib, json, random, sys
from pathlib import Path
base=Path(__file__).resolve().parent
sys.path.insert(0,str(base/'candidate/runtime'))
from c4child.runtime import C4LivingRuntime
old=base/'candidate/model/child_g324_p3_simulation_learned_candidate.c4m'
new=base/'candidate/model/child_g325_p0_hardened_plus_simulation_learned_candidate.c4m'
rt=C4LivingRuntime.open(str(old),store='memory')
rt.enable_hardened_truth()
g=rt.dialogue.g;initial=(len(g.entities),len(g.facts),g.order)
features=('a','b','c','d')
def context(x):return (x['a']^x['b']) if x['c']==0 else (x['a']&x['b'])
def lag(x):return x['a']^x['b'] # a previous observation and b current observation
# Four-way interaction; learner can choose 4 parents using same general search.
def composite(x):return (x['a']&x['b']) | (x['c']&x['d'])
specs=[('CONTEXT_SWITCH',context,840),('LAGGED_TRANSITION',lag,480),('FOUR_WAY_INTEGRATION',composite,1040)]
report={'status':'EXPERIMENTAL_SIMULATION_ONLY','old_model_sha':hashlib.sha256(old.read_bytes()).hexdigest(),
        'experiments':{},'extra_episodes':0,'source':'G324_P3'}
for i,(name,fn,n) in enumerate(specs):
    key='sim_p4_'+name
    rt.begin_causal_study(key,features,frame='SYNTHETIC_ENV',epoch='P4_CONTEXT_2026_10_08',max_parents=4 if name=='FOUR_WAY_INTEGRATION' else 3)
    rng=random.Random(157+i)
    for j in range(n):
        sample={f:rng.randrange(2) for f in features}
        z=rt.learn_simulated_constraint(key,sample,int(fn(sample)),
            root=f'{key}:observed:{j}',receipt=f'simulator:{key}:{j}')
        assert z['status']=='LEARNABLE'
    fit=rt.fit_causal_study(key)
    assert fit['status']=='LEARNED_ASSOCIATION',fit
    evals=[]
    # Train/test episodes disjoint; deliberately shift held-out feature distributions.
    for holdseed in range(2):
        rg=random.Random(8900+i*2+holdseed)
        hits=0;cov=0;total=400
        for k in range(total):
            x={f:rg.randrange(2) for f in features}
            if holdseed==1:x['c']=int(rg.random()>.83)
            p=rt.predict_causal_study(key,x)
            if p['status']=='CANDIDATE':
                cov+=1;hits+=int(int(p['p1']>.5)==int(fn(x)))
        evals.append({'seed':holdseed,'evaluated':total,'coverage':cov/total,'accuracy_when_answered':hits/max(1,cov)})
    report['experiments'][key]={'fit':fit,'heldout':evals,'training_events':n}
    report['extra_episodes']+=n
assert (len(g.entities),len(g.facts),g.order)==initial
rt.save(str(new))
cold=C4LivingRuntime.open(str(new),store='memory')
assert cold.dialogue.g.hardened_gate and cold.epistemic.strict_world
assert (len(cold.dialogue.g.entities),len(cold.dialogue.g.facts),cold.dialogue.g.order)==initial
for name,fn,n in specs:
    key='sim_p4_'+name
    assert cold.causal_studies[key].parents==rt.causal_studies[key].parents
    for bits in range(16):
        x={f:(bits>>k)&1 for k,f in enumerate(features)}
        pred=cold.predict_causal_study(key,x)
        assert pred['status']=='CANDIDATE' and int(pred['p1']>.5)==int(fn(x)),(name,bits,pred)
report['graph_before_after']=initial
report['cold_reload']=True
report['model_sha256']=hashlib.sha256(new.read_bytes()).hexdigest()
report['model_bytes']=new.stat().st_size
(base/'TRAINED_P4_RESULTS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,default=list))
print(json.dumps({k:v for k,v in report.items() if k!='experiments'},ensure_ascii=False,indent=2))
for k,v in report['experiments'].items():print(k,'parents=',v['fit']['parents'],'heldout=',v['heldout'])