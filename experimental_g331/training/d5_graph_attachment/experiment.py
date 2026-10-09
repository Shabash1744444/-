"""C4 D5 experimental LEARNED semantic attachment, not C4 canonical.
Structural node types may be fixed; all edge directions / topology / unary attachments learned.
All output is offline research; no inference fallback to hardcoded Russian phrase rules.
"""
from __future__ import annotations
from collections import defaultdict
from itertools import permutations
import random, json, hashlib, time, sys, math
from pathlib import Path
L=Path(__file__).parent
sys.path.insert(0,'/mnt/data/c4_decisive_lab/runtime_unpacked')
from c4child.d3_scoped import spans,train_weights,decode,build_ast
from c4child.d2_grounder import tokenize

# INPUTS are typed spans only; "what connects to what" is supervised, not predetermined
TRAIN_NAMES=('Мира','Ника','Лена','Ася','Рита','Вера')
TEST_NAMES=('Веста','Нелли','Злата','Дина','Эльза','Сима')
TRAIN_OBJECTS=('куб','медный шар','малый дом','кот','робот','замок')
TEST_OBJECTS=('железный волк','космический чайник','хрустальный кит','плюшевый кракен')
TRAIN_ATTR=('синий','чистый','мокрый','круглый')
TEST_ATTR=('золотой','фиолетовый','прозрачный','пыльный')
VERBS={'BELIEF':('думает','считает','полагает'), 'SAY':('говорит','сообщает','утверждает')}

def example(rng,depth,layout,names,objs,attrs,neg=True):
    kinds=[rng.choice(['BELIEF','SAY']) for _ in range(depth)]
    holders=rng.sample(names,depth)
    outer=[int(rng.random()<0.36) if neg else 0 for _ in range(depth)]
    inner=int(rng.random()<0.32) if neg else 0
    sub=rng.choice(objs);att=rng.choice(attrs)
    part=[]
    def add(text,role):part.append((text,role))
    if layout=='forward':
        for i in range(depth):
            add(holders[i],'HOLDER')
            if outer[i]:add('не','NEG')
            add(rng.choice(VERBS[kinds[i]]),'OP_'+kinds[i]);add('что','O')
        add(sub,'SUBJECT')
        if inner:add('не','NEG')
        add(att,'ATTRIBUTE')
    elif layout=='reversed':
        add(sub,'SUBJECT')
        if inner:add('не','NEG')
        add(att,'ATTRIBUTE')
        for i in reversed(range(depth)):
            if outer[i]:add('не','NEG')
            add(rng.choice(VERBS[kinds[i]]),'OP_'+kinds[i])
            add(holders[i],'HOLDER')
    else:raise ValueError(layout)
    toks=[];tags=[]
    for v,t in part:
        vv=tokenize(v)
        toks+=vv
        tags+=['O']*len(vv) if t=='O' else ['B-'+t]+['I-'+t]*(len(vv)-1)
    payload={'op':'PROPERTY','subject':' '.join(tokenize(sub)),'attribute':' '.join(tokenize(att))}
    if inner:payload={'op':'NOT','arg':payload}
    for i in reversed(range(depth)):
        payload={'op':kinds[i],'holder':holders[i].lower(),'arg':payload}
        if outer[i]:payload={'op':'NOT','arg':payload}
    text=' '.join(v for v,t in part)
    return {'text':text,'tags':tags,'ast':payload,'depth':depth,'layout':layout}

def nodes_of(ex,tags=None):
    w=tokenize(ex['text'])
    spans_=spans(w,list(ex['tags'] if tags is None else tags))
    by=[{'id':i,'tag':t,'text':s,'pos':p} for i,(t,s,p) in enumerate(spans_)]
    return by

