import json
from c4child import C4LivingRuntime


def send(c, op, **fields):
    return c.user_message("@c4 " + json.dumps({"op": op, **fields}, ensure_ascii=False))

def fact(object_value):
    return {"subject":"lamp","relation":"COLOR","object":object_value}

def test_explicit_source_self_correction_and_historical_dialogue():
    c=C4LivingRuntime()
    first=send(c,"REPORT",scope="STORY",scene="novel",fact=fact("red"))
    original=first["inbound_event"]["event_id"]
    corrected=send(c,"CORRECT",scope="STORY",scene="novel",replaces=original,fact=fact("blue"))
    current=send(c,"QUERY",scope="STORY",scene="novel",fact=fact("?"))
    past=send(c,"QUERY",scope="STORY",scene="novel",fact=fact("?"),as_of_turn=1)
    assert corrected["cognitive"]["status"]=="SOURCE_CORRECTED"
    assert current["cognitive"]["status"]=="SOURCE_REPORTED"
    assert current["cognitive"]["values"]==["blue"]
    assert past["cognitive"]["values"]==["red"]
    assert not any("TRUST_PENALTY" in x.get("kind","") for x in c.life_events)


def test_unrelated_contradictions_remain_conflict_without_explicit_correction():
    c=C4LivingRuntime()
    send(c,'REPORT',scope='STORY',scene='alpha',fact={'subject':'seal','relation':'COLOR','object':'white'})
    send(c,'REPORT',scope='STORY',scene='alpha',fact={'subject':'seal','relation':'COLOR','object':'black'})
    out=send(c,'QUERY',scope='STORY',scene='alpha',fact={'subject':'seal','relation':'COLOR','object':'?'})
    assert out['cognitive']['status']=='CONFLICT'
    assert set(out['cognitive']['values'])=={'white','black'}


def test_history_after_two_corrections_and_different_entities():
    c=C4LivingRuntime()
    first=send(c,'REPORT',scope='STORY',scene='history',fact={'subject':'seal','relation':'COLOR','object':'white'})
    e1=first['inbound_event']['event_id']
    second=send(c,'CORRECT',scope='STORY',scene='history',replaces=e1,fact={'subject':'seal','relation':'COLOR','object':'blue'})
    e2=second['inbound_event']['event_id']
    third=send(c,'CORRECT',scope='STORY',scene='history',replaces=e2,fact={'subject':'seal','relation':'COLOR','object':'purple'})
    assert third['cognitive']['status']=='SOURCE_CORRECTED'
    want={'subject':'seal','relation':'COLOR','object':'?'}
    for when,expected in [(1,'white'),(2,'blue'),(3,'purple')]:
        q=send(c,'QUERY',scope='STORY',scene='history',fact=want,as_of_turn=when)
        assert q['cognitive']['values']==[expected]
    assert send(c,'QUERY',scope='STORY',scene='history',fact=want)['cognitive']['values']==['purple']
    assert len(c.dialogue.g.facts)==3
    assert len([f for f in c.dialogue.g.facts.values() if f.status=='SOURCE_SUPERSEDED'])==2


def test_correction_never_changes_other_scope_or_utterance():
    c=C4LivingRuntime()
    origin=send(c,'REPORT',scope='STORY',scene='diary',fact={'subject':'animal','relation':'COLOR','object':'gold'})
    eid=origin['inbound_event']['event_id']
    other=send(c,'REPORT',scope='STORY',scene='separate',fact={'subject':'animal','relation':'COLOR','object':'silver'})
    old_state=len(c.dialogue.g.facts)
    for fields in [
        {'scope':'STORY','scene':'separate','replaces':eid,'fact':{'subject':'animal','relation':'COLOR','object':'copper'}},
        {'scope':'SOURCE','scene':'diary','replaces':eid,'fact':{'subject':'animal','relation':'COLOR','object':'copper'}},
        {'scope':'STORY','scene':'diary','replaces':eid,'fact':{'subject':'another','relation':'COLOR','object':'copper'}},
        {'scope':'STORY','scene':'diary','replaces':eid,'fact':{'subject':'animal','relation':'LOCATION','object':'tree'}},
        {'scope':'STORY','scene':'diary','replaces':'in:forged','fact':{'subject':'animal','relation':'COLOR','object':'copper'}}
    ]:
        assert send(c,'CORRECT',**fields)['cognitive']['status']=='REJECTED'
        assert len(c.dialogue.g.facts)==old_state
    assert send(c,'QUERY',scope='STORY',scene='diary',fact={'subject':'animal','relation':'COLOR','object':'?'})['cognitive']['values']==['gold']
    assert send(c,'QUERY',scope='STORY',scene='separate',fact={'subject':'animal','relation':'COLOR','object':'?'})['cognitive']['values']==['silver']
    assert other['inbound_event']['event_id']!=eid


