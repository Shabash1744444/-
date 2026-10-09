"""Frozen D2-P2 synthetic experiment; one strict native C4 graph, no LLM at inference."""
from __future__ import annotations
import argparse,copy,hashlib,json,random,time
from pathlib import Path
from dataclasses import asdict
from c4child.d2_relational import LearnedRelationBinder,tokenize,ROLES
from c4child.checkpoint import load_c4m_compact,save_c4m_compact
from c4child.scope import LANGUAGE_CONVENTION,fact_scope

SHA='f8ed0e709b565ae0b437b8b273cd70c75762ed09ebb5cbe31bf099e6a412309c'
TRAIN_HOLDERS=['Мира','Ника','Анна','Ира','Лена','Ася','Алиса','Лиза','Соня','Оля']
TEST_HOLDERS=['Искра','Веста','Сима','Нелли','Роза','Эля']
TRAIN_SUBJECTS=['куб','мяч','кот','дом','робот','фонарь','камень','чайник','замок','стол','полосатый чайник','тяжелый стол','спящий кот','большой фонарь','бумажный корабль','медный шар','прозрачный мяч','смелый робот']
TEST_SUBJECTS=['космический чайник','хрустальный кит','гравитационный мяч','плюшевый кракен','звездный робот','светящийся фонарь']
NEG_TEMPLATES_B=[
 '{H} {P} думает, что {S} {V}',
 '{H} {P} считает, что {S} {V}',
 '{H} {P} уверена, что {S} {V}',
 '{H} {P} верит, что {S} {V}',
 '{H} {P}, что {S} {V}',
 'По мнению {H}, {S} {P} {V}',
]
NEG_TEMPLATES_N=[
 'В нашей сказке {S} {P} {V}',
 '{S} {P} {V} в нашей истории',
 'Пусть в сказке {S} {P} {V}',
]
TRAIN_ATTRIBUTES=['синий','красный','зелёный','жёлтый','тяжелый','мокрый','круглый','лёгкий']
TEST_ATTRIBUTES=['фиолетовый','золотой','деревянный','прозрачный']
B_TEMPLATES=[
 '{H} считает, что {S} {V}',
 '{H} думает, что {S} {V}',
 '{H} уверена, что {S} {V}',
 '{H} полагает: {S} {V}',
 '{H} предполагает, что {S} {V}',
 '{H} говорит: {S} {V}',
 'Как считает {H}, {S} {V}',
 'С точки зрения {H} {S} {V}',
 '{S} {V}, думает {H}',
 '{H} верит, что {S} {V}',
 '{S} {V} — по мнению {H}',
 '{S} {V} — в мыслях {H}'
]
N_TEMPLATES=[
 'В нашей сказке {S} {V}',
 'В этой истории {S} {V}',
 'По сюжету {S} {V}',
 '{S} {V} в нашей истории',
 'В придуманном мире {S} {V}',
 'Пусть в сказке {S} {V}',
 '{S} {V} в нашем рассказе',
 'В выдуманном сюжете {S} {V}',
]
B_HELDOUT=[
 'По убеждению {H}, {S} {V}',
 '{H} придерживается мнения, будто {S} {V}',
 'В представлении {H} {S} {V}',
 'О том, что {S} {V}, думает {H}',
 'Будто {S} {V} — такова позиция {H}',
]
N_HELDOUT=[
 'История утверждает: {S} {V}',
 'Для нашей вымышленной вселенной верно: {S} {V}',
 'Считаем в сказке, что {S} {V}',
]
OTHER=['завтра мы едем на дачу','сколько будет четыре плюс три',
       'найди мне телефон','вчера была гроза','привет как дела','посмотри видео',
       'открой приложение','поставь таймер','сегодня мне весело','какая погода завтра',
       'объясни географию','почему шумит ветер','покажи список дел','расскажи анекдот',
       'я не уверен в этом','как у тебя настроение', 'получи почту','купим продукты']
NEGATIONS=[
 'Мира не думает, что куб синий',
 'Ника отрицает, что мяч красный',
 'По мнению Алисы, куб не синий',
 'В рассказе чайник не красный',
 'Ника считает куб зеленым, но в истории он красный',
 'Алиса думает, что мяч синий, но Мира думает, что он красный',
 'Мира знает, что Ника думает, что куб красный',
 'Соня сказала, что Оля думает: мяч синий',
]