def reconstruct(nodes,order,holder,neg):
    if sum(x['tag']=='SUBJECT' for x in nodes)!=1 or sum(x['tag']=='ATTRIBUTE' for x in nodes)!=1:return None
    subj=next(x for x in nodes if x['tag']=='SUBJECT')['text'];attr=next(x for x in nodes if x['tag']=='ATTRIBUTE')['text']
    payload={'op':'PROPERTY','subject':subj,'attribute':attr}
    if 'P' in neg.values():payload={'op':'NOT','arg':payload}
    for opid in reversed(order):
        op=nodes[opid]
        if opid not in holder:return None
        payload={'op':op['tag'][3:],'holder':nodes[holder[opid]]['text'],'arg':payload}
        if opid in neg.values():payload={'op':'NOT','arg':payload}
    return payload

def gold_structure(ex):
    ns=nodes_of(ex)
    ops=[n for n in ns if n['tag'].startswith('OP_')]
    if ex['layout']=='reversed':ops.reverse()
    hs=[n for n in ns if n['tag']=='HOLDER']
    if ex['layout']=='reversed':hs.reverse()
    holder={o['id']:h['id'] for o,h in zip(ops,hs)}
    nids=[n for n in ns if n['tag']=='NEG']
    neg={}
    # Teacher targets from generation semantics, reconstructed by matching expected AST 
    # to all possible NEG attachments; this is only dataset labelling, not inference code.
    import itertools
    dest=['P']+[o['id'] for o in ops]
    for mapping in itertools.product(dest,repeat=len(nids)):
        trial={n['id']:d for n,d in zip(nids,mapping)}
        if reconstruct(ns,[o['id'] for o in ops],holder,trial)==ex['ast']:
            neg=trial;break
    assert len(neg)==len(nids),(ex,ns)
    return ns,tuple(o['id'] for o in ops),holder,neg

def bucket_dist(d):
    a=abs(d)
    return '1' if a<=1 else '2' if a<=2 else '3' if a<=4 else '4' if a<=8 else '5'

def feats(ns,a,b,relation):
    x=ns[a]; y=ns[b]
    d=y['pos']-x['pos']; start=min(x['pos'],y['pos']);end=max(x['pos'],y['pos'])
    between=[t for t in ns if start<t['pos']<end]
    nops=sum(t['tag'].startswith('OP_') for t in between)
    nheads=sum(t['tag']=='HOLDER' for t in between)
    nneg=sum(t['tag']=='NEG' for t in between)
    side='BEFORE' if d<0 else 'AFTER'
    return [(relation,'bias'),(relation,'pair',x['tag'],y['tag']),
            (relation,'side',side),(relation,'dist',bucket_dist(d)),
            (relation,'intervening_ops',min(nops,3)),(relation,'intervening_heads',min(nheads,3)),
            (relation,'intervening_negs',min(nneg,2)),
            (relation,'side_d',side,bucket_dist(d)),
            (relation,'side_inter',side,min(nops,3)),
            (relation,'holder_side',side,x['tag'],y['tag']),
            (relation,'side_d_rel',side,bucket_dist(d),x['tag'],y['tag'])]

def node_virtual(ns):
    # PROPERTY anchor at predicate adjective, not fixed string position; the type is known.
    a=next(x for x in ns if x['tag']=='ATTRIBUTE')
    return ns+[{'id':len(ns),'tag':'PROPERTY','text':'','pos':a['pos']}]

def best_match(ns,ops,heads,w):
    if len(ops)!=len(heads):return {},()
    if len(ops)>5:return {},()
    best=(-1e99,None)
    for hs in permutations(heads,len(ops)):
        score=sum(sum(w.get(f,0.) for f in feats(ns,h,o,'HOLDER')) for o,h in zip(ops,hs))
        if score>best[0]:best=(score,hs)
    return dict(zip(ops,best[1])),best[1]

def choose_chain(ns,ops,w):
    if len(ops)>5:return ()
    prop=next(x['id'] for x in ns if x['tag']=='PROPERTY')
    def arc(a,b):return sum(w.get(f,0.) for f in feats(ns,a,b,'ARG'))
    return max(permutations(ops),key=lambda arr:sum(arc(o,arr[i+1] if i+1<len(arr) else prop) for i,o in enumerate(arr))) if ops else ()

