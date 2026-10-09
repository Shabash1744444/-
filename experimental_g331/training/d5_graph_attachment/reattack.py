"""D5 research reattack with old D3 frozen reversed 32, shuffled supervision,
neutral baselines, non-template natural Russian, plus weight ablation.
Does not modify any previous holdout or training file.
"""
import json,hashlib,random
from pathlib import Path
from logistic import *
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

r=json.loads((L/'D5_HOLDOUT_FROZEN.json').read_text())['generated']
train=json.loads((L/'D5_TRAIN.json').read_text())
m=Model(train);w=train_weights(train,4)
old=json.loads(Path('/mnt/data/c4_decisive_lab/D3_NEW_DEPTH_REATTACK_FROZEN.json').read_text())['reversed_role_order']
# Old D3 is hardcoded to require HOLDER preceding OP, even with oracle labels.
old_builder_good=sum(build_ast(tokenize(e['text']),e['tags'])==e['ast'] for e in old)
logistic_oracle_good=sum(m.predict(e,e['tags'])==e['ast'] for e in old)
logistic_learnt_good=sum(m.predict(e,decode(tokenize(e['text']),w))==e['ast'] for e in old)

class Shuffled(Model):
    def __init__(self,train,seed):
        self.r={};rec=records(train)
        for name,(xx,yy) in rec.items():
            rng=random.Random(seed+{'HOLDER':0,'ARG':1,'NEG':2}[name]);lab=yy[:];rng.shuffle(lab)
            v=DictVectorizer();X=v.fit_transform(xx)
            clf=LogisticRegression(C=1.,max_iter=1000,class_weight='balanced',random_state=0).fit(X,lab)
            self.r[name]=(v,clf)

out={'old_d3_reversed32':{'total':len(old),'old_builder_oracle':old_builder_good,'new_model_oracle':logistic_oracle_good,'new_model_learned_tags':logistic_learnt_good},'scrambled':{},'ablated':{},'out_of_distribution':{}}
for seed in (19,29,41):
    s=Shuffled(train,seed)
    out['scrambled'][str(seed)]={k:measure({k:v},s)[k]['correct'] for k,v in r.items()}
# remove learned argument graph topology and negation, leave Holder; record different scopes
for mod in ('no_ARG','no_HOLDER','no_NEG'):
    mm=Model(train)
    from types import MethodType
    score=mm.score
    def ablated_score(self,n,a,b,name):return 0.0 if ('no_'+name)==mod else score(n,a,b,name)
    mm.score=MethodType(ablated_score,mm)
    out['ablated'][mod]={k:measure({k:v},mm)[k]['correct'] for k,v in r.items()}
# Natural and off-distribution examples (independent of original synthetic training grammar).
# DO NOT treat any resulting AST as a truthful source/world fact.
probes=[
'Нелли считает будто железный волк золотой',
'Нелли не думает что хрустальный кит прозрачный',
'По словам Весты Нелли думает что железный волк золотой',
'Я не знаю думает ли Нелли о железном волке',
'Пожалуйста напомни мне купить молоко',
'Треугольник не является квадратом',
'Злата думает что Веста знает что кит не золотой',
'Что именно сказала Нелли про волка',
'Кот не синий так считает Нелли',
'Вчера Нелли сказала что через час передумает',
]
for p in probes:
    e={'text':p,'tags':[]};tag=decode(tokenize(p),w)
    out['out_of_distribution'][p]={'status':'CANDIDATE' if m.predict(e,tag) is not None else 'ABSTAIN','ast':m.predict(e,tag),'tags':tag}
write_json(L/'D5_REATTACK_RESULTS.json',out)
print('OLD_D3',out['old_d3_reversed32']);print('SHUFFLED',out['scrambled']);print('ABLATION',out['ablated']);print('OUT_OF_DISTRIBUTION',{k:v['status'] for k,v in out['out_of_distribution'].items()})