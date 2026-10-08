"""Frozen adversarial cases for self-similar C4 causal composition.

This tests candidate topology, not cognition, and prevents circular authority.
"""
from itertools import product
from random import Random
import pytest

from c4child.causal_closure import CausalConstraintClosure, Variable
from c4child.recursive_closure import (
    CausalLayer, glue, IncompleteEvaluation, HiddenSharedInterface, CandidateInterface)


def v(k, **kw): return Variable(k, **kw)


def assignment(result):
    assert result.status == 'RESOLVED'
    return dict(zip(result.variable_order,result.candidates[0][0]))


def mk_layer(variables, relations=(), evidence=()):
    model=CausalConstraintClosure()
    for key,dom in variables:model.variable(key,dom)
    for ports,rows in relations:model.factor(ports,rows)
    for ports,rows,root in evidence:model.factor(ports,rows,kind='EVIDENCE',root=root)
    return CausalLayer(model)


def sample():
    x,y,z,w=[v(k,scope='SIMULATION',time='T17') for k in 'xyzw']
    a=mk_layer([(x,(0,1))],[((x,),((1,),))]).project([x])
    b=mk_layer([(q,(0,1)) for q in (x,y,z)],
               [((x,y,z),tuple((i,j,i^j) for i,j in product((0,1),repeat=2))),
                ((y,),((0,),))]).project([x,y,z])
    c=mk_layer([(q,(0,1)) for q in (z,w)],
               [((z,w),((0,0),(1,1)))]).project([z,w])
    return x,y,z,w,a,b,c


def test_exact_projection_is_associative_with_shared_ports():
    x,y,z,w,a,b,c=sample()
    flat=glue((a,b,c)).model.solve()
    left=glue((glue((a,b)).project([x,y,z]),c)).model.solve()
    right=glue((a,glue((b,c)).project([x,y,z,w]))).model.solve()
    assert assignment(flat)==assignment(left)==assignment(right)=={x:1,y:0,z:1,w:1}


def test_recursive_depth_is_unbounded_in_representation_but_finite_in_execution():
    x,y,z,w,a,b,c=sample()
    chain=glue((a,b,c))
    for _ in range(8):
        chain=glue((chain.project([x,y,z,w]),))
    assert chain.depth==9
    assert assignment(chain.model.solve())=={x:1,y:0,z:1,w:1}
    assert not chain.model.solve().world_committed


def test_shared_hidden_port_destroys_sound_composition_and_is_rejected():
    x,h,y=[v(k) for k in 'xhy']
    left=mk_layer([(q,(0,1)) for q in (x,h)],
                  [((x,h),((0,0),(1,1)))]).project([x])
    right=mk_layer([(q,(0,1)) for q in (h,y)],
                   [((h,y),((0,0),(1,1)))]).project([y])
    with pytest.raises(HiddenSharedInterface):glue((left,right))


def test_local_private_variables_can_be_safely_hidden():
    x,hidden,y=[v(k) for k in 'xhy']
    left=mk_layer([(q,(0,1)) for q in (x,hidden)],
                  [((x,hidden),((0,0),(1,1))),((hidden,),((1,),))]).project([x])
    right=mk_layer([(q,(0,1)) for q in (x,y)],
                   [((x,y),((0,1),(1,0)))]).project([x,y])
    assert assignment(glue((left,right)).model.solve())=={x:1,y:0}


def test_incomplete_nested_solver_must_not_claim_exactness():
    model=CausalConstraintClosure()
    names=[model.variable(v(str(i)),(0,1)) for i in range(22)]
    with pytest.raises(IncompleteEvaluation):CausalLayer(model).project([names[0]],budget=128)


def test_child_inconsistency_stays_explicit():
    t=v('x');ch=mk_layer([(t,(0,1))],[((t,),((0,),)),((t,),((1,),))])
    projected=ch.project([t]);assert projected.relation==()
    assert glue((projected,)).model.solve().status=='INCONSISTENT'


