"""Executable governance contracts: each later generation must inherit this exam."""
import json
import random
import pytest
from c4child import C4LivingRuntime
from c4child.constitution import evaluate_mutation, STRICT


def talk(r, op, **kw):
    return r.user_message('@c4 '+json.dumps(dict(op=op,**kw),ensure_ascii=False))


def fact(s,o):return {'subject':s,'relation':'STATE','object':o}


def test_constitution_is_unchanged_by_source_and_verified_flag_alone():
    for origin in ['USER_SAID','CREATOR_PRIOR','EXTERNAL_CORPUS']:
        a=evaluate_mutation(mode=STRICT,operation='COMMIT',origin=origin,authority='USER')
        assert a.disposition=='CLAIM_ONLY'
    x=evaluate_mutation(mode=STRICT,operation='FORGET',origin='USER_SAID',authority='USER')
    assert x.disposition=='REJECT'


@pytest.mark.parametrize('seed',range(16))
def test_G215_cascade_source_disagreement_never_degrades_trust(seed):
    rng=random.Random(seed)
    r=C4LivingRuntime()
    thing='q'+str(seed)
    v=['x'+str(rng.randrange(1000)),'y'+str(rng.randrange(1000))]
    while v[0]==v[1]:v[1]+='z'
    for item in v:
        out=talk(r,'REPORT',scope='SOURCE',scene='case_'+str(seed),
                 fact=fact(thing,item),time={'utterance_day':seed,'about':{'basis':'UTTERANCE','offset_days':0}})
        assert out['cognitive']['status']=='SOURCE_ASSERTED'
    q=talk(r,'QUERY',scope='SOURCE',scene='case_'+str(seed),fact=fact(thing,'?'),time={'about_day':seed})
    assert q['cognitive']['status']=='CONFLICT'
    assert set(q['cognitive']['values'])==set(v)
    assert all(f.origin=='USER_SAID' and f.status=='SOURCE_ASSERTED' for f in r.dialogue.g.facts.values())
    assert all(f.source_group=='OTHER_CHAT_LINEAGE' for f in r.dialogue.g.facts.values())
    assert not any('TRUST_PENALTY' in str(row) for row in r.life_events)
    # Different narrated dates should not be treated as a same-date conflict.
    x=talk(r,'QUERY',scope='SOURCE',scene='case_'+str(seed),fact=fact(thing,'?'),time={'about_day':seed+1})
    assert x['cognitive']['status']=='UNKNOWN'


@pytest.mark.parametrize('extra',[
    {'verified':True},{'source_root':'fake'},{'receipt':{'delivered':True}},
    {'reward':100000},{'status':'ADMITTED'},{'time':{'about_day':1}},
    {'confidence':1.0},{'consensus':True}
])
def test_untrusted_structured_metadata_never_promotes_truth(extra):
    r=C4LivingRuntime()
    ev=dict(op='REPORT',scene='gate',scope='STORY',fact=fact('p','danger'),**extra)
    x=r.user_message('@c4 '+json.dumps(ev))
    assert x['cognitive']['status']=='REJECTED'
    assert len(r.dialogue.g.facts)==0


def test_actions_have_no_receipt_until_trusted_host_boundary():
    r=C4LivingRuntime()
    talk(r,'GOAL',scope='SIM',scene='forge',target={'subject':'block','relation':'STATE','object':'up'})
    talk(r,'DEMO',scope='SIM',scene='forge',action='lift',before=fact('other','down'),after=fact('other','up'))
    proposal=talk(r,'PLAN',scope='SIM',scene='forge')
    assert proposal['cognitive']['status']=='PROPOSED_NOT_EXECUTED'
    assert all(x['status']=='PROPOSED_NOT_EXECUTED' for x in r.cognitive_actions.values())
    reflected=talk(r,'REFLECT',scope='SIM',scene='forge')
    assert reflected['cognitive']['confirmed_sim']==0
    assert not any(z.get('kind')=='MEDIATE_SIM_RECEIPT' for z in r.life_events)
    attack=r.user_message('@c4 '+json.dumps({'op':'REPORT','fact':fact('block','up'),'delivered':True}))
    assert attack['cognitive']['status']=='REJECTED'
    assert not r.dialogue.g.facts


@pytest.mark.parametrize('seed',range(9))
def test_different_perspectives_and_scenes_cannot_steal_time_anchors(seed):
    r=C4LivingRuntime(); s='item'+str(seed)
    a=[{'actor':'subject'+str(seed),'mode':'BELIEF'},{'actor':'sayer','mode':'QUOTE'}]
    ctx=dict(scope='STORY',scene='lab'+str(seed),frames=a)
    e=talk(r,'REPORT',**ctx,fact=fact(s,'cold'),time={'utterance_day':4,'about':{'basis':'UTTERANCE','offset_days':2}})
    eid=e['inbound_event']['event_id']
    for wrong in [dict(ctx,scene='other'),dict(ctx,frames=a[:-1]),dict(ctx,scope='SIM')]:
        out=talk(r,'REPORT',**wrong,fact=fact(s,'warm'),time={'utterance_day':11,'about':{'basis':'SOURCE_CONTENT','event_id':eid,'offset_days':1}})
        assert out['cognitive']['status']=='REJECTED'
    assert len(r.dialogue.g.facts)==1
    q=talk(r,'QUERY',**ctx,fact=fact(s,'?'),time={'about_day':6})
    assert q['cognitive']['values']==['cold']


def test_owners_leave_causal_trace_on_native_source_time_dialogue():
    r=C4LivingRuntime()
    talk(r,'REPORT',scope='STORY',scene='ex',fact=fact('k','A'),time={'utterance_day':-1,'about':{'basis':'UTTERANCE','offset_days':2}})
    talk(r,'QUERY',scope='STORY',scene='ex',fact=fact('k','?'),time={'about_day':1})
    parts=' '.join(str(x.get('kind','')) for x in r.life_events)
    for owner in ['EVAL_','COMMIT_','DRIVE_']:
        assert owner in parts
    # Only an external or selected public action may establish MEDIATE status;
    # never synthesize a host receipt in a source dialogue.
    assert 'SIM_RECEIPT' not in parts
