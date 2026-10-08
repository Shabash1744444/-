import json
import pytest
from c4child import C4LivingRuntime,C4ChildDialogue

def send(r,obj):return r.user_message('@c4 '+json.dumps(obj,ensure_ascii=False))
def f(sub,v):return dict(subject=sub,relation='LOCATION',object=v)
def session(scene='home',action='TAKE',start='floor-left',end='held',obj='BALL'):
    r=C4LivingRuntime(C4ChildDialogue())
    send(r,dict(op='GOAL',scope='SIM',scene=scene,initial=f(obj,start),target=f(obj,end)))
    send(r,dict(op='DEMO',scope='SIM',scene=scene,action=action,before=f('exemplar',start),after=f('exemplar',end)))
    res=send(r,dict(op='PLAN',scope='SIM',scene=scene))
    return r,res,r.poll(100)

def requests(events):return [e for e in events if e.get('type')=='ACTION_REQUEST']

def test_frozen_red_host_dispatch_and_pending_not_executed():
    r,plan,events=session()
    aid=plan['cognitive']['action_id']
    assert any(e.get('requestId')==aid and e.get('action')=='TAKE' and e.get('object')=='BALL' for e in requests(events))
    assert r.cognitive_actions[aid]['status']=='PROPOSED_NOT_EXECUTED'
    assert not any(e.get('type')=='SIM_RECEIPT' for e in events)

def test_unbound_host_cannot_promote():
    r,plan,_=session()
    aid=plan['cognitive']['action_id']
    assert r.sim_action_receipt({'action_id':aid,'success':True})['error']=='SIM_HOST_NOT_BOUND'
    assert r.cognitive_goals[r.cognitive_actions[aid]['goal_id']]['status']=='OPEN'

def test_no_host_dispatch_outside_home_or_without_typed_before():
    for scene in ('room','story','HOME'):
        r,p,e=session(scene=scene)
        assert not requests(e)
    r,p,e=session(obj='MALWARE')
    assert not requests(e)

def test_no_duplicate_host_request_while_pending():
    r,p,ev=session()
    send(r,dict(op='PLAN',scope='SIM',scene='home'))
    assert len(requests(r.poll(100)))==0
    assert len(requests(ev))==1

def test_wrong_sim_host_receipt_rejected():
    r,p,e=session();aid=p['cognitive']['action_id']
    r.bind_sim_receipt_adapter(lambda raw:dict(raw))
    bad={'action_id':aid,'success':True,'observed_action':'LOOK','observed_before':f('BALL','floor-left'),
        'observed_after':f('BALL','held'),'receipt_id':'native-001','root_id':'host-001'}
    with pytest.raises(ValueError,match='WRONG_ACTION'):
        r.sim_action_receipt(bad)
    assert r.cognitive_actions[aid]['status']=='PROPOSED_NOT_EXECUTED'

def test_good_host_sim_receipt_and_replay_safe():
    r,p,e=session();aid=p['cognitive']['action_id']
    r.bind_sim_receipt_adapter(lambda raw:dict(raw))
    receipt={'action_id':aid,'success':True,'observed_action':'TAKE','observed_before':f('BALL','floor-left'),
             'observed_after':f('BALL','held'),'receipt_id':'native-001','root_id':'host-001'}
    out=r.sim_action_receipt(receipt)
    assert out['goal_status']=='ACHIEVED_SIM'
    assert r.cognitive_actions[aid]['status']=='SIM_SUCCESS'
    with pytest.raises(ValueError,match='NO_PENDING_ACTION'):
        r.sim_action_receipt(receipt)

def test_unexecuted_request_survives_cold_without_reissuing():
    r,p,e=session()
    from c4child.checkpoint import save_c4m_compact,load_c4m_compact
    from tempfile import TemporaryDirectory
    from pathlib import Path
    with TemporaryDirectory() as d:
        path=Path(d)/'a.c4m'
        save_c4m_compact(path,r.dialogue.g,runtime_state=r.runtime_state(),include_cold=True)
        g,h,m,rs=load_c4m_compact(path,with_runtime=True)
        newer=C4LivingRuntime(C4ChildDialogue(g));newer.load_runtime_state(rs)
        assert newer.cognitive_actions[p['cognitive']['action_id']]['status']=='PROPOSED_NOT_EXECUTED'
        assert not requests(newer.poll(100))


def native(r,aid,session='c4-foo',action='TAKE',obj='BALL',bef='floor-left',aft='held',success=True):
    return r.native_room_receipt({'requestId':aid,'action':action,'object':obj,
      'origin':'SANDBOX','world':'HOME','accepted':True,'executionSuccess':success,
      'before':{'location':bef},'after':{'location':aft}},session)

def test_native_bridge_verified_only_with_host_session():
    r,p,events=session();aid=p['cognitive']['action_id']
    assert native(r,aid)['error']=='NATIVE_SESSION_MISMATCH'
    r.bind_native_room_session('c4-foo')
    assert native(r,aid,session='c4-other')['error']=='NATIVE_SESSION_MISMATCH'
    assert native(r,aid,action='LOOK')['error']=='NATIVE_ACTION_WITNESS_INVALID'
    assert native(r,aid,bef='shelf')['error']=='NATIVE_STATE_WITNESS_INVALID'
    assert r.cognitive_actions[aid]['status']=='PROPOSED_NOT_EXECUTED'
    good=native(r,aid)
    assert good['accepted'] and good['goal_status']=='ACHIEVED_SIM'
    assert native(r,aid)['error']=='NATIVE_PENDING_ACTION_REQUIRED'

def test_host_session_not_restored_from_model():
    r,p,ev=session();r.bind_native_room_session('c4-prior')
    from c4child.checkpoint import save_c4m_compact,load_c4m_compact
    from tempfile import TemporaryDirectory
    from pathlib import Path
    with TemporaryDirectory() as d:
        path=Path(d)/'a.c4m'
        save_c4m_compact(path,r.dialogue.g,runtime_state=r.runtime_state(),include_cold=True)
        g,h,m,rs=load_c4m_compact(path,with_runtime=True)
        newer=C4LivingRuntime(C4ChildDialogue(g));newer.load_runtime_state(rs)
        assert newer.native_room_receipt({'requestId':p['cognitive']['action_id']},'c4-prior')['error']=='NATIVE_SESSION_MISMATCH'
