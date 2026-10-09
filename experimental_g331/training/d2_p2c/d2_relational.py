"""D2-P2 proof candidate: graph-resident supervised relation-role binding.

No phrase keys or inferences from position-specific strings. Token sequence tags and
utterance kind are trained by teacher labels. Interpretations are SOURCE-reports in
STORY context only, never self-evidence. The result is NOT a broad Russian parser.
"""
from __future__ import annotations
import re
from collections import defaultdict
from .bootstrap import BootstrapTeacher
from .scope import fact_scope,LANGUAGE_CONVENTION
from .d2_grounder import tokenize

REL='D2_RELATION_WEIGHT'
ROOT='curated:assistant-teacher:c4-d2-p2-relational:2026-10-09'
ROLES=('HOLDER','SUBJECT','ATTRIBUTE','POLARITY')
TAGS=('O',)+tuple(q+'-'+r for r in ROLES for q in ('B','I'))


def features(words,i):
    w=words[i]; prev=words[i-1] if i else '<S>'; nxt=words[i+1] if i+1<len(words) else '</S>'
    # Generic contextual morphological signals; no belief words hardcoded.
    return ('bias','w:'+w,'p:'+prev,'n:'+nxt,'p2:'+(' '.join(words[max(i-2,0):i]) or '<S>'),
            'n2:'+(' '.join(words[i+1:i+3]) or '</S>'),'shape:'+('D' if w.isdigit() else 'W'),
            'prefix:'+w[:3],'suffix:'+w[-3:],'suffix2:'+w[-2:],'suffix4:'+w[-4:],
            'last_kind:'+('short' if len(w)<4 else 'long'),
            'p_suffix:'+prev[-3:],'n_suffix:'+nxt[-3:],
            'pos:'+str(min(i,5)),
            'relative_end:'+str(min(len(words)-i-1,5)))


def whole_features(words):
    feats={'BIAS'}
    for i,w in enumerate(words):
        feats.add('w:'+w)
        for n in (3,4):
            for j in range(max(0,len(w)-n+1)):
                feats.add('char'+str(n)+':'+w[j:j+n])
        if i>0:feats.add('bi:'+words[i-1]+'|'+w)
        if i>1:feats.add('tri:'+words[i-2]+'|'+words[i-1]+'|'+w)
    return feats


def decode(words,w):
    if not words:return []
    prev={None:(0.0,())}
    fs=[features(words,i) for i in range(len(words))]
    for f in fs:
        states={}
        for tag in TAGS:
            options=[]
            for previous,(score,path) in prev.items():
                if tag.startswith('I-') and previous not in (tag,'B-'+tag[2:]):continue
                val=score+w.get(('trans',previous,tag),0.0)
                val+=sum(w.get(('emit',tag,x),0.0) for x in f)
                options.append((val,path+(tag,)))
            if options:states[tag]=max(options,key=lambda a:a[0])
        prev=states
    return list(max(prev.values(),key=lambda a:a[0])[1])


def sequence_features(words,tags):
    out=defaultdict(float);old=None
    for i,tag in enumerate(tags):
        for f in features(words,i):out[('emit',tag,f)]+=1
        out[('trans',old,tag)]+=1;old=tag
    return out


def fit(cases,epochs=5):
    kinds=tuple(sorted({x['kind'] for x in cases}))
    wc=defaultdict(float);wt=defaultdict(float)
    for _ in range(epochs):
        for ex in cases:
            words=tokenize(ex['text']);ft=whole_features(words)
            scores={k:sum(wc[(k,f)] for f in ft) for k in kinds}
            predicted=max(kinds,key=lambda k:(scores[k],-kinds.index(k)))
            if predicted!=ex['kind']:
                for f in ft:wc[(ex['kind'],f)]+=1;wc[(predicted,f)]-=1
            expected=ex['tags'];assert len(words)==len(expected)
            prediction=decode(words,wt)
            if prediction!=expected:
                e=sequence_features(words,expected);p=sequence_features(words,prediction)
                for f in set(e)|set(p):wt[f]+=e[f]-p[f]
    params={'class|'+k+'|'+f:v for (k,f),v in wc.items() if v}
    for key,val in wt.items():
        if val:
            if key[0]=='emit': label='tag|emit|'+key[1]+'|'+key[2]
            else:label='tag|trans|'+str(key[1])+'|'+key[2]
            params[label]=val
    return params


