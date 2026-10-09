"""D1 experimental trainable conversation policy on the ORIGINAL C4Graph.

This organ is an intentionally bounded scientific experiment, not a natural
language model or a replacement for C4LivingRuntime. All trained weights and
surface patterns are LANGUAGE_CONVENTION facts inside the native .c4m.

Teacher-produced episodes provide dependent *language supervision*, never WORLD
observations. No teacher report or model-generated answer can self-verify.
"""
from __future__ import annotations
from collections import defaultdict
import json
import re
from .bootstrap import BootstrapTeacher
from .scope import fact_scope, LANGUAGE_CONVENTION

WEIGHT_REL='DIALOGUE_POLICY_WEIGHT'
PATTERN_REL='DIALOGUE_REPLY_PATTERN'
ROOT='curated:assistant-teacher:c4-d1-dialogue:2026-10-09'


def _text_features(s):
    words=re.findall(r'[a-zа-яё0-9]+',str(s).lower().replace('ё','е'))
    # General n-gram representation, no per-word or per-dialogue answers.
    grams=set('w:'+x for x in words)
    grams.update('b:'+words[i]+'|'+words[i+1] for i in range(len(words)-1))
    normalized=' '.join(words)
    grams.update('c:'+normalized[i:i+3] for i in range(len(normalized)-2))
    return grams


def _context_features(frame, intent):
    # Nonlinguistic typed context only. Object/name values are NOT memorized.
    mode=str(frame.get('mode','NONE')).upper()
    prev=str(frame.get('previous_reply_act','NONE')).upper()
    goal=str(frame.get('goal','NONE')).upper()
    focus='YES' if frame.get('focus') else 'NO'
    return {'bias','intent:'+intent,'mode:'+mode,'prev:'+prev,'goal:'+goal,'focus:'+focus,
            'i_prev:'+intent+'|'+prev, 'i_focus:'+intent+'|'+focus,
            'i_goal:'+intent+'|'+goal}


def _fit(examples, feat, *, epochs=8):
    """Standard deterministic online multiclass perceptron. No rule table."""
    labels=tuple(sorted(set(x['label'] for x in examples)))
    w=defaultdict(float)
    for epoch in range(epochs):
        for ex in examples:
            fs=feat(ex)
            scores={a:sum(w[(a,f)] for f in fs) for a in labels}
            predicted=max(labels,key=lambda a:(scores[a], -labels.index(a)))
            if predicted!=ex['label']:
                for f in fs:
                    w[(ex['label'],f)]+=1.0
                    w[(predicted,f)]-=1.0
    return {k:v for k,v in w.items() if v}


