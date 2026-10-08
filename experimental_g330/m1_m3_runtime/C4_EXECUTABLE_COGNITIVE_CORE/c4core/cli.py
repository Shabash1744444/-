"""Interactive newline-JSON runtime: python -m c4core.cli --state ./brain.c4j.

This is a typed event interface. Plain Russian text still requires a language organ.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from .kernel import C4, Proposition as P, Perspective as F, Query as Q, Scope


def decode_meaning(value):
    if 'holder' in value:
        return F(value['holder'], value['mode'], decode_meaning(value['content']))
    return P(value['predicate'], tuple(value['args']))


def result(c: C4, obj: dict) -> dict:
    op=obj['op']
    if op=='teach':
        verdict, cl = c.teach(obj.get('actor','USER'),decode_meaning(obj['content']),
                              scope=Scope(obj.get('scope','SOURCE_ASSERTION')),
                              scene=obj.get('scene','default'),claimed_at=obj.get('claimed_at'))
        return {'verdict':verdict.value,'claim_id':cl.id,'effective_scope':cl.scope.value,'roots':cl.roots}
    if op=='query':
        q=Q(obj['predicate'],tuple(obj['args']),Scope(obj['scope']),obj.get('scene','default'),
            tuple(tuple(x) for x in obj.get('perspective',[])),obj.get('as_of'))
        a, receipt=c.respond(q)
        return {'status':a.status,'bindings':a.bindings,'source_claims':a.claim_ids,
                'roots':a.roots,'reason':a.reason,'public_receipt':receipt.state}
    if op=='gap':
        return {'gap_id':c.open_gap(obj['topic'],obj['question'],utility=obj.get('utility',0.5))}
    if op=='answer_gap':
        claim=c.receive_gap_answer(obj['gap_id'],obj.get('actor','USER'),decode_meaning(obj['content']))
        return {'claim_id': None if claim is None else claim.id,
                'status':'UNRELATED_NOT_LINKED' if claim is None else 'ANSWER_CANDIDATE_NOT_VERIFIED'}
    if op=='tick':
        r=c.tick()
        return {'selected_action_id':r.action_id,'effect':r.state,'asks':c.own_asks()}
    if op=='demonstrate':
        rule=c.learn_example(obj.get('actor','SIM'),[decode_meaning(x) for x in obj['premises']],
                             decode_meaning(obj['consequence']),scope=Scope(obj.get('scope','SIMULATION')),
                             scene=obj.get('scene','default'),successful=obj.get('successful',True))
        return {'learned_rule': None if rule is None else {
            'premises':rule.premises,'consequence':rule.consequence,
            'scope':rule.scope.value,'active':rule.active,'examples':len(rule.supporting_roots)}}
    if op=='replay':
        e=c.replay_source(obj['event_id'])
        return {'event_id':e.id,'inherited_roots':e.roots}
    if op=='status':
        return {'version':c.VERSION,'events':len(c.events),'claims':len(c.claims),
                'rules':len(c.rules),'asks':c.own_asks(),'sha256':c.snapshot_hash()}
    if op=='save':return {'checkpoint_sha256':c.save(obj['path'])}
    if op=='trace':return {'events':c.trace[-obj.get('limit',25):]}
    raise ValueError('UNKNOWN_OPERATION: '+str(op))


def main(argv=None):
    parser=argparse.ArgumentParser()
    parser.add_argument('--state',default=None,help='Auto-load and auto-save state checkpoint')
    args=parser.parse_args(argv)
    state=Path(args.state) if args.state else None
    kernel=C4.load(state) if state and state.exists() else C4()
    print(json.dumps({'ready':True,'version':kernel.VERSION,'state':str(state) if state else None}),flush=True)
    for line in sys.stdin:
        if not line.strip():continue
        try:
            request=json.loads(line)
            if request.get('op')=='exit':
                if state:kernel.save(state)
                print(json.dumps({'bye':True}),flush=True)
                return
            reply=result(kernel,request)
            if state:kernel.save(state)
            print(json.dumps({'ok':True,**reply},ensure_ascii=False),flush=True)
        except (ValueError,KeyError,TypeError) as e:
            print(json.dumps({'ok':False,'error':type(e).__name__,'message':str(e)},ensure_ascii=False),flush=True)

if __name__=='__main__':main()
