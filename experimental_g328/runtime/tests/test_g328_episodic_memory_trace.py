"""Actual G327 LIVE failure class: long quizzes taught graph, memory is lexical garbage.
Freeze behavioral invariants, random names and no-commit evidence boundaries.
"""
from c4child.runtime import C4LivingRuntime
from c4child.dialogue import C4ChildDialogue
from c4child.graph import C4Graph
from c4child.episodic_memory import split_episodes,is_query_batch,features,retrieve
from c4child.checkpoint import save_c4m_compact,load_c4m_compact
import pytest


def fresh():
    return C4LivingRuntime(C4ChildDialogue(C4Graph()),hardened_truth_gate=True)


def test_index_numbered_queries_and_quote_boundaries():
    inp='''Привет, ответь по памяти.
1. Раньше мы говорили: «Кто дома? Я не знаю». Помнишь это?
2. Кто тогда задавал вопрос?
3. Мне нужно объяснение?
А ещё история «Кошка спросила: где сыр?»'''
    eps=split_episodes(inp)
    assert len([x for x in eps if x['kind']=='QUESTION'])>=3
    assert is_query_batch(eps)
    assert len([x for x in eps if x['number']==1])==1
    assert 'Кто дома?' in next(x['text'] for x in eps if x['number']==1)


def test_long_quiz_read_only_and_not_lexical_flood():
    rt=fresh();f0=len(rt.dialogue.g.facts)
    batch='''Синька, проверим память. Не учись на вопросах.
1. Раньше я рассказал, что дуб стоит у реки. Что мы говорили?
2. Маша думает, что меня зовут Синька. Кто это сказал?
3. Вчера ты думала, что кошки могут летать. Это твоя память?
4. Луна сделана из сыра. Ты это запомнила?
5. Какое слово я сказал тогда?'''
    ret=rt.user_message(batch)
    assert ret['status']=='READ_ONLY_BATCH' and ret['reply_kind']=='EVIDENCE_BOUNDED_RECALL'
    assert 'Запомнила' not in ret['reply'] and 'буква И' not in ret['reply']
    assert len(rt.dialogue.g.facts)==f0
    assert rt.dialogue.pending_ask is None
    assert rt.semantic_spine.events
    assert any(x['kind']=='COMMIT_NOOP' for x in rt.life_events)


def test_recalls_actual_old_event_not_a_world_claim():
    rt=fresh()
    rt.user_message('Это только пример: синий камень лежит под деревом.')
    f0=len(rt.dialogue.g.facts)
    out=rt.user_message('Помнишь, раньше я говорил про синий камень под деревом?')
    assert out['reply_kind']=='EVIDENCE_BOUNDED_RECALL'
    assert 'камень' in out['reply'] and 'дерев' in out['reply']
    assert 'запись' in out['reply']
    assert len(rt.dialogue.g.facts)==f0


def test_unseen_names_are_not_answer_templates():
    for a,b in [('фиолетовый фонарь','сквозным мостом'),('зелёный трамвай','старой башней'),('медный ключ','дубовой дверью')]:
        rt=fresh();rt.user_message('Пример: '+a+' находится над '+b+'.')
        got=rt.user_message('Мы раньше говорили про '+a+' над '+b+'?')
        assert a.split()[1] in got['reply'],got['reply']


def test_memory_cannot_use_current_message_as_past_event():
    rt=fresh();before=len(rt.dialogue.g.facts)
    q=rt.user_message('Помнишь, я раньше рассказывал о янтарном дирижабле и оранжевом склоне?')
    assert q['status']=='NO_EVIDENCE'
    assert len(rt.dialogue.g.facts)==before