class LearnedNarrativePolicy:
    """Graph-backed supervised intent + speech-act selectors and reply realization."""
    def __init__(self,graph):
        self.g=graph
        self._params=None
        self._patterns=None

    def _read(self):
        if self._params is not None:return
        self._params={'INTENT':defaultdict(dict),'REPLY':defaultdict(dict)}
        self._patterns={}
        for fact in self.g.facts.values():
            if fact.status!='ADMITTED' or fact_scope(self.g,fact)!=LANGUAGE_CONVENTION:continue
            if fact.relation not in (WEIGHT_REL,PATTERN_REL):continue
            if fact.origin!='EXTERNAL_CORPUS' or fact.authority!='TEACHER':continue
            if not fact.source_group or not str(fact.source_group).startswith('curated:assistant-teacher:c4-d1-dialogue:'):continue
            subject=self.g.entities.get(fact.subject)
            if subject is None:continue
            label=subject.label
            if fact.relation==WEIGHT_REL:
                try:
                    tag,task,act,feature=label.split('|',3)
                    if tag!='d1weight' or task not in self._params:continue
                    weight=float(fact.object_value)
                    self._params[task][act][feature]=weight
                except (ValueError,OverflowError):continue
            else:
                if label.startswith('d1pattern|'):
                    self._patterns[label.split('|',1)[1]]=str(fact.object_value)

    def _predict(self,task,features):
        self._read()
        if not self._params[task]:return None
        if task=='INTENT':
            coverage=sum(1 for f in features if any(f in w for w in self._params[task].values()))
            if coverage<3:return None
        scores={a:sum(w.get(f,0.0) for f in features) for a,w in self._params[task].items()}
        ordered=sorted(scores.items(),key=lambda p:(-p[1],p[0]))
        # One best positive hypothesis is required, ties or no support ABSTAIN.
        if not ordered or ordered[0][1]<=0:return None
        if len(ordered)>1 and ordered[0][1]==ordered[1][1]:return None
        return ordered[0][0]

    def decide(self,text,frame):
        intent=self._predict('INTENT',_text_features(text))
        if intent is None:return {'status':'ABSTAIN','reason':'UNKNOWN_USER_INTENT'}
        act=self._predict('REPLY',_context_features(frame,intent))
        if act is None:return {'status':'ABSTAIN','reason':'UNKNOWN_REPLY_POLICY','intent':intent}
        self._read()
        pattern=self._patterns.get(act)
        if pattern is None:return {'status':'ABSTAIN','reason':'NO_GROUNDED_SURFACE','intent':intent}
        # The pattern itself was learned as a language fact. Whitelisted slot
        # values are caller-provided STORY representation, never WORLD evidence.
        slots={k:frame.get(k) for k in ('focus','object','place','character')}
        required=set(re.findall(r'\{(\w+)\}',pattern))
        if not required <= set(slots):return {'status':'ABSTAIN','reason':'UNAUTHORIZED_SLOT'}
        if any(not isinstance(slots[k],str) or not slots[k].strip() or len(slots[k])>80 for k in required):
            return {'status':'ABSTAIN','reason':'MISSING_OR_UNSAFE_REFERENT'}
        if any(re.search(r'[{}\n\r<>]',slots[k]) for k in required):
            return {'status':'ABSTAIN','reason':'UNSAFE_SURFACE'}
        return {'status':'REPLY','intent':intent,'reply_act':act,
                'reply':pattern.format_map({k:v for k,v in slots.items() if v is not None}),
                'scope':'STORY_SPEECH_NOT_WORLD','provenance':'EXTERNAL_CORPUS_DEPENDENT'}

    @staticmethod
    def teach(graph, intent_examples, response_examples, patterns, *, epochs=8):
        if not graph.hardened_gate or graph.constitutional_mode!='STRICT':
            raise ValueError('D1 strict original C4 graph required')
        iweights=_fit(intent_examples,lambda ex:_text_features(ex['text']),epochs=epochs)
        aweights=_fit(response_examples,lambda ex:_context_features(ex['frame'],ex['intent']),epochs=epochs)
        rows=[]
        def add(subj,rel,val):
            rows.append({'schema':'C4_BOOTSTRAP_EVENT_V0.1','event_id':'c4-d1:%05d'%len(rows),
                         'origin':'EXTERNAL_CORPUS','source_group':ROOT,'authority':'TEACHER',
                         'scope':{'principal':'USER','privacy':'LOCAL'},
                         'constitutional_basis':'LANGUAGE_CONVENTION',
                         'payload':{'kind':'CLAIM','subject':subj,'relation':rel,'object':str(val),'object_kind':'literal'}})
        for (a,f),w in sorted(iweights.items()):add('d1weight|INTENT|'+a+'|'+f,WEIGHT_REL,w)
        for (a,f),w in sorted(aweights.items()):add('d1weight|REPLY|'+a+'|'+f,WEIGHT_REL,w)
        for a,p in sorted(patterns.items()):add('d1pattern|'+a,PATTERN_REL,p)
        s=BootstrapTeacher(graph).ingest(rows)
        if s.rejected or s.admitted+s.dedup!=len(rows):
            raise AssertionError('teacher admission failed or mis-scoped')
        out=LearnedNarrativePolicy(graph)
        if out.decide('абракадабра',{})['status']!='ABSTAIN':
            raise AssertionError('novel nonsense must not become dialogue')
        return {'supervised_intent_examples':len(intent_examples),'supervised_response_examples':len(response_examples),
                'teaching_facts':len(rows),'admitted':s.admitted,'deduplicated':s.dedup,
                'intent_weights':len(iweights),'response_weights':len(aweights),'language_patterns':len(patterns),
                'epoch_count':epochs,'source_root':ROOT}
