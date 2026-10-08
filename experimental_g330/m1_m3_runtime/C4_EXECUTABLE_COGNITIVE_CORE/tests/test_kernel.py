from __future__ import annotations
import json
from pathlib import Path
from dataclasses import replace
import pytest
from c4core import C4, Proposition as P, Perspective as F, Query as Q, Scope as S, Act, Verdict, CommitDenied


def story(c, what, scene='fiction'):
    return c.teach('AUTHOR', what, scope=S.STORY, scene=scene)[1]


def test_scope_isolation_and_source_truth():
    c=C4(); claim=story(c, P('at',('cube','box')))
    assert claim.scope==S.STORY
    assert c.query(Q('at',('cube',None),S.STORY,'fiction')).bindings==(('cube','box'),)
    assert c.query(Q('at',('cube',None),S.WORLD,'fiction')).status=='UNKNOWN'
    source=c.teach('USER', P('is',('moon','cheese')),scope=S.WORLD)
    assert source[0]==Verdict.DOWNGRADE and source[1].scope==S.SOURCE
    assert c.query(Q('is',('moon','cheese'),S.WORLD)).status=='UNKNOWN'


def test_sourced_belief_vs_story_fact():
    c=C4()
    story(c,F('Masha','BELIEF',P('late',('Ivan',))))
    story(c,P('on_time',('Ivan',)))
    assert c.query(Q('late',('Ivan',),S.STORY,'fiction',(('Masha','BELIEF'),))).status=='SUPPORTED'
    assert c.query(Q('late',('Ivan',),S.STORY,'fiction')).status=='UNKNOWN'
    assert c.query(Q('on_time',('Ivan',),S.STORY,'fiction')).status=='SUPPORTED'


@pytest.mark.parametrize('depth',[1,2,3,5,8])
def test_nested_perspective(depth):
    c=C4(); frames=tuple((f'actor{i}','THOUGHT') for i in range(depth))
    meaning=P('owns',('object','person'))
    for holder,mode in reversed(frames): meaning=F(holder,mode,meaning)
    story(c,meaning)
    assert c.query(Q('owns',('object','person'),S.STORY,'fiction',frames)).status=='SUPPORTED'
    assert c.query(Q('owns',('object','person'),S.STORY,'fiction',frames[:-1])).status=='UNKNOWN'


def test_perspective_does_not_escalate_actor_or_world():
    c=C4(); story(c,F('Nina','QUOTE',F('Dima','BELIEF',P('fly',('cat',)))))
    assert c.query(Q('fly',('cat',),S.WORLD,'fiction')).status=='UNKNOWN'
    assert c.query(Q('fly',('cat',),S.STORY,'fiction',(('Nina','QUOTE'),('Dima','BELIEF')))).status=='SUPPORTED'


def test_no_mutation_by_query_or_hypothesis():
    c=C4(); ev=c.receive('AUTHOR',P('at',('stone','bridge')),scope=S.STORY,scene='s')
    h1=c.snapshot_hash(); cand=c.evaluate(ev.id)
    assert cand and c.snapshot_hash()==h1  # hypotheses/trace not in canonical snapshot
    assert c.query(Q('at',('stone','bridge'),S.STORY,'s')).status=='UNKNOWN'
    c.commit(cand)
    assert c.query(Q('at',('stone','bridge'),S.STORY,'s')).status=='SUPPORTED'


def test_fake_candidate_rejected():
    c=C4(); ev=c.receive('A',P('true',('z',)))
    cand=c.evaluate(ev.id)
    with pytest.raises(CommitDenied): c.commit(replace(cand,content=P('false',('z',))))
    with pytest.raises(CommitDenied): c.commit(replace(cand,roots=('invented',)))


def test_lineage_relay_never_adds_independence():
    c=C4(); original=c.receive('Alice',P('heard',('whale','fish')))
    c.commit(c.evaluate(original.id))
    last=original
    for _ in range(40):
        last=c.replay_source(last.id)
        verdict,claim=c.commit(c.evaluate(last.id))
        assert claim.roots==(original.id,)
    assert len(c.claims)==1
    with pytest.raises(CommitDenied): c.receive('RELAY',last.payload,parents=(last.id,),roots=('new_fake_root',))


def test_own_asks_only_self_origin_and_autonomy():
    c=C4(); c.receive('USER','Какие вопросы ты задавала?',kind='USER_QUESTION')
    assert c.own_asks()==()
    g=c.open_gap('temperature','Что такое температура?',utility=0.5)
    r=c.tick(); assert r.state=='SENT' and not r.verified
    assert c.own_asks()==('Что такое температура?',)
    assert c.tick().state=='INTERNAL'
    assert c._questions[g]['status']=='OPEN'
    c.receive_gap_answer(g,'USER',P('is',('temperature','physical_quantity')))
    assert c._questions[g]['status']=='ANSWER_CANDIDATE'
    assert len(c.own_asks())==1


