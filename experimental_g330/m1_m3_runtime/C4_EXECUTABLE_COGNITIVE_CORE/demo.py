"""Run: python demo.py  (structured events, no LLM or external APIs)."""
from pathlib import Path
from c4core import C4, Proposition as P, Perspective as F, Query as Q, Scope as S

c=C4()
print('C4 executable skeleton:', C4.VERSION)
c.teach('storyteller', F('Маша','BELIEF',P('late',('Иван',))),scope=S.STORY,scene='рассказ')
c.teach('storyteller', P('on_time',('Иван',)),scope=S.STORY,scene='рассказ')
for title, q in [
    ('Что думает Маша?',Q('late',('Иван',),S.STORY,'рассказ',(('Маша','BELIEF'),))),
    ('Что произошло по рассказу?',Q('on_time',('Иван',),S.STORY,'рассказ')),
    ('Это доказательство во внешнем мире?',Q('late',('Иван',),S.WORLD,'рассказ')),
]:
    answer, receipt = c.respond(q)
    print(title, '->',answer.status,answer.bindings,'receipt:',receipt.state)

c.receive('USER','Какой вопрос ты сама задавала?',kind='USER_QUESTION')
c.open_gap('temperature','Что такое температура?')
print('Автономный цикл ->', c.tick().state, 'собственные вопросы:',c.own_asks())
print('Следующий цикл ->',c.tick().state)
c.receive_gap_answer(next(iter(c._questions)), 'USER',P('is_a',('температура','физическая величина')))

for name in ('камень','книга'):
    c.learn_example('sim',[P('released',(name,))],P('falling',(name,)),scope=S.SIM)
c.teach('sim',P('released',('чашка',)),scope=S.SIM)
print('Новый предмет по двум демонстрациям ->',c.query(Q('falling',('чашка',),S.SIM)).status)
print('Факт в реальном мире? ->',c.query(Q('falling',('чашка',),S.WORLD)).status)
p=Path('C4_STATE_EXAMPLE.c4j');c.save(p); restored=C4.load(p)
print('Cold restore:',c.snapshot_hash()==restored.snapshot_hash(),'; events:',len(restored.events),'; claims:',len(restored.claims))
print('Owners:',sorted({x['owner'] for x in c.trace}),'; trace records:',len(c.trace))
