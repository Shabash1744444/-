"""Frozen G324-P3 research tests: learn factor candidates, never claim WORLD."""
import random
from c4child.learned_constraints import EmpiricalConstraintLearner
from c4child.runtime import C4LivingRuntime


def fresh(features=('a','b'),**kwargs):
    return EmpiricalConstraintLearner(features,scope='SIMULATION',**kwargs)


def train_rule(rule, *, n=240, seed=17, features=('a','b','noise')):
    rng=random.Random(seed)
    le=fresh(features)
    for i in range(n):
        d={key:rng.randrange(2) for key in features}
        result=rule(d)
        assert le.observe(d,result,root=f'experiment_{seed}_trial_{i}',receipt=f'sim_receipt_{i}')=='LEARNABLE'
    le.fit()
    return le


def accuracy(le,rule,*,n=160,seed=123):
    rng=random.Random(seed);correct=0;abstain=0
    for _ in range(n):
        x={f:rng.randrange(2) for f in le.features}
        p=le.predict(x)
        if p['status']=='ABSTAIN':abstain+=1;continue
        assert p['status']=='CANDIDATE'
        correct+=int(int(p['p1']>0.5)==rule(x))
    return correct,n-abstain,abstain


def test_xor_synergy_is_learned_and_irrelevant_noise_excluded():
    rule=lambda x:x['a']^x['b']
    m=train_rule(rule)
    assert set(m.parents)=={'a','b'}
    assert accuracy(m,rule)[0]==160
    assert m.candidate_factor()['status']=='CANDIDATE_FACTOR'


def test_or_rule_is_learned_without_lexical_handlers():
    rule=lambda x:x['a']|x['b']
    m=train_rule(rule,seed=39)
    assert set(m.parents)=={'a','b'}
    assert accuracy(m,rule)[0]==160


def test_one_feature_rule_is_simplified():
    rule=lambda x:x['a']
    m=train_rule(rule,seed=29)
    assert m.parents==('a',)
    assert accuracy(m,rule)[0]==160


def test_irrelevant_predictor_stays_unselected():
    rule=lambda x:x['b']
    m=train_rule(rule,seed=52)
    assert m.parents==('b',)


def test_unobserved_combinations_abstain_without_hallucination():
    l=fresh(features=('a','b'),min_support=2)
    for i in range(12):l.observe({'a':0,'b':0},0,root=f'r{i}',receipt=f's{i}')
    assert l.fit()['status']=='LEARNED_ASSOCIATION'
    # A constant model is a valid inference but cannot establish counterfactual
    # generalization to unseen feature combinations; never export as hard factor.
    assert l.candidate_factor()['status']=='NOT_DETERMINISTICALLY_GROUNDED' or not l.parents


def test_no_event_without_boundary_receipt():
    l=fresh()
    assert l.observe({'a':0,'b':1},1,root='r',receipt='')=='NO_RECEIPT'
    assert l.fit()['status']=='INSUFFICIENT'


def test_scope_frame_epoch_do_not_cross():
    l=fresh(frame='actor_1',epoch='chapter_1')
    assert l.observe({'a':0,'b':0},1,root='r',receipt='rx',frame='actor_2')=='CONTEXT_MISMATCH'
    assert l.observe({'a':0,'b':0},1,root='r',receipt='rx',epoch='chapter_2')=='CONTEXT_MISMATCH'
    assert l.observe({'a':0,'b':0},1,root='r',receipt='rx',scope='WORLD')=='CONTEXT_MISMATCH'
    assert l.fit()['status']=='INSUFFICIENT'


def test_replay_never_counts_as_new_sample():
    l=fresh();x={'a':0,'b':1}
    assert l.observe(x,1,root='r',receipt='ra')=='LEARNABLE'
    for i in range(100):assert l.observe(x,1,root='r',receipt='new'+str(i))=='DUPLICATE_ROOT'
    assert l.fit()['n']<=1


def test_conflicting_same_root_is_quarantined_permanently():
    l=fresh()
    assert l.observe({'a':0,'b':0},1,root='r',receipt='valid1')=='LEARNABLE'
    assert l.observe({'a':1,'b':1},0,root='r',receipt='valid2')=='ROOT_CONFLICT_QUARANTINED'
    assert l.observe({'a':1,'b':1},0,root='r',receipt='valid2')=='QUARANTINED'
    assert l.fit()['n']==0


def test_cold_roundtrip_does_not_relearn_from_self_output():
    rule=lambda x:x['a']^x['b']
    a=train_rule(rule)
    b=EmpiricalConstraintLearner.from_dict(a.to_dict())
    assert b.parents==a.parents
    assert b.predict({'a':1,'b':0,'noise':0})==a.predict({'a':1,'b':0,'noise':0})
    assert len(b.to_dict()['records'])==len(a.to_dict()['records'])


def test_inference_has_no_commit_or_action_authority():
    l=train_rule(lambda x:x['a']^x['b'])
    a=l.predict({'a':1,'b':1,'noise':0})
    assert a['kind']=='LEARNED_ASSOCIATION' and a['scope']=='SIMULATION'
    assert 'committed' not in a
    f=l.candidate_factor()
    assert f['committed'] is False


