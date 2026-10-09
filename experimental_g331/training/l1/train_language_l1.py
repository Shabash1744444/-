"""C4 L1 supervised lexical-convention transfer: NO new WORLD facts.

Uses the existing 56-module R6 native code and BootstrapTeacher with a
LANGUAGE_CONVENTION constitutional basis, never a new NLP model or claims about
human-level conversational understanding.  Execute with PYTHONPATH set to R6.
"""
from __future__ import annotations
import argparse, hashlib, json, random, copy
from pathlib import Path
from c4child.checkpoint import load_c4m_compact, save_c4m_compact
from c4child.bootstrap import BootstrapTeacher
from c4child.dialogue import C4ChildDialogue
from c4child.scope import fact_scope, LANGUAGE_CONVENTION

# Curated, supervised surface/meaning mappings, NOT autonomous truth learning.
# Classes intentionally reuse the existing C4 relation grammar.
LESSONS = (
    ('предпочитать','LIKES',('предпочитает','предпочитают'),('предпочитал','предпочитала')),
    ('ценить','LIKES',('ценит','ценят'),('ценил','ценила')),
    ('уважать','LIKES',('уважает','уважают'),('уважал','уважала')),
    ('восхищаться','LIKES',('восхищается','восхищаются'),('восхищался','восхищалась')),
    ('провоцировать','CAUSES',('провоцирует','провоцируют'),('провоцировал','провоцировала')),
    ('инициировать','CAUSES',('инициирует','инициируют'),('инициировал','инициировала')),
    ('запускать','CAUSES',('запускает','запускают'),('запускал','запускала')),
    ('стимулировать','CAUSES',('стимулирует','стимулируют'),('стимулировал','стимулировала')),
    ('владеть','HAS',('владеет','владеют'),('владел','владела')),
    ('хранить','HAS',('хранит','хранят'),('хранил','хранила')),
    ('держать','HAS',('держит','держат'),('держал','держала')),
    ('обладать','HAS',('обладает','обладают'),('обладал','обладала')),
)
# Synthetic heldout examples use people and objects not used as training operands.
# Only verbs and their inflections (lexicon) are trained, no complete sentences.
HELDOUT_PEOPLE=('Лира','Нэлли','Тимофей','Гайя','Маркус','Сайра','Роман','Элис','Ярослав','Веста','Данила','Одетта','Федя','Мелания')
HELDOUT_OBJECTS=('мираж','самовар','лавину','аккорд','мандарин','зонтик','ветер','ярмарку','маятник','переполох','термос','рояль','салют','телескоп')
NEGATIVE_FORMS=('сверкает','прыгает','плывёт','дремлет','разглядывает','задремал')
SOURCE_ROOT='curated:assistant-teacher:c4-l1-lexical:2026-10-09' # one dependence root, never 12 independent witnesses


def examples():
    rng=random.Random(81175)
    out=[]
    for i,(lemma,relation,present,past) in enumerate(LESSONS):
        for j,surface in enumerate((present[0],past[0],present[1],past[1])):
            subject=HELDOUT_PEOPLE[(i*5+j+3)%len(HELDOUT_PEOPLE)]
            obj=HELDOUT_OBJECTS[(i*7+j*3+1)%len(HELDOUT_OBJECTS)]
            out.append((f'{subject} {surface} {obj}',relation,surface,j,lemma))
    rng.shuffle(out)
    return out


def parse_results(g, tests):
    d=C4ChildDialogue(g)
    rows=[]
    for sent,relation,surface,j,lemma in tests:
        p=d.predicates.parse_claim(sent)
        # For a language curriculum, only lexical predicate semantics and tense
        # are scored. It is NOT proof of world state, or communicative competence.
        expected_tense='PRESENT' if j in (0,2) else 'PAST'
        ok=(p is not None and p.relation==relation and p.predicate_surface==surface and p.tense==expected_tense)
        rows.append({'sentence':sent,'verb':lemma,'predicted_relation':p.relation if p else None,
                     'expected_relation':relation,'expected_tense':expected_tense,
                     'predicted_tense':p.tense if p else None,'ok':bool(ok)})
    return rows


