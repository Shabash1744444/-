"""Experimental, read-only typed causal constraint closure for C4.

NO graph mutation, model learning, grounding or action authorization.
One generic finite-domain hyperfactor operator handles cross-mechanism compositions.
No lexical triggers or phenotype-specific procedures are present in this module.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from itertools import product
from math import exp, isfinite, log
from typing import Any, Dict, Hashable, Iterable, Mapping, Optional, Sequence, Tuple


@dataclass(frozen=True)
class Variable:
    """An interface is joined ONLY by full typed identity, never by bare name."""
    name: str
    scope: str = 'WORLD'
    frame: str = 'ROOT'
    time: str = 'NOW'
    entity: str = ''


@dataclass(frozen=True)
class Factor:
    ports: Tuple[Variable, ...]
    # Allowed rows: tuples of values. No row -> prohibited by hard factor.
    table: Tuple[Tuple[Hashable, ...], ...]
    kind: str = 'STRUCTURE'  # STRUCTURE or EVIDENCE
    root: str = ''  # dependent replays/copies reuse the same root
    label: str = ''
    strength: float = 1.0


@dataclass(frozen=True)
class ClosureResult:
    status: str  # RESOLVED, AMBIGUOUS, INCONSISTENT, BUDGET_EXHAUSTED
    domains: Dict[Variable, Tuple[Hashable, ...]]
    candidates: Tuple[Tuple[Tuple[Hashable, ...], float], ...]
    variable_order: Tuple[Variable, ...]
    roots: Tuple[str, ...]
    combinations_checked: int
    action_authorized: bool = False
    world_committed: bool = False
    conflicted_roots: Tuple[str, ...] = ()


class CausalConstraintClosure:
    """Finite-domain generalized-arc-consistency plus bounded exhaustive EVAL.

    Tables represent relationships supplied by an observation model/learning.
    We do not assume they arise naturally from four laws. This is deliberately
    a minimal, falsifiable organizational substrate rather than a chatbot.
    """
    def __init__(self):
        self._domains: Dict[Variable, Tuple[Hashable, ...]] = {}
        self._factors = []

    def variable(self, key: Variable, domain: Iterable[Hashable]) -> Variable:
        vals = tuple(dict.fromkeys(domain))
        if not vals:
            raise ValueError('empty domain')
        if key in self._domains and self._domains[key] != vals:
            raise ValueError('incompatible domains for same typed variable')
        self._domains[key] = vals
        return key

    def factor(self, ports: Sequence[Variable], rows: Iterable[Sequence[Hashable]], *,
               kind: str='STRUCTURE', root: str='', label: str='', strength: float=1.0):
        ports = tuple(ports)
        if not ports or len(set(ports)) != len(ports):
            raise ValueError('factor ports must be distinct nonempty')
        if any(p not in self._domains for p in ports):
            raise ValueError('unknown typed port')
        if kind not in {'STRUCTURE','EVIDENCE'}:
            raise ValueError('invalid factor kind')
        if kind == 'EVIDENCE' and not root:
            raise ValueError('evidence MUST have dependency root')
        if not isfinite(strength) or strength < 0:
            raise ValueError('invalid strength')
        normalized = tuple(dict.fromkeys(tuple(row) for row in rows))
        for row in normalized:
            if len(row) != len(ports) or any(v not in self._domains[ports[i]] for i,v in enumerate(row)):
                raise ValueError('out of domain / incorrect arity')
        f = Factor(ports,normalized,kind,root,label,strength)
        self._factors.append(f)
        return f

    def solve(self, budget: int=262144, max_candidates: int=10000) -> ClosureResult:
        if budget < 1 or max_candidates < 1:
            raise ValueError('invalid budget')
        names = tuple(self._domains)
        domains = {v: set(vals) for v,vals in self._domains.items()}
        # Hard constraints prune using generalized arc consistency; EVIDENCE is soft.
        hard = [f for f in self._factors if f.kind == 'STRUCTURE']
        changed = True
        while changed:
            changed = False
            for f in hard:
                live = [row for row in f.table if all(row[i] in domains[v] for i,v in enumerate(f.ports))]
                for i,v in enumerate(f.ports):
                    filtered = domains[v] & {row[i] for row in live}
                    if filtered != domains[v]:
                        domains[v] = filtered
                        changed = True
                    if not filtered:
                        return ClosureResult('INCONSISTENT',
                            {n:tuple(v for v in self._domains[n] if v in domains[n]) for n in names},
                            (),names,(),0)
        # Deduplicate reports/replays with same lineage and identical semantic factor.
        evidence = []
        seen = set()
        for f in self._factors:
            if f.kind != 'EVIDENCE': continue
            token = (f.root,f.ports,f.table)
            if token in seen:continue
            seen.add(token)
            evidence.append(f)
        roots = tuple(sorted(set(f.root for f in evidence)))
        lists = [tuple(v for v in self._domains[n] if v in domains[n]) for n in names]
        complexity=1
        for d in lists: complexity *= len(d)
        if complexity>budget:
            return ClosureResult('BUDGET_EXHAUSTED',
                {n:d for n,d in zip(names,lists)},(),names,roots,0)
        # Make a complete list of *structurally allowed* candidates first.
        # A single dependency root must not invent a preference by telling two
        # mutually exclusive stories. Such a root is quarantined, not counted
        # as multiple independent votes nor silently collapsed by max().
        possible=[]
        for vals in product(*lists):
            assignment = dict(zip(names,vals))
            if any(tuple(assignment[v] for v in f.ports) not in f.table for f in hard):
                continue
            possible.append(vals)
            if len(possible)>max_candidates:
                return ClosureResult('BUDGET_EXHAUSTED',
                    {n:d for n,d in zip(names,lists)},(),names,roots,complexity)
        if not possible:
            return ClosureResult('INCONSISTENT',
                {n:d for n,d in zip(names,lists)},(),names,roots,complexity)
        by_root: Dict[str,list]={}
        for f in evidence: by_root.setdefault(f.root,[]).append(f)
        def all_supported(vals, factors):
            assignment=dict(zip(names,vals))
            return all(tuple(assignment[v] for v in f.ports) in f.table for f in factors)
        conflict_roots=tuple(sorted(root for root,items in by_root.items()
                                    if not any(all_supported(vals,items) for vals in possible)))
        candidates=[]
        for vals in possible:
            score=0.0
            for root,items in by_root.items():
                if root in conflict_roots:
                    continue  # contradictory testimony is not independent corroboration
                strength=min(f.strength for f in items)
                score += strength if all_supported(vals,items) else -strength
            candidates.append((vals,score))
        maxscore=max(s for _,s in candidates)
        weights=[exp(s-maxscore) for _,s in candidates]
        normalizer=sum(weights)
        posterior=tuple((vals,w/normalizer) for (vals,_),w in zip(candidates,weights))
        # Different positive-probability interpretations are left ambiguous.
        status='RESOLVED' if len(posterior)==1 else 'AMBIGUOUS'
        return ClosureResult(status,{n:d for n,d in zip(names,lists)},posterior,names,roots,complexity,conflicted_roots=conflict_roots)