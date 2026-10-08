"""G327: adversarial tests of end-to-end discourse + event graph + ownership."""
import pytest
from c4child.runtime import C4LivingRuntime
from c4child.dialogue import C4ChildDialogue
from c4child.graph import C4Graph
from c4child.perspective_composition import parse_perspective
from c4child.discourse_bridge import resolve_disposition,attributed_frames


def fresh():
    return C4LivingRuntime(C4ChildDialogue(C4Graph()),hardened_truth_gate=True)


def ask(rt,text):
    return rt.user_message(text)


def test_live_query_cross_turn_and_no_world_write():
    rt=fresh();before=len(rt.dialogue.g.facts)
    a=ask(rt,'Маша думает, что Иван опоздал')
    b=ask(rt,'Что думает Маша?')
    assert 'Иван опоздал' in b['reply'] and 'не доказанный' in b['reply']
    assert b['reply_kind']=='ATTRIBUTION_QUERY'
    assert len(rt.dialogue.g.facts)==before


def test_who_query_not_source_named_kto():
    rt=fresh();ask(rt,'Маша думает, что Иван опоздал')
    ret=ask(rt,'Кто думает, что Иван опоздал?')
    assert ret['reply_kind']=='ATTRIBUTION_WHO' and 'Маша' in ret['reply']
    assert 'Кто' not in {r.holder for r in attributed_frames(rt.semantic_spine)}

@pytest.mark.parametrize('text',[
    'Кто думает, что Иван опоздал?',
    'Что сказала Маша?',
    'Ты думаешь, что Иван опоздал?',
    'Маша сказала: «Как дела?»?',
])
def test_interrogatives_not_assertions(text):
    assert parse_perspective(text,source_event='evt-q') is None


def test_quote_not_segmented_on_internal_punctuation():
    rt=fresh()
    s=rt._split_user_surfaces('Маша сказала: «Меня зовут Аня. Я пришла!»')
    assert len(s)==1,s
    o=ask(rt,s[0]);assert o.get('surface_count',1)==1
    assert 'Маша' in o['reply']


def test_quote_still_one_event_with_nested_question():
    rt=fresh()
    q='Маша сказала: «Ты видел это? Я ничего не знаю!»'
    assert len(rt._split_user_surfaces(q))==1
    ask(rt,q)
    ans=ask(rt,'Что сказала Маша?')
    assert 'Ты видел' in ans['reply']
    assert len(rt.dialogue.g.facts)==0


def test_multiple_sources_cross_turn_scope():
    rt=fresh()
    ask(rt,'Маша думает, что Иван опоздал')
    ask(rt,'Нина считает, что Иван опоздал')
    q=ask(rt,'Кто думает, что Иван опоздал?')
    assert 'Маша' in q['reply'] and 'Нина' in q['reply']
    assert len(rt.dialogue.g.facts)==0


def test_nested_quote_does_not_leak_world():
    rt=fresh()
    q='Маша думает, что Иван сказал: «Меня зовут Артём»'
    ask(rt,q)
    vals=attributed_frames(rt.semantic_spine)
    assert len(vals)==2 and [r.holder for r in vals]==['Маша','Иван']
    assert len(rt.dialogue.g.facts)==0
    assert ask(rt,'Что сказал Иван?')['reply_kind']=='ATTRIBUTION_QUERY'


def test_hypothetical_scope_survives():
    rt=fresh();ask(rt,'Представь: Маша думает, что Иван опоздал')
    ret=ask(rt,'Что думает Маша?')
    assert 'гипотетическом' in ret['reply'].lower()
    assert len(rt.dialogue.g.facts)==0


def test_trust_question_never_grounds_world():
    rt=fresh();ask(rt,'Маша думает, что Луна — сыр')
    ret=ask(rt,'Правда ли, что Луна сыр?')
    assert ret['reply_kind']=='SOURCE_WORLD_BOUNDARY'
    assert 'не подтверждают' in ret['reply']
    assert len(rt.dialogue.g.facts)==0


def test_self_why_does_not_generate_receipts():
    rt=fresh();ask(rt,'Маша думает, что Иван опоздал')
    r=ask(rt,'Почему ты так считаешь?')
    assert r['reply_kind']=='DISCOURSE_SELF_AUDIT'
    assert 'независимое наблюдение' in r['reply']
    assert len(rt.dialogue.g.facts)==0


def test_time_report_doesnt_equal_reality():
    rt=fresh();ask(rt,'Маша сказала, что Иван опоздал')
    ret=ask(rt,'Когда Маша сказала это?')
    assert ret['reply_kind']=='SOURCE_TIME'
    assert 'реальное время' in ret['reply']


def test_non_matching_question_not_fake_answer():
    rt=fresh();ask(rt,'Маша думает, что Иван опоздал')
    assert resolve_disposition('Что сказала Ольга?',rt.semantic_spine,[]) is None


def test_different_holder_same_content_still_separate():
    rt=fresh()
    ask(rt,'Мария думает, что мяч покатился')
    ask(rt,'Света думает, что мяч покатился')
    found=attributed_frames(rt.semantic_spine)
    assert len(found)==2 and len({r.event_id for r in found})==2


def test_no_fact_from_repeated_question():
    rt=fresh();ask(rt,'Маша думает, что Иван опоздал')
    for _ in range(5):ask(rt,'Кто думает, что Иван опоздал?')
    assert len(rt.dialogue.g.facts)==0
    assert len(attributed_frames(rt.semantic_spine))==1


def test_state_checkpoint_frozen_reload_preserves_frames():
    rt=fresh();ask(rt,'Маша думает, что Иван опоздал')
    state=rt.runtime_state()
    fresh_rt=fresh();fresh_rt.load_runtime_state(state)
    a=ask(fresh_rt,'Что думает Маша?')
    assert a['reply_kind']=='ATTRIBUTION_QUERY'
    assert 'Иван опоздал' in a['reply']


def test_log_has_eval_drive_no_world():
    rt=fresh();ask(rt,'Маша думает, что Иван опоздал');ask(rt,'Что думает Маша?')
    kinds=[x['kind'] for x in rt.life_events]
    assert 'EVAL_DISCOURSE_GRAPH_QUERY' in kinds
    assert 'DRIVE_SPEECH_ACT' in kinds
    assert len(rt.dialogue.g.facts)==0

@pytest.mark.parametrize('phrase',[
    'Лена считает, что завтра дождь',
    'Олег сообщил, что поезд ушёл',
    'Наташа сказала: «Сегодня среда»',
    'Дима сказал, что мяч упал',
])
def test_generic_names_no_fixed_name_tables(phrase):
    rt=fresh();resp=ask(rt,phrase)
    assert rt.semantic_spine.perspective_frames and len(rt.dialogue.g.facts)==0
    assert resp['reply']


def test_elliptic_truth_doesnt_jump_over_new_self_report():
    rt=fresh()
    ask(rt,'Маша думает, что Иван опоздал')
    ask(rt,'Меня зовут Антон')
    assert resolve_disposition('Это правда?',rt.semantic_spine,rt.dialogue_history) is None


def test_quote_response_does_not_double_quote():
    rt=fresh();ask(rt,'Маша сказала: «Меня зовут Аня»')
    r=ask(rt,'Что сказала Маша?')
    assert '««' not in r['reply']