def test_trace_real_events_and_next_interaction_not_made_up():
    rt=fresh();b=rt.trace_snapshot({'limit':8})
    assert b['accepted'] and b['actualEventRows']==[]
    cfg=rt.trace_config({'mode':'DEEP','scope':'NEXT_INTERACTION','structured':True,'freeFormMonologue':False})
    assert cfg['accepted'] and cfg['mode']=='DEEP'
    rt.user_message('Помнишь, мы говорили про застывший компас и мокрое окно?')
    rows=rt.poll(100)
    traces=[x for x in rows if x.get('type','').startswith('TRACE_')]
    assert traces and all('record' in x and x['record']['event_id']==x['eventId'] for x in traces)
    assert rt._trace_mode=='OFF'
    assert rt.trace_snapshot({'limit':30})['actualEventRows']
    assert not rt.trace_snapshot({'limit':10}).get('claimedHiddenThought',False)
    assert rt.trace_config({'mode':'OFF'})['mode']=='OFF'
    assert rt.poll(100)==[]


def test_tracing_observational_does_not_change_graph_or_reply():
    a=fresh();b=fresh();b.trace_config({'mode':'DEEP','scope':'CONTINUOUS'})
    prompt='1. Что мы говорили про мяч?\n2. Ты помнишь излучение?\n3. Мы обсуждали дождь?'
    va=a.user_message(prompt);vb=b.user_message(prompt)
    assert va['reply']==vb['reply']
    assert len(a.dialogue.g.facts)==len(b.dialogue.g.facts)==0
    assert a.poll(100)[0]['kind']=='REPLY'
    assert any(x.get('type','').startswith('TRACE_') for x in b.poll(100))


def test_cold_reload_read_only_index(tmp_path):
    rt=fresh();rt.user_message('Только пример: серебряный чайник стоит на крыше.')
    checkpoint=tmp_path/'cold.c4m'
    save_c4m_compact(checkpoint,rt.dialogue.g,runtime_state=rt.runtime_state(),include_cold=True)
    g,h,m,rs=load_c4m_compact(checkpoint,with_runtime=True)
    cold=C4LivingRuntime(C4ChildDialogue(g));cold.load_runtime_state(rs)
    res=cold.user_message('Помнишь, мы говорили про серебряный чайник на крыше?')
    assert 'чайник' in res['reply']
    assert cold._trace_mode=='OFF'


def test_existing_ask_not_auto_resolved_by_unrelated_user_memory_query():
    rt=fresh();q=rt._event('ASK','Что такое излучение?','LEARNING_GAP',requires_user=True)
    rt.user_message('Помнишь, раньше я рассказывал про тёплые облака?')
    assert rt.inquiries[q.event_id]['status']=='OPEN'


def test_trace_bad_modes_rejected():
    rt=fresh()
    with pytest.raises(ValueError):rt.trace_config({'mode':'FAKE'})
    with pytest.raises(ValueError):rt.trace_config({'mode':'DEEP','scope':'EVERYWHERE'})


def test_sample_20_memory_questions_is_one_non_teaching_transaction():
    rt=fresh()
    base='Синька, мы уже говорили. '
    q='\n'.join(f'{i}. Помнишь, что раньше я спрашивал про лампу и кнопку?' for i in range(1,21))
    before=rt.dialogue.g.order
    x=rt.user_message(base+q)
    assert x['status']=='READ_ONLY_BATCH'
    assert x['episode_count']>=20
    assert rt.dialogue.g.order==before
    assert rt.step==1
    assert x['reply'].count('Нет надёжно')==20

def test_past_exam_question_does_not_verify_its_story():
    rt=fresh()
    rt.user_message('1. Раньше мы обсуждали хрустальную ракету и золотую звезду?\n2. Ты точно помнишь?\n3. Где была ракета?')
    x=rt.user_message('Помнишь, что раньше мы рассказывали про хрустальную ракету и золотую звезду?')
    assert x['status']=='NO_EVIDENCE',x


def test_explicit_query_about_old_question_retrieves_a_question_only():
    rt=fresh()
    rt.user_message('1. Раньше ты спрашивала про зелёную сову и серую стену?\n2. Кто говорил про дождь?\n3. Куда делась сова?')
    x=rt.user_message('Помнишь старый вопрос про зелёную сову и серую стену?')
    assert x['status']=='RETRIEVED_TEXT',x
    assert 'вопрос' in x['reply'] and 'запись' in x['reply']