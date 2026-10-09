import sys,json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R))
import d8_persist_native as native
import d8_gate as exp
from c4child.checkpoint import load_c4m_compact

def test_exam_file_still_pinned():
    assert hashlib.sha256((R/'D8_FROZEN_EXAM.json').read_bytes()).hexdigest()==exp.REQUIRED_SHA

def test_model_cold_integrity_and_native_registration():
    g,_,_=load_c4m_compact(native.CANDIDATE,hydrate_cold=True)
    reader=native.C4NativeLearnedCritic(g).load()
    assert len(g.facts)==16781 and len(reader.params)==50
    assert 'D8_CRITIC_WEIGHT' in {f.relation for f in g.facts.values()}
    assert all(f.status=='ADMITTED' for f in g.facts.values() if f.relation=='D8_CRITIC_WEIGHT')

def test_native_scalar_scores_match_learner_and_frozen_predictions():
    g,_,_=load_c4m_compact(native.CANDIDATE,hydrate_cold=True)
    reader=native.C4NativeLearnedCritic(g).load()
    records=json.loads((R/'D8_GATE_RESULTS.json').read_text())['fresh_details']
    ntrue=nfalse=0
    for ex in records:
        c=exp.vectors(ex['text'],32)
        actual=reader.predict(c)
        assert actual['ast']==ex['predicted'],ex['text']
        if ex['kind']=='positive':ntrue+=int(actual['ast']==ex['expected'])
        else:nfalse+=int(actual['ast'] is not None)
    assert (ntrue,nfalse)==(5,2)

def test_stream_proxy_short_and_long():
    d=json.loads((R/'D8_RECURRENT_PROXY_RESULTS.json').read_text())
    assert d['selected_alpha_short_train']==0.6
    assert d['results']['3000']['mean_fast_history_accuracy']<d['results']['40']['mean_fast_history_accuracy']
    assert d['results']['3000']['mean_episodic_historical_accuracy']==1

def test_parent_c4m_unchanged():
    assert hashlib.sha256(native.PARENT.read_bytes()).hexdigest()=='b7b2dd0f826bbc217f2a5499e53ba554a61c415817fe5d1f2c5313f2caa81036'