import json
from pathlib import Path
from tools.c4_stage_gate import validate
CONTRACT=json.loads((Path(__file__).parents[1]/'governance/constitution_contract.json').read_text())


def test_four_owner_five_influence_contract_has_no_unlicensed_owners():
    ok,issues=validate(CONTRACT,'constitution_only')
    assert ok,issues
    assert CONTRACT['edge_matrix']=='4x4x5 signatures, not 80 scripted handlers'


def test_unproven_autonomous_pretraining_is_blocked_by_default():
    ok,issues=validate(CONTRACT,'autonomous_pretrain')
    assert not ok
    assert 'PRETRAIN_NOT_AUTHORIZED' in issues
    assert any('A8_open_ended_operator_learning' in s for s in issues)
    assert any('A10_android_physical_trace' in s for s in issues)


def test_removing_law_or_cascade_constraint_fails_gate():
    c=dict(CONTRACT,canonical_owners=['EVAL','COMMIT','DRIVE'])
    assert not validate(c,'constitution_only')[0]
    c=dict(CONTRACT,forbidden_promotions=[])
    assert not validate(c,'constitution_only')[0]
