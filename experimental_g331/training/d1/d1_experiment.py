"""D1 independent limited-domain speech-policy feasibility on native graph C4.

Execute: PYTHONPATH=/mnt/data/c4_d1/runtime python d1_experiment.py ...
Only *training* uses manually labelled artificial examples, never model self-grade.
"""
from __future__ import annotations
import argparse, copy, hashlib, json, random, time, collections
from dataclasses import asdict
from pathlib import Path
from c4child.checkpoint import load_c4m_compact,save_c4m_compact
from c4child.narrative_policy import LearnedNarrativePolicy
from c4child.runtime import C4LivingRuntime
from c4child.dialogue import C4ChildDialogue

MODEL_SHA='bba87b3d1b7c48f929236868c2244d05153532b4b173c8d7768783dadc6ef7ce'
SURFACES={
 'INVITE':['давай сочиним игру','хочу начать игру','может придумаем историю','давай вместе поиграем','приглашаю тебя играть','начнем сочинять историю'],
 'NEXT':['а что дальше','что будем делать дальше','и что теперь','давай продолжим','как быть дальше','что сделаем потом'],
 'DETAIL':['расскажи подробнее','объясни поподробнее','расскажи об этом','а что именно происходит','хочу узнать детали','объясни еще раз'],
 'CORRECT':['нет ты ошиблась','я передумал','надо исправить описание','не так было','поправь меня','нет на самом деле иначе'],
 'UNCLEAR':['не понимаю кого ты имеешь в виду','ничего не понятно','о чем идет речь','кого ты описываешь','не разобрал смысл','это слишком неясно'],
}
HOLDOUT_SURFACES={
 'INVITE':['давай придумаем игру','хочу сочинить историю','давай поиграем вместе'],
 'NEXT':['что делаем дальше','а что теперь будем делать','продолжим нашу историю'],
 'DETAIL':['можно поподробнее','что именно произошло','дай больше подробностей'],
 'CORRECT':['ты ошиблась насчет этого','это надо исправить','я ошибся в описании'],
 'UNCLEAR':['я не понял о чем ты','объясни что имеешь в виду','я ничего не понимаю'],
}
# Training teacher labels. A fixed rubric supplies target supervision but not runtime policy.
# Accepted scope is STORY only; no WORLD facts are admitted.
def human_rubric(intent,frame):
 if intent=='INVITE':return 'OPEN_SCENE'
 if intent=='NEXT':return 'ASK_GOAL' if frame['previous_reply_act']=='OPEN_SCENE' else 'PROPOSE_NEXT'
 if intent=='DETAIL':return 'DETAIL_FOCUS' if frame.get('focus') else 'ASK_REFERENT'
 if intent=='CORRECT':return 'ACK_CORRECTION' if frame.get('focus') else 'ASK_REFERENT'
 if intent=='UNCLEAR':return 'ASK_REFERENT'
 raise ValueError('intent')

PATTERNS={
 'OPEN_SCENE':'Давай придумаем историю про {focus}. С чего начнём?',
 'ASK_GOAL':'А какую цель мы выберем для {focus}?',
 'PROPOSE_NEXT':'Можем переместить {focus} к {place}. Хочешь так продолжить?',
 'DETAIL_FOCUS':'Мы обсуждаем {focus}. Что именно хочешь узнать?',
 'ACK_CORRECTION':'Приняла поправку про {focus} внутри нашей истории. Как теперь продолжим?',
 'ASK_REFERENT':'Уточни, пожалуйста, о каком предмете или персонаже речь.'
}
TRAIN_FOCUS=['кубик','мяч','лодка','кошка','камень','фонарь','карандаш','солнце','арбуз','ветер']
TEST_FOCUS=['космический чайник','плюшевый кракен','лазурная птица','стеклянная сова','дирижабль','медный пес']
TRAIN_PLACE=['корзина','стол','полка','камин','ящик']
TEST_PLACE=['заброшенная станция','красная башня','мост','луна']
PREV=['NONE','OPEN_SCENE','PROPOSE_NEXT','DETAIL_FOCUS','ASK_GOAL','ACK_CORRECTION']
MODES=['STORY','SIM']
GOALS=['PLAY','TELL','EXPLORE']


