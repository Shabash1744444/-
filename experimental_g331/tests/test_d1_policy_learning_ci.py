"""CI gate: actual native C4 graph acquires speech-policy from lessons only.

No original L1 model is needed for this limited operator-learning gate; the full
L1 trained-copy, cold C4M and provenance tests are reported separately.
"""
from c4child.graph import C4Graph
from c4child.scope import LANGUAGE_CONVENTION, fact_scope
from c4child.narrative_policy import LearnedNarrativePolicy, ROOT
from d1_experiment import make_cases, PATTERNS, eval_policy


def _graph():
    g=C4Graph();g.set_constitutional_mode('STRICT');g.hardened_gate=True
    return g


def test_learned_policy_changes_same_code_only_after_teacher_episodes():
    g=_graph();cases=make_cases(256,47);holdout=make_cases(125,90001,holdout=True)
    assert eval_policy(g,holdout)['pass']==0
    data=[{'text':x['text'],'label':x['intent']} for x in cases]
    decisions=[{'frame':x['frame'],'intent':x['intent'],'label':x['label']} for x in cases]
    stats=LearnedNarrativePolicy.teach(g,data,decisions,PATTERNS)
    assert stats['supervised_intent_examples']==256
    assert eval_policy(g,holdout)['pass']==112
    assert all(f.status=='ADMITTED' and fact_scope(g,f)==LANGUAGE_CONVENTION
               and f.source_group==ROOT for f in g.facts.values())
    assert not any(f.relation in {'IS_A','LOCATION'} for f in g.facts.values())


def test_same_message_different_previous_context_changes_learned_act():
    g=_graph();cases=make_cases(256,47)
    LearnedNarrativePolicy.teach(g,[{'text':e['text'],'label':e['intent']} for e in cases],
                                [{'frame':e['frame'],'intent':e['intent'],'label':e['label']} for e in cases],PATTERNS)
    p=LearnedNarrativePolicy(g)
    frame={'mode':'STORY','scope':'STORY','goal':'PLAY','focus':'драконья лампа',
           'place':'дерево','previous_reply_act':'OPEN_SCENE'}
    a=p.decide('а что дальше',frame)
    b=p.decide('а что дальше',{**frame,'previous_reply_act':'PROPOSE_NEXT'})
    assert a['reply_act']=='ASK_GOAL'
    assert b['reply_act']=='PROPOSE_NEXT'
    assert 'драконья лампа' in a['reply'] and 'драконья лампа' in b['reply']


def test_untrained_unsupported_and_nonsense_never_claim_world():
    g=_graph();policy=LearnedNarrativePolicy(g)
    assert policy.decide('давай сочиним игру',{})['status']=='ABSTAIN'
    cases=make_cases(64,47)
    LearnedNarrativePolicy.teach(g,[{'text':e['text'],'label':e['intent']} for e in cases],
                                [{'frame':e['frame'],'intent':e['intent'],'label':e['label']} for e in cases],PATTERNS)
    p=LearnedNarrativePolicy(g)
    assert p.decide('гзф тёмнофлаг ярап',{'focus':'мяч','place':'корзина'})['status']=='ABSTAIN'