"""D8 exploratory confidence gate on genuine C4 D5 stored tag/edge weights.
Samples only from old historical data; frozen D8 exam isolated until after fitting.
No phrase/lexical answer lookup. Research critic weights live separately, NOT a C4M organ.
"""
from __future__ import annotations
import sys,os,json,math,hashlib,time,collections,copy
from pathlib import Path
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
R=Path(__file__).resolve().parent
D=R/'inputs'/'prior_d6'
os.environ['C4_D6_DIR']=str(D)
sys.path.insert(0,str(R/'prior_d7'))
import multipath_native as native
from c4child.d5_graph_attachment import make_nodes,aug
from c4child.d2_grounder import tokenize

MODEL= D/'inputs/d5/C4_D5_LEARNED_EDGE_RESEARCH_ONLY.c4m'
EXAM=R/'D8_FROZEN_EXAM.json'
REQUIRED_SHA='425a02fccf10cbbada79abf64c1a9baf9da8dd8f319792783c221a9026e55300'
FROZEN_SHA=hashlib.sha256(EXAM.read_bytes()).hexdigest()
assert FROZEN_SHA==REQUIRED_SHA, (FROZEN_SHA,'exam changed')
assert hashlib.sha256(MODEL.read_bytes()).hexdigest()=='b7b2dd0f826bbc217f2a5499e53ba554a61c415817fe5d1f2c5313f2caa81036'
PRE_FACTS=len(native.g.facts)

def ast_stats(ast):
    d=0;ops=0;negs=0;acc=ast
    while isinstance(acc,dict):
        d+=1
        typ=acc['op'];ops+=typ in ('SAY','BELIEF');negs+=typ=='NOT'
        acc=acc.get('arg')
    return d,ops,negs

def vectors(text,k):
    words=tokenize(text)
    rows=native.kbest_tags(words,k)
    if not rows:return []
    first=rows[0][0]
    all_=[]
    for rank,(tscore,tags) in enumerate(rows):
        result=native.attach.parse(text,list(tags))
        if result.get('status')!='CANDIDATE':continue
        ast=result['ast']
        ns=make_nodes(text,tags);nodes=aug(ns)
        ops=[n for n in ns if n['tag'].startswith('OP_')];heads=[n for n in ns if n['tag']=='HOLDER'];neg=[n for n in ns if n['tag']=='NEG']
        arc=[]
        for h,o in zip(sorted(heads,key=lambda n:n['pos']),sorted(ops,key=lambda n:n['pos'])):
            arc.append(native.attach.score(nodes,h['id'],o['id'],'HOLDER'))
        y=nodes[-1]['id']
        if ops:arc.append(native.attach.score(nodes,ops[-1]['id'],y,'ARG'))
        d,opn,negn=ast_stats(ast)
        n=max(1,len(words))
        vals=[
          tscore/n, (tscore-first)/n, math.log1p(rank),len(words),
          sum(t=='O' for t in tags)/n,
          sum(t.startswith('B-') for t in tags)/n,
          sum(t.startswith('I-') for t in tags)/n,
          len(ns),len(ops),len(heads),len(neg),d,opn,negn,
          float(np.mean(arc)) if arc else 0.,
          min(arc) if arc else 0.,
        ]
        all_.append({'ast':ast,'rank':rank,'tags_score':tscore,'features':vals})
    return all_

def datasets():
    d7=json.loads((R/'prior_d7'/'D7_FRESH_ADVERSARIAL_FROZEN.json').read_text())
    old=json.loads((D/'inputs/d5/D5_MANUAL_REATTACK_FROZEN.json').read_text())
    d3=json.loads((D/'inputs/d3/D3_NEW_DEPTH_REATTACK_FROZEN.json').read_text())
    train=[{'text':t,'ast':a,'kind':'positive'} for t,a in old['manually_authored_expected']]
    train +=[{'text':t,'kind':'negative'} for t in old['unsupported']]
    train +=[{'text':z['text'],'ast':z['ast'],'kind':'positive'} for z in d3['reversed_role_order']]
    val=[{'text':z['text'],'ast':z['ast'],'kind':'positive'} for z in d7['parse_positive']]
    val +=[{'text':t,'kind':'negative'} for t in d7['should_abstain']]
    return train,val

def feats(rows,k):
    xx=[];yy=[];groups=[];weights=[]
    for i,e in enumerate(rows):
        cs=vectors(e['text'],k)
        if not cs:continue
        for c in cs:
            xx.append(c['features'])
            yy.append(int(e['kind']=='positive' and c['ast']==e.get('ast')))
            groups.append(i)
            weights.append(1/max(1,len(cs)))
    return np.array(xx),np.array(yy),np.array(groups),np.array(weights)

