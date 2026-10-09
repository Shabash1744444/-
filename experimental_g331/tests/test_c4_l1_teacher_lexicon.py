"""L1 language teacher provenance and composition: no WORLD promotion."""
from c4child.graph import C4Graph
from c4child.bootstrap import BootstrapTeacher
from c4child.dialogue import C4ChildDialogue
from c4child.scope import fact_scope, LANGUAGE_CONVENTION, SOURCE_ASSERTION


def strict_graph():
    g=C4Graph();g.set_constitutional_mode('STRICT');g.hardened_gate=True
    return g


def lesson(relation, value, *, basis='LANGUAGE_CONVENTION', origin='EXTERNAL_CORPUS', authority='TEACHER'):
    return {'schema':'C4_BOOTSTRAP_EVENT_V0.1','origin':origin,'authority':authority,
            'source_group':'assistant_curated:one_root','event_id':f'train:{relation}:{value}:{basis}',
            'constitutional_basis':basis,'scope':{'principal':'USER','privacy':'LOCAL'},
            'payload':{'kind':'CLAIM','subject':'варьировать','relation':relation,'object':value,'object_kind':'literal'}}


def test_external_teacher_can_teach_lexical_conventions_only():
    g=strict_graph();teacher=BootstrapTeacher(g)
    x=teacher.ingest([lesson('PREDICATE_RELATION','CAUSES'),lesson('WORD_FORM','варьирует'),
                      lesson('PREDICATE_PRESENT_FORM','варьирует')])
    assert (x.admitted,x.rejected)==(3,0)
    assert C4ChildDialogue(g).predicates.parse_claim('Фея варьирует туман').relation=='CAUSES'
    assert all(f.status=='ADMITTED' and fact_scope(g,f)==LANGUAGE_CONVENTION for f in g.facts.values())


def test_external_teacher_cannot_promote_arbitrary_world_claim():
    g=strict_graph()
    BootstrapTeacher(g).ingest([lesson('LOCATION','место')])
    assert list(g.facts.values())[0].status=='SOURCE_ASSERTED'
    assert not g.canonical


def test_external_teacher_without_language_basis_remains_untrusted():
    g=strict_graph();BootstrapTeacher(g).ingest([lesson('PREDICATE_RELATION','CAUSES',basis='')])
    assert list(g.facts.values())[0].status=='SOURCE_ASSERTED'
    assert C4ChildDialogue(g).predicates.parse_claim('Фея варьирует туман') is None


def test_external_claim_without_teacher_authority_stays_source():
    g=strict_graph();BootstrapTeacher(g).ingest([lesson('PREDICATE_RELATION','CAUSES',authority='CORPUS')])
    assert list(g.facts.values())[0].status=='SOURCE_ASSERTED'


def test_model_self_teacher_cannot_mint_linguistic_fact():
    g=strict_graph()
    # direct graph call simulates a model trying to appoint itself teacher
    eid=g.entity('варьировать','concept')
    f=g.commit(eid,'PREDICATE_RELATION','CAUSES',origin='MODEL',authority='TEACHER',principal='USER',
               constitutional_basis='LANGUAGE_CONVENTION',source_group='model:self')
    assert f.status=='SOURCE_ASSERTED'


def test_source_root_remains_one_dependence():
    g=strict_graph();BootstrapTeacher(g).ingest([lesson('PREDICATE_RELATION','CAUSES'),lesson('WORD_FORM','варьирует')])
    assert {f.source_group for f in g.facts.values()}=={'assistant_curated:one_root'}
