"""Research-only K-best multi-route reinterpretation using authentic C4 D5 native C4M.
Do not mutate graph, do not treat candidate as WORLD. No test strings embedded in inference.
Comparators: native single MAP tags; K-best alternative tag-paths then D5 learned graph links.
No extra training, no oracle labels used at inference."""
import sys,json,hashlib,time,os
from pathlib import Path
R=Path(__file__).resolve().parent
D=Path(os.environ.get('C4_D6_DIR','/mnt/data/c4_replay_d6_lab'))
sys.path.insert(0,str(D/'native_runtime'))
from c4child.checkpoint import load_c4m_compact
from c4child.d3_scoped import ScopedLearner,decode,TAGS
from c4child.d2_relational import features
from c4child.d5_graph_attachment import GraphEdgeAttachment
from c4child.d2_grounder import tokenize

D5=D/'inputs'/'d5'/'C4_D5_LEARNED_EDGE_RESEARCH_ONLY.c4m'
g,_,_=load_c4m_compact(D5,hydrate_cold=True);learner=ScopedLearner(g);learner.load();attach=GraphEdgeAttachment(g);attach.load()
w=learner.weights

def kbest_tags(words,k):
    # Viterbi k-best per ending tag; no gold answer/filter, no lexical rules.
    layer={None:[(0.0,())]}
    for i in range(len(words)):
        feat=features(words,i);nxt={}
        emissions={tag:sum(w.get(('emit',tag,f),0.0) for f in feat) for tag in TAGS}
        for tag in TAGS:
            vals=[]
            for prev, choices in layer.items():
                if tag.startswith('I-') and prev not in (tag,'B-'+tag[2:]):continue
                bias=w.get(('trans',prev,tag),0.0)+emissions[tag]
                vals.extend((score+bias,seq+(tag,)) for score,seq in choices)
            if vals:nxt[tag]=sorted(vals,key=lambda x:x[0],reverse=True)[:k]
        layer=nxt
    all_=sorted([x for q in layer.values() for x in q],key=lambda x:x[0],reverse=True)
    return all_[:k]

def infer(text,k,route='tag_rank'):
    tokens=tokenize(text)
    if not tokens:return {'status':'ABSTAIN','ast':None}
    rows=kbest_tags(tokens,k)
    candidates=[]
    for rank,(tag_score,tagseq) in enumerate(rows):
        p=attach.parse(text,list(tagseq))
        if p.get('status')=='CANDIDATE':candidates.append({'ast':p['ast'],'rank':rank,'score':tag_score,'tags':tagseq})
    if not candidates:return {'status':'ABSTAIN','ast':None,'considered':len(rows),'candidate_count':0}
    # First valid hypothesis ordered by learned tag log-score. No gold used.
    best=candidates[0]
    return {'status':'CANDIDATE','ast':best['ast'],'rank':best['rank'],'considered':len(rows),'candidate_count':len(candidates)}

def run():
    cases=json.loads((D/'inputs'/'d3'/'D3_NEW_DEPTH_REATTACK_FROZEN.json').read_text(encoding='utf8'))['reversed_role_order']
    manu=json.loads((D/'inputs'/'d5'/'D5_MANUAL_REATTACK_FROZEN.json').read_text(encoding='utf8'))
    sets={'old_reverse32':[(e['text'],e['ast']) for e in cases], 'manual10':manu['manually_authored_expected']}
    budget=[1,2,4,8,16,32]
    out={'scope':'REAL_C4M_MULTI_HYPOTHESIS_BEAM_NO_GOLD_INFERENCE','model_sha256':hashlib.sha256(D5.read_bytes()).hexdigest(),'facts':len(g.facts),'budgets':{},'examples':{},'warning':'Known historical heldouts; beam is not trained and first-valid is selection bias; new independent language competence NOT proved.'}
    for name,examples in sets.items():
        batch={}
        for k in budget:
            correct=0;abstain=0;revises=0;futures=[]
            for t,expected in examples:
                res=infer(t,k)
                correct+=res['ast']==expected
                abstain+=res['status']=='ABSTAIN'
                revises+=res.get('rank',0)>0
                futures.append({'input':t,'expected':expected,'actual':res})
            batch[str(k)]={'exact':correct,'total':len(examples),'abstain':abstain,'uses_alternative_tag_path':revises}
            if k in (1,8,32):out['examples'][name+'_'+str(k)]=futures
        out['budgets'][name]=batch
    ood=manu['unsupported'];out['ood']={str(k):{'false_candidates':sum(infer(t,k)['status']=='CANDIDATE' for t in ood),'total':len(ood)} for k in budget}
    (R/'D7_NATIVE_KBEST_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps({'budgets':out['budgets'],'ood':out['ood']},ensure_ascii=False,indent=2))
if __name__=='__main__':run()