def predict(rows,model,threshold,k):
    results=[]
    for e in rows:
        cs=vectors(e['text'],k)
        if cs:
            prob=model.predict_proba(np.asarray([c['features'] for c in cs]))[:,1]
            pick=int(np.argmax(prob));best=cs[pick];p=float(prob[pick])
            yes=p>=threshold
            predicted=best['ast'] if yes else None
        else:predicted=None; p=0.;pick=-1
        results.append({'text':e['text'],'predicted':predicted,'expected':e.get('ast'),
          'kind':e['kind'],'accepted':predicted is not None,'correct':e['kind']=='positive' and predicted==e.get('ast'),
          'false_accept':e['kind']=='negative' and predicted is not None,'max_probability':round(p,4),
          'selected_candidate':pick})
    return results

def naive(rows,k):
    r=[]
    for e in rows:
        v=native.infer(e['text'],k);ast=v.get('ast')
        r.append({'kind':e['kind'],'accepted':ast is not None,'correct':e['kind']=='positive' and ast==e.get('ast'),
                  'false_accept':e['kind']=='negative' and ast is not None,'text':e['text'],'ast':ast})
    return r

def stat(rows):
    pos=[x for x in rows if x['kind']=='positive'];neg=[x for x in rows if x['kind']=='negative']
    return {'positive_correct':sum(x['correct'] for x in pos),'positive_total':len(pos),'positive_accepted':sum(x['accepted'] for x in pos),
            'negative_false_candidate':sum(x['false_accept'] for x in neg),'negative_total':len(neg)}

def main():
    originalhash=hashlib.sha256(MODEL.read_bytes()).hexdigest()
    train,val=datasets()
    k=32
    X,y,group,sw=feats(train,k)
    assert set(y)=={0,1},collections.Counter(y)
    print('train candidates',len(y),'correct',sum(y),'train messages',len(train),'validation',len(val),flush=True)
    clf=make_pipeline(StandardScaler(),LogisticRegression(C=0.1,max_iter=2000,class_weight='balanced',random_state=17))
    clf.fit(X,y,logisticregression__sample_weight=sw)
    # Threshold tuned exclusively on OLD D7 data, not D8 exam. Predeclared objective:
    # expected utility = 3*true AST - 5*false OOD - 0.15*all accepted incorrect.
    validation={}
    chosen=None
    for th in (0.2,0.35,0.5,0.65,0.8,0.9,0.95,0.99):
        vr=predict(val,clf,th,k);st=stat(vr)
        utility=3*st['positive_correct']-5*st['negative_false_candidate']-0.15*(st['positive_accepted']-st['positive_correct'])
        validation[str(th)]={'score':round(utility,3),**st}
        if chosen is None or utility>chosen[0]:chosen=(utility,th)
    threshold=chosen[1]
    # Serialize frozen learned scalar parameters BEFORE first new-exam read. Native C4M writer will import this file, not train again.
    st=clf.named_steps['standardscaler']; lr=clf.named_steps['logisticregression']
    checkpoint={'schema':'C4_D8_CRITIC_SCALARS_V1','feature_order':'d8_gate.vectors.v1',
        'model_sha256':originalhash,'training_examples':len(train),'validation_examples':len(val),
        'threshold':float(threshold),'coef':[float(x) for x in lr.coef_[0]],
        'intercept':float(lr.intercept_[0]),'mean':[float(x) for x in st.mean_],
        'scale':[float(x) for x in st.scale_],'training_lineage':'one correlated synthetic/assistant annotation dataset; NOT independent evidence'}
    (R/'D8_FROZEN_CRITIC_WEIGHTS.json').write_text(json.dumps(checkpoint,ensure_ascii=False,indent=2),encoding='utf8')
    # Critic is FROZEN at this point, no changes after D8 exam opened.
    fresh=json.loads(EXAM.read_text());exam=[{'kind':'positive',**z} for z in fresh['positive']]
    exam +=[{'kind':'negative','text':x} for x in fresh['negative']]
    baseline={str(k):stat(naive(exam,k)) for k in (1,2,4,8,16,32)}
    chosen_pred=predict(exam,clf,threshold,32)
    stats=stat(chosen_pred)
    report={'scope':'RESEARCH_CRITIC_NOT_NATIVE_C4M','parent_c4m_sha256':originalhash,'exam_sha256':FROZEN_SHA,
         'train_groups':len(train),'train_candidate_count':len(y),'train_correct_candidates':int(sum(y)),
         'validation_groups':len(val),'validation_utility_by_threshold':validation,'threshold_chosen_without_D8_exam':threshold,
         'baseline_on_fresh':baseline,'learned_gate_on_fresh':stats,'fresh_details':chosen_pred,
         'warning':'Small correlated teacher datasets, post-D7 exploratory learned critic, not independently authored blind test; gate trained in sklearn and NOT saved to C4M; no conversational ability proven.'}
    assert PRE_FACTS==len(native.g.facts) and originalhash==hashlib.sha256(MODEL.read_bytes()).hexdigest()
    (R/'D8_GATE_RESULTS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps({key:report[key] for key in ('threshold_chosen_without_D8_exam','baseline_on_fresh','learned_gate_on_fresh')},ensure_ascii=False,indent=2),flush=True)

if __name__=='__main__':main()