def make_text(tpl,h,s,v,kind,neg_word=None):
    # Reference-grade synthetic teacher annotation, not inference heuristics.
    values={'H':h,'S':s,'V':v,'P':(neg_word or 'не')}
    chunks=[];cursor=0;text='';spans=[]
    import re
    for match in re.finditer(r'\{([HSVP])\}',tpl):
        literal=tpl[cursor:match.start()];text+=literal
        start=len(text);val=values[match.group(1)];text+=val
        spans.append((match.group(1),start,len(text)));cursor=match.end()
    text+=tpl[cursor:]
    token_offsets=[m.span() for m in __import__('c4child.d2_grounder',fromlist=['TOK']).TOK.finditer(text)]
    tags=['O']*len(token_offsets)
    mapping={'H':'HOLDER','S':'SUBJECT','V':'ATTRIBUTE','P':'POLARITY'}
    for symbol,start,end in spans:
        ids=[i for i,(a,b) in enumerate(token_offsets) if a>=start and b<=end]
        for k,i in enumerate(ids):tags[i]=('B-' if k==0 else 'I-')+mapping[symbol]
    if len(tags)!=len(tokenize(text)):raise ValueError('tokenizer mismatch')
    return {'text':text,'kind':kind,'roles':{'SUBJECT':s.lower().replace('ё','е'),'ATTRIBUTE':v.lower().replace('ё','е'),
                                           **({'HOLDER':h.lower().replace('ё','е')} if kind=='BELIEF' else {}),
                                           **({'POLARITY':(neg_word or 'не').lower()} if neg_word else {})},
            'tags':tags}


def frozen():
    rng=random.Random(1767)
    train=[]
    for i in range(1100):
        h=rng.choice(TRAIN_HOLDERS);s=rng.choice(TRAIN_SUBJECTS);v=rng.choice(TRAIN_ATTRIBUTES)
        k='BELIEF' if i%2==0 else 'NARRATOR'
        tpl=rng.choice(B_TEMPLATES if k=='BELIEF' else N_TEMPLATES)
        train.append(make_text(tpl,h,s,v,k))
    for i in range(480):
        h=rng.choice(TRAIN_HOLDERS);sb=rng.choice(TRAIN_SUBJECTS);v=rng.choice(TRAIN_ATTRIBUTES)
        k='BELIEF' if i%2==0 else 'NARRATOR';templ=rng.choice(NEG_TEMPLATES_B if k=='BELIEF' else NEG_TEMPLATES_N)
        p='отрицает' if '{P}, что' in templ else 'не'
        train.append(make_text(templ,h,sb,v,k,neg_word=p))
    for i in range(300):
        text=rng.choice(OTHER)
        train.append({'text':text,'kind':'OTHER','tags':['O']*len(tokenize(text)),'roles':{}})
    rng.shuffle(train)
    seen=[];novel=[]
    for i in range(120):
        h=rng.choice(TEST_HOLDERS);s=rng.choice(TEST_SUBJECTS);v=rng.choice(TEST_ATTRIBUTES)
        k='BELIEF' if i%2==0 else 'NARRATOR'
        seen.append(make_text(rng.choice(B_TEMPLATES if k=='BELIEF' else N_TEMPLATES),h,s,v,k))
    for i in range(100):
        h=rng.choice(TEST_HOLDERS);s=rng.choice(TEST_SUBJECTS);v=rng.choice(TEST_ATTRIBUTES)
        k='BELIEF' if i%2==0 else 'NARRATOR'
        novel.append(make_text(rng.choice(B_HELDOUT if k=='BELIEF' else N_HELDOUT),h,s,v,k))
    negatives=[make_text(rng.choice(NEG_TEMPLATES_B if i%2==0 else NEG_TEMPLATES_N),rng.choice(TEST_HOLDERS),rng.choice(TEST_SUBJECTS),rng.choice(TEST_ATTRIBUTES),'BELIEF' if i%2==0 else 'NARRATOR',neg_word='не') for i in range(80)]
    return {'train':train,'heldout_negation_new_entities':negatives,'heldout_seen_constructions_new_entities':seen,
            'heldout_new_constructions_new_entities':novel,
            'heldout_new_people_and_entities_familiar_values': [make_text(rng.choice(B_TEMPLATES if i%2==0 else N_TEMPLATES),rng.choice(TEST_HOLDERS),rng.choice(TEST_SUBJECTS),rng.choice(TRAIN_ATTRIBUTES),'BELIEF' if i%2==0 else 'NARRATOR') for i in range(120)],
            'heldout_unsupported':NEGATIONS+OTHER}


