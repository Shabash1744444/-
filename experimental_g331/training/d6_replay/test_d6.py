"""D6 read-only scientific regression. Runs in extracted proof archive, no external files."""
from pathlib import Path
import json,hashlib,subprocess,sys
ROOT=Path(__file__).resolve().parent

def data(n):return json.loads((ROOT/n).read_text(encoding='utf8'))

def test_native_immutable_replay():
    subprocess.run([sys.executable,str(ROOT/'replay_native.py')],check=True,stdout=subprocess.DEVNULL)
    r=data('D6_RETROSPECTIVE_RESULTS.json')
    assert r['d3_old_reverse_exact']==0
    assert r['d5_reinterpreted_reverse_exact']==21
    assert r['corrected_old_interpretations']==21
    assert r['graph_mutation'] is False
    assert r['candidate_promoted_to_WORLD'] is False
    assert r['graph_facts_and_audit_before_after'][0]==r['graph_facts_and_audit_before_after'][1]
    assert r['native_retrieve_hit_at_2']==12
    assert r['native_retrieve_full_source_oracle_hit_at_2']==32

def test_unchanged_iteration_is_stagnant():
    r=data('D6_RETROSPECTIVE_RESULTS.json')
    assert len(r['unchanged_repeat_curve'])==7
    assert all(x['correct']==21 for x in r['unchanged_repeat_curve'])
    assert r['unchanged_repeat_curve'][-1]['passes']==100

def test_replay_versions_share_root_not_independent_evidence():
    ledger=data('D6_VERSIONED_INTERPRETATION_LEDGER.json')
    assert len(ledger)==32
    assert all(x['source_lineage']=='SINGLE_PRIOR_USER_EVENT_NOT_WORLD' for x in ledger)
    assert all(x['interpretation_lineage'].startswith('DERIVED_FROM_SAME_RAW_EPISODE') for x in ledger)
    assert sum(x['gold_exact_after'] for x in ledger)==21
    assert sum(x['gold_exact_before'] for x in ledger)==0

def test_micrograph_pass_count_and_overshoot():
    subprocess.run([sys.executable,str(ROOT/'iterative_graph_micro.py')],check=True,stdout=subprocess.DEVNULL)
    r=data('D6_ITERATIVE_GRAPH_MICRO_RESULTS.json')
    z={x['passes']:x for x in r['rows']}
    assert z[1]['graph_exact']==31 and z[4]['graph_exact']==200
    assert z[5]['graph_exact']==194 and z[100]['graph_exact']==194
    assert r['trained_scalar_weight']==1.0

if __name__=='__main__':
    import pytest
    raise SystemExit(pytest.main([__file__,'-q']))