"""G329 frozen cross-cascade tests. No hand-coded names/answers in runtime.

Change axes: question set size, out-of-order answer, distractor, ambiguities,
quoted questions, graph contamination, trace observational-only, cold reload.
"""
import pytest
from c4child.runtime import C4LivingRuntime
from c4child.dialogue import C4ChildDialogue
from c4child.graph import C4Graph
from c4child.episodic_memory import split_episodes,is_query_batch
from c4child.inquiry_link import evaluate_inquiry_link
from c4child.checkpoint import save_c4m_compact,load_c4m_compact


def new():return C4LivingRuntime(C4ChildDialogue(C4Graph()),hardened_truth_gate=True)


@pytest.mark.parametrize('story',[
    'Маша сказала: «Где фонарь?»',
    'Антон вспоминал: «Что случилось? Почему темно?»',
    'На стене было написано «Куда ушёл поезд?»',
])
def test_nested_quote_question_not_direct(story):
    e=split_episodes(story)
    assert not is_query_batch(e)
    assert all(x['kind']!='QUESTION' for x in e)


@pytest.mark.parametrize('pair',[
    'Что такое валентность?\nЧто означает диффузия?',
    '1. Куда делся лис?\n2. Зачем летит самолёт?',
    'Кто сказал?\nЧто произошло?',
])
def test_two_query_spans_readonly_without_three_question_threshold(pair):
    r=new();b=(len(r.dialogue.g.facts),len(r.dialogue.g.entities),r.dialogue.g.order)
    x=r.user_message(pair)
    assert x['status']=='READ_ONLY_BATCH'
    assert (len(r.dialogue.g.facts),len(r.dialogue.g.entities),r.dialogue.g.order)==b
    assert r.last_inquiry_evaluation['status']=='NOT_ANSWER'
    assert r.trace_snapshot()['lastCascade']['graph_delta']['added_fact_ids']==[]


@pytest.mark.parametrize('subject,other',[
    ('излучение','величина'),('облако','солнце'),('электрон','кислород'),
    ('движение','тепло')
])
def test_earlier_answer_is_candidate_not_auto_resolved(subject,other):
    r=new();q1=r._event('ASK',f'Что такое {subject}?','GAP',requires_user=True)
    q2=r._event('ASK',f'Что такое {other}?','GAP',requires_user=True)
    r.user_message(f'{subject.capitalize()} — физическое понятие.')
    link=r.last_inquiry_evaluation
    assert link['status']=='CANDIDATE',link
    assert link['candidates'][0]['question_event_id']==q1.event_id,link
    assert r.inquiries[q1.event_id]['answer_candidates'][-1]['status']=='UNVERIFIED'
    assert r.inquiries[q1.event_id]['status']=='OPEN'
    assert r.inquiries[q2.event_id]['status']=='OPEN'
    cas=r.trace_snapshot()['lastCascade']
    assert cas['inquiry_changes'] and cas['inquiry_changes'][0]['question_event_id']==q1.event_id
    assert cas['source_event_id']==link['source_event_id']
    assert cas['selected_public_event_id']


def test_neither_answer_nor_latest_lock():
    r=new();q1=r._event('ASK','Что такое отрезок?','GAP');q2=r._event('ASK','Что такое многогранник?','GAP')
    r.user_message('Погода сегодня изменчива.')
    assert r.last_inquiry_evaluation['status']=='NO_MATCH'
    assert all(not q.get('answer_candidates') for q in r.inquiries.values())
    assert all(q['status']=='OPEN' for q in r.inquiries.values())


def test_ambiguous_answer_is_not_bound_to_arbitrary_question():
    r=new();r._event('ASK','Что такое диффузия?','GAP');r._event('ASK','Что такое диффузия?','GAP')
    r.user_message('Диффузия происходит при смешивании.')
    assert r.last_inquiry_evaluation['status']=='AMBIGUOUS'
    assert all(not q.get('answer_candidates') for q in r.inquiries.values())


def test_question_about_topic_not_answer_topic():
    r=new();r._event('ASK','Что такое капилляр?','GAP')
    r.user_message('Помнишь вопрос про капилляр?')
    assert r.last_inquiry_evaluation['status']=='NOT_ANSWER'
    assert all(not q.get('answer_candidates') for q in r.inquiries.values())


def test_c4_speech_not_world_receipt():
    r=new();r._event('ASK','Что такое пружина?','GAP')
    r.user_message('Пружина — металлический предмет.')
    assert r.inquiries[next(iter(r.inquiries))]['status']=='OPEN'
    assert not any(row.get('kind')=='MEDIATED_WORLD_VERIFICATION' for row in r.life_events)