def test_same_evidence_root_with_opposing_claims_is_quarantined():
    t=v('T',scope='SOURCE_ASSERTION')
    model=CausalConstraintClosure();model.variable(t,(0,1))
    model.factor((t,),((0,),),kind='EVIDENCE',root='R1',strength=12)
    model.factor((t,),((1,),),kind='EVIDENCE',root='R1',strength=2)
    out=model.solve()
    assert out.status=='AMBIGUOUS'
    assert out.conflicted_roots==('R1',)
    assert out.candidates[0][1]==out.candidates[1][1]==0.5
    assert not out.world_committed


def test_one_bad_root_never_overrules_independent_root():
    t=v('T')
    model=CausalConstraintClosure();model.variable(t,(0,1))
    model.factor((t,),((0,),),kind='EVIDENCE',root='R1',strength=50)
    model.factor((t,),((1,),),kind='EVIDENCE',root='R1',strength=1)
    model.factor((t,),((1,),),kind='EVIDENCE',root='R2',strength=2)
    z=model.solve()
    assert z.conflicted_roots==('R1',)
    assert z.candidates[1][1]>z.candidates[0][1]


def test_repeated_reports_ancestry_is_not_new_evidence_across_layers():
    t=v('claim',scope='SOURCE_ASSERTION')
    child=mk_layer([(t,(0,1))],evidence=[((t,),((1,),),'ONE')])
    source=child.project([t])
    assert source.dependency_roots==('ONE',)
    layer=glue((source,source,source)).project([t])
    assert layer.dependency_roots==('ONE',)
    assert layer.epistemic_status=='EVAL_CANDIDATE_ONLY'
    assert not layer.action_authorized and not layer.world_committed


def test_world_and_simulation_ports_do_not_match():
    world=v('moon',scope='WORLD');sim=v('moon',scope='SIMULATION')
    child=mk_layer([(sim,(0,1))],[((sim,),((1,),))]).project([sim])
    outside=mk_layer([(world,(0,1))]).project([world])
    z=glue((child,outside)).model.solve()
    assert z.status=='AMBIGUOUS'
    assert {dict(zip(z.variable_order,a))[world] for a,_ in z.candidates}=={0,1}


def test_frames_and_time_do_not_collapse_at_nesting():
    older=v('I',frame='Masha',time='PAST');current=v('I',frame='Self',time='NOW')
    old=mk_layer([(older,('Anya','Masha'))],[((older,),(('Anya',),))]).project([older])
    new=mk_layer([(current,('Anya','Masha'))]).project([current])
    z=glue((old,new)).model.solve()
    assert z.status=='AMBIGUOUS'
    assert len(z.candidates)==2


def test_untrusted_child_candidates_cannot_be_passed_as_committed_interfaces():
    x=v('a');base=mk_layer([(x,(0,1))]).project([x])
    forged=CandidateInterface(base.ports,base.domains,base.relation,base.hidden_ports,(),
                              epistemic_status='WORLD_CERTIFIED')
    with pytest.raises(ValueError):glue((forged,))


def test_constraint_cycle_is_not_a_proof_of_one_state():
    x,y,z=[v(k) for k in 'xyz']
    relations=[((x,y),((0,0),(1,1))),((y,z),((0,0),(1,1))),
               ((z,x),((0,0),(1,1)))]
    layer=mk_layer([(q,(0,1)) for q in (x,y,z)],relations)
    verdict=layer.model.solve()
    assert verdict.status=='AMBIGUOUS' and len(verdict.candidates)==2
    assert not verdict.world_committed