def test_invalid_time_and_future_query_never_rewrite_past():
    c=C4LivingRuntime()
    send(c,'REPORT',fact={'subject':'sky','relation':'COLOR','object':'blue'})
    before=len(c.dialogue.g.facts)
    for bad in ['2',-1,True,1.5]:
        assert send(c,'QUERY',fact={'subject':'sky','relation':'COLOR','object':'?'},as_of_turn=bad)['cognitive']['status']=='REJECTED'
    assert send(c,'QUERY',fact={'subject':'sky','relation':'COLOR','object':'?'},as_of_turn=1000)['cognitive']['status']=='REJECTED'
    assert len(c.dialogue.g.facts)==before


def test_correction_cold_reload_true_c4m(tmp_path):
    from pathlib import Path
    from c4child import C4ChildDialogue
    from c4child.checkpoint import save_c4m_compact,load_c4m_compact
    c=C4LivingRuntime()
    e=send(c,'REPORT',scope='STORY',scene='past',fact={'subject':'crate','relation':'COLOR','object':'white'})['inbound_event']['event_id']
    send(c,'CORRECT',scope='STORY',scene='past',replaces=e,fact={'subject':'crate','relation':'COLOR','object':'black'})
    path=Path(tmp_path)/'model.c4m'
    save_c4m_compact(path,c.dialogue.g,runtime_state=c.runtime_state(),include_cold=True)
    graph,h,meta,rs=load_c4m_compact(path,with_runtime=True)
    fresh=C4LivingRuntime(C4ChildDialogue(graph));fresh.load_runtime_state(rs)
    q={'scope':'STORY','scene':'past','fact':{'subject':'crate','relation':'COLOR','object':'?'}}
    assert send(fresh,'QUERY',**q)['cognitive']['values']==['black']
    assert send(fresh,'QUERY',**q,as_of_turn=1)['cognitive']['values']==['white']
    assert len(graph.facts)==2
    assert sorted(f.status for f in graph.facts.values())==['SOURCE_ASSERTED','SOURCE_SUPERSEDED']


def test_source_correction_not_world_and_no_truth_trust_penalty():
    c=C4LivingRuntime()
    a=send(c,'REPORT',fact={'subject':'comet','relation':'MATERIAL','object':'ice'})
    send(c,'CORRECT',replaces=a['inbound_event']['event_id'],fact={'subject':'comet','relation':'MATERIAL','object':'dust'})
    assert all(f.status!='ADMITTED' for f in c.dialogue.g.facts.values())
    assert not any('TRUST_PENALTY' in x.get('kind','') for x in c.life_events)
    assert not any(x.get('kind')=='MEDIATE_SIM_RECEIPT' for x in c.life_events)


def test_native_entity_typed_relation_is_supported_without_world_promotion():
    c=C4LivingRuntime()
    out=send(c,'REPORT',fact={'subject':'cat','relation':'IS_A','object':'animal'})
    assert out['cognitive']['status']=='SOURCE_ASSERTED'
    f=next(iter(c.dialogue.g.facts.values()))
    assert f.object_kind=='entity' and c.dialogue.g.label(f.object_value)=='animal'
    q=send(c,'QUERY',fact={'subject':'cat','relation':'IS_A','object':'?'})
    assert q['cognitive']['values']==['animal']
    assert f.status=='SOURCE_ASSERTED'
    assert send(c,'SOCIAL',act='GREET')['reply']=='Привет!'


def test_real_g329_trained_entity_schema_cold_history(tmp_path):
    import pytest
    from pathlib import Path
    from c4child import C4ChildDialogue
    from c4child.checkpoint import load_c4m_compact,save_c4m_compact
    source=Path('/mnt/data/files/C4_G329_ANDROID_CLEAN_ORGANISM.c4m')
    if not source.exists():pytest.skip('G329 model binary unavailable in GitHub CI')
    g,h,meta,rs=load_c4m_compact(source,with_runtime=True)
    initial=len(g.facts)
    assert g.relation_spec('COLOR').object_mode=='entity'
    c=C4LivingRuntime(C4ChildDialogue(g));c.load_runtime_state(rs or {})
    first=send(c,'REPORT',scope='STORY',scene='unknown-room',fact={'subject':'prism','relation':'COLOR','object':'mint'})
    send(c,'CORRECT',scope='STORY',scene='unknown-room',replaces=first['inbound_event']['event_id'],
         fact={'subject':'prism','relation':'COLOR','object':'ochre'})
    assert len(g.facts)==initial+2
    path=tmp_path/'real_model_with_c001.c4m'
    save_c4m_compact(path,c.dialogue.g,h3=h,meta=meta,runtime_state=c.runtime_state(),include_cold=True)
    g2,h2,m2,rs2=load_c4m_compact(path,with_runtime=True)
    c2=C4LivingRuntime(C4ChildDialogue(g2));c2.load_runtime_state(rs2)
    q={'scope':'STORY','scene':'unknown-room','fact':{'subject':'prism','relation':'COLOR','object':'?'}}
    assert send(c2,'QUERY',**q)['cognitive']['values']==['ochre']
    assert send(c2,'QUERY',**q,as_of_turn=1)['cognitive']['values']==['mint']
    assert len(g2.facts)==initial+2