def curriculum():
    ev=[]
    for i,(lemma,relation,present,past) in enumerate(LESSONS):
        rows=[('PREDICATE_RELATION',relation)]+[('WORD_FORM',x) for x in [lemma,*present,*past]]
        rows += [('PREDICATE_PRESENT_FORM',x) for x in present]
        rows += [('PREDICATE_PAST_FORM',x) for x in past]
        for k,(rel,obj) in enumerate(rows):
            ev.append({'schema':'C4_BOOTSTRAP_EVENT_V0.1','event_id':f'c4-l1-20261009:{i}:{k}',
                       'origin':'EXTERNAL_CORPUS','source_group':SOURCE_ROOT,'scope':{'principal':'USER','privacy':'LOCAL'},
                       'authority':'TEACHER','constitutional_basis':'LANGUAGE_CONVENTION',
                       'payload':{'kind':'CLAIM','subject':lemma,'relation':rel,'object':obj,'object_kind':'literal'}})
    return ev


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    a=argparse.ArgumentParser();a.add_argument('--input',required=True);a.add_argument('--output',required=True);a.add_argument('--report',required=True)
    cfg=a.parse_args();src=Path(cfg.input);dst=Path(cfg.output);dst.parent.mkdir(parents=True,exist_ok=True)
    if src.resolve()==dst.resolve(): raise SystemExit('REFUSE_IN_PLACE_MODEL_MUTATION')
    oldsha=sha(src)
    if oldsha!='dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f': raise SystemExit('BASELINE_SHA_MISMATCH: never stack unreviewed lessons')
    g,h,manifest,state,organs=load_c4m_compact(src,hydrate_cold=True,with_runtime=True,with_organs=True)
    assert manifest['schema']=='C4M_CHILD_V0.4_COMPACT'
    assert getattr(g,'hardened_gate',False) and getattr(g,'constitutional_mode','')=='STRICT'
    initial=len(g.facts);entities_before=len(g.entities);before_canonical=copy.deepcopy(g.canonical)
    tests=examples();baseline=parse_results(g,tests)
    # Explicitly authorized language-convention COMMIT through native BootstrapTeacher.
    training=curriculum();stats=BootstrapTeacher(g,principal='USER').ingest(training)
    assert stats.rejected==0 and stats.admitted+stats.dedup==len(training)
    trained=parse_results(g,tests)
    learned_rels={'WORD_FORM','PREDICATE_RELATION','PREDICATE_PRESENT_FORM','PREDICATE_PAST_FORM'}
    new_facts=[f for f in g.facts.values() if f.source_group==SOURCE_ROOT]
    assert len(new_facts)==stats.admitted
    assert all(f.status=='ADMITTED' and f.relation in learned_rels and fact_scope(g,f)==LANGUAGE_CONVENTION for f in new_facts)
    # Do not claim 12 independent teacher roots: every lesson is same curated source.
    assert all(f.source_group==SOURCE_ROOT for f in new_facts)
    assert len(g.facts)==initial+stats.admitted
    assert all(g.canonical.get(k)==v for k,v in before_canonical.items()), 'original canonical knowledge was modified'
    # Original runtime state, LIFE, source, and any other organs are left untouched.
    oldmeta=copy.deepcopy(manifest.get('meta') or {})
    newmeta=dict(oldmeta)
    newmeta['c4_l1_curriculum']={'status':'SUPERVISED_LANGUAGE_CONVENTIONS_ONLY','teacher_root':SOURCE_ROOT,
                                'curriculum_size':len(training),'no_autonomous_world_admission':True,
                                'no_claim_human_dialogue':True,'base_file_sha256':oldsha}
    save_c4m_compact(dst,g,h,meta=newmeta,runtime_state=state,organs=organs,include_cold=True)
    outsha=sha(dst)
    reloaded,_,newmanifest,newstate,neworg=load_c4m_compact(dst,hydrate_cold=True,with_runtime=True,with_organs=True)
    cold=parse_results(reloaded,tests)
    assert [x['ok'] for x in trained]==[x['ok'] for x in cold]
    assert len(reloaded.facts)==len(g.facts) and len(reloaded.entities)==len(g.entities)
    assert state==newstate and organs==neworg
    assert sha(src)==oldsha
    before=sum(x['ok'] for x in baseline);after=sum(x['ok'] for x in trained);coldpass=sum(x['ok'] for x in cold)
    assert after>before and after==coldpass
    # Negative control: an untrained predicate MUST remain unknown.
    d=C4ChildDialogue(reloaded)
    negatives={s:d.predicates.parse_claim('Зоя '+s+' облака') is None for s in NEGATIVE_FORMS}
    assert all(negatives.values()),negatives
    report={'schema':'C4_L1_SUPERVISED_LEXICAL_TRANSFER_V1','description':'Existing G329 graph + minimally repaired R6 provenance gate acquired lexical forms, NOT free discourse.',
            'baseline_sha256':oldsha,'trained_sha256':outsha,'original_facts':initial,'final_facts':len(reloaded.facts),
            'new_facts':stats.admitted,'deduplicated_lessons':stats.dedup,'original_entities':entities_before,'final_entities':len(reloaded.entities),
            'lessons':len(LESSONS),'training_events':len(training),'one_dependent_teacher_root':SOURCE_ROOT,'training_origin':'EXTERNAL_CORPUS','teacher':'ASSISTANT_CURATED_NOT_USER_WITNESS',
            'holdout_unit':'full sentences and subject/object combinations; learned lexeme/forms included in training',
            'holdout_cases':len(tests),'baseline_pass':before,'trained_pass':after,'cold_pass':coldpass,
            'negative_unknown_predicates':negatives,'no_world_commit':True,'original_canonical_slots_unchanged':True,'runtime_state_unchanged':True,
            'retained_original_organs':True,'old_model_sha_unchanged':True,
            'untested':['free language dialogue','nested speakers','ellipsis','unseen verbs','semantic action selection','real Android LIVE']}
    Path(cfg.report).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('negative_unknown_predicates','untested')},ensure_ascii=False,indent=2))
    if after < len(tests):
        print('WARNING: some lexical transfer trials failed, recorded in heldout_results')
        Path(cfg.report.replace('.json','.heldout.json')).write_text(json.dumps({'baseline':baseline,'after':trained},ensure_ascii=False,indent=2),encoding='utf-8')

if __name__=='__main__': main()
