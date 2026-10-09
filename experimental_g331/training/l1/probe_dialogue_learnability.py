#!/usr/bin/env python3
"""Diagnostic only: exact native L1 C4 dialogue smoke test. Never writes .c4m."""
import argparse
import hashlib
import json
import sys
import tempfile
import zipfile
from pathlib import Path

MODEL_SHA='bba87b3d1b7c48f929236868c2244d05153532b4b173c8d7768783dadc6ef7ce'
RUNTIME_SHA='c9726f5a5645716b61d2ffe07ccb80d1fea48ceab3dbd76f384abcdc6344b9cc'
PROMPTS=[
 'Привет! Как у тебя дела? Чем хочешь заняться?',
 'В нашей выдуманной истории меня зовут Артём, а тебя Ника.',
 'Представь: на столе красный кубик, но Маша считает его зелёным.',
 'Как думаешь, почему Маша могла ошибиться?',
 'Если кубик упадёт со стола, что произойдёт?',
 'Давай придумаем историю про мяч и коробку.',
 'Мне скучно, придумай что-нибудь интересное.',
 'А теперь поменяем роли: ты — Маша, а я — Ника.',
 'Какие два способа можно придумать, чтобы достать мяч?',
 'Лира предпочитает самовар.',
]
def sha(path):
 return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--model',required=True,help='L1 trained .c4m from Library')
 ap.add_argument('--runtime',required=True,help='L1 native runtime ZIP from Library')
 ap.add_argument('--json-out')
 a=ap.parse_args()
 if sha(a.model)!=MODEL_SHA or sha(a.runtime)!=RUNTIME_SHA:
  raise SystemExit('BLOCK: wrong L1 .c4m or native runtime SHA')
 with tempfile.TemporaryDirectory() as tmp:
  with zipfile.ZipFile(a.runtime) as z:
   if 'c4child/runtime.py' not in z.namelist():raise SystemExit('Not native 56-module runtime')
   z.extractall(tmp)
  sys.path.insert(0,tmp)
  from c4child.checkpoint import load_c4m_compact
  from c4child.dialogue import C4ChildDialogue
  from c4child.runtime import C4LivingRuntime
  g,_,_,_,_=load_c4m_compact(a.model,hydrate_cold=True,with_runtime=True,with_organs=True)
  if g.constitutional_mode!='STRICT' or not g.hardened_gate:
   raise SystemExit('BLOCK: origin gate not strict')
  d=C4ChildDialogue(g)
  parsing=[]
  for s in PROMPTS:
   parsed=d.semantic_intent(s)
   parsing.append({'user':s,'kind':parsed.kind,'relation':parsed.relation})
  r=C4LivingRuntime(C4ChildDialogue(g))
  turns=[]
  for s in PROMPTS[:7]:
   res=r.user_message(s)
   turns.append({'user':s,'reply':res.get('reply'),'parsed_kind':(res.get('parsed') or {}).get('kind'),
                 'reply_kind':res.get('reply_kind')})
  if sha(a.model)!=MODEL_SHA:raise SystemExit('FAIL: source model overwritten')
  out={'schema':'C4_D0_L1_DIALOGUE_SMOKE_V1','model_sha':MODEL_SHA,'runtime_sha':RUNTIME_SHA,
       'parse_results':parsing,'dialogue_results':turns,'source_file_unchanged':True,
       'not_fluent_dialogue_benchmark':True}
  raw=json.dumps(out,ensure_ascii=False,indent=2)
  if a.json_out:Path(a.json_out).write_text(raw+'\n',encoding='utf-8')
  print(raw)
if __name__=='__main__':main()
