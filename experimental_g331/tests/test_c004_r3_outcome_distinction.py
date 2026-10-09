"""C004-R3: host action execution is not the same as predicted goal success."""
import json
from c4child import C4ChildDialogue, C4LivingRuntime

def speak(r,msg):
    return r.user_message('@c4 '+json.dumps(msg))

def fact(subject,location):
    return {'subject':subject,'relation':'LOCATION','object':location}

def scenario(obj='BALL',action='LOOK',initial='floor-left',target='held'):
    r=C4LivingRuntime(C4ChildDialogue())
    speak(r,{'op':'GOAL','scope':'SIM','scene':'home','initial':fact(obj,initial),'target':fact(obj,target)})
    speak(r,{'op':'DEMO','scope':'SIM','scene':'home','action':action,'before':fact('EXAMPLE',initial),'after':fact('EXAMPLE',target)})
    plan=speak(r,{'op':'PLAN','scope':'SIM','scene':'home'})
    return r,plan['cognitive']['action_id']

def native(r,aid,action='LOOK',obj='BALL',before='floor-left',after='floor-left',success=True):
    r.bind_native_room_session('c4-r3')
    receipt={'requestId':aid,'action':action,'object':obj,'origin':'SANDBOX','world':'HOME',
             'accepted':True,'executionSuccess':success,
             'before':{'location':before},'after':{'location':after}}
    return r.native_room_receipt(receipt,'c4-r3')

def test_frozen_red_look_executed_but_expected_transition_missing():
    r,aid=scenario()
    out=native(r,aid)
    assert out['accepted'] and out['goal_status']=='OPEN'
    a=r.cognitive_actions[aid]
    assert a['status']=='SIM_FAILURE'
    assert a['execution_success'] is True
    assert a['prediction_confirmed'] is False
    assert a['observed_after']==fact('BALL','floor-left')
    assert r.cognitive_goals[a['goal_id']]['current']==fact('BALL','floor-left')

def test_host_execution_success_does_not_turn_false_effect_into_credit():
    r,aid=scenario()
    native(r,aid)
    assert native(r,aid)['error']=='NATIVE_PENDING_ACTION_REQUIRED'
    assert r.cognitive_goals[r.cognitive_actions[aid]['goal_id']]['status']=='OPEN'

def test_counterexample_transfers_to_unseen_subject_and_before_state():
    r,aid=scenario('BOOK','LOOK','shelf','held')
    out=native(r,aid,obj='BOOK',before='shelf',after='shelf')
    assert out['accepted'] and out['goal_status']=='OPEN'
    assert r.cognitive_actions[aid]['status']=='SIM_FAILURE'
    assert r.cognitive_actions[aid]['observed_after']==fact('BOOK','shelf')

def test_failed_actuator_does_not_get_success_credit_even_when_state_matches_goal():
    r,aid=scenario('BALL','TAKE','floor-left','held')
    out=native(r,aid,action='TAKE',after='held',success=False)
    assert out['accepted'] and out['goal_status']=='OPEN'
    assert r.cognitive_actions[aid]['status']=='SIM_FAILURE'
    assert r.cognitive_actions[aid]['execution_success'] is False

def test_successful_actuator_and_expected_transition_still_succeed():
    r,aid=scenario('BALL','TAKE','floor-left','held')
    out=native(r,aid,action='TAKE',after='held')
    assert out['accepted'] and out['goal_status']=='ACHIEVED_SIM'
    assert r.cognitive_actions[aid]['status']=='SIM_SUCCESS'
    assert r.cognitive_actions[aid]['prediction_confirmed'] is True

def test_wrong_before_witness_is_rejected_not_learning_feedback():
    r,aid=scenario()
    out=native(r,aid,before='shelf',after='shelf')
    assert out['error']=='NATIVE_STATE_WITNESS_INVALID'
    assert r.cognitive_actions[aid]['status']=='PROPOSED_NOT_EXECUTED'

def test_cold_reload_retains_negative_prediction_evidence_without_host_authority():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from c4child.checkpoint import save_c4m_compact,load_c4m_compact
    r,aid=scenario()
    assert native(r,aid)['accepted']
    with TemporaryDirectory() as d:
        p=Path(d)/'organism.c4m'
        save_c4m_compact(p,r.dialogue.g,runtime_state=r.runtime_state(),include_cold=True)
        g,h,m,rs=load_c4m_compact(p,with_runtime=True)
        new=C4LivingRuntime(C4ChildDialogue(g))
        new.load_runtime_state(rs)
        a=new.cognitive_actions[aid]
        assert a['status']=='SIM_FAILURE'
        assert a['execution_success'] is True and a['prediction_confirmed'] is False
        assert new.cognitive_goals[a['goal_id']]['status']=='OPEN'
        assert new.native_room_receipt({'requestId':aid},'c4-r3')['error']=='NATIVE_SESSION_MISMATCH'

def test_contradictory_take_success_rejected_without_reward():
    import pytest
    r,aid=scenario('BALL','TAKE','floor-left','held')
    with pytest.raises(ValueError,match='SIM_OBSERVATION_CONTRADICTS_SUCCESS'):
        native(r,aid,action='TAKE',after='floor-left',success=True)
    assert r.cognitive_actions[aid]['status']=='PROPOSED_NOT_EXECUTED'

def test_contradictory_place_success_rejected_without_reward():
    import pytest
    r,aid=scenario('BALL','PLACE','held','basket')
    with pytest.raises(ValueError,match='SIM_OBSERVATION_CONTRADICTS_SUCCESS'):
        native(r,aid,action='PLACE',before='held',after='floor-right',success=True)
    assert r.cognitive_actions[aid]['status']=='PROPOSED_NOT_EXECUTED'
