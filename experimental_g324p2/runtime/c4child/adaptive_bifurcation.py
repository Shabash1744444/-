"""G324-P2: exploratory nonlinear state/topology co-evolution.

Toy simulator ONLY. No claims of cognition, graph/world fact, real observation,
COMMIT, DRIVE authority, or identified physical evolutionary mechanisms.
A mesoscopic component and a global mean feed down to individual node dynamics;
node dynamics proposes edge rewiring on a distinct step. Bounded and deterministic.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import FrozenSet, Iterable, Sequence, Tuple


Edge = Tuple[int, int]


def components(n: int, edges: Iterable[Edge]) -> Tuple[Tuple[int, ...], ...]:
    adjacency = [set() for _ in range(n)]
    for a, b in edges:
        if not (0 <= a < b < n):
            raise ValueError('invalid undirected edge')
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = set()
    groups = []
    for k in range(n):
        if k not in seen:
            todo = [k]
            seen.add(k)
            group = []
            while todo:
                v = todo.pop()
                group.append(v)
                for w in sorted(adjacency[v]):
                    if w not in seen:
                        seen.add(w)
                        todo.append(w)
            groups.append(tuple(sorted(group)))
    return tuple(groups)


@dataclass(frozen=True)
class DynamicsConfig:
    r: float = 3.5
    neighbor_coupling: float = 0.08
    component_feedback: float = 0.16
    global_feedback: float = 0.02
    link_on: float = 0.045
    link_off: float = 0.085
    perturbation: Tuple[float, ...] = ()
    rewire: bool = True
    top_down: bool = True

    def validate(self, n: int) -> None:
        if n < 2 or not isfinite(self.r) or not (0 < self.r <= 4):
            raise ValueError('invalid nodes/control')
        w = (self.neighbor_coupling, self.component_feedback,
             self.global_feedback)
        if any(not isfinite(x) or x < 0 for x in w) or sum(w) > 1:
            raise ValueError('feedback weights must form a bounded convex update')
        if (not isfinite(self.link_on) or not isfinite(self.link_off) or
                not (0 < self.link_on <= self.link_off <= 1)):
            raise ValueError('invalid hysteresis thresholds')
        if self.perturbation and len(self.perturbation) != n:
            raise ValueError('perturbation count mismatch')
        if any(not isfinite(p) or not (0 <= self.r + p <= 4)
               for p in self.perturbation):
            raise ValueError('local nonlinear control outside bounded domain')


@dataclass(frozen=True)
class DynamicState:
    t: int
    x: Tuple[float, ...]
    edges: FrozenSet[Edge]
    # The forward trajectory is a hypothetical simulation with explicit scope.
    scope: str = 'SIMULATION'
    world_committed: bool = False
    action_authorized: bool = False

    def validated(self) -> 'DynamicState':
        if self.t < 0 or len(self.x) < 2 or any(not isfinite(x) or
                                                    not (0 <= x <= 1) for x in self.x):
            raise ValueError('invalid state')
        components(len(self.x), self.edges)
        if self.scope != 'SIMULATION' or self.world_committed or self.action_authorized:
            raise ValueError('a toy trajectory must not claim world truth or execution authority')
        return self


@dataclass(frozen=True)
class StepResult:
    state: DynamicState
    old_components: Tuple[Tuple[int, ...], ...]
    new_components: Tuple[Tuple[int, ...], ...]
    removed: FrozenSet[Edge]
    added: FrozenSet[Edge]
    # Candidate macro values were computed by read-only aggregation.
    macro_before: float
    macro_after: float


def update(state: DynamicState, cfg: DynamicsConfig) -> StepResult:
    state.validated()
    n = len(state.x)
    cfg.validate(n)
    groups = components(n, state.edges)
    node_to_group = {v: group for group in groups for v in group}
    neighbors = [set() for _ in range(n)]
    for a, b in state.edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    perturb = cfg.perturbation or (0.,) * n
    local = tuple((cfg.r + perturb[i]) * v * (1-v) for i, v in enumerate(state.x))
    global_mean = sum(local)/n
    eps = cfg.neighbor_coupling
    beta = cfg.component_feedback if cfg.top_down else 0.0
    gamma = cfg.global_feedback if cfg.top_down else 0.0
    out = []
    for i in range(n):
        nei = sum(local[j] for j in neighbors[i])/len(neighbors[i]) if neighbors[i] else local[i]
        grp = node_to_group[i]
        meso = sum(local[j] for j in grp)/len(grp)
        value = (1-eps-beta-gamma)*local[i] + eps*nei + beta*meso + gamma*global_mean
        out.append(min(1.,max(0.,value)))
    next_edges = set(state.edges)
    if cfg.rewire:
        next_edges.clear()
        for a in range(n):
            for b in range(a+1, n):
                edge = (a, b)
                distance = abs(out[a]-out[b])
                if edge in state.edges:
                    if distance <= cfg.link_off:
                        next_edges.add(edge)
                elif distance <= cfg.link_on:
                    next_edges.add(edge)
    nxt = DynamicState(state.t+1,tuple(out),frozenset(next_edges)).validated()
    return StepResult(nxt, groups, components(n,nxt.edges),
                      frozenset(state.edges-next_edges),
                      frozenset(next_edges-state.edges),
                      sum(state.x)/n,sum(out)/n)


def run(initial: DynamicState, cfg: DynamicsConfig, steps: int) -> Tuple[StepResult,...]:
    if not 0 <= steps <= 10000:
        raise ValueError('bounded finite iteration budget required')
    current=initial
    history=[]
    for _ in range(steps):
        next_step=update(current,cfg)
        history.append(next_step)
        current=next_step.state
    return tuple(history)


def logistic_series(r: float, x0: float=.177, *, burn: int=1800, keep: int=256) -> Tuple[float,...]:
    if not (0 <= r <= 4) or not (0 <= x0 <= 1) or burn<0 or keep<1 or burn+keep>100000:
        raise ValueError('invalid logistic domain/budget')
    x=x0
    out=[]
    for t in range(burn+keep):
        x = r*x*(1-x)
        if t>=burn:
            out.append(x)
    return tuple(out)


def period_bound(values: Sequence[float], max_period: int=32, tol: float=1e-7) -> int|None:
    """Return a small approximate attracting period, or None (not 'chaos')."""
    if len(values) < 2*max_period:
        raise ValueError('insufficient recent trajectory')
    for k in range(1,max_period+1):
        if max(abs(values[-1-j]-values[-1-j-k]) for j in range(max_period))<tol:
            return k
    return None