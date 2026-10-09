"""Research-only directed verification on real saved C4M; NOT human conversation certification."""
import sys,json,hashlib
from dataclasses import asdict
from pathlib import Path
import pytest
L=Path(__file__).parent;sys.path.insert(0,str(L/'native_runtime'))
from c4child.d3_scoped import ScopedLearner,decode,build_ast
from c4child.d2_grounder import tokenize
from c4child.d5_graph_attachment import GraphEdgeAttachment,REL,ROOT
from c4child.checkpoint import load_c4m_compact
from c4child.scope import fact_scope,LANGUAGE_CONVENTION
from c4child.dialogue import C4ChildDialogue
from c4child.runtime import C4LivingRuntime

@pytest.fixture(scope='module')
def models():
 parent=Path('/mnt/data/c4_decisive_lab/original/C4_D2_P2C_RELBINDER_NEGATION_CANDIDATE.c4m')
 candidate=L/'C4_D5_LEARNED_EDGE_RESEARCH_ONLY.c4m'
 ga,_,_=load_c4m_compact(parent,hydrate_cold=True);gb,_,_=load_c4m_compact(candidate,hydrate_cold=True)
 tag=ScopedLearner(gb);tag.load();link=GraphEdgeAttachment(gb)
 return ga,gb,tag,link

def test_real_c4m_language_weights(models):
 ga,gb,tag,link=models
 assert len(ga.facts)==15863 and len(gb.facts)==16731
 assert all(k in gb.facts and asdict(gb.facts[k])==asdict(f) for k,f in ga.facts.items())
 assert len(tag.weights)>0 and len([f for f in gb.facts.values() if f.relation==REL])==181

def test_teacher_dependency_world_immutability(models):
 ga,gb,tag,link=models
 old=set(ga.facts)
 new=[f for k,f in gb.facts.items() if k not in old]
 assert len(new)==868
 assert all(fact_scope(gb,f)==LANGUAGE_CONVENTION and f.origin=='EXTERNAL_CORPUS' and f.authority=='TEACHER' and f.status=='ADMITTED' for f in new)
 assert ROOT in set(f.source_group for f in new)

def test_prior_frozen_reverse_32_gold_and_cold(models):
 _,_,_,link=models
 rows=json.loads(Path('/mnt/data/c4_decisive_lab/D3_NEW_DEPTH_REATTACK_FROZEN.json').read_text())['reversed_role_order']
 assert sum(build_ast(tokenize(e['text']),e['tags'])==e['ast'] for e in rows)==0
 assert sum(link.parse(e['text'],e['tags']).get('ast')==e['ast'] for e in rows)==32

def test_new_frozen_oracle_2_3_levels(models):
 _,_,_,link=models
 sets=json.loads((L/'D5_HOLDOUT_FROZEN.json').read_text())['generated']
 for k,want in [('reverse_depth2_new_entities',100),('reverse_depth3_new_entities',87),('forward_depth3_new_entities',74)]:
  assert sum(link.parse(e['text'],e['tags']).get('ast')==e['ast'] for e in sets[k])==want

def test_new_frozen_real_tagging_2_3_levels(models):
 _,_,tag,link=models
 sets=json.loads((L/'D5_HOLDOUT_FROZEN.json').read_text())['generated']
 for k,want in [('reverse_depth2_new_entities',63),('reverse_depth3_new_entities',50),('forward_depth3_new_entities',5)]:
  assert sum(link.parse(e['text'],decode(tokenize(e['text']),tag.weights)).get('ast')==e['ast'] for e in sets[k])==want

def test_real_user_message_not_d5(models):
 _,gb,_,_=models
 rt=C4LivingRuntime(C4ChildDialogue(gb))
 res=rt.user_message('Веста думает что Дина говорит что железный волк золотой')
 assert (res.get('parsed') or {}).get('kind')=='UNKNOWN'
 assert not res.get('mutated')