"""Frozen P2 controls: nonlinear bifurcation != fractal C4 consciousness.

All tests operate on an isolated SIMULATION toy: they must never write
canonical knowledge or exercise DRIVE/MEDIATE authorization.
"""
from dataclasses import replace
from math import isfinite, log
from random import Random
import pytest
from c4child.adaptive_bifurcation import (
    DynamicsConfig, DynamicState, components, update, run,
    logistic_series, period_bound
)


def make_init(n=12):
    return DynamicState(0, tuple(.13 + .73 * ((i*7)%13)/13 for i in range(n)),
                        frozenset((i, i+1) for i in range(n-1)))


@pytest.mark.parametrize('r,expected',[(2.90,1),(3.20,2),(3.50,4),(3.56,8)])
def test_known_period_doubling_on_single_logistic_map(r, expected):
    assert period_bound(logistic_series(r)) == expected


def test_chaotic_map_is_not_mislabelled_as_small_exact_period():
    assert period_bound(logistic_series(3.80)) is None


def test_lyapunov_sign_is_attracting_vs_chaotic():
    def lam(r):
        series=logistic_series(r, burn=2000, keep=1500)
        return sum(log(max(1e-15,abs(r*(1-2*x)))) for x in series)/len(series)
    assert lam(3.20) < -.01
    assert lam(3.80) > .1


def test_graph_is_endogenous_and_can_switch_topology():
    data=run(make_init(),DynamicsConfig(r=3.65,component_feedback=0,global_feedback=0,
                 perturbation=tuple(((i%5)-2)*.008 for i in range(12))),220)
    assert any(s.added for s in data)
    assert any(s.removed for s in data)
    assert len({s.state.edges for s in data[-80:]})>10
    assert any(s.old_components!=s.new_components for s in data)


def test_top_down_macro_influences_an_otherwise_disconnected_node():
    start=DynamicState(0,(.19,.41,.77,.59),frozenset())
    cfg=DynamicsConfig(r=3.45,neighbor_coupling=0,component_feedback=0,
                       global_feedback=.30,rewire=False)
    a=update(start,cfg).state
    b=update(start,replace(cfg,top_down=False)).state
    assert any(abs(x-y)>.001 for x,y in zip(a.x,b.x))
    # On following iteration the changed leaf affects the next macro aggregate.
    assert update(a,cfg).macro_before==update(b,cfg).macro_before
    assert update(a,cfg).macro_after!=update(b,cfg).macro_after


def test_node_perturbation_crosses_component_boundary_only_through_global_macro():
    init=DynamicState(0,(.20,.35,.70,.90),frozenset())
    alt=DynamicState(0,(.21,.35,.70,.90),frozenset())
    cfg=DynamicsConfig(r=3.2,neighbor_coupling=0,component_feedback=.15,
                       global_feedback=.3,rewire=False)
    with_feedback=update(init,cfg).state.x,update(alt,cfg).state.x
    no_feedback=update(init,replace(cfg,top_down=False)).state.x,update(alt,replace(cfg,top_down=False)).state.x
    assert with_feedback[0][3]!=with_feedback[1][3]
    assert no_feedback[0][3]==no_feedback[1][3]


def test_ablations_topology_only_and_top_down_only_have_distinct_consequences():
    init=make_init(); perturb=tuple(((i%5)-2)*.008 for i in range(12))
    cfg=DynamicsConfig(r=3.8,component_feedback=.3,global_feedback=.06,perturbation=perturb)
    full=run(init,cfg,200)
    frozen=run(init,replace(cfg,rewire=False),200)
    no_td=run(init,replace(cfg,top_down=False),200)
    assert all(s.state.edges==init.edges for s in frozen)
    assert any(s.state.edges!=init.edges for s in full)
    assert full[-1].state.x!=no_td[-1].state.x
    assert full[-1].state.x!=frozen[-1].state.x


