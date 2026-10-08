"""C002 frozen unseen contract: nested perspectives and event time, not lexical answer templates."""
import json
import pytest
from c4child import C4LivingRuntime


def send(c, op, **fields):
    return c.user_message('@c4 '+json.dumps(dict(op=op,**fields),ensure_ascii=False))


def f(who, verb, what):
    return dict(subject=who,relation=verb,object=what)


@pytest.mark.parametrize('who,verb,was,now,scene',[('Taro','LOCATION','dock','tower','novel'),('Lena','COLOR','green','violet','dream'),('Oak','STATE','closed','open','game')])
def test_nested_report_vs_real_world_and_relative_time(who,verb,was,now,scene):
    c=C4LivingRuntime()
    frames=[{'actor':'Ada','mode':'BELIEF'},{'actor':'Taro','mode':'QUOTE'}]
    x=send(c,'REPORT',scope='STORY',scene=scene,frames=frames,
           time={'utterance_day':13,'about':{'basis':'UTTERANCE','offset_days':2}},fact=f(who,verb,was))
    assert x['cognitive']['status']=='SOURCE_ASSERTED'
    event=x['inbound_event']['event_id']
    # Distinguish time of *represented event* (day 15) from day of original speech (13).
    query=dict(scope='STORY',scene=scene,frames=frames,fact=f(who,verb,'?'))
    assert send(c,'QUERY',**query,time={'about_day':15})['cognitive']['values']==[was]
    assert send(c,'QUERY',**query,time={'about_day':13})['cognitive']['values']==[]
    assert send(c,'QUERY',scope='STORY',scene=scene,fact=f(who,verb,'?'),time={'about_day':15})['cognitive']['values']==[]
    # A subsequent utterance may anchor its represented time to a previous event's content.
    second=send(c,'REPORT',scope='STORY',scene=scene,frames=frames,
                time={'utterance_day':16,'about':{'basis':'SOURCE_CONTENT','event_id':event,'offset_days':1}},fact=f(who,verb,now))
    assert second['cognitive']['status']=='SOURCE_ASSERTED'
    assert send(c,'QUERY',**query,time={'about_day':16})['cognitive']['values']==[now]
    assert send(c,'QUERY',**query,time={'about_day':15})['cognitive']['values']==[was]
    assert len(c.dialogue.g.facts)==2


def test_telemetry_three_times_and_cold_reload(tmp_path):
    from c4child import C4ChildDialogue
    from c4child.checkpoint import save_c4m_compact,load_c4m_compact
    c=C4LivingRuntime()
    p=dict(scope='STORY',scene='indigo',frames=[{'actor':'R','mode':'QUOTE'}],fact=f('globe','STATE','lit'))
    send(c,'REPORT',**p,time={'utterance_day':-8,'about':{'basis':'UTTERANCE','offset_days':4}})
    fid=next(iter(c.dialogue.g.facts.values())).source_ref
    row=c.semantic_spine.events[fid]
    t=row['c4_temporal']
    assert t['claimed_utterance_day']==-8 and t['about_day']==-4
    assert t['known_turn']==row['external_order'] and isinstance(row['wall_time'],float)
    assert t['basis']=='UTTERANCE'
    assert send(c,'QUERY',scope=p['scope'],scene=p['scene'],frames=p['frames'],fact=f('globe','STATE','?'),time={'about_day':-4})['cognitive']['values']==['lit']
    path=tmp_path/'native.c4m'
    save_c4m_compact(path,c.dialogue.g,runtime_state=c.runtime_state(),include_cold=True)
    g,h,m,rs=load_c4m_compact(path,with_runtime=True)
    cold=C4LivingRuntime(C4ChildDialogue(g));cold.load_runtime_state(rs)
    assert cold.semantic_spine.events[fid]['c4_temporal']==t
    assert send(cold,'QUERY',scope=p['scope'],scene=p['scene'],frames=p['frames'],fact=f('globe','STATE','?'),time={'about_day':-4})['cognitive']['values']==['lit']
    assert send(cold,'QUERY',scope=p['scope'],scene=p['scene'],frames=p['frames'],fact=f('globe','STATE','?'),time={'about_day':-3})['cognitive']['status']=='UNKNOWN'


