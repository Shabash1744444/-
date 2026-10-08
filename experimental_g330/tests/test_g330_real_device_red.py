"""RED tests from real G329 Android failure; intentionally fail until architectural repair.

Tests assert general event provenance and semantic branch availability, not hardcoded
objects, names or answer strings. The input text merely varies circumstances.
"""
from pathlib import Path
# PYTHONPATH=/path/to/G329/runtime pytest -q tests/test_g330_real_device_red.py
from c4child.episodic_memory import split_episodes,answer_batch,answer_memory_query,index_event
import pytest

@pytest.mark.parametrize('premise,question',[
 ('Ира унесла большой камень к мосту.','Кто унес камень?'),
 ('Сева поставил стакан на полку.','Где находится стакан в этом рассказе?'),
])
def test_current_episode_query_not_replaced_by_blanket_refusal(premise,question):
    spans=split_episodes('1. '+premise+'\n2. '+question+'\n3. Откуда ты знаешь ответ?')
    output=answer_batch(spans,index={},inquiries=())
    assert 'Это отдельный вопрос. Я пока не могу надёжно связать его' not in output['reply']


def test_own_ask_recall_cannot_source_from_user_exam_question():
    archive={'u1':index_event('u1',1,'1. Какие вопросы ты сама задавала?\n2. Помнишь, какой вопрос задала мне?')}
    result=answer_memory_query('Какие вопросы ты сама мне задавала раньше?',archive,inquiries=())
    assert not any(r.get('source_kind')=='USER_MESSAGE' for r in result.get('refs',[])), result