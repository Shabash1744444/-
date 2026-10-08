"""End-to-end cascade checks across old teaching, inquiry, store and trace.

Truth baselines are graph objects. A good public reply cannot excuse mutation.
"""
from c4child.runtime import C4LivingRuntime
from c4child.dialogue import C4ChildDialogue
from c4child.graph import C4Graph
import pytest


def new():return C4LivingRuntime(C4ChildDialogue(C4Graph()),hardened_truth_gate=True)


@pytest.mark.parametrize('a,b',[
 ('льдина','верёвка'),('атмосфера','масса'),('энергия','колесо'),
 ('кедр','маяк'),('карта','камера'),('телескоп','кружка'),
 ('длина','градус'),('плотность','ток'),('узел','объём'),
 ('пружина','звезда'),('кристалл','стекло'),('солнечник','бронепластина'),
 ('маркер','компас'),('лампа','батарея'),('электрод','капля'),
 ('река','мост'),('сигнал','свет'),('поток','ледник'),
])
def test_generic_ask_matching_across_unseen_subjects(a,b):
    r=new();earlier=r._event('ASK',f'Что такое {a}?','UNKNOWN');later=r._event('ASK',f'Что такое {b}?','UNKNOWN')
    r.user_message(f'{a.capitalize()} — интересное понятие.')
    z=r.last_inquiry_evaluation
    assert z['status']=='CANDIDATE' and z['candidates'][0]['question_event_id']==earlier.event_id,z
    assert later.event_id not in [q['question_event_id'] for q in z['candidates']]
    assert r.inquiries[later.event_id]['status']=='OPEN'


def test_real_delta_in_trace_equals_public_graph_after_one_lawful_claim():
    r=new();r.trace_config({'mode':'DEEP'})
    before=set(r.dialogue.g.facts)
    result=r.user_message('Сапфировая берёза — растение.')
    cas=r.trace_snapshot()['lastCascade']
    actual=set(r.dialogue.g.facts)-before
    assert actual==set(cas['graph_delta']['added_fact_ids'])
    assert cas['selected_public_event_id']==result['event']['event_id']
    assert cas['source_event_id']==r.semantic_spine.last_external_event_id
    # Surface user evidence must never be mistaken for verified WORLD receipts.
    for fid in actual:assert r.dialogue.g.facts[fid].status!='VERIFIED_WORLD'


def test_trace_has_no_effect_on_cascade_or_inquiry_persistence():
    a=new();b=new();b.trace_config({'mode':'DEEP'})
    for r in (a,b):
        r._event('ASK','Что такое проницаемость?','GAP')
        r._event('ASK','Что такое давление?','GAP')
    for inp in ('Ты помнишь свои два вопроса?',
                'Проницаемость — свойство вещества.',
                'Какие твои вопросы остались без ответа?',
                'Что говорила Маша про компас?'):
        ar=a.user_message(inp);br=b.user_message(inp)
        assert ar['reply']==br['reply']
        assert ar.get('status')==br.get('status')
        assert a.last_inquiry_evaluation['status']==b.last_inquiry_evaluation['status']
        assert (len(a.dialogue.g.facts),a.dialogue.g.order)==(len(b.dialogue.g.facts),b.dialogue.g.order)
        assert {(qid,q.get('status'),len(q.get('answer_candidates',[]))) for qid,q in a.inquiries.items()}=={(qid,q.get('status'),len(q.get('answer_candidates',[]))) for qid,q in b.inquiries.items()}
    assert any(v.get('type')=='TRACE_EVENT' for v in b.poll(1000))
    assert not any(v.get('type')=='TRACE_EVENT' for v in a.poll(1000))


def test_two_questions_without_automatic_assignment_even_with_legacy_pointer():
    r=new();a=r.dialogue._eid('кинетический ток');b=r.dialogue._eid('медный сигнал')
    r._event('ASK','Что такое кинетический ток?','GAP');r._event('ASK','Что такое медный сигнал?','GAP')
    r.dialogue.pending_ask={'eid':b,'label':'медный сигнал'}
    before=(len(r.dialogue.g.facts),r.dialogue.g.order)
    r.user_message('Это животное.')
    assert (len(r.dialogue.g.facts),r.dialogue.g.order)==before
    assert r.dialogue.pending_ask['eid']==b
    assert r.last_inquiry_evaluation['status']=='NO_MATCH'
    assert r.trace_snapshot()['lastCascade']['graph_delta']['added_fact_ids']==[]