def choose_neg(ns,negs,ops,w):
    prop=next(x['id'] for x in ns if x['tag']=='PROPERTY')
    dest=[prop]+list(ops)
    def arc(a,b):return sum(w.get(f,0.) for f in feats(ns,a,b,'NEG'))
    return {n:max(dest,key=lambda p:arc(n,p)) for n in negs}

def encoding(ns,order,holder,neg):
    f=defaultdict(float)
    prop=next(x['id'] for x in ns if x['tag']=='PROPERTY')
    for o,h in holder.items():
        for x in feats(ns,h,o,'HOLDER'):f[x]+=1
    for i,o in enumerate(order):
        target=order[i+1] if i+1<len(order) else prop
        for x in feats(ns,o,target,'ARG'):f[x]+=1
    for n,dest in neg.items():
        for x in feats(ns,n,prop if dest=='P' else dest,'NEG'):f[x]+=1
    return f

def predict_links(ns,w):
    if not any(n['tag']=='ATTRIBUTE' for n in ns):return None
    ext=node_virtual(ns)
    ops=[n['id'] for n in ns if n['tag'].startswith('OP_')]
    heads=[n['id'] for n in ns if n['tag']=='HOLDER']
    negs=[n['id'] for n in ns if n['tag']=='NEG']
    if not ops or len(ops)>5 or len(ops)!=len(heads) or not any(n['tag']=='SUBJECT' for n in ns) or not any(n['tag']=='ATTRIBUTE' for n in ns):return None
    order=choose_chain(ext,ops,w)
    holder,_=best_match(ext,ops,heads,w)
    neg=choose_neg(ext,negs,ops,w)
    neg={k:('P' if v==len(ns) else v) for k,v in neg.items()}
    return ext,order,holder,neg

def train_links(rows,epochs,seed):
    w=defaultdict(float);lst=list(rows)
    for ep in range(epochs):
        random.Random(seed+ep*997).shuffle(lst)
        for e in lst:
            ns,go,gh,gn=gold_structure(e)
            pred=predict_links(ns,w)
            if pred is None:continue
            ext,po,ph,pn=pred
            if (go,gh,gn)!=(po,ph,pn):
                good=encoding(ext,go,gh,gn);bad=encoding(ext,po,ph,pn)
                for f in good.keys()|bad.keys():w[f]+=good.get(f,0.)-bad.get(f,0.)
    return dict((k,v) for k,v in w.items() if v)

def predict_tree(ex,w,tags=None):
    ns=nodes_of(ex,tags)
    pred=predict_links(ns,w)
    if not pred:return None
    _,order,holder,neg=pred
    return reconstruct(ns,order,holder,neg)

def evaluate(rows,w,tagweights=None):
    good=0;oracle=0; abstain=0; mistakes=[]; tags_ok=0
    for e in rows:
        rawtags=decode(tokenize(e['text']),tagweights) if tagweights is not None else e['tags']
        gold_tags=(rawtags==e['tags']);tags_ok+=gold_tags
        actual=predict_tree(e,w,rawtags)
        aok=(actual==e['ast']); good+=aok; abstain+=int(actual is None)
        if len(mistakes)<4 and not aok:mistakes.append({'text':e['text'],'gold':e['ast'],'got':actual,'gold_tags':gold_tags})
    return {'correct':good,'total':len(rows),'tags_exact':tags_ok,'abstain':abstain,'examples':mistakes}

def write_json(path,obj):
    raw=json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=2)
    Path(path).write_text(raw,encoding='utf-8');return hashlib.sha256(raw.encode()).hexdigest()