def make_cases(n,seed,holdout=False):
 rng=random.Random(seed)
 phrases=HOLDOUT_SURFACES if holdout else SURFACES
 # Balancing classes and sparse cross-features. Test stories/entities never seen in training.
 intents=list(phrases)
 out=[]
 for i in range(n):
  intent=intents[i%len(intents)]
  prev=rng.choice(PREV)
  focus=rng.choice(TEST_FOCUS if holdout else TRAIN_FOCUS) if rng.random()<.8 else None
  if intent in {'INVITE','NEXT'}:focus=rng.choice(TEST_FOCUS if holdout else TRAIN_FOCUS)
  # For heldout, forbid spelling-overlap with training phrases where possible.
  text=rng.choice(phrases[intent])
  frame={'mode':rng.choice(MODES),'scope':'STORY','goal':rng.choice(GOALS),
         'previous_reply_act':prev,'focus':focus,'place':rng.choice(TEST_PLACE if holdout else TRAIN_PLACE),
         'object':focus,'character':('Аглая' if holdout else 'Лена')}
  expected=human_rubric(intent,frame)
  out.append({'text':text,'intent':intent,'frame':frame,'label':expected,
              'episode':('heldout-new-story:%04d'%i if holdout else 'teacher-episode:%04d'%i)})
 rng.shuffle(out)
 return out


def eval_policy(g,cases,*,trace=False):
 p=LearnedNarrativePolicy(g)
 results=[]
 for row in cases:
  got=p.decide(row['text'],row['frame'])
  ok=got.get('intent')==row['intent'] and got.get('reply_act')==row['label'] and got.get('status')=='REPLY'
  if ok and '{' in got.get('reply',''):ok=False
  if ok and row['frame']['focus'] and row['label'] not in {'ASK_REFERENT'}:
   ok=row['frame']['focus'] in got['reply']
  results.append({'expected_intent':row['intent'],'expected_act':row['label'],
                  'predicted_intent':got.get('intent'),'predicted_act':got.get('reply_act'),
                  'status':got['status'],'ok':bool(ok),
                  **({'user':row['text'],'context':row['frame'],'reply':got.get('reply'),'reason':got.get('reason')} if trace else {})})
 return {'pass':sum(x['ok'] for x in results),'total':len(results),'failures':[r for r in results if not r['ok']][:15],
         'results':results if trace else None}


