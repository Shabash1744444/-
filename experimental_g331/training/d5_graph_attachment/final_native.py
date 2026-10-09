"""Independent manually-authored natural-form reattack + exact cold model proof.
No input sentence in the teacher's D5 generated training corpus.
"""
import sys,json,hashlib,random,time
from pathlib import Path
L=Path(__file__).parent
sys.path.insert(0,str(L/'native_runtime'))
from c4child.checkpoint import load_c4m_compact
from c4child.d3_scoped import ScopedLearner,decode
from c4child.d2_grounder import tokenize
from c4child.d5_graph_attachment import GraphEdgeAttachment
from c4child.dialogue import C4ChildDialogue
from c4child.runtime import C4LivingRuntime
from c4child.scope import fact_scope,LANGUAGE_CONVENTION
from c4child.d5_graph_attachment import REL
model=L/'C4_D5_LEARNED_EDGE_RESEARCH_ONLY.c4m'
g,h,_=load_c4m_compact(model,hydrate_cold=True)
tagger=ScopedLearner(g);tagger.load();linker=GraphEdgeAttachment(g)

def property_(s,a):return {'op':'PROPERTY','subject':s,'attribute':a}
def unary(op,holder,leaf):return {'op':op,'holder':holder,'arg':leaf}
def not_(node):return {'op':'NOT','arg':node}
# Each pair is a truthful *expected meaning* of an independently hand-authored
# natural or colloquial example. Some are OUTSIDE the training grammar.
manual=[
('Нелли считает будто железный волк золотой',unary('BELIEF','нелли',property_('железный волк','золотой'))),
('Веста думает что железный волк не золотой',unary('BELIEF','веста',not_(property_('железный волк','золотой')))),
('Веста не думает что железный волк золотой',not_(unary('BELIEF','веста',property_('железный волк','золотой')))),
('железный волк золотой думает Веста',unary('BELIEF','веста',property_('железный волк','золотой'))),
('По словам Весты железный волк золотой',unary('SAY','веста',property_('железный волк','золотой'))),
('Веста уверена что железный волк золотой',unary('BELIEF','веста',property_('железный волк','золотой'))),
('Веста думает что Дина говорит что железный волк золотой',unary('BELIEF','веста',unary('SAY','дина',property_('железный волк','золотой')))),
('Железный волк золотой считает Дина утверждает Веста',unary('SAY','веста',unary('BELIEF','дина',property_('железный волк','золотой')))),
('Нелли по словам Весты думает что железный волк золотой',unary('SAY','веста',unary('BELIEF','нелли',property_('железный волк','золотой')))),
('Согласно Весте Нелли ошибочно полагает что волк золотой',unary('SAY','веста',unary('BELIEF','нелли',property_('волк','золотой')))),
]
# Some unsupported input should abstain and never produce admitted WORLD facts.
unsupported=[
'Который час сейчас?',
'Ты веришь мне или нет?',
'Что за странная штуковина?',
'Скажи честно, Нелли вообще думает?',
'Перепроверь, что Веста сообщала вчера',
'Мне кажется Нелли хочет, чтобы волк оказался золотым',
]
manual_src=json.dumps({'manually_authored_expected':manual,'unsupported':unsupported},ensure_ascii=False,sort_keys=True,indent=2)
(L/'D5_MANUAL_REATTACK_FROZEN.json').write_text(manual_src,encoding='utf-8')

def classify(text):
    tok=tokenize(text)
    tags=decode(tok,tagger.weights)
    res=linker.parse(text,tags)
    return res
score=0;rows=[]
for text,gold in manual:
    parsed=classify(text);hit=parsed.get('ast')==gold and parsed['status']=='CANDIDATE';score+=hit
    rows.append({'text':text,'correct':bool(hit),'status':parsed['status'],'predicted':parsed.get('ast'),'expected':gold})
others=[]
for text in unsupported:
    result=classify(text);others.append({'text':text,'status':result['status'],'guess':result.get('ast')})
# real public path still uses C4 runtime not D5 test binder; don't call this integrated
rt=C4LivingRuntime(C4ChildDialogue(g))
target='Веста думает что Дина говорит что железный волк золотой'
resp=rt.user_message(target)
native={'parsed_kind':(resp.get('parsed') or {}).get('kind'),'reply':resp.get('reply'),'mutated':resp.get('mutated')}
new=[f for f in g.facts.values() if f.relation==REL];roots=list(sorted(set(f.source_group for f in new)))
assert all(fact_scope(g,f)==LANGUAGE_CONVENTION for f in new)
record={'manual_exact':score,'manual_total':len(manual),'manually_authored':rows,'out_of_domain':others,'native_user_message':native,'graph_cold_facts':len(g.facts),'c4_native_relation_count':len(new),'teacher_source_groups':roots}
(L/'D5_MANUAL_RESULT.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf8')
print('MANUAL EXACT',score,'/',len(manual),flush=True)
print('OUT OF DOMAIN',[(v['text'],v['status']) for v in others],flush=True)
print('NATIVE',native,flush=True)