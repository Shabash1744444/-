"""G325-P0: hardened mutation door, not a new cognitive law.

No preexisting historical facts are reclassified; freshly ingested external reports
must not become WORLD through any of the known graph mutation doors.
"""
import pytest
from c4child.graph import C4Graph
from c4child.runtime import C4LivingRuntime
from c4child.bootstrap import BootstrapTeacher


def secure():
    return C4LivingRuntime(hardened_truth_gate=True)


def test_all_known_external_origins_denied_even_with_forged_basis_and_verified():
    g=C4Graph();g.set_constitutional_mode('STRICT');g.hardened_gate=True
    s=g.entity('луна','concept');o=g.entity('сыр','concept')
    bases=['HUMAN_TEACHING','EPISTEMIC_ADMISSION','VERIFIED_RECEIPT',
           'VERIFIED_OBSERVATION','SYSTEM_MIGRATION']
    for origin in ('USER_SAID','EXTERNAL_CORPUS','CREATOR_PRIOR','OBS','RECEIPT','SIMULATION','MODEL'):
        for basis in bases:
            f=g.commit(s,'IS_A',o,object_kind='entity',origin=origin,
                       authority='TEACHER',constitutional_basis=basis,verified=True)
            assert f.status=='SOURCE_ASSERTED'
            assert g.truth(s,'IS_A',o,object_kind='entity',scope='WORLD')=='UNKNOWN'
    assert len(g.canonical)==0


def test_unguarded_bootstrap_path_cannot_claim_world_when_hardened():
    rt=secure();g=rt.dialogue.g
    x={'origin':'EXTERNAL_CORPUS','source_ref':'fake_news','authority':'TEACHER',
       'constitutional_basis':'EPISTEMIC_ADMISSION','verified':True,
       'payload':{'kind':'CLAIM','subject':'луна','relation':'IS_A','object':'сыр'}}
    metrics=BootstrapTeacher(g).ingest([x])
    assert metrics.admitted==1 # admitted as source assertion only, not WORLD
    a=g.resolve('луна');b=g.resolve('сыр')
    assert g.truth(a,'IS_A',b,object_kind='entity',scope='WORLD')=='UNKNOWN'
    assert g.source_assertions(subject=a,relation='IS_A')


def test_forged_epistemic_authority_no_canonical_mutation():
    rt=secure();g=rt.dialogue.g;s=g.entity('луна','concept');o=g.entity('сыр','concept')
    f=g.commit(s,'IS_A',o,object_kind='entity',origin='EXTERNAL_CORPUS',authority='EPISTEMIC_CHALLENGE',
               constitutional_basis='EPISTEMIC_ADMISSION',verified=True)
    assert f.status=='SOURCE_ASSERTED';assert not g.canonical


def test_replacement_of_canonical_fact_from_untrusted_input_is_claim_only():
    rt=secure();g=rt.dialogue.g;s=g.entity('мяч','concept')
    # Offline kernel invariant may add an internal fact under the explicit trusted gate.
    g.commit(s,'COLOR','красный',origin='SYSTEM',authority='SYSTEM',constitutional_basis='SYSTEM_INVARIANT')
    before=dict(g.canonical)
    new=g.replace_relation(s,'COLOR','синий',origin='USER_SAID',authority='TEACHER',
                           constitutional_basis='HUMAN_TEACHING')
    assert new.status=='SOURCE_ASSERTED'
    assert g.canonical==before


def test_untrusted_forget_cannot_erase_canonical_state():
    rt=secure();g=rt.dialogue.g;s=g.entity('мяч','concept')
    g.commit(s,'COLOR','красный',origin='SYSTEM',authority='SYSTEM',constitutional_basis='SYSTEM_INVARIANT')
    before=dict(g.canonical)
    assert not g.forget(s,'COLOR',origin='USER_SAID',authority='TEACHER',
                        constitutional_basis='EPISTEMIC_RETRACTION',verified=True)
    assert g.canonical==before


def test_direct_dialogue_human_teaching_does_not_auto_become_world():
    rt=secure();g=rt.dialogue.g
    rt.user_message('Запомни: луна — сыр')
    s=g.resolve('луна');o=g.resolve('сыр')
    if s and o:assert g.truth(s,'IS_A',o,object_kind='entity',scope='WORLD')=='UNKNOWN'


def test_social_naming_still_works_as_scoped_social_report():
    rt=secure();g=rt.dialogue.g
    z=rt.user_message('Ты Синька')
    me=g.resolve('SELF');assert me
    f=g.get(me,'NAME',viewer='USER',principal='USER',scope='SOCIAL_REPORT')
    assert f is not None and f.object_value.lower()=='синька'
    assert g.get(me,'NAME',viewer='USER',principal='USER',scope='WORLD') is None


def test_strict_epistemic_blocks_three_source_consensus():
    rt=secure();g=rt.dialogue.g
    for k,cl,ph in [('model','MODEL','PROPOSAL'),('corpus','CORPUS','PROPOSAL'),('human','HUMAN','CHALLENGE')]:
        rt.register_epistemic_source(k,k,cl)
        result=rt.submit_epistemic_claim('луна','IS_A','сыр',object_kind='entity',
            source_id=k,source_family=k,source_class=cl,phase=ph)
        assert result['status']=='NEEDS_GROUNDING'
    assert g.resolve('луна') is None


def test_hardened_gate_roundtrips_graph_and_runtime_state():
    rt=secure();g=rt.dialogue.g
    graph2=C4Graph.from_dict(g.to_dict())
    assert graph2.hardened_gate
    rt2=C4LivingRuntime();rt2.load_runtime_state(rt.runtime_state())
    assert rt2.dialogue.g.hardened_gate and rt2.epistemic.strict_world
    s=rt2.dialogue.g.entity('луна','concept');o=rt2.dialogue.g.entity('сыр','concept')
    f=rt2.dialogue.g.commit(s,'IS_A',o,object_kind='entity',origin='USER_SAID',constitutional_basis='HUMAN_TEACHING')
    assert f.status=='SOURCE_ASSERTED'


def test_default_mode_remains_comparable_with_historical_baseline():
    rt=C4LivingRuntime();g=rt.dialogue.g
    assert not g.hardened_gate
    s=g.entity('x','concept');o=g.entity('y','concept')
    f=g.commit(s,'IS_A',o,object_kind='entity')
    assert f.status=='ADMITTED'


def test_raw_linguistic_fact_only_in_language_scope():
    rt=secure();g=rt.dialogue.g
    s=g.entity('кот','concept')
    fact=g.commit(s,'WORD_FORM','коты',origin='USER_SAID',authority='TEACHER',
                  constitutional_basis='LANGUAGE_CONVENTION')
    assert fact.status=='ADMITTED'
    assert g.get(s,'WORD_FORM',viewer='SELF',principal='SELF',scope='WORLD') is None
    assert g.get(s,'WORD_FORM',viewer='SELF',principal='SELF',scope='LANGUAGE_CONVENTION') is not None