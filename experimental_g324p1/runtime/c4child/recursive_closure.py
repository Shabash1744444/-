"""G324-P1 experimental multi-scale hypothesis composition for C4.

Read-only, exact finite-domain relational joins. A child solver publishes only a
conditional *candidate* relation plus its dependency roots; it cannot authorize
WORLD COMMIT, DRIVE actions, or MEDIATE receipts.

Matryoshka test: a cluster of local relations may be treated as another relation,
provided every shared variable is explicitly exposed at the interface.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from math import exp, log, isfinite
from typing import Hashable, Iterable, Sequence, Tuple, Union

from .causal_closure import CausalConstraintClosure, Variable, ClosureResult


class IncompleteEvaluation(ValueError):
    """Cannot promote a partial/timeout evaluation into an exact interface."""


class HiddenSharedInterface(ValueError):
    """Factor projection loses necessary correlations through a hidden shared port."""


class SharedDependentRoot(ValueError):
    """Cannot treat two distinct summaries of the same evidence as independent."""


@dataclass(frozen=True)
class CandidateInterface:
    ports: Tuple[Variable, ...]
    domains: Tuple[Tuple[Hashable, ...], ...]
    relation: Tuple[Tuple[Hashable, ...], ...]
    hidden_ports: Tuple[Variable, ...]
    dependency_roots: Tuple[str, ...]
    depth: int = 0
    epistemic_status: str = 'EVAL_CANDIDATE_ONLY'
    action_authorized: bool = False
    world_committed: bool = False
    probabilities: Tuple[float, ...] = ()  # Soft EVAL scores, NOT COMMIT authority.


@dataclass
class CausalLayer:
    """A finite-domain graph plus lineage inherited from all nested children."""
    model: CausalConstraintClosure
    inherited_roots: Tuple[str, ...] = ()
    depth: int = 0
    child_messages: Tuple[CandidateInterface, ...] = ()

    def solve(self, *, budget: int=262144, max_candidates: int=10000) -> ClosureResult:
        base=self.model.solve(budget=budget,max_candidates=max_candidates)
        if base.status in {'BUDGET_EXHAUSTED','INCONSISTENT'} or not self.child_messages:
            return base
        position={port:i for i,port in enumerate(base.variable_order)}
        weights=[]
        for vals,_ in base.candidates:
            score=0.0
            for child in self.child_messages:
                row=tuple(vals[position[v]] for v in child.ports)
                idx=child.relation.index(row)
                p=child.probabilities[idx]
                if p<=0 or not isfinite(p):
                    raise ValueError('invalid child probability')
                score+=log(p)
            weights.append(score)
        pivot=max(weights)
        probs=[exp(x-pivot) for x in weights]
        total=sum(probs)
        return replace(base,candidates=tuple((vals,p/total) for (vals,_),p in zip(base.candidates,probs)))

    def project(self, public: Sequence[Variable], *, budget: int=262144,
                max_candidates: int=10000) -> CandidateInterface:
        public=tuple(public)
        if not public:
            raise ValueError('an exact exported interface needs at least one port')
        if len(set(public)) != len(public):
            raise ValueError('duplicated public port')
        if any(p not in self.model._domains for p in public):
            raise ValueError('unknown public port')
        verdict=self.solve(budget=budget,max_candidates=max_candidates)
        if verdict.status=='BUDGET_EXHAUSTED':
            raise IncompleteEvaluation('a partial trace cannot be projected as complete')
        pos={v:i for i,v in enumerate(verdict.variable_order)}
        marginals={}
        for vals,prob in verdict.candidates:
            key=tuple(vals[pos[p]] for p in public)
            marginals[key]=marginals.get(key,0.0)+prob
        relation=tuple(marginals)
        return CandidateInterface(
            ports=public,
            domains=tuple(tuple(self.model._domains[p]) for p in public),
            relation=relation,
            hidden_ports=tuple(v for v in verdict.variable_order if v not in public),
            dependency_roots=tuple(sorted(set(self.inherited_roots)|set(verdict.roots))),
            depth=self.depth,
            probabilities=tuple(marginals.values()))


def glue(layers: Sequence[CandidateInterface]) -> CausalLayer:
    """Join child candidate relations in a read-only hypothesis sandbox.

    Associative up to variable ordering for exact finite projections, *if* no
    cross-child shared variable has been hidden. The result is not evidence.
    """
    layers=tuple(layers)
    if not layers:
        raise ValueError('cannot glue empty ensemble')
    unique=[]
    # Repeated identical child report is a replay, not new information.
    # Conflicting summaries with overlapping roots need a joint evidence model;
    # fail closed rather than double counting their posteriors.
    for a in layers:
        if a in unique:
            continue
        for b in unique:
            if set(a.dependency_roots)&set(b.dependency_roots):
                raise SharedDependentRoot('overlapping source lineage cannot be multiplied')
        unique.append(a)
    layers=tuple(unique)
    for i,a in enumerate(layers):
        if a.epistemic_status != 'EVAL_CANDIDATE_ONLY' or a.world_committed or a.action_authorized:
            raise ValueError('only non-authoritative candidate interfaces permitted')
        if not a.ports or len(a.ports)!=len(a.domains) or len(a.relation)!=len(a.probabilities):
            raise ValueError('malformed candidate interface')
        if any(len(row)!=len(a.ports) for row in a.relation):
            raise ValueError('malformed candidate tuples')
        if a.relation and (any(not isfinite(p) or p<=0 for p in a.probabilities) or
                           abs(sum(a.probabilities)-1)>1e-7):
            raise ValueError('malformed candidate probabilities')
        all_ports=set(a.ports)|set(a.hidden_ports)
        for b in layers[i+1:]:
            # Intersection not carried through the shared exposed boundary = information loss.
            if (set(a.hidden_ports) & (set(b.ports)|set(b.hidden_ports)) or
                set(b.hidden_ports) & all_ports):
                raise HiddenSharedInterface('missing shared identity in one or more interfaces')
    m=CausalConstraintClosure()
    for layer in layers:
        for v,values in zip(layer.ports,layer.domains):
            if v in m._domains:
                if set(m._domains[v])!=set(values):
                    raise ValueError('incompatible public domains')
            else:
                m.variable(v,values)
    for i,layer in enumerate(layers):
        m.factor(layer.ports,layer.relation,label=f'conditional_child_{i}')
    roots=tuple(sorted({root for layer in layers for root in layer.dependency_roots}))
    return CausalLayer(model=m,inherited_roots=roots,depth=1+max(x.depth for x in layers),child_messages=layers)