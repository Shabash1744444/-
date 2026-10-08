"""C003 FROZEN RED: native C4 SIM action hypotheses, receipts and dependency roots."""
import json
import pytest
from c4child import C4LivingRuntime, C4ChildDialogue
from c4child.checkpoint import save_c4m_compact,load_c4m_compact


def send(c,op,**p):
    return c.user_message('@c4 '+json.dumps({'op':op,**p},ensure_ascii=False))['cognitive']

def fact(s,r,o):return {'subject':s,'relation':r,'object':o}

def setup(c,scene='toy',target='glow'):
    start=fact('new_obj','PHASE','sealed')
    send(c,'GOAL',scope='SIM',scene=scene,initial=start,target=fact('new_obj','PHASE',target))
    for action,a,b in [('release','sealed','opened'),('ignite','opened','glow')]:
        send(c,'DEMO',scope='SIM',scene=scene,action=action,
             before=fact('old_obj','PHASE',a),after=fact('old_obj','PHASE',b))


def test_multi_step_holdout_binds_each_delayed_host_result_to_next_step():
    c=C4LivingRuntime();setup(c)
    a=send(c,'PLAN',scope='SIM',scene='toy')
    assert a['action']=='release'
    aid=a['action_id']
    # Speech cannot make a simulation outcome or impersonate the host.
    assert send(c,'REFLECT',scope='SIM',scene='toy')['confirmed_sim']==0
    assert c.sim_action_receipt({'action_id':aid,'success':True})['accepted'] is False
    c.bind_sim_receipt_adapter(lambda item: dict(item))
    # Legacy boolean success is not a witnessed transition for a chained goal.
    r=c.sim_action_receipt({'action_id':aid,'success':True})
    assert r['status']=='SIM_UNVERIFIED_TRANSITION'
    assert c.cognitive_goals[c.cognitive_actions[aid]['goal_id']]['current']['object']=='sealed'
    again=send(c,'PLAN',scope='SIM',scene='toy')
    assert again['action']=='release'
    r=c.sim_action_receipt({'action_id':again['action_id'],'success':True,
                            'observed_action':'release','observed_before':fact('new_obj','PHASE','sealed'),
                            'observed_after':fact('new_obj','PHASE','opened'),
                            'receipt_id':'host-a','root_id':'physics-cycle-a'})
    assert r['status']=='SIM_SUCCESS'
    assert c.cognitive_goals[c.cognitive_actions[aid]['goal_id']]['status']=='OPEN'
    b=send(c,'PLAN',scope='SIM',scene='toy')
    assert b['action']=='ignite'
    assert b['action_id']!=again['action_id']
    r=c.sim_action_receipt({'action_id':b['action_id'],'success':True,
                            'observed_action':'ignite','observed_before':fact('new_obj','PHASE','opened'),
                            'observed_after':fact('new_obj','PHASE','glow'),
                            'receipt_id':'host-b','root_id':'physics-cycle-b'})
    assert r['status']=='SIM_SUCCESS'
    assert c.cognitive_goals[c.cognitive_actions[b['action_id']]['goal_id']]['status']=='ACHIEVED_SIM'


def test_host_failure_does_not_skip_causal_step_and_world_remains_empty():
    c=C4LivingRuntime();setup(c,scene='S')
    c.bind_sim_receipt_adapter(lambda x:dict(x))
    first=send(c,'PLAN',scope='SIM',scene='S')
    c.sim_action_receipt({'action_id':first['action_id'],'success':False,
                          'receipt_id':'f','root_id':'r'})
    g=c.cognitive_goals[c.cognitive_actions[first['action_id']]['goal_id']]
    assert g['current']['object']=='sealed' and g['status']=='OPEN'
    assert not c.dialogue.g.facts
    assert send(c,'PLAN',scope='SIM',scene='S').get('action')!='ignite'


def test_host_mismatch_rejects_incorrect_success_without_state_mutation():
    c=C4LivingRuntime();setup(c)
    c.bind_sim_receipt_adapter(lambda x:dict(x))
    p=send(c,'PLAN',scope='SIM',scene='toy')
    with pytest.raises(ValueError):
        c.sim_action_receipt({'action_id':p['action_id'],'success':True,
                              'observed_action':'ignite','observed_before':fact('new_obj','PHASE','opened'),
                            'observed_after':fact('new_obj','PHASE','glow'),
                              'receipt_id':'false','root_id':'r'})
    assert c.cognitive_actions[p['action_id']]['status']=='PROPOSED_NOT_EXECUTED'
    assert c.cognitive_goals[c.cognitive_actions[p['action_id']]['goal_id']]['current']['object']=='sealed'


def test_dependent_host_feedback_is_not_treated_as_independent_corroborration():
    c=C4LivingRuntime();scene='independent'
    send(c,'DEMO',scope='SIM',scene=scene,action='press',before=fact('x','STATE','OFF'),after=fact('x','STATE','ON'))
    c.bind_sim_receipt_adapter(lambda x:dict(x))
    for i in range(2):
        send(c,'GOAL',scope='SIM',scene=scene,target=fact('a'+str(i),'STATE','ON'))
        p=send(c,'PLAN',scope='SIM',scene=scene)
        c.sim_action_receipt({'action_id':p['action_id'],'success':True,'root_id':'same-original-experiment', 'receipt_id':'receipt-'+str(i)})
    counts=send(c,'REFLECT',scope='SIM',scene=scene)
    assert counts['independent_sim_roots']==1
    assert counts['confirmed_sim']==2
    assert len({d['source_root'] for d in c.cognitive_demonstrations})==1
    assert not any('TRUST_PENALTY' in str(x) for x in c.life_events)