def main():
 pa=argparse.ArgumentParser();pa.add_argument('--input',required=True);pa.add_argument('--output',required=True);pa.add_argument('--report',required=True);pa.add_argument('--data',required=True);pa.add_argument('--runtime-package',default='');a=pa.parse_args()
 data=json.loads(Path(a.data).read_text(encoding='utf8'))
 assert data['schema']=='C4_D1_FROZEN_NARRATIVE_CASES_V1'
 oldsha=hashlib.sha256(Path(a.input).read_bytes()).hexdigest();assert oldsha==MODEL_SHA
 output=Path(a.output);assert output.resolve()!=Path(a.input).resolve()
 g,h,manifest,state,organs=load_c4m_compact(a.input,hydrate_cold=True,with_runtime=True,with_organs=True)
 assert g.hardened_gate and g.constitutional_mode=='STRICT'
 initial_ids=set(g.facts);old_canonical=copy.deepcopy(g.canonical)
 test=data['test']; train=data['train']
 t0=time.perf_counter();baseline=eval_policy(g,test)
 stage=[]
 for n in [16,32,64,128,256]:
  # Independent copy of the original L1 for every learning-curve checkpoint.
  small,_,_,_,_=load_c4m_compact(a.input,hydrate_cold=True,with_runtime=True,with_organs=True)
  batch=train[:n]; intent=[{'text':e['text'],'label':e['intent']} for e in batch]
  reply=[{'frame':e['frame'],'intent':e['intent'],'label':e['label']} for e in batch]
  tm=time.perf_counter();stats=LearnedNarrativePolicy.teach(small,intent,reply,PATTERNS)
  measured=eval_policy(small,test)
  stage.append({'training_episodes':n,'training_event_operations':stats['supervised_intent_examples']+stats['supervised_response_examples'],
                'training_seconds':round(time.perf_counter()-tm,5),'pass':measured['pass'],'total':measured['total'],
                'new_language_facts':stats['admitted']})
 # The 256-sample model is the persisted final copy.
 intent=[{'text':e['text'],'label':e['intent']} for e in train[:256]]
 reply=[{'frame':e['frame'],'intent':e['intent'],'label':e['label']} for e in train[:256]]
 trainstats=LearnedNarrativePolicy.teach(g,intent,reply,PATTERNS)
 trained=eval_policy(g,test,trace=True)
 assert len(g.facts)==len(initial_ids)+trainstats['admitted']
 assert all(asdict(g.facts[k])==asdict(load_c4m_compact(a.input,hydrate_cold=True)[0].facts[k]) for k in list(initial_ids)[:10])
 assert all(g.canonical.get(k)==v for k,v in old_canonical.items())
 assert not any('WORLD'==str(f.authority) for f in g.facts.values() if f.source_group==trainstats['source_root'])
 # Negative: invented utterances and invalid semantic scope must fail closed.
 negative=LearnedNarrativePolicy(g).decide('гзф тёмнофлаг ярап',test[0]['frame'])
 assert negative['status']=='ABSTAIN',negative
 # Ablation 1: exact new runtime with original L1 untrained.
 untrained,_,_,_,_=load_c4m_compact(a.input,hydrate_cold=True,with_runtime=True,with_organs=True)
 same_code=eval_policy(untrained,test)
 # Ablation 2: shuffled labels, retrained on identical inputs, on native C4 graph.
 shuffled,_,_,_,_=load_c4m_compact(a.input,hydrate_cold=True,with_runtime=True,with_organs=True)
 perm={'OPEN_SCENE':'ACK_CORRECTION','ACK_CORRECTION':'DETAIL_FOCUS',
       'DETAIL_FOCUS':'ASK_REFERENT','ASK_REFERENT':'PROPOSE_NEXT',
       'PROPOSE_NEXT':'ASK_GOAL','ASK_GOAL':'OPEN_SCENE'}
 altered=[{**e,'label':perm[e['label']]} for e in train[:256]]
 LearnedNarrativePolicy.teach(shuffled,intent,[{'frame':e['frame'],'intent':e['intent'],'label':e['label']} for e in altered],PATTERNS)
 label_shuffled=eval_policy(shuffled,test)
 meta=dict(manifest.get('meta') or {});meta['c4_d1']={'status':'EXPERIMENTAL_DIALOGUE_POLICY_NOT_FREE_CONVERSATION',
      'source':'EXTERNAL_CORPUS_DEPENDENT','teacher_root':trainstats['source_root'],'baseline_sha256':oldsha,
      'holdout':'new object labels and withheld surface utterances; not new entire grammar operation'}
 save_c4m_compact(output,g,h,meta=meta,runtime_state=state,organs=organs,include_cold=True)
 reload,_,_,state2,organs2=load_c4m_compact(output,hydrate_cold=True,with_runtime=True,with_organs=True)
 cold=eval_policy(reload,test)
 assert state==state2 and organs==organs2
 assert len(reload.facts)==len(g.facts)
 assert hashlib.sha256(Path(a.input).read_bytes()).hexdigest()==MODEL_SHA
 # Actual existing runtime interface, with new native experimental method. No second graph.
 runtime=C4LivingRuntime(C4ChildDialogue(reload))
 e=test[0]
 native=runtime.learned_narrative_turn(e['text'],e['frame'])
 assert native==LearnedNarrativePolicy(reload).decide(e['text'],e['frame'])
 assert any(x.get('kind')=='COMMIT_NOOP' for x in runtime.life_events)
 assert runtime.dialogue.g is reload
 assert baseline['pass']==same_code['pass'] and cold['pass']==trained['pass']
 report={'schema':'C4_D1_NARRATIVE_TRAINABILITY_REPORT_V1','data_sha256':hashlib.sha256(Path(a.data).read_bytes()).hexdigest(),
  'source_sha256':oldsha,'output_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
  'source_facts':len(initial_ids),'output_facts':len(g.facts),'output_bytes':output.stat().st_size,
  'training':trainstats,'train_size':256,'test_size':len(test),
  'baseline':baseline['pass'],'same_new_code_untrained':same_code['pass'],
  'trained_pass':trained['pass'],'shuffled_label_pass':label_shuffled['pass'],'cold_pass':cold['pass'],
  'training_curve':stage,'negative_nonsense':negative['status'], 'raw_native_test':native,
  'native_life_event_kinds':[x.get('kind') for x in runtime.life_events],
  'unchanged_runtime_state':state==state2,'unchanged_organs':organs==organs2,'unchanged_input_sha':True,
  'holdout_failures':trained['failures'],'time_elapsed_seconds':round(time.perf_counter()-t0,4),
  'known_limitations':['requires externally supplied typed STORY frames','finite teacher-provided reply patterns',
    'not proven natural free-text end-to-end comprehension','no new speech-act operator held out',
    'only synthetic curriculum and benchmark','no Android device validation',
    'no multi-turn narrative with independent human judges','not demonstration of human-level conversation']}
 Path(a.report).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
 print(json.dumps({k:v for k,v in report.items() if k not in ['holdout_failures','training','known_limitations']},ensure_ascii=False,indent=2))
 Path(a.report).with_suffix('.cases.json').write_text(json.dumps({'cases':test,'results':trained['results']},ensure_ascii=False,indent=2),encoding='utf8')

if __name__=='__main__':main()