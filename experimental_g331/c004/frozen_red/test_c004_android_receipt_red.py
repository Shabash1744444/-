"""C004 frozen RED: native action receipt must not be confused with speech.
Run against the unchanged C003 runtime before implementing Android integration.
"""
import json
from c4child import C4ChildDialogue, C4LivingRuntime

def scenario():
    r = C4LivingRuntime(C4ChildDialogue())
    def send(x):
        return r.user_message('@c4 ' + json.dumps(x, ensure_ascii=False))
    send({'op':'GOAL','scope':'SIM','scene':'home',
          'initial':{'subject':'BALL','relation':'LOCATION','object':'floor-left'},
          'target':{'subject':'BALL','relation':'LOCATION','object':'held'}})
    send({'op':'DEMO','scope':'SIM','scene':'home','action':'TAKE',
          'before':{'subject':'SAMPLE','relation':'LOCATION','object':'floor-left'},
          'after':{'subject':'SAMPLE','relation':'LOCATION','object':'held'}})
    plan=send({'op':'PLAN','scope':'SIM','scene':'home'})
    events=r.poll(100)
    return r,plan,events

def test_c4_action_proposal_has_unambiguous_host_dispatch():
    r,plan,events=scenario()
    aid=plan['cognitive']['action_id']
    assert any(e.get('kind')=='ACTION_REQUEST' and e.get('requestId')==aid
               and e.get('action')=='TAKE' and e.get('object')=='BALL'
               for e in events), 'NO_NATIVE_HOST_ACTION_REQUEST: PLAN emitted REPLY only'
    assert r.cognitive_actions[aid]['status']=='PROPOSED_NOT_EXECUTED'

def test_unbound_receipt_does_not_claim_execution():
    r,plan,_=scenario()
    aid=plan['cognitive']['action_id']
    result=r.sim_action_receipt({'action_id':aid,'success':True})
    assert result['error']=='SIM_HOST_NOT_BOUND'
    assert r.cognitive_actions[aid]['status']=='PROPOSED_NOT_EXECUTED'
