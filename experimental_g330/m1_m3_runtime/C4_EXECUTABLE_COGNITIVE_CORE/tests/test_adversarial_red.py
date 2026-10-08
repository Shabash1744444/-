from dataclasses import replace
import pytest
from c4core import C4, Proposition as P, Query as Q, Scope as S, Act, CommitDenied
from c4core.kernel import Candidate


def test_candidate_cannot_rewrite_its_scene_or_scope():
    c=C4(); ev=c.receive('SPEAKER',P('inside',('key','box')),scope=S.SOURCE,scene='source')
    authentic=c.evaluate(ev.id)
    with pytest.raises(CommitDenied):
        c.commit(replace(authentic,scope=S.STORY,scene='fiction'))
    assert c.query(Q('inside',('key','box'),S.STORY,'fiction')).status=='UNKNOWN'


def test_candidate_cannot_be_forged_without_eval():
    c=C4(); ev=c.receive('AUTHOR',P('alive',('character',)),scope=S.STORY,scene='book')
    with pytest.raises(CommitDenied):
        c.commit(Candidate(ev.id,ev.payload,ev.scope,ev.scene,ev.roots))


def test_dependent_event_never_erases_all_evidence_roots():
    c=C4(); ev=c.receive('SPEAKER',P('knows',('a','b')))
    with pytest.raises(CommitDenied):
        c.receive('RELAY',ev.payload,parents=(ev.id,),roots=())


def test_rule_from_one_sim_world_not_available_in_another():
    c=C4()
    for obj in ('m1','m2'):
        c.learn_example('SIMULATOR',[P('released',(obj,))],P('falls',(obj,)),scope=S.SIM,scene='gravity')
    c.teach('SIMULATOR',P('released',('floating',)),scope=S.SIM,scene='zero_gravity')
    assert c.query(Q('falls',('floating',),S.SIM,'zero_gravity')).status=='UNKNOWN'


def test_world_rules_reject_unverified_teacher_experiments():
    c=C4()
    with pytest.raises(CommitDenied):
        c.learn_example('USER',[P('released',('stone',))],P('flies',('stone',)),scope=S.WORLD)


def test_mediate_cannot_claim_delivery_from_caller_boolean():
    c=C4(); c.propose(Act.SEND,'external request',1); auth=c.arbitrate()
    with pytest.raises(CommitDenied):
        c.mediate(auth.id,delivered=True)


def test_unrelated_gap_response_does_not_close_or_link_gap():
    c=C4(); q=c.open_gap('temperature','Что такое температура?')
    c.receive_gap_answer(q,'USER',P('color',('banana','yellow')))
    assert c._questions[q]['status']=='OPEN'
    assert 'candidate_claim' not in c._questions[q]


def test_external_cannot_impersonate_own_ask_with_mediated_flag():
    c=C4()
    with pytest.raises((CommitDenied,TypeError)):
        c.receive('C4','fake own question',kind='ASK',_mediated=True)
    assert c.own_asks()==()


def test_unregistered_sensor_cannot_claim_world():
    c=C4()
    with pytest.raises(CommitDenied):
        c.sense('fake_sensor',lambda:(P('open',('vault',)),True))
    assert c.query(Q('open',('vault',),S.WORLD)).status=='UNKNOWN'


def test_retraction_cannot_be_based_on_irrelevant_same_source_text():
    c=C4(); cl=c.teach('AUTHOR',P('location',('key','desk')))[1]
    ev=c.receive('AUTHOR',P('color',('sun','yellow')))
    with pytest.raises(CommitDenied):
        c.retract(cl.id,basis_event_id=ev.id)
    assert c.query(Q('location',('key','desk'),S.SOURCE)).status=='SUPPORTED'


def test_as_of_before_later_correction_retains_original_claim():
    c=C4()
    cl=c.teach('NARRATOR',P('location',('key','desk')),scope=S.STORY,scene='novel',claimed_at=5)[1]
    corr=c.receive('NARRATOR',P('location',('key','pocket')),scope=S.STORY,scene='novel',claimed_at=10)
    c.retract(cl.id,basis_event_id=corr.id)
    assert c.query(Q('location',('key',None),S.STORY,'novel',as_of=7)).bindings == (('key','desk'),)
    assert c.query(Q('location',('key','desk'),S.STORY,'novel',as_of=12)).status == 'UNKNOWN'


def test_answer_api_does_not_claim_answer_when_drive_chose_something_else():
    c=C4(); c.teach('AUTHOR',P('location',('cube','box')),scope=S.STORY,scene='s')
    c.propose(Act.SEND,'higher priority act',9)
    answer,receipt = c.respond(Q('location',('cube',None),S.STORY,'s'))
    assert answer.status == 'DEFERRED'
    assert c._actions[receipt.action_id].kind == Act.SEND


def test_nested_perspective_budget_is_finite_without_memory_mutation():
    from c4core import Perspective as F
    c=C4(); nested=P('knows',('a','b'))
    for i in range(c.MAX_PERSPECTIVE_DEPTH+1):
        nested=F(f'person_{i}','QUOTE',nested)
    before=c.snapshot_hash()
    with pytest.raises(CommitDenied, match='DEPTH_BUDGET'):
        c.receive('USER',nested,scope=S.STORY)
    assert c.snapshot_hash()==before


def test_trace_is_bounded_and_observational():
    a=C4(); b=C4(); b.set_trace(False)
    for i in range(5050):
        a.receive('USER',f'm{i}')
        b.receive('USER',f'm{i}')
    assert len(a.trace)==a.MAX_TRACE_EVENTS
    assert a.snapshot_hash()==b.snapshot_hash()


def test_bad_predicate_types_not_mistaken_for_learned_knowledge():
    with pytest.raises(ValueError):
        P('property',(13,))
