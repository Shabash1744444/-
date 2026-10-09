"""Frozen phone RED: a correction needs a grounded referent, not 'latest'.

Two xfail cases remain intentionally unimplemented learned conversational abilities.
"""
import pytest
from c4child import C4ChildDialogue
from c4child.graph import C4Graph
from c4child.episodic_memory import split_episodes,is_query_batch
from c4child.perspective_composition import parse_perspective


def fixture_dialogue():
    g=C4Graph()
    d=C4ChildDialogue(g)
    predicate=g.entity('ошибся')
    meaning=g.entity('самокоррекция утверждения')
    g.commit_entity(predicate,'MEANS',meaning,principal='USER',origin='CREATOR_PRIOR',authority='CREATOR')
    assert d._semantic_source_retraction('Я ошибся: предмет неправильный.') is not None
    return g,d


def source(g, ref, subject='FACT'):
    return g._record_claim_only(g.entity(subject),'NAME',str(len(ref)),principal='USER',
                 origin='USER_SAID',authority='USER',source_ref=ref,source_group='USER:USER')


def test_phone_red_correcting_cube_must_not_retract_name_claim():
    g,d=fixture_dialogue()
    name=source(g,'В ней меня зовут Север, тебя — Лада.')
    before=g.order
    response=d._semantic_source_retraction('Я ошибся: кубик на самом деле синий.')
    assert response[0]=='CORRECTION'
    assert 'ничего не отзываю' in response[1].lower()
    assert name.status=='SOURCE_ASSERTED'
    assert g.order==before


def test_supported_same_referent_correction_can_retract():
    g,d=fixture_dialogue()
    name=source(g,'В ней меня зовут Север, тебя — Лада.')
    assert d._semantic_source_retraction('Я ошибся: Север не тот.')
    assert name.status=='RETRACTED'
    assert any(a['type']=='SOURCE_ASSERTION_RETRACT' for a in g.audit)


def test_same_entity_two_independent_old_claims_requires_clarification():
    g,d=fixture_dialogue()
    f1=source(g,'Кубик красный на полке.','FIRST')
    f2=source(g,'Кубик синий у двери.','SECOND')
    out=d._semantic_source_retraction('Я ошибся: кубик зелёный.')
    assert 'ничего не отзываю' in out[1].lower()
    assert f1.status==f2.status=='SOURCE_ASSERTED'


def test_exact_target_retracts_matched_older_claim_not_latest_unrelated():
    g,d=fixture_dialogue()
    first=source(g,'Вчера кубик красный на столе.','FIRST')
    second=source(g,'Сегодня часы большие на стене.','SECOND')
    out=d._semantic_source_retraction('Я ошибся: кубик оказался синим.')
    assert out[0]=='CORRECTION'
    assert first.status=='RETRACTED'
    assert second.status=='SOURCE_ASSERTED'


def test_graph_exact_target_missing_must_not_fallback_to_latest():
    g,d=fixture_dialogue()
    last=source(g,'Сегодня часы большие на стене.')
    result=g.retract_latest_source_assertion(source_group='USER:USER',principal='USER',
                 target_source_ref='Вчера кубик красный на столе.')
    assert result==[] and last.status=='SOURCE_ASSERTED'


def test_free_correction_without_referent_must_abstain():
    g,d=fixture_dialogue()
    last=source(g,'Утром собака сидела у двери.')
    out=d._semantic_source_retraction('Я ошибся.')
    assert 'ничего не отзываю' in out[1].lower()
    assert last.status=='SOURCE_ASSERTED'


@pytest.mark.xfail(strict=True,reason='C004-R6: generic multi-question discourse act composition not learned yet')
def test_future_learned_composition_greeting_not_fake_historical_exam():
    msg='Привет! Как у тебя дела? О чём ты сейчас думаешь?'
    assert not is_query_batch(split_episodes(msg))


@pytest.mark.xfail(strict=True,reason='C004-R6: belief content and narrator contrast need independent recursive frames')
def test_future_belief_frame_must_not_absorb_narrator_contrast():
    p=parse_perspective('Маша думает, что кубик зелёный, хотя в нашей истории он синий.',source_event='in:example')
    assert 'хотя' not in p['child']['content']