def test_trace_does_not_change_reply_or_inquiry_link():
    a=new();b=new();b.trace_config({'mode':'DEEP','scope':'CONTINUOUS'})
    for r in (a,b):
        r._event('ASK','Что такое гипербола?','GAP')
        r._event('ASK','Что такое стрекоза?','GAP')
    ra=a.user_message('Гипербола — литературный приём.')
    rb=b.user_message('Гипербола — литературный приём.')
    assert ra['reply']==rb['reply']
    assert a.last_inquiry_evaluation['status']==b.last_inquiry_evaluation['status']
    assert list(x['text'] for x in a.poll(20) if x.get('kind')=='REPLY')==list(x['text'] for x in b.poll(20) if x.get('kind')=='REPLY')
    assert len(a.dialogue.g.facts)==len(b.dialogue.g.facts)


def test_cold_reload_open_inquiry_link_without_fake_confirmation(tmp_path):
    r=new();a=r._event('ASK','Что такое орбита?','GAP',requires_user=True)
    r._event('ASK','Что такое гравитация?','GAP',requires_user=True)
    r.user_message('Орбита — путь вокруг тела.')
    path=tmp_path/'checkpoint.c4m'
    save_c4m_compact(path,r.dialogue.g,runtime_state=r.runtime_state(),include_cold=True)
    g,_,_,state=load_c4m_compact(path,with_runtime=True)
    cold=C4LivingRuntime(C4ChildDialogue(g));cold.load_runtime_state(state)
    assert cold.inquiries[a.event_id]['answer_candidates'][0]['status']=='UNVERIFIED'
    assert cold.inquiries[a.event_id]['status']=='OPEN'
    assert cold.last_inquiry_evaluation['status']=='CANDIDATE'


def test_trace_contains_actual_cascade_ids_and_no_answer_hallucination():
    r=new();r.trace_config({'mode':'DEEP','scope':'NEXT_INTERACTION'})
    r.user_message('1. Мы раньше обсуждали лунный поток?\n2. Кто видел лунный поток?')
    evs=r.poll(200)
    cascade=next(x for x in evs if x.get('type')=='TRACE_EVENT' and x['record'].get('kind')=='CASCADE_OUTCOME')
    s=r.trace_snapshot({'limit':40})
    assert cascade['eventId']==s['lastCascade']['event_id']
    assert not s['lastCascade']['graph_delta']['added_fact_ids']
    assert r._trace_mode=='OFF'
    assert not any(x.get('status')=='VERIFIED_WORLD' for x in evs)


def test_published_c4_ask_is_witnessed_as_question_not_world_truth():
    r=new();q=r._event('ASK','Что такое бирюзовый поршень?','GAP')
    x=r.user_message('Помнишь старый вопрос про бирюзовый поршень?')
    assert x['status']=='RETRIEVED_TEXT',x
    assert 'бирюзовый поршень' in x['reply']
    assert 'вопрос' in x['reply']
    assert r.episode_index[q.event_id]['source_kind']=='C4_ASK'
    assert r.episode_index[q.event_id]['epistemic']=='SOURCE_SAID_ONLY'


def test_unrelated_followup_cannot_bind_legacy_last_pending_definition():
    r=new()
    a=r.dialogue._eid('квантовый насос')
    r._event('ASK','Что такое квантовый насос?','GAP',requires_user=True)
    r._event('ASK','Что такое бумажный дирижабль?','GAP',requires_user=True)
    r.dialogue.pending_ask={'eid':a,'label':'квантовый насос'}
    before=len(r.dialogue.g.facts)
    r.user_message('Это живое существо.')
    assert r.last_inquiry_evaluation['status']=='NO_MATCH'
    assert r.dialogue.pending_ask['eid']==a
    assert len(r.dialogue.g.facts)==before
    assert any(x.get('kind')=='EVAL_LEGACY_ANSWER_POINTER' and x.get('status')=='SUSPENDED' for x in r.life_events)


def test_out_of_order_topic_answer_does_not_claim_latest_legacy_pointer():
    r=new()
    e1=r.dialogue._eid('излучение');e2=r.dialogue._eid('величина')
    a=r._event('ASK','Что такое излучение?','GAP',requires_user=True)
    r._event('ASK','Что такое величина?','GAP',requires_user=True)
    r.dialogue.pending_ask={'eid':e2,'label':'величина'}
    r.user_message('Излучение — поток энергии.')
    assert r.last_inquiry_evaluation['candidates'][0]['question_event_id']==a.event_id
    assert r.dialogue.pending_ask['eid']==e2
    assert r.inquiries[a.event_id]['answer_candidates']