if __name__=='__main__':
    rng=random.Random(202610091)
    TEST={
        'reverse_depth2_new_entities':[example(rng,2,'reversed',TEST_NAMES,TEST_OBJECTS,TEST_ATTR) for _ in range(100)],
        'reverse_depth3_new_entities':[example(rng,3,'reversed',TEST_NAMES,TEST_OBJECTS,TEST_ATTR) for _ in range(100)],
        'forward_depth3_new_entities':[example(rng,3,'forward',TEST_NAMES,TEST_OBJECTS,TEST_ATTR) for _ in range(100)],
        'reverse_depth1_new_entities':[example(rng,1,'reversed',TEST_NAMES,TEST_OBJECTS,TEST_ATTR) for _ in range(80)],
        'forward_depth1_new_entities':[example(rng,1,'forward',TEST_NAMES,TEST_OBJECTS,TEST_ATTR) for _ in range(80)],
    }
    # Separate adversarial set: new lexical syntactic constructions (not generated by teacher grammar).
    # No examples from this set enter training, score fixed independently of any changes.
    CUSTOM=[
     ('Нелли считает будто железный волк золотой',{'op':'BELIEF','holder':'нелли','arg':{'op':'PROPERTY','subject':'железный волк','attribute':'золотой'}}),
     ('Золотой железный волк по мнению Нелли',{'op':'BELIEF','holder':'нелли','arg':{'op':'PROPERTY','subject':'железный волк','attribute':'золотой'}}),
     ('Нелли по словам Весты думает что железный волк золотой',{'op':'SAY','holder':'веста','arg':{'op':'BELIEF','holder':'нелли','arg':{'op':'PROPERTY','subject':'железный волк','attribute':'золотой'}}}),
     ('Не Нелли считает железный волк золотой',None),
     ('Железный волк золотой хотя Нелли считает иначе',None),
     ('Разве Нелли думает что железный волк золотой',None),
    ]
    # Freeze before training: hash hard-coded generated records plus assertions and protocol
    frozen_sha=write_json(L/'D5_HOLDOUT_FROZEN.json',{'generated':TEST,'independent_reattack':CUSTOM,'protocol':'D5_ATTACH_TOPOLOGY_FIRST'});
    print('FROZEN',frozen_sha,flush=True)
    rr=random.Random(719)
    # 80 unary reverse+forward, 64 two-level forward+reverse, NO THREE-LEVEL TRAINING
    train=[example(rr,1,layout,TRAIN_NAMES,TRAIN_OBJECTS,TRAIN_ATTR) for layout in ('forward','reversed') for _ in range(80)]
    train+=[example(rr,2,layout,TRAIN_NAMES,TRAIN_OBJECTS,TRAIN_ATTR) for layout in ('forward','reversed') for _ in range(64)]
    print('LESSONS',len(train), 'TRAIN_SHA',write_json(L/'D5_TRAIN.json',train),flush=True)
    for e in train:
        ns,order,holder,neg=gold_structure(e)
        assert reconstruct(ns,order,holder,neg)==e['ast']
    print('PRECHECK_GOLD_GOOD',len(train),flush=True)
    out={'frozen_sha256':frozen_sha,'training_count':len(train),'seeds':{},'source':'C4 D3 research extension not native runtime yet'}
    start=time.monotonic()
    for seed in [3,11,23,37]:
        tic=time.monotonic()
        w=train_links(train,6,seed)
        # test with oracle semantic spans, then with a separately learned tagger
        # tags same D3 universal learner, no fixed lexeme mapping
        tm=train_weights(train,4)
        oracle={label:evaluate(cases,w) for label,cases in TEST.items()}
        learned={label:evaluate(cases,w,tm) for label,cases in TEST.items()}
        out['seeds'][str(seed)]={'link_parameters':len(w),'tag_parameters':len(tm),'oracle_tags':oracle,'learned_tags':learned,'seconds':round(time.monotonic()-tic,2)}
        print('SEED',seed,'ORACLE',{k:v['correct'] for k,v in oracle.items()},'LEARNED',{k:v['correct'] for k,v in learned.items()},'elapsed',round(time.monotonic()-start),flush=True)
        if seed==3:
            out['example_link_weights']=[repr(z) for z in list(w.items())[:12]]
            # small numerical model not native yet, will be embedded only if narrow gates pass
            write_json(L/'D5_SEED3_WEIGHTS.json',{'weights':[[list(k),v] for k,v in w.items()],'seed':3})
    write_json(L/'D5_RESULTS.json',out)