def test_feedback_can_reduce_topological_churn_but_not_as_universal_law():
    perturb=tuple(((i%5)-2)*.008 for i in range(12))
    cfg=DynamicsConfig(r=3.65,component_feedback=0,global_feedback=0,perturbation=perturb)
    a=run(make_init(),cfg,500)
    b=run(make_init(),replace(cfg,component_feedback=.16,global_feedback=.02),500)
    churn=lambda hist:sum(bool(z.added or z.removed) for z in hist[-300:])
    assert churn(a)>100
    assert churn(b)<20
    # This is one parameter window, not a general convergence proof.


def test_reversible_reporting_does_not_mutate_past_snapshots():
    init=make_init(6)
    original_edges=init.edges
    first=update(init,DynamicsConfig())
    second=update(first.state,DynamicsConfig())
    assert init.edges==original_edges
    assert init.t==0 and first.state.t==1 and second.state.t==2
    assert first.old_components==components(len(init.x),init.edges)


def test_simulated_branch_never_grants_c4_authority():
    init=make_init(6)
    hist=run(init,DynamicsConfig(),10)
    assert all(z.state.scope=='SIMULATION' and not z.state.world_committed
               and not z.state.action_authorized for z in hist)


@pytest.mark.parametrize('param',[
    {'r':float('nan')}, {'r':float('inf')}, {'r':4.2},
    {'neighbor_coupling':float('nan')}, {'global_feedback':-.1},
    {'component_feedback':.8,'neighbor_coupling':.3},
    {'link_on':float('nan')}, {'link_off':-1},
    {'perturbation':(1.0,)}
])
def test_poisoned_configuration_fails_closed(param):
    with pytest.raises(ValueError):update(make_init(4),DynamicsConfig(**param))


@pytest.mark.parametrize('bad_x',[(float('nan'),.1),(.1,float('inf')),(-.1,.1)])
def test_poisoned_state_fails_closed(bad_x):
    with pytest.raises(ValueError):update(DynamicState(0,bad_x,frozenset()),DynamicsConfig())


def test_external_graph_edges_must_be_canonical_undirected_pairs():
    with pytest.raises(ValueError):components(4,[(2,1)])
    with pytest.raises(ValueError):components(4,[(0,9)])


def test_iteration_budget_and_reproducibility():
    init=make_init(6); cfg=DynamicsConfig(r=3.6)
    with pytest.raises(ValueError):run(init,cfg,10001)
    assert run(init,cfg,70)==run(init,cfg,70)
    assert run(init,cfg,0)==()


def test_seeded_random_graphs_remain_bounded_and_legal_after_many_iterations():
    r=Random(3242026)
    for trial in range(64):
        n=r.randint(3,12)
        v=tuple(r.uniform(.03,.97) for _ in range(n))
        edges=frozenset((a,b) for a in range(n) for b in range(a+1,n) if r.random()<.3)
        start=DynamicState(0,v,edges)
        cfg=DynamicsConfig(r=r.uniform(2.8,3.99),neighbor_coupling=r.uniform(0,.12),
                           component_feedback=r.uniform(0,.22),global_feedback=r.uniform(0,.12),
                           link_on=.03,link_off=.10)
        results=run(start,cfg,40)
        for step in results:
            assert all(isfinite(x) and 0<=x<=1 for x in step.state.x)
            assert not step.state.world_committed and not step.state.action_authorized
            assert all(0<=a<b<n for a,b in step.state.edges)
        assert results[-1].state.t==40


def test_same_trajectory_has_multiple_organizational_scales():
    init=DynamicState(0,(.10,.12,.70,.72),frozenset({(0,1),(2,3)}))
    step=update(init,DynamicsConfig(r=3.1,neighbor_coupling=.05,component_feedback=.2,
                                    global_feedback=.1,rewire=False))
    assert len(step.old_components)==2
    assert step.macro_after==sum(step.state.x)/4
    assert step.macro_before==sum(init.x)/4
    assert step.state.x[0]!=step.state.x[2]