class LearnedRelationBinder:
    def __init__(self,graph):self.g=graph;self.params=None
    def load(self):
        if self.params is not None:return
        self.params={}
        for f in self.g.facts.values():
            if f.status!='ADMITTED' or f.relation!=REL or f.origin!='EXTERNAL_CORPUS' or f.authority!='TEACHER':continue
            if f.source_group!=ROOT or fact_scope(self.g,f)!=LANGUAGE_CONVENTION:continue
            node=self.g.entities.get(f.subject)
            if node and node.label.startswith('d2rel|'):
                try:self.params[node.label[6:]]=float(f.object_value)
                except (ValueError,TypeError):pass

    def interpret(self,text):
        self.load();p=self.params
        if not p:return {'status':'ABSTAIN','reason':'UNTRAINED'}
        words=tokenize(text)
        if not words or len(words)>32:return {'status':'ABSTAIN','reason':'BAD_LENGTH'}
        kinds={key.split('|',2)[1] for key in p if key.startswith('class|')}
        ft=whole_features(words)
        scores={k:sum(p.get('class|'+k+'|'+f,0.0) for f in ft) for k in kinds}
        ordered=sorted(scores,key=lambda k:(-scores[k],k))
        if not ordered or scores[ordered[0]]<=0:return {'status':'ABSTAIN','reason':'LOW_CONFIDENCE'}
        if len(ordered)>1 and scores[ordered[0]]-scores[ordered[1]]<1:return {'status':'ABSTAIN','reason':'AMBIGUOUS'}
        kind=ordered[0]
        if kind=='OTHER':return {'status':'ABSTAIN','reason':'OTHER','kind':kind}
        w={}
        for key,val in p.items():
            if key.startswith('tag|emit|'):
                _,_,tag,feature=key.split('|',3);w[('emit',tag,feature)]=val
            elif key.startswith('tag|trans|'):
                _,_,prev,tag=key.split('|',3);w[('trans',None if prev=='None' else prev,tag)]=val
        tags=decode(words,w)
        roles={}
        for role in ROLES:
            segments=[];start=None
            for i,t in enumerate(tags+['O']):
                if t=='B-'+role:
                    if start is not None:segments.append(' '.join(words[start:i]))
                    start=i
                elif t!='I-'+role:
                    if start is not None:segments.append(' '.join(words[start:i]));start=None
            if segments:roles[role]=segments
        # Structural validity, not phrase keyed. Competing spans => safe abstention.
        needed=('SUBJECT','ATTRIBUTE')+ (('HOLDER',) if kind=='BELIEF' else ())
        if any(len(roles.get(r,[]))!=1 for r in needed):return {'status':'ABSTAIN','reason':'ROLE_BINDING_FAILED','kind':kind,'roles':roles,'tags':tags}
        if kind=='NARRATOR' and roles.get('HOLDER'):return {'status':'ABSTAIN','reason':'EXTRA_HOLDER','roles':roles}
        if any(len(v)!=1 for v in roles.values()):return {'status':'ABSTAIN','reason':'MULTI_CLAUSE_UNSUPPORTED','roles':roles}
        return {'status':'CANDIDATE','kind':kind,'roles':{k:v[0] for k,v in roles.items()},
                'polarity':'NEGATED' if roles.get('POLARITY') else 'POSITIVE',
                'scope':'ATTRIBUTED_USER_REPORT_NOT_WORLD' if kind=='BELIEF' else 'STORY_SOURCE_REPORT',
                'source':'USER_SAID_NOT_OBSERVED','tags':tags}

    @staticmethod
    def train(g,examples,epochs=5):
        if not g.hardened_gate or g.constitutional_mode!='STRICT':raise ValueError('Strict C4 graph expected')
        weights=fit(examples,epochs)
        records=[]
        for i,(key,value) in enumerate(sorted(weights.items())):
            records.append({'schema':'C4_BOOTSTRAP_EVENT_V0.1','event_id':f'c4-d2-p2:{i:07d}',
                'origin':'EXTERNAL_CORPUS','source_group':ROOT,'authority':'TEACHER',
                'scope':{'principal':'USER','privacy':'LOCAL'},'constitutional_basis':'LANGUAGE_CONVENTION',
                'payload':{'kind':'CLAIM','subject':'d2rel|'+key,'relation':REL,
                           'object':str(value),'object_kind':'literal'}})
        result=BootstrapTeacher(g).ingest(records)
        if result.rejected or result.admitted+result.dedup!=len(records):raise AssertionError('Admission not strict and clean: '+str(result))
        return {'episodes':len(examples),'epochs':epochs,'parameter_facts':result.admitted,'dedup':result.dedup,'root':ROOT}