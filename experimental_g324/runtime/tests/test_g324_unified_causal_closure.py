"""Adversarial structural experiments: do not confuse toy CSPs with cognition."""
import pytest
from itertools import product
from random import Random
from c4child.causal_closure import Variable, CausalConstraintClosure


def V(name,**kw): return Variable(name,**kw)


def test_three_way_synergy_cannot_be_recovered_from_isolated_inputs():
    m=CausalConstraintClosure()
    a,b,y=[m.variable(V(k),(0,1)) for k in 'aby']
    # Hard three-way constraint, not 54 separate handlers.
    m.factor((a,b,y),((i,j,i^j) for i,j in product((0,1),repeat=2)))
    out=m.solve();assert out.status=='AMBIGUOUS';assert len(out.candidates)==4
    assert all(k[2]==(k[0]^k[1]) for k,_ in out.candidates)
    # Fix two independent incoming observations, new output follows without a special procedure.
    m.factor((a,),((1,),));m.factor((b,),((0,),))
    out=m.solve();assert out.status=='RESOLVED';assert out.candidates[0][0]==(1,0,1)
    assert not out.world_committed and not out.action_authorized


def test_source_replay_cannot_gain_independence():
    m=CausalConstraintClosure();t=m.variable(V('truth',scope='SOURCE_ASSERTION'),(0,1))
    m.factor((t,),((1,),),kind='EVIDENCE',root='ONE_SOURCE',strength=2)
    a=m.solve();assert len(a.roots)==1
    for _ in range(200):m.factor((t,),((1,),),kind='EVIDENCE',root='ONE_SOURCE',strength=2)
    b=m.solve();assert a.candidates==b.candidates and len(b.roots)==1
    m.factor((t,),((0,),),kind='EVIDENCE',root='INDEPENDENT_SOURCE',strength=2)
    assert len(m.solve().roots)==2


def test_typed_frames_cannot_conflate_identical_words():
    m=CausalConstraintClosure();self_ref=m.variable(V('I',frame='CURRENT_USER'),('Ruslan','Anya'))
    other=m.variable(V('I',frame='MASHA_QUOTE'),('Ruslan','Anya'))
    m.factor((other,),(('Anya',),));m.factor((self_ref,),(('Ruslan',),))
    out=m.solve();assert out.status=='RESOLVED'
    assert dict(zip(out.variable_order,out.candidates[0][0]))[self_ref]=='Ruslan'
    assert dict(zip(out.variable_order,out.candidates[0][0]))[other]=='Anya'


def test_simulation_cannot_change_world_by_same_name():
    m=CausalConstraintClosure();u=m.variable(V('SIGHTING',scope='WORLD'),('seen','not_seen'))
    sim=m.variable(V('SIGHTING',scope='SIMULATION'),('seen','not_seen'))
    m.factor((sim,),(('seen',),))
    z=m.solve();assert z.status=='AMBIGUOUS'
    assert {dict(zip(z.variable_order,a))[u] for a,_ in z.candidates}=={'seen','not_seen'}


def test_temporal_scope_cannot_replace_current_identity():
    m=CausalConstraintClosure();now=m.variable(V('NAME',time='NOW'),('a','b'))
    past=m.variable(V('NAME',time='PAST'),('a','b'))
    m.factor((past,),(('a',),));out=m.solve()
    assert {dict(zip(out.variable_order,a))[now] for a,_ in out.candidates}=={'a','b'}


def test_deep_nested_role_frames_survive_distinct_contexts():
    m=CausalConstraintClosure()
    vars=[m.variable(V('belief',frame='/'.join('A' if j%2 else 'B' for j in range(i+1))),(0,1)) for i in range(6)]
    m.factor((vars[-1],),((1,),));o=m.solve()
    assert o.status=='AMBIGUOUS';assert len(o.candidates)==32


def test_opposing_independent_hard_constraints_produce_inconsistency():
    m=CausalConstraintClosure();x=m.variable(V('X'),(0,1))
    m.factor((x,),((0,),));m.factor((x,),((1,),))
    assert m.solve().status=='INCONSISTENT'


def test_resource_exhaustion_yields_unknown_not_guessed():
    m=CausalConstraintClosure()
    for i in range(22):m.variable(V('v'+str(i)),(0,1))
    out=m.solve(budget=1024)
    assert out.status=='BUDGET_EXHAUSTED' and not out.candidates


def test_no_user_authored_action_from_factor_inference():
    m=CausalConstraintClosure();x=m.variable(V('send_command'),(0,1))
    m.factor((x,),((1,),));z=m.solve()
    assert z.status=='RESOLVED' and not z.action_authorized and not z.world_committed


def test_bad_inputs_fail_closed():
    m=CausalConstraintClosure();x=m.variable(V('x'),(0,1))
    with pytest.raises(ValueError):m.factor((x,),((2,),))
    with pytest.raises(ValueError):m.factor((x,),((1,),),kind='EVIDENCE')
    with pytest.raises(ValueError):m.variable(x,(0,1,2))