def test_drive_arbitrates_one_action_and_mediate_cannot_forge_outcome():
    c=C4(); a=c.propose(Act.ASK,'question',0.2); b=c.propose(Act.THINK,'reflect',0.7)
    with pytest.raises(CommitDenied): c.mediate('missing')
    auth=c.arbitrate(); assert auth.action_id==b.id
    rc=c.mediate(auth.id); assert rc.state=='INTERNAL' and not rc.verified
    other=c.arbitrate(); assert other.action_id==a.id
    sent=c.mediate(other.id);assert sent.state=='SENT' and not sent.verified
    assert [x['owner'] for x in c.trace if x['operation']=='SELECT']==['DRIVE','DRIVE']


def test_event_clock_vs_statement_time_vs_causal_order():
    c=C4(); a=c.receive('USER',P('plans',('Ivan','travel')),claimed_at=80,received_at=500)
    b=c.receive('USER',P('happened',('rain',)),parents=(a.id,),claimed_at=30,received_at=510)
    assert a.step < b.step and b.claimed_at < a.claimed_at
    assert c.query(Q('done',('Ivan','travel'),S.WORLD)).status=='UNKNOWN'


def test_retract_requires_owner_and_retains_history():
    c=C4(); claim=c.teach('AUTHOR',P('at',('a','b')))[1]
    bad=c.receive('OTHER',P('at',('a','c')))
    with pytest.raises(CommitDenied):c.retract(claim.id,basis_event_id=bad.id)
    same=c.receive('AUTHOR',P('at',('a','c')))
    c.retract(claim.id,basis_event_id=same.id)
    assert c.query(Q('at',('a','b'),S.SOURCE)).status=='UNKNOWN'
    assert c._claims[claim.id].status=='RETRACTED'
    assert c._events[claim.event_ids[0]].payload==P('at',('a','b'))


def test_query_trace_off_has_same_state_as_trace_on():
    a=C4(); b=C4(); b.set_trace(False)
    for c in (a,b):
        story(c,P('inside',('tea','cup')))
        c.respond(Q('inside',('tea',None),S.STORY,'fiction'))
        c.open_gap('what','What?',utility=0.2)
        c.tick()
    assert a.snapshot_hash()==b.snapshot_hash()
    assert len(a.trace)>0 and len(b.trace)==0


def test_cold_reload_preserves_questions_asks_and_perspectives(tmp_path):
    c=C4(); story(c,F('AI','EXPECTS',P('appears',('rain',))))
    c.open_gap('test','А кто мой собеседник?')
    c.tick(); path=tmp_path/'state.c4j'; d=c.save(path)
    z=C4.load(path)
    assert z.snapshot_hash()==c.snapshot_hash() and d==c.snapshot_hash()
    assert z.own_asks()==c.own_asks()
    assert z.query(Q('appears',('rain',),S.STORY,'fiction',(('AI','EXPECTS'),))).status=='SUPPORTED'
    z.tick(); assert z.own_asks()==c.own_asks()


def test_checkpoint_tampering_detected(tmp_path):
    c=C4(); p=tmp_path/'s.json';c.save(p)
    doc=json.loads(p.read_text('utf8'));doc['payload']['step']=999
    p.write_text(json.dumps(doc),encoding='utf8')
    with pytest.raises(ValueError,match='INTEGRITY'):C4.load(p)


def test_induction_two_examples_generalize_but_not_commit():
    c=C4()
    for obj in ('stone','book'):
        rule=c.learn_example('SIMULATOR',(P('released',(obj,)),),P('falls',(obj,)),scope=S.SIM)
    assert rule and rule.active
    c.teach('SIMULATOR',P('released',('plate',)),scope=S.SIM)
    a=c.query(Q('falls',('plate',),S.SIM))
    assert a.status=='INFERRED' and len(a.roots)>=3
    assert c.query(Q('falls',('plate',),S.WORLD)).status=='UNKNOWN'
    assert not any(cl.content==P('falls',('plate',)) for cl in c.claims)


