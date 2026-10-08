"""C4 G326 isolated pre-live harness. No external API/PC permissions.

Usage:
  python LIVE_SESSION.py
  python LIVE_SESSION.py --replay FROZEN_LIVE_PROMPTS.txt --out LIVE_REPLAY.jsonl
  python LIVE_SESSION.py --save-state my_post_live.c4m

Default model is READ ONLY. Explicit --save-state can create a separate model
snapshot; do not overwrite canonical or input model.
"""
from pathlib import Path
import argparse, sys, json, time, hashlib, traceback

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'runtime'))
from c4child.runtime import C4LivingRuntime

def parse():
    a=argparse.ArgumentParser()
    a.add_argument('--model',type=Path,default=ROOT/'model/child_g326_p0_unified_pre_live_candidate.c4m')
    a.add_argument('--out',type=Path,default=ROOT/'LIVE_session.jsonl')
    a.add_argument('--replay',type=Path,default=None)
    a.add_argument('--save-state',type=Path,default=None)
    a.add_argument('--fail-on-unsafe',action='store_true')
    return a.parse_args()

def main():
    args=parse()
    if not args.model.is_file():raise SystemExit('MODEL NOT FOUND: '+str(args.model))
    if args.save_state and args.save_state.resolve()==args.model.resolve():
        raise SystemExit('REFUSING TO OVERWRITE INPUT MODEL')
    if args.save_state and args.save_state.suffix!='.c4m':raise SystemExit('save-state must end in .c4m')
    model_sha=hashlib.sha256(args.model.read_bytes()).hexdigest()
    rt=C4LivingRuntime.open(str(args.model),store='memory')
    if not (getattr(rt.dialogue.g,'hardened_gate',False) and rt.epistemic.strict_world):
        raise SystemExit('FAIL CLOSED: unguarded state/model; not approved for this harness')
    print('C4 G326 experimental. SIMULATED local talk ≠ human/device LIVE validation')
    print('Model SHA256:',model_sha,'| Source logs:',args.out)
    if not args.replay:print('Введите текст; /exit завершает. /save сохранит отдельный checkpoint при указании --save-state.')
    if args.replay:
        lines=args.replay.read_text(encoding='utf-8').splitlines()
    else:
        lines=None
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open('a',encoding='utf-8') as out:
        counter=0
        while True:
            if lines is None:
                try:line=input('USER> ')
                except (EOFError,KeyboardInterrupt):break
            else:
                if counter>=len(lines):break
                line=lines[counter]
            counter+=1
            if not line.strip() or line.startswith('#'):continue
            if line.strip()=='/exit':break
            if line.strip()=='/save':
                if args.save_state:
                    rt.save(str(args.save_state));print('SAVED:',args.save_state)
                else:print('No --save-state specified; input model unchanged.')
                continue
            before_f=len(rt.dialogue.g.facts);before_e=len(rt.dialogue.g.entities)
            stamp=time.time()
            try:
                response=rt.user_message(line)
                ev=response.get('inbound_event') or {}
                frame=getattr(rt.semantic_spine,'perspective_frames',{}).get(ev.get('event_id',''))
                row={'user':line,'reply':response.get('reply'),'parsed':response.get('parsed'),
                     'reply_kind':response.get('reply_kind'),'source_event_id':ev.get('event_id'),
                     'perspective_frame':frame,'delta_facts':len(rt.dialogue.g.facts)-before_f,
                     'delta_entities':len(rt.dialogue.g.entities)-before_e,
                     'gated':bool(rt.dialogue.g.hardened_gate),'epistemic_strict':bool(rt.epistemic.strict_world),
                     'time':stamp,'status':'PROCESSED','model_sha256':model_sha}
                print('C4>',response.get('reply'))
            except Exception as ex:
                row={'user':line,'time':stamp,'status':'EXCEPTION',
                     'exception':type(ex).__name__,'error':str(ex),'model_sha256':model_sha}
                print('C4 EXCEPTION>',str(ex))
            out.write(json.dumps(row,ensure_ascii=False,default=str)+'\n');out.flush()
            if args.fail_on_unsafe and ((row.get('status')!='PROCESSED') or (frame and row.get('delta_facts',0)!=0)):
                raise SystemExit('UNSAFE LIVE RESULT: see JSONL')
    if args.save_state:
        rt.save(str(args.save_state));print('POST-LIVE MODEL SAVED:',args.save_state)
    print('Turns logged:',counter)
if __name__=='__main__':main()