def test_multi_step_goal_persists_checkpoint_with_pending_action(tmp_path):
    c=C4LivingRuntime();setup(c,scene='save')
    c.bind_sim_receipt_adapter(lambda x:dict(x))
    p=send(c,'PLAN',scope='SIM',scene='save')
    c.sim_action_receipt({'action_id':p['action_id'],'success':True,
                          'observed_action':'release','observed_before':fact('new_obj','PHASE','sealed'),
                            'observed_after':fact('new_obj','PHASE','opened'),
                          'receipt_id':'save-r1','root_id':'save-root-1'})
    path=tmp_path/'state.c4m'
    save_c4m_compact(path,c.dialogue.g,runtime_state=c.runtime_state(),include_cold=True)
    g,h,manifest,rs=load_c4m_compact(path,with_runtime=True)
    cold=C4LivingRuntime(C4ChildDialogue(g));cold.load_runtime_state(rs)
    p2=send(cold,'PLAN',scope='SIM',scene='save')
    assert p2['action']=='ignite'
    assert not cold.dialogue.g.facts

@pytest.mark.parametrize('seed',range(12))
def test_heldout_three_step_symbolic_transfer(seed):
    c=C4LivingRuntime();scene='random-scene-'+str(seed)
    starts=['a'+str(seed),'b'+str(seed),'c'+str(seed),'d'+str(seed)]
    target=fact('heldout-'+str(seed),'R'+str(seed),starts[3])
    send(c,'GOAL',scope='SIM',scene=scene,initial=fact(target['subject'],target['relation'],starts[0]),target=target)
    for i,act in enumerate(['verb-'+str(seed)+'-'+str(j) for j in range(3)]):
        send(c,'DEMO',scope='SIM',scene=scene,action=act,
             before=fact('training-other-'+str(i),target['relation'],starts[i]),
             after=fact('training-other-'+str(i),target['relation'],starts[i+1]))
    c.bind_sim_receipt_adapter(lambda p:dict(p))
    for i in range(3):
        p=send(c,'PLAN',scope='SIM',scene=scene)
        assert p['action']=='verb-'+str(seed)+'-'+str(i)
        wait=send(c,'PLAN',scope='SIM',scene=scene)
        assert wait['status']=='PENDING_RECEIPT'
        r=c.sim_action_receipt({'action_id':p['action_id'],'success':True,
                                'observed_action':p['action'],
                                'observed_before':fact(target['subject'],target['relation'],starts[i]),
                                'observed_after':fact(target['subject'],target['relation'],starts[i+1]),
                                'receipt_id':'simreceipt-'+str(seed)+'-'+str(i),
                                'root_id':'simroot-'+str(seed)+'-'+str(i)})
        assert r['status']=='SIM_SUCCESS'
        if i!=2: assert r['goal_status']=='OPEN'
    assert r['goal_status']=='ACHIEVED_SIM'
    assert not c.dialogue.g.facts


def test_bad_host_receipt_does_not_contaminate_plan_or_graph():
    c=C4LivingRuntime();setup(c)
    c.bind_sim_receipt_adapter(lambda d:dict(d))
    p=send(c,'PLAN',scope='SIM',scene='toy')
    bad=[{'observed_action':'ignite','observed_before':fact('new_obj','PHASE','sealed'),
          'observed_after':fact('new_obj','PHASE','opened')},
         {'observed_action':'release','observed_before':fact('other','PHASE','sealed'),
          'observed_after':fact('new_obj','PHASE','opened')},
         {'observed_action':'release','observed_before':fact('new_obj','PHASE','sealed'),
          'observed_after':fact('new_obj','PHASE','glow')}]
    for i,change in enumerate(bad):
        with pytest.raises(ValueError):
            c.sim_action_receipt({'action_id':p['action_id'],'success':True,
                'receipt_id':'invalid-'+str(i),'root_id':'r',**change})
        assert c.cognitive_actions[p['action_id']]['status']=='PROPOSED_NOT_EXECUTED'
    r=c.sim_action_receipt({'action_id':p['action_id'],'success':True,
        'observed_action':'release','observed_before':fact('new_obj','PHASE','sealed'),
        'observed_after':fact('new_obj','PHASE','opened'),'receipt_id':'unique','root_id':'r'})
    assert r['status']=='SIM_SUCCESS'
    new=send(c,'PLAN',scope='SIM',scene='toy')
    assert new['action']=='ignite'
    with pytest.raises(ValueError,match='SIM_RECEIPT_REPLAY'):
        c.sim_action_receipt({'action_id':new['action_id'],'success':True,'receipt_id':'unique',
            'root_id':'r','observed_action':'ignite',
            'observed_before':fact('new_obj','PHASE','opened'),
            'observed_after':fact('new_obj','PHASE','glow')})
    assert c.cognitive_goals[c.cognitive_actions[p['action_id']]['goal_id']]['status']=='OPEN'
    forged=send(c,'REPORT',scope='SIM',scene='toy',fact=fact('new_obj','PHASE','glow'),
                receipt={'success':True})
    assert forged['status']=='REJECTED'
    assert not c.dialogue.g.facts