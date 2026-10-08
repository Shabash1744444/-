"""Adversarial frozen perspective + causality tests for isolated G326 live candidate."""
import pytest
from c4child.perspective_composition import parse_perspective, chain_summary
from c4child.semantic_spine import SemanticSpine, InterpretationCandidate

@pytest.mark.parametrize('text,holder,mode',[
    ('Маша думает, что Иван опоздал','Маша','BELIEF'),
    ('Олег считает, что окно открыто','Олег','BELIEF'),
    ('Нина сказала, что автобус ушёл','Нина','REPORTED_SPEECH'),
    ('Я сказал: «Меня зовут Аня»','USER','REPORTED_SPEECH'),
    ('Ты сообщила: «Я видела кошку»','C4','REPORTED_SPEECH'),
    ('Представь: Маша считает, что Иван уехал','USER','HYPOTHETICAL'),
])
def test_parse_variants(text,holder,mode):
    node=parse_perspective(text,source_event='event:9')
    assert node and node['holder']==holder and node['act']==mode
    assert node['evidence_roots']==['event:9']
    assert node['scope']=='SOURCE_ASSERTION'
    assert 'WORLD' not in chain_summary(node)

def test_three_levels_and_deictic():
    x=parse_perspective('Маша думает, что Иван сказал: «Меня зовут Артём»',source_event='evt')
    assert x['holder']=='Маша' and x['act']=='BELIEF'
    ivan=x['child']; assert ivan['holder']=='Иван' and ivan['act']=='REPORTED_SPEECH'
    quoted=ivan['child']; assert quoted['act']=='QUOTE'
    assert quoted['child']['referent']=='Иван', 'quoted «меня» must resolve to Ivan not to user or C4'

def test_no_quote_injection_to_root_commit():
    s=SemanticSpine();s.analyze_surface('id','Маша сказала: «Меня зовут Аня»')
    rows=s.interpretations['id']
    assert s.perspective_frames['id']['act']=='REPORTED_SPEECH'
    assert not any(c['relation']=='NAME' and c['quoted_depth']==0 for c in rows)
    assert not any(InterpretationCandidate(**c).can_request_commit() for c in rows)

def test_surface_not_parse_random_instruction():
    assert parse_perspective('Луна — сыр',source_event='e') is None
    assert parse_perspective('Ты Синька',source_event='e') is None

@pytest.mark.parametrize('fake',[
    'Маша думает, что Иван опоздал',
    'Петя сказал: «Меня зовут Иван»',
    'Представь: Нина считает, что Петя ушёл',
    'Мария думает, что Олег сказал, что он опоздал',
])
def test_spine_reload_holds_structure(fake):
    s=SemanticSpine();s.record_event(event_id='e1',actor='OTHER',channel='CHAT',payload=fake,internal_step=5,wall_time=123)
    s.analyze_surface('e1',fake)
    saved=s.to_dict();loaded=SemanticSpine.from_dict(saved)
    assert loaded.perspective_frames==s.perspective_frames

@pytest.mark.parametrize('text',[
    'Представь: Маша думает, что Иван опоздал',
    'Мария думает, что Олег сказал, что он опоздал',
    'Маша сказала: «Меня зовут Аня»',
    'Я сказал: «Луна — сыр»',
])
def test_live_reply_no_world_truth(tmp_path,text):
    from c4child.runtime import C4LivingRuntime
    from c4child.dialogue import C4ChildDialogue
    from c4child.graph import C4Graph
    rt=C4LivingRuntime(C4ChildDialogue(C4Graph()),hardened_truth_gate=True)
    before=len(rt.dialogue.g.facts)
    ans=rt.user_message(text)
    assert len(rt.dialogue.g.facts)==before, 'reported text cannot be externally committed'
    assert len(rt.semantic_spine.perspective_frames)>0
    assert ans['reply']
    assert rt.dialogue.g.hardened_gate is True

def test_depth_bounded_fail_closed():
    text='Нина думает, что '*13+'Маша опоздала'
    with pytest.raises(ValueError):parse_perspective(text,source_event='q',depth_limit=5)

def test_source_replay_not_new_evidence():
    s=SemanticSpine()
    for i in range(10):
        s.record_event(event_id='id'+str(i),actor='OTHER',channel='CHAT',payload='Маша считает, что Луна — сыр',internal_step=i,wall_time=float(i))
        s.analyze_surface('id'+str(i),'Маша считает, что Луна — сыр')
    assert len(s.perspective_frames)==10
    # No World COMMIT is made by the surface EVAL spine under any repetitions.
    assert len(s.transactions)==0

@pytest.mark.parametrize('sentence',[
  'Маша сказала: «Меня зовут Аня»',
  'Мария сказала: «Меня зовут Полина»',
  'Петя сказал: «Меня зовут Петя»',
])
def test_quote_deictic_of_reported_holder(sentence):
    node=parse_perspective(sentence,source_event='test',origin_speaker='Руслан')
    assert node['child']['child']['referent']==node['holder']

