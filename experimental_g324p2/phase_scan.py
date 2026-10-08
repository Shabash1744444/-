import sys,json,hashlib,statistics
from dataclasses import replace
from math import log
from random import Random
from pathlib import Path
sys.path.insert(0,'/mnt/data/c4_g324p2/candidate/runtime')
from c4child.adaptive_bifurcation import *

outdir=Path('/mnt/data/c4_g324p2')
def init(seed, n=12):
    r=Random(seed)
    vals=tuple(.05+.9*r.random() for _ in range(n))
    return DynamicState(0,vals,frozenset((i,i+1) for i in range(n-1)))
def summary(history):
    window=history[-100:]
    return dict(churn=sum(bool(s.removed or s.added) for s in window),
                distinct_graphs=len({s.state.edges for s in window}),
                edges_last=len(history[-1].state.edges),
                components_last=len(history[-1].new_components),
                macro_span=max(s.macro_after for s in window)-min(s.macro_after for s in window))

r_values=[2.9,3.2,3.5,3.56,3.65,3.8]
feedback_variants={'none':(0.0,0.0),'meso_global':(.16,.02),'strong':(.30,.06)}
probes=[]
for rv in r_values:
    for name,(beta,gamma) in feedback_variants.items():
        samples=[]
        for seed in range(8):
            cfg=DynamicsConfig(r=rv, component_feedback=beta,global_feedback=gamma,
                        perturbation=tuple(((i%5)-2)*.008 for i in range(12)))
            samples.append(summary(run(init(seed+20261008),cfg,420)))
        row={'r':rv,'feedback':name,'mean_churn_last100':round(statistics.mean(v['churn'] for v in samples),3),
             'min_churn':min(v['churn'] for v in samples),'max_churn':max(v['churn'] for v in samples),
             'mean_graph_states':round(statistics.mean(v['distinct_graphs'] for v in samples),3),
             'mean_final_components':round(statistics.mean(v['components_last'] for v in samples),3),
             'mean_edges':round(statistics.mean(v['edges_last'] for v in samples),3),
             'max_macro_span':round(max(v['macro_span'] for v in samples),6)}
        probes.append(row)
logistic=[]
for rv in r_values:
    s=logistic_series(rv,burn=2000,keep=1400)
    lyap=sum(log(max(1e-15,abs(rv*(1-2*x)))) for x in s)/len(s)
    logistic.append(dict(r=rv,period=period_bound(s[-256:]),lyapunov=round(lyap,5)))

# The simplest possible nonlocal test: a single leaf perturbation influences
# non-neighbor leaves through global-mean recursion but not when removed.
start=DynamicState(0,(.20,.35,.70,.90),frozenset())
perturbed=DynamicState(0,(.21,.35,.70,.90),frozenset())
cfg=DynamicsConfig(r=3.2,neighbor_coupling=0,component_feedback=.15,global_feedback=.3,rewire=False)
leaf_effect=(update(perturbed,cfg).state.x[3]-update(start,cfg).state.x[3])
without_effect=(update(perturbed,replace(cfg,top_down=False)).state.x[3]-update(start,replace(cfg,top_down=False)).state.x[3])

result={
 'experiment':'C4_G324_P2_ADAPTIVE_GRAPH_BIFURCATION',
 'date':'2026-10-08', 'scope':'SIMULATION_ONLY',
 'parent':'G324-P1 candidate derived from G322-P8 model; no trained weights changed',
 'model_baseline_sha256':'6baf2864ce8a811738d13cf3593f739e8dcc5a8734d17ce0f5647bc23da06301',
 'method':'toy deterministic coupled logistic node maps + local rewiring with hysteresis + two levels of coarse-grained top-down feedback',
 'frozen_cases':len(r_values),'seeds_per_setting':8,'regimes':probes,'logistic_control':logistic,
 'nonlocal_leaf_effect':round(leaf_effect,9),'nonlocal_without_macro':round(without_effect,9),
 'statistical_note':'8 initializations per setting are an exploratory sensitivity scan; no parameter fitting or inferential statistics; do not generalize to all adaptive graphs',
 'negative_findings':['P2 is not a fractal dimension test', 'logistic period doubling is textbook known, not emergent from C4', 'threshold rewiring is not by itself a mathematically proven topology bifurcation', 'no perceptual learning, general intelligence or 54 cognitive effect reproduction', 'the existing G322 false WORLD admission was not touched']
}
(outdir/'G324_P2_PHASE_SCAN_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
for z in logistic: print('logistic',z)
for z in probes: print('network',z['r'],z['feedback'],'churn',z['mean_churn_last100'],'graphs',z['mean_graph_states'],'finalcomponents',z['mean_final_components'])
print('nonlocal',leaf_effect,without_effect)

# One chart per concept (no subplots and default styles/colors).
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
param_points=[2.85+i*(3.86-2.85)/299 for i in range(300)]
xx=[]; yy=[]
for p in param_points:
    vs=logistic_series(p,burn=850,keep=55)
    xx.extend([p]*len(vs)); yy.extend(vs)
fig,ax=plt.subplots(figsize=(9,5))
ax.scatter(xx,yy,s=.06,alpha=.45)
ax.set(xlabel='r (nonlinear map control)',ylabel='long-run x',title='Reference logistic-map period-doubling (NOT C4 emergence)')
fig.tight_layout();fig.savefig(outdir/'G324_P2_LOGISTIC_BIFURCATION.png',dpi=160);plt.close(fig)
fig,ax=plt.subplots(figsize=(9,5))
for name in feedback_variants:
    subset=[x for x in probes if x['feedback']==name]
    ax.plot([x['r'] for x in subset],[x['mean_churn_last100'] for x in subset],marker='o',label=name)
ax.set(xlabel='r',ylabel='topology-changing updates (last 100 steps, mean of 8 seeds)',title='Adaptive topology turnover vs nonlinear control and feedback')
ax.legend();fig.tight_layout();fig.savefig(outdir/'G324_P2_TOPOLOGY_PHASE_SCAN.png',dpi=160);plt.close(fig)
print('outputs',[(p.name,p.stat().st_size) for p in outdir.glob('G324_P2_*.png')])