"""G324-P3: experimental empirical causal-factor candidates from *receipted* events.

The learner detects predictive associations, NOT causal necessity or WORLD truth.
It never changes C4Graph, acts, or authorizes COMMIT. Synthetic input stays SIMULATION.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations, product
from math import log
from typing import Dict, Mapping


@dataclass(frozen=True)
class ObservedTransition:
    root: str
    x: tuple
    y: int
    scope: str
    frame: str
    epoch: str
    receipt: str


class EmpiricalConstraintLearner:
    """Context-scoped finite-domain structure search using penalized Bernoulli NLL.

    A finite, explicit feature dictionary is an interface, not a lookup of answers.
    Each independently receipted transition contributes at most one observation.
    Minimum support and abstention prevent gaps from becoming certain facts.
    """
    def __init__(self, features, *, scope='SIMULATION', frame='ROOT', epoch='E0', max_parents=3, min_support=2):
        self.features=tuple(features)
        if not self.features or len(set(self.features))!=len(self.features) or len(self.features)>12:
            raise ValueError('invalid feature interface')
        if scope not in {'SIMULATION','OBSERVATION'}:
            raise ValueError('learner cannot claim WORLD evidence')
        if not 0 < max_parents <= 4:
            raise ValueError('invalid max_parents')
        self.scope=str(scope);self.frame=str(frame);self.epoch=str(epoch)
        self.max_parents=min(int(max_parents),len(self.features));self.min_support=max(1,int(min_support))
        self._records:Dict[str,ObservedTransition]={}
        self._quarantined=set()
        self.parents=None
        self.counts={}
        self.score=None

    def observe(self, values:Mapping[str,int], outcome:int, *, root:str, receipt:str,
                scope:str=None, frame:str=None, epoch:str=None):
        if not root or not receipt: return 'NO_RECEIPT'
        if str(scope or self.scope)!=self.scope or str(frame or self.frame)!=self.frame or str(epoch or self.epoch)!=self.epoch:
            return 'CONTEXT_MISMATCH'
        if set(values)!=set(self.features) or any(type(values[k]) is not int or values[k] not in (0,1) for k in self.features):
            raise ValueError('expected all binary features')
        if type(outcome) is not int or outcome not in (0,1):raise ValueError('binary outcome required')
        t=ObservedTransition(str(root),tuple(values[k] for k in self.features),outcome,self.scope,self.frame,self.epoch,str(receipt))
        prev=self._records.get(t.root)
        if t.root in self._quarantined:return 'QUARANTINED'
        if prev is not None:
            if (prev.x,prev.y)==(t.x,t.y):return 'DUPLICATE_ROOT'
            # Root used to attest contradictory events; both are excluded.
            self._records.pop(t.root);self._quarantined.add(t.root)
            self.parents=None;self.counts={}
            return 'ROOT_CONFLICT_QUARANTINED'
        self._records[t.root]=t
        self.parents=None;self.counts={}
        return 'LEARNABLE'

    def fit(self):
        samples=list(self._records.values());n=len(samples)
        if n<max(8,self.min_support*4):
            self.parents=None;self.counts={};self.score=None
            return {'status':'INSUFFICIENT','n':n}
        best=None
        # Include the constant model as an unbiased baseline. Penalize parameters
        # instead of always selecting all features (which memorizes every observation).
        for k in range(self.max_parents+1):
            for indexes in combinations(range(len(self.features)),k):
                tbl={}
                for o in samples:
                    key=tuple(o.x[i] for i in indexes)
                    ct=tbl.setdefault(key,[0,0]);ct[o.y]+=1
                nll=0.
                for c0,c1 in tbl.values():
                    # Beta(1,1) smoothing prevents spuriously certain probabilities.
                    p=(c1+1)/(c0+c1+2)
                    nll-=c1*log(p)+c0*log(1-p)
                # BIC parameter cost: a binary conditional table has 2**k parameters.
                objective=nll+0.5*(2**k)*log(n)
                option=(objective,k,indexes,tbl)
                if best is None or option[:3]<best[:3]:best=option
        score,k,indexes,tbl=best
        self.parents=tuple(self.features[i] for i in indexes)
        self.counts={tuple(key):tuple(val) for key,val in tbl.items()}
        self.score=score
        return {'status':'LEARNED_ASSOCIATION','n':n,'parents':self.parents,'penalized_nll':score,
                'quarantined_roots':len(self._quarantined),'scope':self.scope}

    def predict(self, values:Mapping[str,int]):
        if self.parents is None:return {'status':'UNTRAINED','p1':None}
        if not set(self.parents)<=set(values):return {'status':'MISSING_INPUT','p1':None}
        key=tuple(values[x] for x in self.parents)
        vals=self.counts.get(key)
        if vals is None or sum(vals)<self.min_support:
            return {'status':'ABSTAIN','p1':None,'parents':self.parents,'support':sum(vals) if vals else 0}
        c0,c1=vals;p=(c1+1)/(c0+c1+2)
        return {'status':'CANDIDATE','p1':p,'parents':self.parents,'support':c0+c1,
                'kind':'LEARNED_ASSOCIATION','scope':self.scope,'frame':self.frame,'epoch':self.epoch}

    def candidate_factor(self):
        """Emit learned *candidate* factor rows, never a WORLD or authorized COMMIT.

        Only fully covered, unanimously consistent rows are proposed; uncertainty
        remains ABSTAIN. Caller is responsible for retaining SIMULATION scope.
        """
        if self.parents is None:return {'status':'UNTRAINED','rows':()}
        required=list(product((0,1),repeat=len(self.parents)))
        if not all(key in self.counts and sum(self.counts[key])>=self.min_support and 0 in self.counts[key] for key in required):
            return {'status':'NOT_DETERMINISTICALLY_GROUNDED','rows':()}
        rows=[]
        for key in required:
            c0,c1=self.counts[key]
            rows.append(tuple(key)+(0 if c0 else 1,))
        return {'status':'CANDIDATE_FACTOR','ports':self.parents+('outcome',),'rows':tuple(rows),
                'scope':self.scope,'frame':self.frame,'epoch':self.epoch,
                'source_roots':tuple(sorted(self._records)),'committed':False}

    def to_dict(self):
        return {'schema':'C4_EMPIRICAL_CONSTRAINT_V0_1','features':list(self.features),'scope':self.scope,
                'frame':self.frame,'epoch':self.epoch,'max_parents':self.max_parents,
                'min_support':self.min_support,'records':[r.__dict__ for r in self._records.values()],
                'quarantined_roots':sorted(self._quarantined)}

    @classmethod
    def from_dict(cls,d):
        o=cls(d['features'],scope=d['scope'],frame=d['frame'],epoch=d['epoch'],
              max_parents=d['max_parents'],min_support=d['min_support'])
        o._quarantined=set(d['quarantined_roots'])
        for row in d['records']:
            r=ObservedTransition(str(row['root']),tuple(row['x']),int(row['y']),str(row['scope']),
                                 str(row['frame']),str(row['epoch']),str(row['receipt']))
            if r.root in o._quarantined:raise ValueError('quarantined root in records')
            o._records[r.root]=r
        o.fit();return o