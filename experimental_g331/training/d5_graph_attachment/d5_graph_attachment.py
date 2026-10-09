"""D5 scientific module: learned graph attachment scores, *read-only* semantics.
Training targets from one synthetic teacher dependent root. The architecture fixes
only node types, a rooted graph form, and finite graph search; all relative
arc direction and negation scope link scores are learned and persist as C4 facts.
NOT a fluent parser, NOT integrated into ordinary user_message, NOT production.
"""
from itertools import permutations
from .d3_scoped import spans
from .d2_grounder import tokenize
from .scope import LANGUAGE_CONVENTION, fact_scope

REL='D5_GRAPH_EDGE_WEIGHT'
ROOT='curated:assistant-teacher:c4-d5-edge-2026-10-09'

def make_nodes(text,tags):
    words=tokenize(text)
    if len(words)!=len(tags) or len(words)>36:return []
    return [{'id':i,'tag':role,'text':value,'pos':start} for i,(role,value,start) in enumerate(spans(words,list(tags)))]

def aug(ns):
    attr=next(n for n in ns if n['tag']=='ATTRIBUTE')
    return ns+[{'id':len(ns),'tag':'PROPERTY','text':'','pos':attr['pos']}]

def bucket(x):
    x=abs(x)
    return '1' if x<=1 else '2' if x<=2 else '3' if x<=4 else '4' if x<=8 else '5'

def edge_features(nodes,a,b,rel):
    x=nodes[a];y=nodes[b];dx=y['pos']-x['pos'];lo=min(x['pos'],y['pos']);hi=max(x['pos'],y['pos'])
    mid=[n for n in nodes if lo<n['pos']<hi];nops=sum(z['tag'].startswith('OP_') for z in mid);nheads=sum(z['tag']=='HOLDER' for z in mid);nneg=sum(z['tag']=='NEG' for z in mid)
    side='BEFORE' if dx<0 else 'AFTER';length=bucket(dx)
    return [repr(f) for f in [
      (rel,'bias'),(rel,'pair',x['tag'],y['tag']),(rel,'side',side),
      (rel,'dist',length),(rel,'intervening_ops',min(nops,3)),
      (rel,'intervening_heads',min(nheads,3)),(rel,'intervening_negs',min(nneg,2)),
      (rel,'side_d',side,length),(rel,'side_inter',side,min(nops,3)),
      (rel,'holder_side',side,x['tag'],y['tag']),
      (rel,'side_d_rel',side,length,x['tag'],y['tag'])
    ]]

def reconstruct(ns,order,hmap,neg):
    subj=[n['text'] for n in ns if n['tag']=='SUBJECT'];attr=[n['text'] for n in ns if n['tag']=='ATTRIBUTE']
    if len(subj)!=1 or len(attr)!=1:return None
    ast={'op':'PROPERTY','subject':subj[0],'attribute':attr[0]}
    if 'P' in neg.values():ast={'op':'NOT','arg':ast}
    for opid in reversed(order):
        if opid not in hmap:return None
        ast={'op':ns[opid]['tag'][3:],'holder':ns[hmap[opid]]['text'],'arg':ast}
        if opid in neg.values():ast={'op':'NOT','arg':ast}
    return ast

class GraphEdgeAttachment:
    def __init__(self,graph):self.graph=graph;self._cache=None
    def load(self):
        if self._cache is not None:return
        scores={}
        for f in self.graph.facts.values():
            if f.status!='ADMITTED' or f.relation!=REL or f.source_group!=ROOT or f.origin!='EXTERNAL_CORPUS' or f.authority!='TEACHER' or fact_scope(self.graph,f)!=LANGUAGE_CONVENTION:continue
            subject=self.graph.entities.get(f.subject)
            if not subject or not subject.label.startswith('d5edge|'):continue
            try:
                _,rtype,name=subject.label.split('|',2)
                scores[rtype,name]=float(f.object_value)
            except (ValueError,TypeError):continue
        self._cache=scores
    def score(self,ns,a,b,rel):
        self.load()
        return self._cache.get((rel,'__intercept__'),0.)+sum(self._cache.get((rel,f),0.) for f in edge_features(ns,a,b,rel))
    def parse(self,text,tags):
        self.load()
        if not self._cache:return {'status':'ABSTAIN','reason':'UNTRAINED'}
        ns=make_nodes(text,tags)
        if not ns or sum(n['tag']=='SUBJECT' for n in ns)!=1 or sum(n['tag']=='ATTRIBUTE' for n in ns)!=1:return {'status':'ABSTAIN','reason':'UNSUPPORTED_TAGS'}
        nodes=aug(ns);ops=[n['id'] for n in ns if n['tag'].startswith('OP_')];heads=[n['id'] for n in ns if n['tag']=='HOLDER'];negs=[n['id'] for n in ns if n['tag']=='NEG'];P=len(ns)
        if len(ops)!=len(heads) or not ops or len(ops)>5:return {'status':'ABSTAIN','reason':'UNSUPPORTED_STRUCTURE'}
        # These two optimizations learn attachment; they do NOT hardcode relative word order.
        chain=max(permutations(ops),key=lambda v:sum(self.score(nodes,o,v[i+1] if i+1<len(v) else P,'ARG') for i,o in enumerate(v)))
        hperm=max(permutations(heads),key=lambda v:sum(self.score(nodes,h,o,'HOLDER') for o,h in zip(ops,v)))
        hmap=dict(zip(ops,hperm))
        neg={n:max([P]+ops,key=lambda p:self.score(nodes,n,p,'NEG')) for n in negs}
        neg={n:'P' if p==P else p for n,p in neg.items()}
        ast=reconstruct(ns,chain,hmap,neg)
        if ast is None:return {'status':'ABSTAIN','reason':'UNPARSEABLE'}
        return {'status':'CANDIDATE','epistemic_scope':'USER_STORY_NOT_WORLD',
                'provenance':'DEPENDENT_TEACHER_LANGUAGE_ONLY','ast':ast}