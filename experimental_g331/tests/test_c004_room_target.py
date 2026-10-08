"""C004-R2: native host must execute the very destination chosen by C4 DRIVE.
No Android attestation is inferred from these unit tests.
"""
import json
import pytest
from c4child import C4LivingRuntime,C4ChildDialogue

def fact(sub,obj):return {'subject':sub,'relation':'LOCATION','object':obj}
def propose(action='PLACE',destination='basket',start='held',subject='BALL'):
    r=C4LivingRuntime(C4ChildDialogue())
    def put(p):return r.user_message('@c4 '+json.dumps(p))
    put({'op':'GOAL','scope':'SIM','scene':'home','initial':fact(subject,start),'target':fact(subject,destination)})
    put({'op':'DEMO','scope':'SIM','scene':'home','action':action,'before':fact('TRAINING_OBJECT',start),'after':fact('TRAINING_OBJECT',destination)})
    response=put({'op':'PLAN','scope':'SIM','scene':'home'})
    return r,response,[x for x in r.poll(100) if x.get('type')=='ACTION_REQUEST']

@pytest.mark.parametrize('verb,place',[('PLACE','basket'),('RELEASE','desk'),('PLACE','shelf'),('RELEASE','floor-left')])
def test_plan_destination_is_preserved_in_native_request(verb,place):
    r,res,requests=propose(verb,place)
    assert len(requests)==1
    a=requests[0]
    assert a['target']==place
    assert a['requestId']==res['cognitive']['action_id']
    assert r.cognitive_actions[a['requestId']]['status']=='PROPOSED_NOT_EXECUTED'

@pytest.mark.parametrize('bad_destination',['UNREGISTERED','../../escape','held','BALL'])
def test_unsupported_destinations_have_no_native_dispatch(bad_destination):
    r,res,requests=propose('PLACE',bad_destination)
    assert not requests
    if res['cognitive'].get('action_id'):
        assert r.cognitive_actions[res['cognitive']['action_id']]['status']=='PROPOSED_NOT_EXECUTED'
    else:
        assert res['cognitive']['status']=='ALREADY_REACHED'

def test_take_does_not_add_spurious_place_target():
    r,res,requests=propose('TAKE','held',start='floor-left')
    assert len(requests)==1
    assert requests[0]['action']=='TAKE'
    assert 'target' not in requests[0]

def test_native_receipt_only_admits_exact_destination():
    r,res,req=propose('PLACE','basket')
    aid=res['cognitive']['action_id']
    r.bind_native_room_session('c4-native-target-test')
    receipt={'requestId':aid,'action':'PLACE','object':'BALL','accepted':True,'executionSuccess':True,
             'origin':'SANDBOX','world':'HOME','before':{'location':'held'},'after':{'location':'floor-right'}}
    with pytest.raises(ValueError,match='SIM_OBSERVATION_CONTRADICTS_SUCCESS'):
        r.native_room_receipt(receipt,'c4-native-target-test')
    assert r.cognitive_actions[aid]['status']=='PROPOSED_NOT_EXECUTED'
    receipt['after']['location']='basket'
    assert r.native_room_receipt(receipt,'c4-native-target-test')['goal_status']=='ACHIEVED_SIM'
