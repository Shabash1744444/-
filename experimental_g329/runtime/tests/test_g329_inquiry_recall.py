"""ASK ledger queries are derived from the recorded events, not lookup facts."""
from c4child.runtime import C4LivingRuntime
from c4child.dialogue import C4ChildDialogue
from c4child.graph import C4Graph


def new():return C4LivingRuntime(C4ChildDialogue(C4Graph()),hardened_truth_gate=True)


def test_recall_three_previous_own_questions_without_topics():
    r=new()
    for topic in ('диффузия','излучение','величина'):
        r._event('ASK',f'Что такое {topic}?','GAP')
    x=r.user_message('Ты помнишь свои три вопроса?')
    assert x['status']=='RETRIEVED_INQUIRIES',x
    for topic in ('диффузия','излучение','величина'):assert topic in x['reply']
    assert len(r.inquiries)==3


def test_open_asks_not_lost_after_one_candidate():
    r=new()
    a=r._event('ASK','Что такое кристалл?','GAP')
    b=r._event('ASK','Что такое вектор?','GAP')
    r.user_message('Кристалл — твёрдое вещество.')
    x=r.user_message('Какие твои вопросы ещё остались без ответа?')
    assert x['status']=='RETRIEVED_INQUIRIES',x
    assert 'кристалл' in x['reply'] and 'вектор' in x['reply']
    assert r.inquiries[a.event_id]['status']=='OPEN'
    assert r.inquiries[b.event_id]['status']=='OPEN'


def test_no_c4_ask_not_fabricated():
    r=new();x=r.user_message('Ты помнишь свои три вопроса?')
    assert x['status']=='NO_EVIDENCE',x
    assert 'вопроса' not in x['reply'].lower()


def test_specific_old_question_excludes_unrelated():
    r=new();r._event('ASK','Что такое гребёнка?','GAP');r._event('ASK','Что такое тополь?','GAP')
    x=r.user_message('Ты помнишь свой старый вопрос про тополь?')
    assert 'тополь' in x['reply'] and 'гребёнка' not in x['reply'],x


def test_single_distinctive_name_recalls_actual_witnessed_statement_not_world_fact():
    r=new();r.user_message('Это пример: Олег принёс уху.')
    x=r.user_message('Помнишь, раньше мы говорили об Олеге?')
    assert x['status']=='RETRIEVED_TEXT',x
    assert 'Олег' in x['reply']
    assert 'доказательство' in x['reply']


def test_c4_own_reply_recall_does_not_mint_external_truth():
    r=new();r.user_message('Серебряная вилка — предмет.')
    old=[v for v in r.episode_index.values() if v['source_kind']=='C4_REPLY']
    assert old, 'Publicly emitted C4 reply must be in witnessed event history'
    x=r.user_message('Ты раньше отвечала о серебряной вилке?')
    assert x['status']=='RETRIEVED_TEXT',x
    assert 'запись' in x['reply']
    assert not any(v['source_kind']=='C4_REPLY' and v['scope']=='WORLD' for v in r.episode_index.values())


def test_open_inquiry_query_without_explicit_memory_word():
    r=new();r._event('ASK','Что такое аргон?','GAP')
    x=r.user_message('Какие твои вопросы ещё без ответа?')
    assert x['status']=='RETRIEVED_INQUIRIES',x
    assert 'аргон' in x['reply']