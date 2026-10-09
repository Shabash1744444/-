"""D2 strict RED control: raw user_message, no external STORY frame and no model file writes.

It is not a human correctness grading harness: logs must be independently read.
"""
import argparse,json,hashlib
from pathlib import Path
from c4child.checkpoint import load_c4m_compact
from c4child.dialogue import C4ChildDialogue
from c4child.runtime import C4LivingRuntime


TURNS=[
 'Привет. Давай придумаем историю про космический чайник.',
 'В нашей истории я Кирилл, а ты Жужа.',
 'Космический чайник лежит на синей планете.',
 'А вдруг чайник умеет летать? Что тогда?',
 'Нет, я передумал: чайник не летает, он плавает.',
 'Что ты сама предложишь дальше?',
 'А если Жужа думает, что чайник летает, но Кирилл знает, что нет?',
 'Как завершить нашу историю неожиданно?',
]

def trial(path):
 g,*_=load_c4m_compact(path,hydrate_cold=True)
 rt=C4LivingRuntime(C4ChildDialogue(g))
 out=[]
 for text in TURNS:
  r=rt.user_message(text)
  out.append({'input':text,'reply':r.get('reply'),'reply_kind':r.get('reply_kind'),
              'parsed':r.get('parsed'),'mutated':r.get('mutated')})
 return out

parser=argparse.ArgumentParser()
parser.add_argument('--l1',required=True)
parser.add_argument('--d1',required=True)
parser.add_argument('--output',required=True)
args=parser.parse_args()
result={'schema':'C4_D2_FROZEN_FREE_TEXT_RED_V1','turns':len(TURNS),
        'l1':trial(args.l1),'d1':trial(args.d1),
        'caveat':'Semantic correctness requires independent human audit. D1 experimental policy route is NOT invoked by user_message.'}
Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps({'identical_outputs':[(x['reply'],str(x['parsed']))==(y['reply'],str(y['parsed'])) for x,y in zip(result['l1'],result['d1'])],
                'd1_replies':[{'input':i+1,'reply':r['reply'],'kind':r['reply_kind']} for i,r in enumerate(result['d1'])]},ensure_ascii=False,indent=2))
