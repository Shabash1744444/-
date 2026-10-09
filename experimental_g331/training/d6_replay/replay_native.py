"""C4 D6: read-only backdated re-interpretation using two REAL prior C4M models.
No training, no language phrase lookup, no examiner labels supplied to parse functions.
"""
from __future__ import annotations
from pathlib import Path
import sys,json,hashlib,time,re,copy,os
R=Path(__file__).resolve().parent
D5=Path(os.environ.get('C4_D6_D5_DIR',str(R/'inputs'/'d5')))
D3=Path(os.environ.get('C4_D6_D3_DIR',str(R/'inputs'/'d3')))
sys.path.insert(0,str(R/'native_runtime'))
from c4child.checkpoint import load_c4m_compact
from c4child.d3_scoped import ScopedLearner, build_ast, decode
from c4child.d5_graph_attachment import GraphEdgeAttachment
from c4child.d2_grounder import tokenize
from c4child.episodic_memory import index_event,retrieve

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def load(p):
    graph,_,_=load_c4m_compact(p,hydrate_cold=True)
    tagger=ScopedLearner(graph);tagger.load();linker=GraphEdgeAttachment(graph);linker.load()
    return graph,tagger,linker

def parse_d3(text,tagger):
    tok=tokenize(text);tags=decode(tok,tagger.weights)
    ast=build_ast(tok,tags)
    return {'status':'CANDIDATE' if ast is not None else 'ABSTAIN','ast':ast}

def parse_d5(text,tagger,linker):
    t=decode(tokenize(text),tagger.weights)
    return linker.parse(text,t)

