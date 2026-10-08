import json
from pathlib import Path
from c4child import C4LivingRuntime,C4ChildDialogue
from c4child import structured_cognition as sc
from c4child.checkpoint import load_c4m_compact, save_c4m_compact
import pytest


def msg(c,op,**kw):
    return c.user_message('@c4 '+json.dumps({'op':op,**kw},ensure_ascii=False))

def F(s,r,o):return {'subject':s,'relation':r,'object':o}

def test_real_runtime_same_graph_no_dup():
    c=C4LivingRuntime();graph=c.dialogue.g
    result=msg(c,'REPORT',fact=F('marmot','PROPERTY','warm'))
    assert c.dialogue.g is graph and len(graph.facts)==1
    f=list(graph.facts.values())[0]
    assert f.status=='SOURCE_ASSERTED' and f.origin=='USER_SAID'
    assert result['cognitive']['fact_id']==f.fact_id

def test_social_three_turns_link_and_genuine_reply():
    c=C4LivingRuntime()
    assert msg(c,'SOCIAL',act='PRAISE')['reply']=='Спасибо!'
    linked=msg(c,'SOCIAL',act='ACCEPT_THANKS')
    assert linked['cognitive']['prior_reply_event_id']
    assert 'Можем' in linked['reply']
    assert msg(C4LivingRuntime(),'SOCIAL',act='ACCEPT_THANKS')['cognitive']['status']=='UNRESOLVED_SOCIAL_REFERENCE'

def test_perspective_scope_scene_boundaries():
    c=C4LivingRuntime()
    frame=[{'actor':'Masha','mode':'BELIEF'},{'actor':'Ivan','mode':'QUOTE'}]
    msg(c,'REPORT',scope='STORY',scene='A',frames=frame,fact=F('object','COLOR','red'))
    assert msg(c,'QUERY',scope='STORY',scene='A',frames=frame,fact=F('object','COLOR','?'))['cognitive']['status']=='SOURCE_REPORTED'
    for key in ({'scope':'SOURCE','scene':'A','frames':frame}, {'scope':'STORY','scene':'B','frames':frame}, {'scope':'STORY','scene':'A','frames':frame[:-1]}):
        assert msg(c,'QUERY',**key,fact=F('object','COLOR','?'))['cognitive']['status']=='UNKNOWN'

def test_g215_conflict_is_not_calibrated_against_old_belief():
    c=C4LivingRuntime()
    msg(c,'REPORT',fact=F('moon','MATERIAL','cheese'))
    msg(c,'REPORT',fact=F('moon','MATERIAL','rock'))
    answer=msg(c,'QUERY',fact=F('moon','MATERIAL','?'))
    assert answer['cognitive']['status']=='CONFLICT'
    assert len(answer['cognitive']['basis'])==2
    assert set(f.source_group for f in c.dialogue.g.facts.values())=={'OTHER_CHAT_LINEAGE'}
    assert all(f.status=='SOURCE_ASSERTED' for f in c.dialogue.g.facts.values())
    assert not any('TRUST_PENALTY' in e.get('kind','') for e in c.life_events)

def test_not_world_through_text():
    c=C4LivingRuntime()
    r=msg(c,'REPORT',scope='WORLD',fact=F('moon','MATERIAL','cheese'))
    assert r['cognitive']['status']=='REJECTED'
    assert len(c.dialogue.g.facts)==0

@pytest.mark.parametrize('payload',[{'op':'REPORT','actor':'C4','fact':F('x','P','y')},
                                      {'op':'REPORT','verified':True,'fact':F('x','P','y')},
                                      {'op':'REPORT','delivered':True,'fact':F('x','P','y')},
                                      {'op':'GOAL','scope':'WORLD','target':F('x','P','y')},
                                      {'op':'PLAN','as_actor':'C4'},
                                      {'op':'REPORT','frames':[{'actor':'a','mode':'BELIEF'}]*13,'fact':F('x','P','y')},
                                      {'op':'REPORT','fact':{'subject':'x','relation':'P','object':'y','verified':True}},
                                      {'op':'DEMO','scope':'WORLD','before':F('x','P','y'),'after':F('x','P','z'),'action':'press'},
                                      {'op':'BAD'}])
def test_malicious_input_fail_closed_without_service_crash(payload):
    c=C4LivingRuntime();before=len(c.dialogue.g.facts)
    out=c.user_message('@c4 '+json.dumps(payload))
    assert out['cognitive']['status']=='REJECTED'
    assert len(c.dialogue.g.facts)==before
    assert any(e.get('kind')=='EVAL_STRUCTURED_REJECT' for e in c.life_events)

def test_invalid_json_survives():
    c=C4LivingRuntime();assert c.user_message('@c4 {') ['cognitive']['status']=='REJECTED'
    assert msg(c,'SOCIAL',act='GREET')['reply']=='Привет!'

def test_goal_and_cross_entity_procedural_transfer_no_fake_result():
    c=C4LivingRuntime()
    msg(c,'GOAL',scope='SIM',scene='room',target=F('lamp','LIGHT','ON'))
    msg(c,'DEMO',scope='SIM',scene='room',before=F('stone','LIGHT','OFF'),after=F('stone','LIGHT','ON'),action='press')
    a=msg(c,'PLAN',scope='SIM',scene='room')
    assert a['cognitive']['status']=='PROPOSED_NOT_EXECUTED'
    assert a['cognitive']['action']=='press'
    assert not any(ev.get('kind')=='MEDIATE_SIM_RECEIPT' for ev in c.life_events)
    assert msg(c,'REFLECT',scope='SIM',scene='room')['cognitive']['confirmed_sim']==0