def test_budget_under_minimum_training_examples_refuses_guess():
    l=fresh()
    for i in range(4):l.observe({'a':i%2,'b':(i//2)%2},i%2,root=str(i),receipt=str(i))
    assert l.fit()['status']=='INSUFFICIENT'
    assert l.predict({'a':0,'b':1})['status']=='UNTRAINED'


def test_world_constructor_refuses_new_learner_in_default_scope():
    import pytest
    with pytest.raises(ValueError):EmpiricalConstraintLearner(('x',),scope='WORLD')


def test_strict_world_block_three_sources_and_no_entity_mutation():
    rt=C4LivingRuntime(strict_world_admission=True)
    g=rt.dialogue.g
    before=(len(g.facts),len(g.entities))
    for sid,cls,phase in [('MODEL_A','MODEL','PROPOSAL'),('CORPUS_A','CORPUS','PROPOSAL'),('HUMAN_A','HUMAN','CHALLENGE')]:
        rt.register_epistemic_source(sid,sid,cls)
        out=rt.submit_epistemic_claim('луна','IS_A','сыр',object_kind='entity',
            source_id=sid,source_family=sid,source_class=cls,phase=phase)
        assert out['status']=='NEEDS_GROUNDING' and out['mutated'] is False
    assert (len(g.facts),len(g.entities))==before
    assert g.resolve('луна') is None and g.resolve('сыр') is None
    assert rt.epistemic_status(out['candidate_id'])['status']=='NEEDS_GROUNDING'


def test_strict_mode_persists_after_cold_runtime_state_reload():
    rt=C4LivingRuntime(strict_world_admission=True)
    rt.register_epistemic_source('teacher','teacher','HUMAN')
    rt.submit_epistemic_claim('луна','IS_A','сыр',object_kind='entity',source_id='teacher',source_family='teacher',source_class='HUMAN')
    st=rt.runtime_state()
    reboot=C4LivingRuntime();reboot.load_runtime_state(st)
    assert reboot.epistemic.strict_world is True
    reboot.register_epistemic_source('teacher2','teacher2','HUMAN')
    s=reboot.submit_epistemic_claim('луна','IS_A','сыр',object_kind='entity',source_id='teacher2',source_family='teacher2',source_class='HUMAN')
    assert s['status']=='NEEDS_GROUNDING'


def test_strict_rejects_fake_simulation_receipt_as_world_evidence():
    rt=C4LivingRuntime(strict_world_admission=True)
    for i in range(3):
        k=f'report_{i}';cls='HUMAN' if i==2 else 'CORPUS'
        rt.register_epistemic_source(k,k,cls)
        rt.register_epistemic_evidence_origin(f'ev{i}',f'root{i}')
        r=rt.submit_epistemic_claim('a','CAUSES','b',source_id=k,source_family=k,
             source_class=cls,phase='CHALLENGE' if i==2 else 'PROPOSAL',evidence_id=f'ev{i}',dependency_root=f'root{i}')
        assert r['status']=='NEEDS_GROUNDING'
    assert not rt.dialogue.g.resolve('a')


def test_legacy_admission_remains_explicitly_comparable():
    rt=C4LivingRuntime(strict_world_admission=False)
    for k,cls,phase in [('m','MODEL','PROPOSAL'),('c','CORPUS','PROPOSAL'),('h','HUMAN','CHALLENGE')]:
        rt.register_epistemic_source(k,k,cls)
        s=rt.submit_epistemic_claim('луна','IS_A','сыр',source_id=k,source_family=k,source_class=cls,phase=phase)
    assert s['status']=='ADMITTED'  # known bad historical baseline, not accepted live policy


def test_real_runtime_can_learn_candidate_and_reload_without_world_mutation():
    rt=C4LivingRuntime(strict_world_admission=True)
    g=rt.dialogue.g;before=(len(g.entities),len(g.facts))
    rt.begin_causal_study('experiment_physics',('left','right','distractor'))
    rng=random.Random(911)
    for i in range(160):
        v={k:rng.randrange(2) for k in ('left','right','distractor')}
        ack=rt.learn_simulated_constraint('experiment_physics',v,v['left']^v['right'],root=f'sim_{i}',receipt=f'kin_{i}')
        assert ack['world_committed'] is False
    fit=rt.fit_causal_study('experiment_physics')
    assert fit['status']=='LEARNED_ASSOCIATION'
    assert set(fit['parents'])=={'left','right'}
    for a in range(2):
        for b in range(2):
            out=rt.predict_causal_study('experiment_physics',{'left':a,'right':b,'distractor':1})
            assert (out['p1']>0.5)==bool(a^b)
    assert (len(g.entities),len(g.facts))==before
    st=rt.runtime_state()
    reboot=C4LivingRuntime();reboot.load_runtime_state(st)
    assert reboot.epistemic.strict_world is True
    assert reboot.predict_causal_study('experiment_physics',{'left':1,'right':0,'distractor':0})['p1']>0.5
    assert (len(g.entities),len(g.facts))==before


def test_runtime_rejects_untrusted_simulation_without_receipt():
    rt=C4LivingRuntime(strict_world_admission=True)
    rt.begin_causal_study('test',('x',))
    out=rt.learn_simulated_constraint('test',{'x':1},1,root='r',receipt='')
    assert out['status']=='NO_RECEIPT'
    assert rt.fit_causal_study('test')['status']=='INSUFFICIENT'