def test_temporal_source_correction_is_slot_scoped():
    c=C4LivingRuntime()
    p=dict(scope='STORY',scene='amber',frames=[{'actor':'speaker','mode':'BELIEF'}])
    a=send(c,'REPORT',**p,fact=f('rope','STATE','weak'),time={'utterance_day':5,'about':{'basis':'UTTERANCE','offset_days':1}})
    first=a['inbound_event']['event_id']
    wrong=send(c,'CORRECT',**p,replaces=first,fact=f('rope','STATE','strong'),time={'utterance_day':7,'about':{'basis':'UTTERANCE','offset_days':2}})
    assert wrong['cognitive']['status']=='REJECTED'
    good=send(c,'CORRECT',**p,replaces=first,fact=f('rope','STATE','strong'),time={'utterance_day':7,'about':{'basis':'UTTERANCE','offset_days':-1}})
    assert good['cognitive']['status']=='SOURCE_CORRECTED'
    q=dict(**p,fact=f('rope','STATE','?'),time={'about_day':6})
    assert send(c,'QUERY',**q)['cognitive']['values']==['strong']
    assert send(c,'QUERY',**q,as_of_turn=1)['cognitive']['values']==['weak']


def test_ambiguous_temporal_reference_rejected_without_mutation():
    c=C4LivingRuntime()
    a=send(c,'REPORT',scope='STORY',scene='inside',fact=f('bar','STATE','quiet'),time={'utterance_day':12,'about':{'basis':'UTTERANCE','offset_days':0}})
    eid=a['inbound_event']['event_id']
    n=len(c.dialogue.g.facts)
    bad=[
        dict(scope='STORY',scene='outside',fact=f('bar','STATE','loud'),time={'utterance_day':15,'about':{'basis':'SOURCE_CONTENT','event_id':eid,'offset_days':0}}),
        dict(scope='STORY',scene='inside',fact=f('bar','STATE','loud'),time={'utterance_day':15,'about':{'basis':'SOURCE_CONTENT','event_id':'fake','offset_days':0}}),
        dict(scope='STORY',scene='inside',fact=f('bar','STATE','loud'),time={'utterance_day':15,'about':{'basis':'UTTERANCE','offset_days':True}}),
        dict(scope='STORY',scene='inside',fact=f('bar','STATE','loud'),time={'about':{'basis':'UTTERANCE','offset_days':0}}),
    ]
    for fields in bad:
        out=send(c,'REPORT',**fields)
        assert out['cognitive']['status']=='REJECTED'
        assert len(c.dialogue.g.facts)==n
    assert all(x.status=='SOURCE_ASSERTED' for x in c.dialogue.g.facts.values())


def test_g215_nonpenalization_even_when_temporal_claims_conflict():
    c=C4LivingRuntime()
    k=dict(scope='SOURCE',scene='glass',fact=f('bird','STATE','sleeping'),time={'utterance_day':2,'about':{'basis':'UTTERANCE','offset_days':0}})
    send(c,'REPORT',**k)
    send(c,'REPORT',scope='SOURCE',scene='glass',fact=f('bird','STATE','flying'),time={'utterance_day':2,'about':{'basis':'UTTERANCE','offset_days':0}})
    q=send(c,'QUERY',scope='SOURCE',scene='glass',fact=f('bird','STATE','?'),time={'about_day':2})
    assert q['cognitive']['status']=='CONFLICT'
    assert not any('TRUST_PENALTY' in str(x) for x in c.life_events)
    assert all(x.status=='SOURCE_ASSERTED' for x in c.dialogue.g.facts.values())

def test_correction_without_utterance_date_inherits_target_not_speech_time():
    c=C4LivingRuntime()
    p={'scope':'STORY','scene':'revise'}
    e=send(c,'REPORT',**p,fact=f('book','STATE','lost'),time={'utterance_day':27,'about':{'basis':'UTTERANCE','offset_days':3}})
    old=e['inbound_event']['event_id']
    n=send(c,'CORRECT',**p,replaces=old,fact=f('book','STATE','found'))
    assert n['cognitive']['status']=='SOURCE_CORRECTED'
    t=c.semantic_spine.events[n['inbound_event']['event_id']]['c4_temporal']
    assert t['about_day']==30
    assert t['claimed_utterance_day'] is None
    assert t['basis']=='INHERITED_TARGET_ONLY'
    assert send(c,'QUERY',**p,fact=f('book','STATE','?'),time={'about_day':30})['cognitive']['values']==['found']