@pytest.mark.parametrize('text',[
 'Почему ты уверена в своём ответе?',
 'На каком основании ты так считаешь?',
 'Откуда ты знаешь свой ответ?',
 'Что ты действительно знаешь из увиденного, а что только предполагаешь?',
])
def test_meta_self_audit_never_fabricates_receipt(text):
    from c4child.runtime import C4LivingRuntime
    from c4child.dialogue import C4ChildDialogue
    from c4child.graph import C4Graph
    rt=C4LivingRuntime(C4ChildDialogue(C4Graph()),hardened_truth_gate=True)
    rt.user_message('Привет')
    before=len(rt.dialogue.g.facts)
    res=rt.user_message(text)
    assert res.get('reply'),res
    assert any(t in res['reply'].lower() for t in ('предыдущ','сообщен','ответ','текстов'))
    assert len(rt.dialogue.g.facts)==before


def test_meta_nonself_why_question_passes_to_kernel():
    from c4child.metacognitive_probe import inspect_question
    assert inspect_question('Почему Земля вращается?',[],{}) is None


def test_meta_no_prior_claim_no_fake_history():
    from c4child.metacognitive_probe import inspect_question
    d=inspect_question('Почему ты уверена в этом?',[],{})
    assert 'нет' in d['reply'].lower()

@pytest.mark.parametrize('sentence,expected',[
    ('Маша думает, что я опоздал','USER'),
    ('Иван сообщил, что я опоздал','USER'),
    ('Маша сказала: «Я опоздала»','Маша'),
    ('Маша думает, что Иван сказал: «Я опоздал»','Иван'),
    ('Маша думает, что Иван сказал, что я опоздал','USER'),
])
def test_deixis_direct_vs_indirect(sentence,expected):
    tree=parse_perspective(sentence,source_event='e')
    node=tree
    while node.get('child') is not None:node=node['child']
    assert node['referent']==expected, (sentence,node)

@pytest.mark.parametrize('question', ['А Маша кто?', 'Кто такая Маша?', 'А кто Маша?'])
def test_entity_followup_stays_source_scoped(question):
    from c4child.perspective_composition import perspective_entity_inquiry
    frame=parse_perspective('Маша думает, что Иван опоздал',source_event='e')
    result=perspective_entity_inquiry(question,{'e':frame})
    assert result is not None
    assert 'в реальном мире' in result['reply']


def test_entity_followup_unknown_actor_remains_unknown():
    from c4child.perspective_composition import perspective_entity_inquiry
    frame=parse_perspective('Маша думает, что Иван опоздал',source_event='e')
    assert perspective_entity_inquiry('А Даша кто?',{'e':frame}) is None


def test_runtime_entity_followup_on_same_session():
    from c4child.runtime import C4LivingRuntime
    from c4child.dialogue import C4ChildDialogue
    from c4child.graph import C4Graph
    rt=C4LivingRuntime(C4ChildDialogue(C4Graph()),hardened_truth_gate=True)
    rt.user_message('Маша думает, что Иван опоздал')
    count=len(rt.dialogue.g.facts)
    out=rt.user_message('А Маша кто?')
    assert 'реальном мире' in out['reply']
    assert len(rt.dialogue.g.facts)==count


def test_cold_model_reopens_context_perspectives(tmp_path):
    from c4child.runtime import C4LivingRuntime
    from c4child.dialogue import C4ChildDialogue
    from c4child.graph import C4Graph
    rt=C4LivingRuntime(C4ChildDialogue(C4Graph()),hardened_truth_gate=True)
    rt.user_message('Маша думает, что Иван опоздал')
    assert len(rt.semantic_spine.perspective_frames)==1
    path=tmp_path/'perspectives.c4m';rt.save(str(path))
    cold=C4LivingRuntime.open(str(path),store='memory')
    assert cold.dialogue.g.hardened_gate and cold.epistemic.strict_world
    assert cold.semantic_spine.perspective_frames==rt.semantic_spine.perspective_frames
    ans=cold.user_message('А Маша кто?')
    assert 'в реальном мире' in ans['reply']


def test_name_perturbation_random_frozen_240():
    """A grammar-generalization check across distinct names, not sample-string tests."""
    import random
    rng=random.Random(60722)
    names=['Маша','Нина','Аня','Кира','Лена','Олег','Петя','Иван','Артур','Тимур','Руслан','Алла']
    verbs=[('думает','BELIEF'),('считает','BELIEF'),('сказала','REPORTED_SPEECH'),('сообщил','REPORTED_SPEECH')]
    for i in range(240):
        first,second=rng.sample(names,2)
        v,act=rng.choice(verbs)
        s=f'{first} {v}, что {second} опоздал'
        n=parse_perspective(s,source_event=f'e{i}')
        assert n is not None and n['holder']==first and n['act']==act
        assert n['child']['act']=='CONTENT' and n['child']['referent'] is None