def score(g,rows):
    binder=LearnedRelationBinder(g);correct=0;kind_correct=0;samples=[]
    for ex in rows:
        result=binder.interpret(ex['text'])
        kind=result.get('kind')
        expected=ex['kind']
        kp=(result.get('status')=='CANDIDATE' and kind==expected)
        joint=kp and result.get('roles')==ex['roles']
        kind_correct+=int(kp);correct+=int(joint)
        if not joint and len(samples)<10:samples.append({'text':ex['text'],'expected':ex['roles'],'got':result})
    return {'exact':correct,'kind_correct':kind_correct,'total':len(rows),'failures':samples}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',required=True);ap.add_argument('--output',required=True)
    ap.add_argument('--dataset',required=True);ap.add_argument('--report',required=True)
    args=ap.parse_args()
    src=Path(args.input);sha=hashlib.sha256(src.read_bytes()).hexdigest()
    if sha!=SHA:raise AssertionError('P1 baseline SHA mismatch '+sha)
    d=frozen();Path(args.dataset).write_text(json.dumps(d,ensure_ascii=False,indent=2))
    dsha=hashlib.sha256(Path(args.dataset).read_bytes()).hexdigest()
    g,h,m,state,organs=load_c4m_compact(src,hydrate_cold=True,with_runtime=True,with_organs=True)
    prior_ids=set(g.facts);prior=len(g.facts)
    baseline={k:score(g,ex) for k,ex in d.items() if k.startswith('heldout_') and k!='heldout_unsupported'}
    start=time.perf_counter();t=LearnedRelationBinder.train(g,d['train'],epochs=9);duration=time.perf_counter()-start
    result={k:score(g,ex) for k,ex in d.items() if k.startswith('heldout_') and k!='heldout_unsupported'}
    unsupported=[{'text':text,'result':LearnedRelationBinder(g).interpret(text)} for text in d['heldout_unsupported']]
    new=[f for k,f in g.facts.items() if k not in prior_ids]
    assert len(g.facts)==prior+t['parameter_facts']
    assert all(fact_scope(g,f)==LANGUAGE_CONVENTION and f.origin=='EXTERNAL_CORPUS' and f.authority=='TEACHER' for f in new)
    md=dict(m.get('meta') or {});md['d2_p2']={'status':'RESEARCH_CANDIDATE_NOT_GENERAL_LANGUAGE',
        'parent_sha256':sha,'dataset_sha256':dsha,'root':t['root']}
    save_c4m_compact(args.output,g,h,meta=md,runtime_state=state,organs=organs,include_cold=True)
    cold,_,_,s2,o2=load_c4m_compact(args.output,hydrate_cold=True,with_runtime=True,with_organs=True)
    after_cold={k:score(cold,ex) for k,ex in d.items() if k.startswith('heldout_') and k!='heldout_unsupported'}
    assert s2==state and o2==organs
    assert all(result[k]['exact']==v['exact'] for k,v in after_cold.items())
    assert all(asdict(f)==asdict(cold.facts[k]) for k,f in g.facts.items())
    assert hashlib.sha256(src.read_bytes()).hexdigest()==SHA
    # Untrained baseline on SAME new runtime, teacher ablation + static source integrity.
    shuf,_,_,_,_=load_c4m_compact(src,hydrate_cold=True,with_runtime=True,with_organs=True)
    mapping={'BELIEF':'NARRATOR','NARRATOR':'OTHER','OTHER':'BELIEF'}
    other=[{**x,'kind':mapping[x['kind']]} for x in d['train']]
    LearnedRelationBinder.train(shuf,other,epochs=9)
    shuffled={k:score(shuf,ex) for k,ex in d.items() if k.startswith('heldout_') and k!='heldout_unsupported'}
    report={'schema':'C4_D2_P2C_RELATIONAL_POLARITY_CANDIDATE','src_sha':sha,'new_sha':hashlib.sha256(Path(args.output).read_bytes()).hexdigest(),
            'dataset_sha':dsha,'parent_facts':prior,'new_facts':len(g.facts)-prior,'total_facts':len(g.facts),'size_bytes':Path(args.output).stat().st_size,
            'training':t,'training_seconds':duration,'baseline':baseline,'trained':result,'cold':after_cold,'shuffle_intent_only':shuffled,
            'unsupported_diagnostics':unsupported,'immutable_src':True,'old_facts_unchanged':True,'runtime_state_unchanged':True,
            'limits':['scoped synthetic BELIEF vs NARRATOR; no free language','no independent human ratings',
                'not supported: negation, multiple nested beliefs, causal time, narrative contrast',
                'learned-role graph candidate; no WORLD observation or original model mutation']}
    Path(args.report).write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps({k:report[k] for k in ['new_sha','parent_facts','new_facts','total_facts','size_bytes','training_seconds']},ensure_ascii=False))
    for k in baseline:
        print(k,'baseline',baseline[k]['exact'],'trained',result[k]['exact'],'cold',after_cold[k]['exact'],'shuffled',shuffled[k]['exact'],'total',result[k]['total'])
    print('Unsupported abstained',sum(x['result']['status']=='ABSTAIN' for x in unsupported),'/',len(unsupported))
    print('Known negative cases with correct polarity',sum(x['result'].get('polarity')=='NEGATED' for x in unsupported[:4]),'/4')

if __name__=='__main__':main()