"""D6 micro-demonstration: learned scalar iterative event-graph propagation.
Separate toy scratch graph (NOT proof of native C4 language/AGI).
No phrase keys or access to labels during inference. Graph topology externally given.
"""
import json,random,hashlib
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent

def sample(rng,n=14):
    # directed (time-like) acyclic graph; no fixed chain, random cross-links and distractors
    a=np.zeros((n,n),dtype=np.float64)
    for i in range(n):
        for j in range(i+1,n):
            if rng.random()<0.13:a[i,j]=1.
    s=rng.randrange(n-3)
    # one anchored source, with at least one 4-hop relation spanning previous events
    if n-s>=5 and rng.random()<.85:
        path=rng.sample(list(range(s+1,n)),4)
        path.sort();v=s
        for j in path:a[v,j]=1;v=j
    return a,s

def gold(a,start,hops):
    support=np.zeros(len(a));support[start]=1
    for k in range(hops):
        support=np.maximum(support,(a.T@support)>0)
    return support.astype(int)

def infer(a,start,w,hops):
    # generic shared operator with a *learned* scalar message transmission strength.
    v=np.zeros(len(a));v[start]=1.
    for k in range(hops):v=np.clip(np.maximum(v,w*(a.T@v)),0,1)
    return (v>.5).astype(int)

def main():
    # training only one-step direct neighbors, no multi-hop supervision; unique random seed
    rg=random.Random(3301)
    train=[sample(rg) for _ in range(60)]
    # Estimate message strength by a 1D least squares fit to the first-hop edge states.
    numer=denom=0.
    for a,s in train:
        v=np.zeros(len(a));v[s]=1.
        X=a.T@v
        y=gold(a,s,1)-v
        numer+=float(X@y);denom+=float(X@X)
    w=numer/denom
    # Frozen, untouched test random seed different from training; target is 4-hop.
    te=random.Random(9027)
    tests=[sample(te) for _ in range(200)]
    rows=[]
    for k in (0,1,2,3,4,5,10,30,100):
        # FIXED QUESTION: Can the model recover all nodes reachable in <=4 hops?
        exact=sum(np.array_equal(infer(a,s,w,k),gold(a,s,4)) for a,s in tests)
        tp=fp=fn=0
        for a,s in tests:
            pr=infer(a,s,w,k);go=gold(a,s,4)
            tp+=int(np.sum((pr==1)&(go==1)))
            fp+=int(np.sum((pr==1)&(go==0)))
            fn+=int(np.sum((pr==0)&(go==1)))
        precision=tp/max(tp+fp,1);recall=tp/max(tp+fn,1)
        rows.append({'passes':k,'graph_exact':exact,'n_graphs':len(tests),'precision':round(precision,3),'recall':round(recall,3)})
    out={'type':'separate toy learned graph message propagation; NOT native C4 learner','trained_scalar_weight':float(w),
         'train_one_step_graphs':len(train),'test_different_graphs':len(tests),'target':'which nodes reachable in <=4 steps',
         'rows':rows,'source':'synthetic independent generated DAG; graph edge topology is GIVEN, NOT inferred from text',
         'important_limit':'The propagation formula is a hand-provided universal inductive bias; it proves only that iteration can compose supplied edges, not that C4 has learned language, graph topology, or biological cognition.'}
    (R/'D6_ITERATIVE_GRAPH_MICRO_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()