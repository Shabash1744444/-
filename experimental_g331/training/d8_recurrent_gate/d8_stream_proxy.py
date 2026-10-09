"""D8 proxy experiment: constant-sized decaying recurrent state vs growing episodic store.
This IS NOT Mamba/RWKV and is NOT current C4 native speech learning.
Same stream and queries presented to both; episodes immutable and retrievable by ID.
"""
from __future__ import annotations
import numpy as np,json,time,math
from pathlib import Path
R=Path(__file__).resolve().parent
NUM_KEYS=24; NUM_VALUES=8
TRAIN_SEEDS=(201,202,203,204)
TEST_SEEDS=(901,902,903,904,905)
NSET=(40,300,3000)
ALPHAS=(0.6,0.8,0.9,0.95,0.97,0.98,0.99,0.995,0.998,0.999)

def stream(seed,n):
    rng=np.random.default_rng(seed)
    # Realistic collisions/overwrites: each recurring topic may change asserted value.
    keys=rng.integers(NUM_KEYS,size=n)
    vals=rng.integers(NUM_VALUES,size=n)
    return keys,vals

def recurrent(keys,vals,alpha):
    W=np.zeros((NUM_KEYS,NUM_VALUES),dtype=np.float64)
    recent={}
    for k,v in zip(keys,vals):
        W*=alpha
        W[int(k),int(v)]+=1
        recent[int(k)]=int(v)
    return W,recent

def latest_accuracy(W,recent):
    return sum(int(np.argmax(W[k])==v) for k,v in recent.items()),len(recent)

def earliest_at_id_accuracy(W,keys,vals,positions):
    return sum(int(np.argmax(W[keys[i]])==vals[i]) for i in positions),len(positions)

def episode_memory(keys,vals):
    # One entry per source event. Exact event-ID search, NOT semantic retrieval.
    return [(int(k),int(v)) for k,v in zip(keys,vals)]

def select_positions(n):
    # time-scoped queries that request the historical version of an assertion
    return sorted(set([0,1,2,n//5,n//2,3*n//4,n-10,n-1]))

def alpha_train():
    scored=[]
    for a in ALPHAS:
        tot=0;den=0
        for s in TRAIN_SEEDS:
            keys,vals=stream(s,40)
            w,recent=recurrent(keys,vals,a)
            ok,sz=latest_accuracy(w,recent)
            tot+=ok;den+=sz
        scored.append({'alpha':a,'latest_accuracy':tot/den})
    # choose by latest score only, tie break favor lower alpha (faster current adjustment)
    best=max(scored,key=lambda x:(x['latest_accuracy'],-x['alpha']))
    return best['alpha'],scored

def main():
    alpha,tune=alpha_train()
    out={'scope':'SEPARATE_MATH_PROXY_NOT_MAMBA_NOT_RWKV_NOT_C4M','selected_alpha_short_train':alpha,
         'alpha_grid_train_only':tune,'results':{},'seeds':TEST_SEEDS,
         'retrieval_type':'explicit event ID; exact storage+lookup is not autonomous semantic understanding',
         'source_provenance':'event index fully identifies original episode; no WORLD verification by recall'}
    for n in NSET:
        rows=[]
        for s in TEST_SEEDS:
            keys,vals=stream(s,n)
            t0=time.perf_counter(); W,recent=recurrent(keys,vals,alpha);step_seconds=time.perf_counter()-t0
            pos=select_positions(n)
            fok,ft=latest_accuracy(W,recent)
            oldok,oldt=earliest_at_id_accuracy(W,keys,vals,pos)
            em=episode_memory(keys,vals)
            exact_historical=sum(int(em[i][1]==vals[i]) for i in pos)
            exact_latest=sum(int(next(v for k,v in reversed(em) if k==key)==recent[key]) for key in recent)
            assert exact_historical==len(pos) and exact_latest==len(recent)
            rows.append({'seed':s,'events':n,'fast_latest_correct':fok,'fast_latest_total':ft,
                'fast_history_by_event_id_correct':oldok,'fast_history_total':oldt,
                'episodic_exact_historical_correct':exact_historical,'episodic_latest_correct':exact_latest,
                'recurrence_seconds':step_seconds,'episode_memory_records':len(em),
                'fast_state_scalar_count':W.size,'fast_state_bytes':W.nbytes,
                'episode_min_payload_bytes':len(em)*2*8})
        out['results'][str(n)]={'runs':rows,'mean_fast_latest_accuracy':float(np.mean([r['fast_latest_correct']/r['fast_latest_total'] for r in rows])),
            'mean_fast_history_accuracy':float(np.mean([r['fast_history_by_event_id_correct']/r['fast_history_total'] for r in rows])),
            'mean_episodic_historical_accuracy':1.0,'mean_episodic_latest_accuracy':1.0}
    # Decay of one-time memory trace as token/events flow in, if no refresh for that key.
    out['trace_decay_without_rehearsal']={str(d):alpha**d for d in (30,300,3000)}
    (R/'D8_RECURRENT_PROXY_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps({'trained_alpha':alpha,'scores':{k:{z:v for z,v in data.items() if z!='runs'} for k,data in out['results'].items()},'trace_decay':out['trace_decay_without_rehearsal']},ensure_ascii=False,indent=2))

if __name__=='__main__':main()