def test_54_independent_schemas_with_cross_domain_triples():
    # 54 is experimental coverage of diverse schema identities; NOT 54 cognitive laws proved.
    ids=(['P%02d'%i for i in range(1,7)]+['A%02d'%i for i in range(1,7)]+
         ['M%02d'%i for i in range(1,9)]+['L%02d'%i for i in range(1,8)]+
         ['G%02d'%i for i in range(1,8)]+['J%02d'%i for i in range(1,7)]+
         ['S%02d'%i for i in range(1,8)]+['R%02d'%i for i in range(1,8)])
    assert len(ids)==54
    rnd=Random(1744444)
    for i,case in enumerate(ids):
        m=CausalConstraintClosure()
        x,y,z=[m.variable(V(j,scope=case,frame='case_'+str(i)),(0,1)) for j in 'xyz']
        invert=rnd.randrange(2);v1=rnd.randrange(2);v2=rnd.randrange(2)
        m.factor((x,y,z),((a,b,a^b^invert) for a,b in product((0,1),repeat=2)))
        m.factor((x,),((v1,),));m.factor((y,),((v2,),))
        out=m.solve()
        assert out.status=='RESOLVED' and out.candidates[0][0]==(v1,v2,v1^v2^invert)
        assert not out.world_committed and not out.action_authorized


def test_permutations_and_order_do_not_change_explanatory_content():
    rnd=Random(722)
    for i in range(64):
        x,y,z=[V(j,scope=str(i)) for j in ('x','y','z')]
        bits=[rnd.randrange(2) for _ in range(3)]
        rows=[(a,b,a^b^bits[2]) for a,b in product((0,1),repeat=2)]
        variants=[]
        for backwards in (False,True):
            m=CausalConstraintClosure()
            for key in ([x,y,z] if not backwards else [z,y,x]):m.variable(key,(0,1))
            m.factor((x,y,z),rows)
            fx=[((x,),((bits[0],),)),((y,),((bits[1],),))]
            for ports,allowed in (fx[::-1] if backwards else fx):m.factor(ports,allowed)
            a=m.solve();assert a.status=='RESOLVED'
            variants.append(dict(zip(a.variable_order,a.candidates[0][0])))
        assert variants[0]==variants[1]

@pytest.mark.parametrize('message',[ 
    'Маша сказала: «Меня зовут Аня»',
    'Маша сказала: «Тебя зовут Лира»',
    'Я подумал: «Меня зовут Вера»',
    'Проверим фразу: «Тебя зовут Никита»',
])
def test_real_g322_nested_quote_no_outer_identity_candidate(message):
    from c4child.graph import C4Graph
    from c4child.dialogue import C4ChildDialogue
    from c4child.runtime import C4LivingRuntime
    g=C4Graph();g.set_constitutional_mode('STRICT')
    d=C4ChildDialogue(graph=g,principal='USER');r=C4LivingRuntime(d)
    original=(len(g.entities),len(g.facts),g.order)
    r.user_message(message)
    candidates=r.semantic_spine.interpretations[r.semantic_spine.last_external_event_id]
    assert any(c['quoted_depth']==1 for c in candidates)
    assert not any(c['relation']=='NAME' and c['quoted_depth']==0 for c in candidates)
    assert g.get(d.self_eid,'NAME',viewer='USER',principal='USER',scope='SOCIAL_REPORT') is None
    assert g.get(d.user_eid,'NAME',viewer='USER',principal='USER',scope='SOCIAL_REPORT') is None


def test_real_g322_outer_name_remains_available_when_quote_is_other_content():
    from c4child.semantic_spine import SemanticSpine
    s=SemanticSpine();s.record_event(event_id='test',actor='OTHER',channel='CHAT_TEXT',payload='',internal_step=1)
    results=s.analyze_surface('test','Меня зовут Руслан. Маша сказала: «Меня зовут Аня»')
    direct=[x for x in results if x['relation']=='NAME']
    assert len(direct)==1 and direct[0]['object_value']=='Руслан'


def test_54_simultaneous_crosslinked_processes_resolve_with_one_algorithm():
    """One coupled hypernetwork, not 54 separately executed toy worlds.
    Does NOT validate the empirical laws whose atlas IDs inspired the count.
    """
    rnd=Random(32054)
    m=CausalConstraintClosure()
    variables=[m.variable(V('process_'+str(i),scope='SYNTHETIC_WORLD',time='T0'),(0,1)) for i in range(54)]
    # A single constraint family, heterogeneous shared ports, 54 nodes.
    # Anchor first two nodes, then every new node depends on the previous two.
    for i in range(2,54):
        offset=rnd.randrange(2)
        m.factor((variables[i-2],variables[i-1],variables[i]),
                 ((a,b,a^b^offset) for a,b in product((0,1),repeat=2)))
    m.factor((variables[0],),((1,),))
    m.factor((variables[1],),((0,),))
    result=m.solve(budget=1024)
    assert result.status=='RESOLVED' and len(result.candidates)==1
    assert len(result.candidates[0][0])==54
    assert result.combinations_checked==1
    assert not result.world_committed


def test_ablation_breaking_one_shared_intersection_creates_ambiguity():
    # Same information and algorithm, remove one hyperedge and track loss of determinacy.
    def build(join):
        m=CausalConstraintClosure()
        a,b,c,d=[m.variable(V(x), (0,1)) for x in 'abcd']
        m.factor((a,b,c), ((x,y,x^y) for x,y in product((0,1),repeat=2)))
        if join:
            m.factor((b,c,d), ((x,y,x^y) for x,y in product((0,1),repeat=2)))
        m.factor((a,),((1,),));m.factor((b,),((0,),))
        return m.solve()
    complete,cut=build(True),build(False)
    assert complete.status=='RESOLVED' and len(complete.candidates)==1
    assert cut.status=='AMBIGUOUS' and len(cut.candidates)==2