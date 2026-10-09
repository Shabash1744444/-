"""C004-R4: independent provenance root != individual intervention identity."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from c4child import C4LivingRuntime,C4ChildDialogue
from c4child.checkpoint import save_c4m_compact,load_c4m_compact
from c4child.structured_cognition import _score_actions

def msg(r,p):return r.user_message('@c4 '+json.dumps(p))

def execute(r,obj,session):
    def f(sub,loc):return dict(subject=sub,relation='LOCATION',object=loc)
    msg(r,dict(op='GOAL',scope='SIM',scene='home',initial=f(obj,'floor-left'),target=f(obj,'held')))
    msg(r,dict(op='DEMO',scope='SIM',scene='home',action='TAKE',
               before=f('EXAMPLE','floor-left'),after=f('EXAMPLE','held')))
    aid=msg(r,dict(op='PLAN',scope='SIM',scene='home'))['cognitive']['action_id']
    r.bind_native_room_session(session)
    receipt=dict(requestId=aid,action='TAKE',object=obj,origin='SANDBOX',world='HOME',
                 accepted=True,executionSuccess=True,
                 before={'location':'floor-left'},after={'location':'held'})
    assert r.native_room_receipt(receipt,session)['status']=='SIM_SUCCESS'
    return aid

def scores(r):
    return _score_actions(r,dict(scope='SIM',scene='home',frames=[]),['TAKE'])['TAKE']

def test_same_host_session_not_two_independent_sources():
    r=C4LivingRuntime(C4ChildDialogue())
    a=execute(r,'BALL','c4-shared')
    b=execute(r,'BLOCK','c4-shared')
    x,y=r.cognitive_actions[a],r.cognitive_actions[b]
    assert x['outcome_root']==y['outcome_root']=='host_room_session:c4-shared'
    assert x['receipt_id']!=y['receipt_id']
    assert x['outcome_trial_id']!=y['outcome_trial_id']
    summary=msg(r,dict(op='REFLECT',scope='SIM',scene='home'))['cognitive']
    assert summary['confirmed_sim']==2
    assert summary['independent_sim_roots']==1
    assert scores(r)==3

def test_two_sessions_are_two_distinct_roots():
    r=C4LivingRuntime(C4ChildDialogue())
    a=execute(r,'BALL','c4-one')
    b=execute(r,'BLOCK','c4-two')
    assert r.cognitive_actions[a]['outcome_root']!=r.cognitive_actions[b]['outcome_root']
    assert msg(r,dict(op='REFLECT',scope='SIM',scene='home'))['cognitive']['independent_sim_roots']==2
    assert scores(r)==6

def test_cold_reload_keeps_root_and_trial_separate():
    r=C4LivingRuntime(C4ChildDialogue())
    a=execute(r,'BALL','c4-same')
    b=execute(r,'BLOCK','c4-same')
    with TemporaryDirectory() as d:
        p=Path(d)/'test.c4m'
        save_c4m_compact(p,r.dialogue.g,runtime_state=r.runtime_state(),include_cold=True)
        g,h,m,rs=load_c4m_compact(p,with_runtime=True)
        cold=C4LivingRuntime(C4ChildDialogue(g))
        cold.load_runtime_state(rs)
        assert cold.cognitive_actions[a]['outcome_root']==cold.cognitive_actions[b]['outcome_root']
        assert cold.cognitive_actions[a]['receipt_id']!=cold.cognitive_actions[b]['receipt_id']
        assert cold.cognitive_actions[a]['outcome_trial_id']!=cold.cognitive_actions[b]['outcome_trial_id']
        assert cold._native_room_session is None
        assert msg(cold,dict(op='REFLECT',scope='SIM',scene='home'))['cognitive']['independent_sim_roots']==1