def run():
    parent=D3/'C4_D3_64_NESTED_LEARNED_CANDIDATE_NONCANONICAL.c4m'
    child=D5/'C4_D5_LEARNED_EDGE_RESEARCH_ONLY.c4m'
    tests=json.loads((D3/'D3_NEW_DEPTH_REATTACK_FROZEN.json').read_text(encoding='utf8'))['reversed_role_order']
    manual=json.loads((D5/'D5_MANUAL_REATTACK_FROZEN.json').read_text(encoding='utf8'))
    expected_manual=manual['manually_authored_expected'];other=manual['unsupported']
    gd,td,_=load(parent);g5,t5,ed5=load(child)
    # SOURCE_SAID_ONLY native episodes, unique event ids, no WORLD claims.
    index={}
    for i,x in enumerate(tests):
        key=f'prior-synthetic-ep:{i:03d}'
        index[key]=index_event(key,i+1,x['text'])
    model_hashes_before=(sha(parent),sha(child))
    graph_state_before=(len(gd.facts),len(g5.facts),len(gd.audit),len(g5.audit))
    rows=[];old_hits=0;new_hits=0;recovers=0
    for i,ex in enumerate(tests):
        past=parse_d3(ex['text'],td)
        now=parse_d5(ex['text'],t5,ed5)
        before=past.get('ast')==ex['ast']
        after=now.get('status')=='CANDIDATE' and now.get('ast')==ex['ast']
        old_hits+=before;new_hits+=after;recovers+=not before and after
        rows.append({'event_id':f'prior-synthetic-ep:{i:03d}', 'source_sha256':hashlib.sha256(ex['text'].encode()).hexdigest(),
                     'previous':past,'reinterpreted':now,'gold_exact_before':before,'gold_exact_after':after,
                     'source_lineage':'SINGLE_PRIOR_USER_EVENT_NOT_WORLD',
                     'interpretation_lineage':'DERIVED_FROM_SAME_RAW_EPISODE_AND_PRETRAINED_MODEL'})
    # Re-running unmodified trained parser cannot improve, without added information or candidate selection.
    budgets=(1,2,3,5,10,30,100)
    steady=[]
    for k in budgets:
        correct=0
        for ex in tests:
            ans=None
            for _ in range(k):ans=parse_d5(ex['text'],t5,ed5)
            correct+=ans.get('ast')==ex['ast'] and ans.get('status')=='CANDIDATE'
        steady.append({'passes':k,'correct':correct,'total':len(tests)})
    # Old AST is None on structurally impossible reverse statements. No raw bytes -> cannot rederive gold.
    blind_old_with_no_raw=sum(parse_d3(x['text'],td)['ast'] is not None for x in tests)
    # Same-model re-examination on manually authored unfamiliar input, no training.
    human=sum(parse_d5(text,t5,ed5).get('ast')==gold for text,gold in expected_manual)
    false_positive=sum(parse_d5(text,t5,ed5).get('status')=='CANDIDATE' for text in other)
    # Native episode search, terms from query based on expected semantic subject: data is not training the semantic parser.
    retrieved=[]
    for i,x in enumerate(tests):
        key=f'prior-synthetic-ep:{i:03d}'
        gold=x['ast']
        while 'arg' in gold:gold=gold['arg']
        subject=gold.get('subject','')
        q=f'Что раньше говорилось про {subject}?'
        matches=retrieve(q,index,limit=2)
        retrieved.append({'event_id':key,'query':q,'hit_at_2':any(m['event_id']==key for m in matches),'match_ids':[m['event_id'] for m in matches]})
    # Oracle-context upper bound: full exact source surface supplied as retrieval query.
    # This is NOT a natural user's available question, only a diagnostic of index capacity.
    full_context_hits=sum(any(m['event_id']==f'prior-synthetic-ep:{i:03d}'
                              for m in retrieve(x['text'],index,limit=2)) for i,x in enumerate(tests))
    graph_state_after=(len(gd.facts),len(g5.facts),len(gd.audit),len(g5.audit))
    assert graph_state_before==graph_state_after
    assert model_hashes_before==(sha(parent),sha(child))
    report={
      'scope':'REAL_NATIVE_C4M_RETROSPECTIVE_READONLY_NONCANONICAL',
      'source_models_sha256':dict(d3=model_hashes_before[0],d5=model_hashes_before[1]),
      'raw_episode_count':len(tests),'native_event_scope':'SOURCE_SAID_ONLY',
      'd3_old_reverse_exact':old_hits,'d5_reinterpreted_reverse_exact':new_hits,
      'corrected_old_interpretations':recovers,'unchanged_repeat_curve':steady,
      'no_raw_cached_old_ast_nonnull':blind_old_with_no_raw,
      'manual_prior_frozen_exact':human,'manual_prior_frozen_total':len(expected_manual),
      'unsupported_false_semantic_candidates':false_positive,'unsupported_total':len(other),
      'native_retrieve_hit_at_2':sum(x['hit_at_2'] for x in retrieved),'native_retrieve_queries':len(retrieved),
      'native_retrieve_full_source_oracle_hit_at_2':full_context_hits,
      'native_retrieve_failure_samples':[x for x in retrieved if not x['hit_at_2']][:5],
      'graph_facts_and_audit_before_after':[graph_state_before,graph_state_after],
      'graph_mutation':False,'candidate_promoted_to_WORLD':False,
      'episodic_index_temporary_in_memory_only':True,
      'scientific_caveats':['old benchmarks were known before this experiment, not new independent blind holdout',
                            'gain is entirely due to previously trained D5 operator, NOT recursion alone',
                            'no evidence yet that C4 autonomously selects or initiates replay, no claim of general language',
                            'native event index is read-only; interpretation versions kept in research-only ledger']}
    (R/'D6_RETROSPECTIVE_RESULTS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    (R/'D6_VERSIONED_INTERPRETATION_LEDGER.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
    assert all(v['correct']==new_hits for v in steady)
    print(json.dumps({k:report[k] for k in ('d3_old_reverse_exact','d5_reinterpreted_reverse_exact','corrected_old_interpretations','unchanged_repeat_curve','manual_prior_frozen_exact','unsupported_false_semantic_candidates','native_retrieve_hit_at_2','native_retrieve_queries','native_retrieve_full_source_oracle_hit_at_2')},ensure_ascii=False,indent=2))
if __name__=='__main__':run()