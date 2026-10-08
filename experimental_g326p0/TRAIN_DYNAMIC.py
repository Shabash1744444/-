"""G326 experimental finite learned dynamics from *generated simulator trajectories*.

All experience is SIMULATION; preserves old graph; no WORLD evidence.
"""
import random,sys,json,hashlib
from pathlib import Path
import statistics
base=Path(__file__).resolve().parent
sys.path.insert(0,str(base/'candidate/runtime'))
from c4child.runtime import C4LivingRuntime
from c4child.adaptive_bifurcation import DynamicState,DynamicsConfig,update

src=base/'candidate/model/child_g325_p0_hardened_plus_simulation_learned_candidate.c4m'
dst=base/'candidate/model/child_g326_p0_unified_pre_live_candidate.c4m'
rt=C4LivingRuntime.open(str(src),store='memory')
assert rt.dialogue.g.hardened_gate and rt.epistemic.strict_world
initial=(len(rt.dialogue.g.entities),len(rt.dialogue.g.facts),rt.dialogue.g.order)
key='sim_g326_ADAPTIVE_GRAPH_EDGE_TRANSITION'
features=('old_edge','local_close','local_far','macro_high','r_high','feedback_high')
rt.begin_causal_study(key,features,frame='ADAPTIVE_GRAPH_SIM',epoch='G326_PRELIVE',max_parents=4)

def sample(seed,num_states):
 rng=random.Random(seed)
 for epi in range(num_states):
  n=8;x=tuple(rng.uniform(0.02,0.98) for _ in range(n))
  edges=frozenset((i,j) for i in range(n) for j in range(i+1,n) if rng.random()<.24)
  cfg=DynamicsConfig(r=rng.choice([2.95,3.2,3.55,3.7,3.85]),
                     neighbor_coupling=.08,component_feedback=rng.choice([0.,.12,.26]),
                     global_feedback=rng.choice([0.,.03]),link_on=.045,link_off=.085,top_down=True)
  state=DynamicState(0,x,edges)
  for t in range(3):
   nxt=update(state,cfg).state
   for a in range(n):
    for b in range(a+1,n):
     old=int((a,b) in state.edges)
     distance=abs(state.x[a]-state.x[b])
     feat={'old_edge':old,'local_close':int(distance<.15),
           'local_far':int(distance>.40),'macro_high':int((sum(state.x)/n)>.52),
           'r_high':int(cfg.r>3.5),'feedback_high':int(cfg.component_feedback>.15)}
     out=int((a,b) in nxt.edges)
     yield epi,t,a,b,feat,out
   state=nxt

n=0
for epi,t,a,b,x,out in sample(546,90):
 status=rt.learn_simulated_constraint(key,x,out,root=f'G326:train:{epi}:{t}:{a}-{b}',receipt=f'SIM:{epi}:{t}')
 assert status['status']=='LEARNABLE',status
 n+=1
fit=rt.fit_causal_study(key)
assert fit['status']=='LEARNED_ASSOCIATION',fit

def heldout(seed,epi_count):
 hits=cov=0;baselines=[];observed=[];briers=[]
 for epi,t,a,b,x,out in sample(seed,epi_count):
  p=rt.predict_causal_study(key,x)
  observed.append(out)
  if p['status']=='CANDIDATE':
   cov+=1;hits+=int((p['p1']>=.5)==bool(out));briers.append((p['p1']-out)**2)
 baseline=max(sum(observed),len(observed)-sum(observed))/len(observed)
 return {'total':len(observed),'answered':cov,'coverage':cov/len(observed),
         'accuracy_answered':hits/max(1,cov),'majority_baseline_accuracy':baseline,
         'brier_answered':statistics.fmean(briers) if briers else None,
         'label_positive_fraction':sum(observed)/len(observed)}

held=[heldout(767,40),heldout(881,40),heldout(991,40)]
rt.save(str(dst))
cold=C4LivingRuntime.open(str(dst),store='memory')
assert len(cold.causal_studies)==len(rt.causal_studies)
assert cold.causal_studies[key].parents==rt.causal_studies[key].parents
assert cold.dialogue.g.hardened_gate and cold.epistemic.strict_world
assert (len(cold.dialogue.g.entities),len(cold.dialogue.g.facts),cold.dialogue.g.order)==initial
p1=rt.predict_causal_study(key,dict(zip(features,(1,0,0,1,0,1))))
p2=cold.predict_causal_study(key,dict(zip(features,(1,0,0,1,0,1))))
assert p1==p2
out={'status':'SIMULATION_ONLY','parent_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
     'trained_model_sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'trained_model_bytes':dst.stat().st_size,
     'train_events':n,'fit':fit,'heldout':held,'original_graph_counts':initial,
     'cold_reload':True,'model_scoped':'SIMULATION','study_count':len(cold.causal_studies)}
(base/'DYNAMIC_HELDOUT_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,default=list))
print(json.dumps(out,ensure_ascii=False,indent=2,default=list))