def test_random_grouping_and_permutation_invariant_exact_projection():
    rnd=Random(20261008)
    for trial in range(48):
        x,y,z,w=[v(k,scope=f'T{trial}') for k in 'xyzw']
        a,b,c,d=[rnd.randrange(2) for _ in range(4)]
        u=mk_layer([(q,(0,1)) for q in (x,y)],
                   [((x,y),tuple((j,j^a) for j in (0,1))),((x,),((b,),))]).project([x,y])
        q=mk_layer([(q,(0,1)) for q in (y,z)],
                   [((y,z),tuple((j,j^c) for j in (0,1)))]).project([y,z])
        v1=mk_layer([(q,(0,1)) for q in (z,w)],
                    [((z,w),tuple((j,j^d) for j in (0,1)))]).project([z,w])
        baseline=glue((u,q,v1)).model.solve()
        left=glue((glue((u,q)).project([x,y,z]),v1)).model.solve()
        right=glue((u,glue((q,v1)).project([y,z,w]))).model.solve()
        expected={x:b,y:b^a,z:b^a^c,w:b^a^c^d}
        assert assignment(baseline)==assignment(left)==assignment(right)==expected


def test_boundary_domain_mismatch_rejected():
    x=v('x');a=mk_layer([(x,(0,1))]).project([x]);b=mk_layer([(x,(0,1,2))]).project([x])
    with pytest.raises(ValueError):glue((a,b))


def test_nested_lexical_evidence_is_not_an_external_receipt():
    x=v('moon_is_cheese',scope='WORLD')
    guessed=mk_layer([(x,(0,1))],evidence=[((x,),((1,),),'REPLAY_001')])
    tree=glue((guessed.project([x]),))
    assert tree.project([x]).dependency_roots==('REPLAY_001',)
    assert len(tree.model.solve().candidates)==2
    assert tree.model.solve().status=='AMBIGUOUS'
    assert not tree.model.solve().world_committed


def test_soft_evidence_preserves_probabilities_under_exact_gluing():
    x,y=[v(k,scope='SOURCE_ASSERTION') for k in 'xy']
    left=mk_layer([(x,(0,1))],evidence=[((x,),((1,),),'SOURCE_A')]).project([x])
    right=mk_layer([(x,(0,1)),(y,(0,1))],
                   relations=[((x,y),((0,1),(1,0)))],
                   evidence=[((y,),((1,),),'SOURCE_B')]).project([x,y])
    merged=glue((left,right));z=merged.solve()
    assert z.status=='AMBIGUOUS'
    # Product of two child likelihoods gives equal confidence for both assignments:
    # Source A prefers x=1; source B prefers y=1 (i.e. x=0).
    assert abs(z.candidates[0][1]-0.5)<1e-12
    assert abs(z.candidates[1][1]-0.5)<1e-12
    assert merged.project([x]).dependency_roots==('SOURCE_A','SOURCE_B')
    assert abs(sum(merged.project([x]).probabilities)-1)<1e-12


def test_soft_marginalization_keeps_hidden_multiplicity():
    x,h=[v(k) for k in 'xh']
    # x=0 has two hidden completions, x=1 has one.
    left=mk_layer([(x,(0,1)),(h,(0,1))],
                  relations=[((x,h),((0,0),(0,1),(1,1)))]).project([x])
    assert left.relation==((0,),(1,))
    assert left.probabilities==(pytest.approx(2/3),pytest.approx(1/3))
    z=glue((left,)).solve()
    assert z.candidates[0][1]==pytest.approx(2/3)
    assert z.candidates[1][1]==pytest.approx(1/3)


def test_duplicate_child_interface_does_not_multiply_evidence():
    x=v('x');candidate=mk_layer([(x,(0,1))],evidence=[((x,),((1,),),'ONE')]).project([x])
    a=glue((candidate,)).solve()
    b=glue((candidate,candidate,candidate,candidate)).solve()
    assert a.candidates==b.candidates
    assert glue((candidate,candidate)).project([x]).dependency_roots==('ONE',)


def test_shared_root_across_distinct_children_is_not_independent():
    x,y=[v(k) for k in 'xy']
    a=mk_layer([(x,(0,1))],evidence=[((x,),((1,),),'R')]).project([x])
    b=mk_layer([(y,(0,1))],evidence=[((y,),((1,),),'R')]).project([y])
    from c4child.recursive_closure import SharedDependentRoot
    with pytest.raises(SharedDependentRoot):glue((a,b))


