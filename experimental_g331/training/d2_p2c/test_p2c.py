import json,os
from pathlib import Path
from dataclasses import asdict
from c4child.d2_relational import LearnedRelationBinder
from c4child.checkpoint import load_c4m_compact
from c4child.dialogue import C4ChildDialogue
from c4child.runtime import C4LivingRuntime
from c4child.scope import fact_scope,LANGUAGE_CONVENTION

SOURCE=Path(os.environ.get('C4_P2_PARENT','/mnt/data/c4_d2_pilot/out/C4_G329_D2_P1_GROUNDED_STORY_CANDIDATE.c4m'))
WEIGHTS=Path(os.environ.get('C4_P2_MODEL','/mnt/data/c4_d2_p2c/results/C4_D2_P2C_RELBINDER_NEGATION_CANDIDATE.c4m'))

def graphs():
    a,*_=load_c4m_compact(SOURCE,hydrate_cold=True)
    b,*_=load_c4m_compact(WEIGHTS,hydrate_cold=True)
    return a,b

def test_native_graph_provenance_unchanged():
    source,trained=graphs()
    assert len(source.facts)==12767 and len(trained.facts)==15863
    assert all(asdict(f)==asdict(trained.facts[k]) for k,f in source.facts.items())
    novel=[f for k,f in trained.facts.items() if k not in source.facts]
    assert len(novel)==3096
    assert all(f.status=='ADMITTED' and f.origin=='EXTERNAL_CORPUS' and f.authority=='TEACHER'
               and fact_scope(trained,f)==LANGUAGE_CONVENTION for f in novel)
    assert len({f.source_group for f in novel})==1

def test_negation_is_not_a_positive_belief_in_native_user_message():
    source,trained=graphs();text='Мира не думает, что куб синий'
    r0=C4LivingRuntime(C4ChildDialogue(source)).user_message(text)
    assert (r0.get('parsed') or {}).get('kind')!='LEARNED_RELATION_CANDIDATE'
    before=len(trained.facts)
    runtime=C4LivingRuntime(C4ChildDialogue(trained))
    r=runtime.user_message(text)
    assert r['parsed']['kind']=='LEARNED_RELATION_CANDIDATE'
    assert r['parsed']['relation_kind']=='BELIEF' and r['parsed']['polarity']=='NEGATED'
    assert r['parsed']['roles']['SUBJECT']=='куб'
    assert r['reply'] is None and r['mutated'] is False
    assert before==len(trained.facts)
    assert any(x.get('kind')=='EVAL_D2_RELATION' for x in runtime.life_events)
    assert any(x.get('kind')=='COMMIT_NOOP' for x in runtime.life_events)

def test_distinguish_story_fact_from_attributed_report_with_new_entities():
    _,trained=graphs();b=LearnedRelationBinder(trained)
    a=b.interpret('Нелли думает, что хрустальный кит золотой')
    b1=b.interpret('В нашей сказке космический чайник прозрачный')
    assert a['kind']=='BELIEF' and a['roles']['HOLDER']=='нелли'
    assert a['scope']=='ATTRIBUTED_USER_REPORT_NOT_WORLD'
    assert b1['kind']=='NARRATOR' and 'HOLDER' not in b1['roles']
    assert b1['scope']=='STORY_SOURCE_REPORT'
    assert a['roles']['SUBJECT']=='хрустальный кит' and b1['roles']['SUBJECT']=='космический чайник'

def test_nested_opinions_do_not_get_falsely_admitted():
    _,trained=graphs();b=LearnedRelationBinder(trained)
    assert b.interpret('Алиса думает, что мяч синий, но Мира думает, что он красный')['status']=='ABSTAIN'
    assert b.interpret('Мира знает, что Ника думает, что куб красный')['status']=='ABSTAIN'

def test_training_experiment_frozen_metrics():
    x=json.load(open(os.environ.get('C4_P2_REPORT','/mnt/data/c4_d2_p2c/results/P2C_REPORT.json')))
    assert x['trained']['heldout_negation_new_entities']['exact']==63
    assert x['trained']['heldout_seen_constructions_new_entities']['exact']==106
    assert x['trained']['heldout_new_constructions_new_entities']['exact']==11
    assert x['cold']['heldout_negation_new_entities']['exact']==63