"""D5-SV: alternate learned edge-scoring model (L2 logistic) for graph-attachment.
Uses no handwritten order/direction rules. Fit on edge supervision only.
Compared with online structured perceptron using same train/test. Does not install in native runtime.
"""
from experiment import *
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

def dictfeatures(ns,a,b,relation):
    return {repr(feature):1 for feature in feats(ns,a,b,relation)}

def records(rows):
    r={'HOLDER':([],[]),'ARG':([],[]),'NEG':([],[])}
    for ex in rows:
        ns,gorder,gh,gn=gold_structure(ex);ns=node_virtual(ns)
        ops=list(gorder); heads=[x['id'] for x in ns if x['tag']=='HOLDER'];negs=[x['id'] for x in ns if x['tag']=='NEG'];P=len(ns)-1
        want_arcs={(o,ops[i+1] if i+1<len(ops) else P) for i,o in enumerate(ops)}
        for h in heads:
            for o in ops:
                r['HOLDER'][0].append(dictfeatures(ns,h,o,'HOLDER'));r['HOLDER'][1].append(int(gh[o]==h))
        for o in ops:
            for to in ops+[P]:
                if to==o:continue
                r['ARG'][0].append(dictfeatures(ns,o,to,'ARG'));r['ARG'][1].append(int((o,to) in want_arcs))
        for n in negs:
            for to in ops+[P]:
                r['NEG'][0].append(dictfeatures(ns,n,to,'NEG'));r['NEG'][1].append(int((P if gn[n]=='P' else gn[n])==to))
    return r

class Model:
    def __init__(self,rows,C=1.):
        self.r={};r=records(rows)
        for name,(xx,yy) in r.items():
            v=DictVectorizer();X=v.fit_transform(xx)
            clf=LogisticRegression(C=C,max_iter=1000,class_weight='balanced',random_state=0)
            clf.fit(X,yy);self.r[name]=(v,clf)
    def score(self,ns,a,b,name):
        v,clf=self.r[name]
        x=v.transform([dictfeatures(ns,a,b,name)])
        return float(clf.decision_function(x)[0])
    def predict(self,ex,tags=None):
        ns=nodes_of(ex,tags)
        if not any(x['tag']=='ATTRIBUTE' for x in ns) or sum(x['tag'].startswith('OP_') for x in ns)>5:return None
        n=node_virtual(ns);ops=[x['id'] for x in ns if x['tag'].startswith('OP_')]; heads=[x['id'] for x in ns if x['tag']=='HOLDER'];negs=[x['id'] for x in ns if x['tag']=='NEG'];P=len(ns)
        if not ops or len(ops)!=len(heads):return None
        # Joint max-weight one-to-one matching and one rooted op chain; no positional hardcode.
        order=max(permutations(ops),key=lambda oo:sum(self.score(n,o,oo[i+1] if i+1<len(oo) else P,'ARG') for i,o in enumerate(oo)))
        hs=max(permutations(heads),key=lambda hh:sum(self.score(n,h,o,'HOLDER') for o,h in zip(ops,hh)))
        holder=dict(zip(ops,hs))
        neg={z:max([P]+ops,key=lambda p:self.score(n,z,p,'NEG')) for z in negs}
        neg={k:'P' if p==P else p for k,p in neg.items()}
        return reconstruct(ns,order,holder,neg)

def measure(test,model,tm=None):
    ans={}
    for name,rows in test.items():
        n=0;ab=0;tagsok=0;bad=[]
        for ex in rows:
            tt=decode(tokenize(ex['text']),tm) if tm is not None else ex['tags']
            tagsok+=tt==ex['tags']
            ast=model.predict(ex,tt);good=ast==ex['ast'];n+=good;ab+=ast is None
            if not good and len(bad)<2:bad.append({'text':ex['text'],'pred':ast,'gold':ex['ast']})
        ans[name]={'correct':n,'total':len(rows),'tag_exact':tagsok,'abstain':ab,'failures':bad}
    return ans

if __name__=='__main__':
    # USE IMMUTABLE D5 holdout and training, do not regenerate or edit.
    frozen=json.loads((L/'D5_HOLDOUT_FROZEN.json').read_text())['generated']
    train=json.loads((L/'D5_TRAIN.json').read_text())
    sha=hashlib.sha256((L/'D5_HOLDOUT_FROZEN.json').read_bytes()).hexdigest()
    r={'frozen_sha256':sha,'training_samples':len(train),'family':'L2_logreg_pairwise_graph_attachment','results':{}}
    for C in [1.0]:
        m=Model(train,C);tw=train_weights(train,4)
        r['results'][str(C)]={'oracle_tags':measure(frozen,m),'learned_tags':measure(frozen,m,tw)}
        print('LOGISTIC',C,'ORACLE',{k:v['correct'] for k,v in r['results'][str(C)]['oracle_tags'].items()},flush=True)
        print('LOGISTIC',C,'LEARNED',{k:v['correct'] for k,v in r['results'][str(C)]['learned_tags'].items()},flush=True)
    write_json(L/'D5_LOGISTIC_RESULTS.json',r)