def test_recursive_evidence_marginalization_is_associative_without_shared_roots():
    x,y,z=[v(k) for k in 'xyz']
    a=mk_layer([(x,(0,1))],evidence=[((x,),((1,),),'A')]).project([x])
    b=mk_layer([(q,(0,1)) for q in (x,y)],
               relations=[((x,y),((0,1),(1,0)))],
               evidence=[((y,),((1,),),'B')]).project([x,y])
    c=mk_layer([(q,(0,1)) for q in (y,z)],
               relations=[((y,z),((0,0),(0,1),(1,1)))],
               evidence=[((z,),((1,),),'C')]).project([y,z])
    flat=glue((a,b,c)).solve()
    left=glue((glue((a,b)).project([x,y]),c)).solve()
    right=glue((a,glue((b,c)).project([x,y,z]))).solve()
    for o in (left,right):
        assert tuple(a for a,p in o.candidates)==tuple(a for a,p in flat.candidates)
        assert tuple(p for a,p in o.candidates)==pytest.approx(tuple(p for a,p in flat.candidates))


def test_256_seed_randomized_nested_vs_flat_candidate_and_probability_oracle():
    """Random constrained hypergraphs, independent sources, separate hidden variables.

    Flat brute-force model is the reference oracle; no target answers entered.
    """
    rng=Random(324101)
    for seed in range(256):
        x,y,z=[v(n,scope=f'S_{seed}') for n in 'xyz']
        internals=[v(f'private_{i}',scope=f'S_{seed}') for i in range(3)]
        clusters=[(x,z,internals[0]),(y,z,internals[1]),(x,y,internals[2])]
        flat=CausalConstraintClosure()
        for key in (x,y,z,*internals):flat.variable(key,(0,1))
        pieces=[]
        for idx,ports in enumerate(clusters):
            allrows=list(product((0,1),repeat=3))
            rows=[row for row in allrows if rng.random()<0.58]
            observed=rng.randrange(2)
            root=f'R{seed}_{idx}'
            sub=mk_layer([(k,(0,1)) for k in ports],
                         relations=[(ports,rows)],
                         evidence=[((ports[2],),((observed,),),root)])
            partial=sub.project(ports[:2],budget=128)
            pieces.append(partial)
            flat.factor(ports,rows)
            flat.factor((ports[2],),((observed,),),kind='EVIDENCE',root=root)
        global_result=flat.solve(budget=128)
        hierarchical=glue(pieces).solve(budget=128)
        if global_result.status=='INCONSISTENT':
            assert hierarchical.status=='INCONSISTENT',seed
            continue
        assert hierarchical.status in {'RESOLVED','AMBIGUOUS'},seed
        assert global_result.status in {'RESOLVED','AMBIGUOUS'}
        global_out={}
        for vals,p in global_result.candidates:
            key=tuple(dict(zip(global_result.variable_order,vals))[t] for t in (x,y,z))
            global_out[key]=global_out.get(key,0)+p
        hierarchy_out={}
        for vals,p in hierarchical.candidates:
            key=tuple(dict(zip(hierarchical.variable_order,vals))[t] for t in (x,y,z))
            hierarchy_out[key]=hierarchy_out.get(key,0)+p
        assert set(global_out)==set(hierarchy_out),seed
        for vals,p in global_out.items():
            assert abs(p-hierarchy_out[vals])<1e-11,(seed,vals,p,hierarchy_out[vals])


def test_malformed_or_empty_projected_interface_does_not_gain_authority():
    x=v('x')
    layer=mk_layer([(x,(0,1))])
    with pytest.raises(ValueError):layer.project([])
    good=layer.project([x])
    bad=CandidateInterface(good.ports,good.domains,good.relation,good.hidden_ports,(),
                           probabilities=(1.0,1.0))
    with pytest.raises(ValueError):glue((bad,))