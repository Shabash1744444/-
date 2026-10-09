import hashlib,json
from pathlib import Path
from multipath_native import infer,D5,g,R

def test_old_frozen_multi_hypothesis_gain():
    examples=json.loads((R/'D7_NATIVE_KBEST_RESULTS.json').read_text())['budgets']['old_reverse32']
    assert examples['1']['exact']==21 and examples['2']['exact']==25
    assert all(examples[str(k)]['exact']==25 for k in (4,8,16,32))

def test_unprepared_language_small_gain_and_failure():
    x=json.loads((R/'D7_NATIVE_KBEST_RESULTS.json').read_text())
    assert x['budgets']['manual10']['1']['exact']==4
    assert x['budgets']['manual10']['8']['exact']==5
    assert x['budgets']['manual10']['32']['exact']==5

def test_invalid_hypotheses_increase_with_search():
    x=json.loads((R/'D7_NATIVE_KBEST_RESULTS.json').read_text())['ood']
    assert x['1']['false_candidates']==1
    assert x['8']['false_candidates']==5

def test_original_graph_bytewise_unchanged():
    assert hashlib.sha256(D5.read_bytes()).hexdigest()=='b7b2dd0f826bbc217f2a5499e53ba554a61c415817fe5d1f2c5313f2caa81036'
    assert len(g.facts)==16731

def test_alternative_routes_do_not_promote_claim():
    r=infer('пожалуйста напомни мне купить молоко',32)
    assert r['status'] in ('ABSTAIN','CANDIDATE')
    assert 'WORLD' not in r and 'world' not in r