def test_competing_strategies_after_negative_consequence():
    c=C4LivingRuntime()
    msg(c,'GOAL',scope='SIM',scene='world-a',target=F('lamp','LIT','YES'))
    for a in ['press','turn']:
        msg(c,'DEMO',scope='SIM',scene='world-a',action=a,before=F('seed','LIT','NO'),after=F('seed','LIT','YES'))
    first=msg(c,'PLAN',scope='SIM',scene='world-a')['cognitive']
    assert first['action'] in {'press','turn'}
    with pytest.raises(ValueError): sc.verified_sim_receipt(c,{'action_id':'unknown','success':True})
    assert c.handle_runtime_command('SIM_ACTION_RECEIPT',{'action_id':first['action_id'],'success':False})['accepted'] is False
    c.bind_sim_receipt_adapter(lambda payload:dict(payload))
    ok=c.handle_runtime_command('SIM_ACTION_RECEIPT',{'action_id':first['action_id'],'success':False})
    assert ok['status']=='SIM_FAILURE'
    second=msg(c,'PLAN',scope='SIM',scene='world-a')['cognitive']
    assert second['action']!=first['action']
    ok=c.handle_runtime_command('SIM_ACTION_RECEIPT',{'action_id':second['action_id'],'success':True})
    assert ok['status']=='SIM_SUCCESS'
    assert c.cognitive_goals[ok['goal_status'] if False else c.cognitive_actions[second['action_id']]['goal_id']]['status']=='ACHIEVED_SIM'
    assert msg(c,'REFLECT',scope='SIM',scene='world-a')['cognitive']['confirmed_sim']==2
    assert all(f.origin!='SIM' for f in c.dialogue.g.facts.values())

def test_no_sim_learning_in_world_or_other_scene():
    c=C4LivingRuntime()
    msg(c,'GOAL',scope='SIM',scene='scene-B',target=F('o','COLOR','RED'))
    msg(c,'DEMO',scope='SIM',scene='scene-A',action='paint',before=F('x','COLOR','WHITE'),after=F('x','COLOR','RED'))
    assert msg(c,'PLAN',scope='SIM',scene='scene-B')['cognitive']['status']=='NO_MODEL'

def test_no_proof_from_repeated_user_labels():
    c=C4LivingRuntime()
    msg(c,'DEMO',scope='SIM',scene='sim',action='jump',before=F('a','Y','0'),after=F('a','Y','1'))
    msg(c,'DEMO',scope='SIM',scene='sim',action='jump',before=F('b','Y','0'),after=F('b','Y','1'))
    assert set(d['source_root'] for d in c.cognitive_demonstrations)=={'OTHER_CHAT_LINEAGE'}
    assert not any(d['status']=='VERIFIED' for d in c.cognitive_demonstrations)

def test_cold_state_roundtrip_with_old_contract():
    c=C4LivingRuntime()
    msg(c,'REPORT',scope='STORY',scene='s',fact=F('a','COLOR','red'))
    msg(c,'GOAL',scope='SIM',scene='room',target=F('lamp','LIT','ON'))
    d=c.runtime_state();fresh=C4LivingRuntime(C4ChildDialogue(c.dialogue.g));fresh.load_runtime_state(d)
    assert fresh.runtime_state()['cognitive_g331']==d['cognitive_g331']
    assert msg(fresh,'QUERY',scope='STORY',scene='s',fact=F('a','COLOR','?'))['cognitive']['status']=='SOURCE_REPORTED'


def test_existing_runtime_russian_dialogue_unmodified():
    c=C4LivingRuntime();out=c.user_message('Привет')
    assert out.get('reply') is not None
    assert out.get('parsed',{}).get('kind')!='PSEUDO'


def test_real_c4m_original_graph_conserved(tmp_path):
    path=Path('/mnt/data/files/C4_G329_ANDROID_CLEAN_ORGANISM.c4m')
    if not path.exists():pytest.skip('Real G329 state file not present in CI')
    graph,h,meta,rs=load_c4m_compact(path,with_runtime=True)
    c=C4LivingRuntime(C4ChildDialogue(graph));c.load_runtime_state(rs or {})
    original_facts=len(graph.facts)
    msg(c,'SOCIAL',act='PRAISE')
    msg(c,'REPORT',scope='STORY',scene='episode',fact=F('key','LOCATION','desk'))
    path2=tmp_path/'cold.c4m'
    save_c4m_compact(path2,c.dialogue.g,h3=h,meta=meta,runtime_state=c.runtime_state(),include_cold=True)
    graph2,h2,meta2,rs2=load_c4m_compact(path2,with_runtime=True)
    new=C4LivingRuntime(C4ChildDialogue(graph2));new.load_runtime_state(rs2)
    assert len(graph2.facts)==original_facts+1
    assert msg(new,'QUERY',scope='STORY',scene='episode',fact=F('key','LOCATION','?'))['cognitive']['status']=='SOURCE_REPORTED'
    assert rs2['cognitive_g331']['goals']=={}
