"""C4 pretraining admission gate. Exits nonzero unless independently evidenced.

Unlike test success counters, an absent capability is always NOT VERIFIED.
A future cycle may update the contract's version after attaching evidence for
all required gates. This checker never mints a VERIFIED label for itself.
"""
import argparse
import json
from pathlib import Path


def validate(contract,request='autonomous_pretrain'):
    if contract['canonical_owners']!=['EVAL','COMMIT','DRIVE','MEDIATE']:
        return False,['CONSTITUTIONAL_OWNER_DRIFT']
    if set(contract['influence_classes'])!={'MASK','VALUE','AVAIL','TRIGGER','STATUS'}:
        return False,['INFLUENCE_CLASS_DRIFT']
    required={'SOURCE_ASSERTION_TO_WORLD_WITHOUT_INDEPENDENT_ADMISSION',
              'STORY_OR_SIM_TO_WORLD','REPLAY_TO_OBSERVATION',
              'PROPOSED_ACTION_TO_DELIVERED_WITHOUT_HOST_RECEIPT',
              'DISAGREEMENT_WITH_INTERNAL_BELIEF_TO_TRUST_PENALTY',
              'DEPENDENT_EXAMPLES_TO_INDEPENDENT_SUPPORT'}
    if not required.issubset(contract['forbidden_promotions']):
        return False,['FORBIDDEN_TRANSITION_REMOVED']
    if request=='autonomous_pretrain':
        missing=[k+':'+v for k,v in contract['acceptance_gates'].items() if v!='PASS']
        if not contract['mass_autonomous_pretraining_allowed']:missing+=['PRETRAIN_NOT_AUTHORIZED']
        if missing:return False,missing
    return True,[]


def main():
    p=argparse.ArgumentParser();p.add_argument('--contract',default=str(Path(__file__).resolve().parents[1]/'governance'/'constitution_contract.json'))
    p.add_argument('--request',default='autonomous_pretrain',choices=['autonomous_pretrain','constitution_only'])
    a=p.parse_args();contract=json.loads(Path(a.contract).read_text())
    allowed,issues=validate(contract,a.request)
    print(('PASS' if allowed else 'BLOCKED')+' '+a.request)
    for issue in issues:print(' - '+issue)
    if not allowed:raise SystemExit(2)
if __name__=='__main__':main()