def test_induction_local_exception_and_recovery():
    c=C4()
    for obj in ('a','b'):
        c.learn_example('SIMULATOR',[P('released',(obj,))],P('falls',(obj,)),scope=S.SIM)
    c.teach('SIMULATOR',P('released',('c',)),scope=S.SIM)
    assert c.query(Q('falls',('c',),S.SIM)).status=='INFERRED'
    c.learn_example('SIMULATOR',[P('released',('c',))],P('falls',('c',)),scope=S.SIM,successful=False)
    assert c.query(Q('falls',('c',),S.SIM)).status=='UNKNOWN'
    assert c.query(Q('falls',('d',),S.SIM)).status=='UNKNOWN'


def test_randomized_never_known_world_from_story():
    for i in range(80):
        c=C4(); actor=f'person{i}'; obj=f'object{i}'; box=f'box{i}'
        story(c,P('located',(obj,box)),scene=actor)
        assert c.query(Q('located',(obj,None),S.STORY,actor)).bindings==((obj,box),)
        assert c.query(Q('located',(obj,None),S.WORLD,actor)).status=='UNKNOWN'


def test_introspection_events_vs_own_utterances():
    c=C4()
    c.receive('USER','What did you yourself ask?',kind='USER_QUESTION')
    c.respond(Q('nonsense',('a',),S.SOURCE))
    assert c.own_asks()==()
    c.open_gap('why','Why does this happen?')
    c.tick()
    assert c.own_asks()==('Why does this happen?',)
    assert len([e for e in c.events if e.actor=='C4' and e.kind=='ANSWER'])==1


def test_sensor_receipt_boundary_has_real_world_path():
    c=C4()
    receipt,verdict,claim=c.sense('trusted_probe',lambda:(P('temperature',('room','21C')),True),received_at=100)
    assert receipt.state=='OBSERVED' and receipt.verified
    assert verdict==Verdict.ADMIT and claim.scope==S.WORLD
    assert c.query(Q('temperature',('room',None),S.WORLD)).status=='SUPPORTED'
    false_receipt,verdict2,claim2=c.sense('unverified_probe',lambda:(P('temperature',('room','90C')),False))
    assert false_receipt.state=='UNVERIFIED' and not false_receipt.verified
    assert claim2.scope==S.SOURCE
    assert c.query(Q('temperature',('room','90C'),S.WORLD)).status=='UNKNOWN'


def test_cold_reload_preserves_induction_and_source_demos(tmp_path):
    c=C4()
    for obj in ('a','b'):
        c.learn_example('sim',[P('released',(obj,))],P('falls',(obj,)))
    c.teach('sim',P('released',('c',)),scope=S.SIM)
    p=tmp_path/'state.c4j';c.save(p);z=C4.load(p)
    assert z.query(Q('falls',('c',),S.SIM)).status=='INFERRED'
    assert z.snapshot_hash()==c.snapshot_hash()


def test_rule_rejects_unbacked_examples():
    c=C4(); ev=c.receive('untrusted',P('arbitrary',('a',)),scope=S.SIM)
    with pytest.raises(CommitDenied):
        c.add_example((P('released',('a',)),),P('falls',('a',)),ev.id)


def test_event_time_query_filter():
    c=C4();c.teach('NARRATOR',P('has',('a','red')),scope=S.STORY,claimed_at=5)
    c.teach('NARRATOR',P('has',('a','blue')),scope=S.STORY,claimed_at=10)
    assert c.query(Q('has',('a',None),S.STORY,as_of=7)).bindings==(('a','red'),)
    assert len(c.query(Q('has',('a',None),S.STORY,as_of=12)).bindings)==2


def test_cli_functional_episode_roundtrip(tmp_path):
    from c4core.cli import result
    c=C4()
    x=result(c,{'op':'teach','actor':'U','scope':'NARRATIVE','scene':'z',
                'content':{'predicate':'located','args':['ball','bag']}})
    assert x['effective_scope']=='NARRATIVE'
    y=result(c,{'op':'query','predicate':'located','args':['ball',None],
                'scope':'NARRATIVE','scene':'z'})
    assert y['bindings']==(('ball','bag'),)
    assert result(c,{'op':'query','predicate':'located','args':['ball',None],
                     'scope':'WORLD','scene':'z'})['status']=='UNKNOWN'
    assert result(c,{'op':'gap','topic':'t','question':'Как тебя зовут?'})['gap_id']
    assert result(c,{'op':'tick'})['asks']==('Как тебя зовут?',)
    s=tmp_path/'state.c4j';result(c,{'op':'save','path':str(s)})
    assert C4.load(s).own_asks()==('Как тебя зовут?',)


def test_cannot_forge_self_ask_from_external_ingest():
    c=C4()
    with pytest.raises(CommitDenied):c.receive('C4','fake own question',kind='ASK')
    assert c.own_asks()==()
