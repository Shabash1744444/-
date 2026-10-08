"""G331 structured-language cognition on the *existing* C4LivingRuntime / C4Graph.

This is an input organ, not another brain, memory, model, or checkpoint format.
All event evidence goes into the pre-existing graph/life-line. The only extra
persistent state is procedural predictions and pending action/goal contracts.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from .constitution import evaluate_mutation, STRICT

PREFIX='@c4 '
OPS={'SOCIAL','TOPIC','REPORT','CORRECT','QUERY','GOAL','DEMO','PLAN','REFLECT'}
SOCIAL={'GREET','PRAISE','THANK','ACCEPT_THANKS','ACK'}
SCOPES={'SOURCE','STORY','SIM'} # NO WORLD admission from text
MODES={'BELIEF','QUOTE','REPORT','WISH','JOKE','IRONY','SIMULATED'}

def _atom(value):
    if not isinstance(value,str) or not value or len(value)>120 or any(ord(c)<32 for c in value):
        raise ValueError('INVALID_SYMBOL')
    return value

def _fact(d):
    if not isinstance(d,dict) or set(d)!={'subject','relation','object'}:raise ValueError('INVALID_PROPOSITION')
    return {k:_atom(d[k]) for k in ('subject','relation','object')}

def _frame(d):
    if d is None:return []
    if not isinstance(d,list) or len(d)>12:raise ValueError('FRAME_DEPTH_OR_TYPE')
    frames=[]
    for p in d:
        if not isinstance(p,dict) or set(p)!={'actor','mode'}:raise ValueError('FRAME_INVALID')
        actor=_atom(p['actor']);mode=_atom(p['mode']).upper()
        if mode not in MODES:raise ValueError('FRAME_MODE_INVALID')
        frames.append({'actor':actor,'mode':mode})
    return frames

def _ctx(payload):
    scope=str(payload.get('scope','SOURCE')).upper()
    if scope not in SCOPES:raise ValueError('WORLD_NOT_AUTHORIZED')
    scene=_atom(str(payload.get('scene','dialogue')))
    frames=_frame(payload.get('frames',[]))
    context={'scope':scope,'scene':scene,'frames':frames}
    principal='PSEUDO:'+hashlib.sha256(json.dumps(context,sort_keys=True,ensure_ascii=False).encode()).hexdigest()[:24]
    return context,principal

def parse(text):
    if not isinstance(text,str) or not text.startswith(PREFIX):return None
    if len(text)>8192:raise ValueError('INPUT_SIZE_LIMIT')
    p=json.loads(text[len(PREFIX):])
    if not isinstance(p,dict):raise ValueError('EXPECTED_OBJECT')
    op=str(p.get('op','')).upper()
    if op not in OPS:raise ValueError('UNKNOWN_OPERATION')
    # No forged origin, source, result verification or agent speech through chat.
    forbidden={'verified','origin','source_group','source_ref','as_actor','reward','delivered','receipt','actor','source_root'}
    if forbidden.intersection(p):raise ValueError('SPOOFED_AUTHORITY')
    _ctx(p)
    if op in {'REPORT','CORRECT','QUERY'}:_fact(p.get('fact'))
    if op=='CORRECT':_atom(p.get('replaces'))
    if op=='QUERY' and p.get('as_of_turn') is not None:
        n=p['as_of_turn']
        if type(n) is not int or n < 0:raise ValueError('INVALID_DIALOGUE_TURN')
    if op!='QUERY' and 'as_of_turn' in p:raise ValueError('UNUSED_TEMPORAL_FIELD')
    if op=='SOCIAL' and str(p.get('act','')).upper() not in SOCIAL:raise ValueError('UNKNOWN_SOCIAL_ACT')
    if op in {'TOPIC'}:_atom(p.get('subject'))
    if op=='GOAL':_fact(p.get('target'))
    if op=='DEMO':
        if str(p.get('scope','SIM')).upper()!='SIM':raise ValueError('DEMO_ONLY_SIM')
        _atom(p.get('action'));_fact(p.get('before'));_fact(p.get('after'))
    if op=='PLAN' and p.get('goal_id') is not None:_atom(p.get('goal_id'))
    return p

def _record(r,owner,kind,source,**details):
    r._record_life_event('C4',owner+'_'+kind,status=details.pop('status','RECORDED'),
                         source_event_id=source,extra=details)

def _key(ctx,prop):
    return json.dumps({'context':ctx,'fact':prop},ensure_ascii=False,sort_keys=True)

def _claim_value(g, fact):
    """Surface form of a typed graph object; never treat entity ID as speech."""
    return g.label(fact.object_value) if fact.object_kind=='entity' else fact.object_value


def _claim_object(g, relation, object_symbol):
    """Preserve the native per-relation object type of the loaded C4M graph."""
    mode=g.relation_spec(relation).object_mode
    if mode=='entity':return 'entity',g.entity(object_symbol)
    return 'literal',object_symbol


def _source_turn(r, f):
    """External reception order, never the event-time asserted by the speaker."""
    event=r.semantic_spine.events.get(f.source_ref,{})
    n=event.get('external_order')
    return n if type(n) is int else None


def _claims_at(r, matches, as_of_turn):
    """Reconstruct which SOURCE claims were active at a dialogue cutoff.

    A SOURCE_SUPERSEDED claim is evidence of a historic utterance. It is not
    currently asserted, but may be quoted by an as-of query before its explicit
    linked correction. No graph canonical truth is changed by this read.
    """
    if as_of_turn is None:
        return [f for f in matches if f.status in {'SOURCE_ASSERTED','ADMITTED','REVISED'}]
    corrections={f.correction_of: f for f in r.dialogue.g.facts.values() if f.correction_of}
    out=[]
    for f in matches:
        recv=_source_turn(r,f)
        if recv is None or recv>as_of_turn:continue
        if f.status=='SOURCE_SUPERSEDED':
            replacement=corrections.get(f.fact_id)
            # Do not resurrect an orphaned or non-temporally verifiable record.
            if replacement is None:continue
            at=_source_turn(r,replacement)
            if at is None or at<=as_of_turn:continue
        elif f.status not in {'SOURCE_ASSERTED','ADMITTED','REVISED'}:
            continue
        out.append(f)
    return out


def _reply(r,reply,op,source,*,mutated=False,publish=True,semantic=None):
    r._record_turn('USER',r.semantic_spine.events.get(source,{}).get('payload',''),kind='PSEUDO_'+op,event_id=source)
    ev=None
    if publish:
        ev=r._event('REPLY',reply,'COGNITIVE_'+op,.76,source,False)
        r._record_turn('C4',reply,kind='REPLY',reason='COGNITIVE_'+op,event_id=ev.event_id)
    else:
        r._queue_public_act(reply,reason='COGNITIVE_'+op,cause_id=source,reply_kind='COGNITIVE_'+op,
                            parsed={'kind':'PSEUDO_'+op},value=.76,source_event_id=source)
    r._autosave_tick(mutated)
    return {'reply':reply if publish else None,'proposed_reply':None if publish else reply,
            'mutated':mutated,'event':None if ev is None else ev.__dict__,
            'parsed':{'kind':'PSEUDO_'+op},'reply_kind':'COGNITIVE_'+op,'cognitive':semantic or {}}

def process(r,p,source,publish=True):
    """Interpret already-validated symbolic input via the existing runtime organs."""
    op=str(p['op']).upper();ctx,principal=_ctx(p)
    r.step+=1;r.last_user_step=r.step;r.human_active=True
    _record(r,'EVAL','STRUCTURED_EVENT',source,operation=op,context=ctx,authority='OTHER_CHAT_TEXT')
    g=r.dialogue.g
    if op=='REPORT':
        prop=_fact(p['fact'])
        # EVAL->COMMIT exactly as ordinary USER_SAID must be: CLAIM_ONLY, never WORLD.
        law=evaluate_mutation(mode=STRICT,operation='COMMIT',origin='USER_SAID',authority='USER')
        if law.disposition!='CLAIM_ONLY':raise RuntimeError('SOURCE_ONLY_CONSTITUTION_BROKEN')
        # Existing graph records source-only evidence; no parallel memory/database.
        object_kind,object_value=_claim_object(g,prop['relation'],prop['object'])
        f=g._record_claim_only(g.entity(prop['subject']),prop['relation'],object_value,
                               object_kind=object_kind,origin='USER_SAID',principal=principal,privacy='PRIVATE',authority='USER',
                               source_ref=source,source_group='OTHER_CHAT_LINEAGE',
                               decision_reason=law.reason)
        _record(r,'COMMIT','SOURCE_ASSERTION',source,fact_id=f.fact_id,claim_status=f.status,
                scope=ctx['scope'],scene=ctx['scene'],frames=ctx['frames'])
        msg=f"Приняла как сообщение источника в {ctx['scope']}/{ctx['scene']}: {prop['subject']} {prop['relation']} {prop['object']}. Это не проверенный факт мира."
        _record(r,'DRIVE','SPEECH_CHOICE',source,choice='SOURCE_ACK')
        return _reply(r,msg,op,source,mutated=True,publish=publish,semantic={'fact_id':f.fact_id,'status':f.status})
    if op=='CORRECT':
        prop=_fact(p['fact']);replaces=p['replaces']
        eid=g.resolve(prop['subject'])
        # Only the actual earlier report of this user, in this exact context,
        # with this subject and predicate, is eligible. No time/context shift,
        # no correction of another source, no trust-score adjustment.
        old=next((f for f in g.facts.values() if f.source_ref==replaces and
                  f.origin=='USER_SAID' and f.status=='SOURCE_ASSERTED' and
                  f.principal==principal and f.subject==eid and
                  f.relation==prop['relation'].upper()),None)
        if old is None or _claim_value(g,old).casefold()==prop['object'].casefold():
            _record(r,'COMMIT','CORRECTION_REJECTED',source,replaces=replaces,
                    reason='NO_MATCHING_ACTIVE_SOURCE_CLAIM_OR_NO_CHANGE')
            return _reply(r,'Не могу связать исправление с прежним сообщением этого источника в том же контексте.',
                          op,source,publish=publish,semantic={'status':'REJECTED','replaces':replaces})
        spec=g.relation_spec(prop['relation'])
        law=evaluate_mutation(mode=STRICT,operation='COMMIT',origin='USER_SAID',authority='USER')
        if law.disposition!='CLAIM_ONLY':raise RuntimeError('SOURCE_ONLY_CONSTITUTION_BROKEN')
        object_kind,object_value=_claim_object(g,prop['relation'],prop['object'])
        # A learned schema change cannot silently change the object type of the
        # assertion being corrected. Both facts must live in the same typed slot.
        if object_kind!=old.object_kind:
            _record(r,'COMMIT','CORRECTION_REJECTED',source,replaces=replaces,reason='OBJECT_TYPE_MISMATCH')
            return _reply(r,'Тип значения изменился: прежнее сообщение не заменено.',op,source,
                          publish=publish,semantic={'status':'REJECTED'})
        new=g._record_claim_only(eid,prop['relation'],object_value,object_kind=object_kind,origin='USER_SAID',
                                 principal=principal,privacy='PRIVATE',authority='USER',
                                 source_ref=source,source_group=old.source_group,
                                 decision_reason='EXPLICIT_SAME_SOURCE_CORRECTION')
        new.correction_of=old.fact_id;g._touch_fact(new)
        old.status='SOURCE_SUPERSEDED';g._touch_fact(old)
        g.audit.append({'order':g.order,'type':'SOURCE_CORRECTION','old_fact_id':old.fact_id,
                        'new_fact_id':new.fact_id,'owner':'COMMIT','scope':ctx['scope'],
                        'source_event_id':source,'replaces_source_event_id':replaces})
        _record(r,'COMMIT','SOURCE_CORRECTION',source,status='SOURCE_CORRECTED',
                old_fact_id=old.fact_id,new_fact_id=new.fact_id,replaces=replaces,
                scope=ctx['scope'],scene=ctx['scene'])
        _record(r,'DRIVE','SPEECH_CHOICE',source,choice='ACK_SOURCE_REVISION')
        return _reply(r,'Исправление источника записано: '+prop['subject']+' '+prop['relation']+' '+prop['object']+
                      '. Предыдущее сообщение сохранено для исторического запроса, не как факт мира.',
                      op,source,mutated=True,publish=publish,
                      semantic={'status':'SOURCE_CORRECTED','old_fact_id':old.fact_id,
                                'new_fact_id':new.fact_id,'replaces':replaces})
    if op=='QUERY':
        prop=_fact(p['fact'])
        as_of=p.get('as_of_turn')
        if as_of is not None and as_of>r.external_seq:
            _record(r,'EVAL','RETRIEVAL_REJECTED',source,reason='FUTURE_DIALOGUE_CUTOFF')
            return _reply(r,'Нельзя проверить ещё не наступившую реплику диалога.',op,source,publish=publish,
                          semantic={'status':'REJECTED','as_of_turn':as_of})
        eid=g.resolve(prop['subject'])
        same=[f for f in g.facts.values() if eid and f.subject==eid and f.principal==principal and
              f.relation==prop['relation'].upper()]
        matches=_claims_at(r,same,as_of)
        values={_claim_value(g,f) for f in matches}
        want=prop['object']; found=[f for f in matches if want=='?' or _claim_value(g,f).casefold()==want.casefold()]
        if len(values)>1:status='CONFLICT'
        elif found:status='SOURCE_REPORTED'
        else:status='UNKNOWN'
        # A conflict triggers inquiry, NEVER calibration of source trust against C4's belief.
        if status=='CONFLICT':
            msg='Есть несовместимые сообщения в одном контексте: '+', '.join(sorted(values))+'. Нужна независимая проверка.'
        elif status=='SOURCE_REPORTED':
            msg='По сообщению источника: '+', '.join(sorted({_claim_value(g,f) for f in found}))+'. Проверки мира нет.'
        else:
            msg='В этом контексте не знаю. Что могло бы проверить '+prop['relation']+' для '+prop['subject']+'?'
        _record(r,'EVAL','RETRIEVAL',source,status=status,basis=[f.fact_id for f in matches],scope=ctx['scope'],scene=ctx['scene'])
        _record(r,'COMMIT','NOOP',source,reason='QUERY_NOT_TEACHING')
        _record(r,'DRIVE','SPEECH_CHOICE',source,choice='INQUIRE' if status!='SOURCE_REPORTED' else 'ANSWER_BOUNDED')
        return _reply(r,msg,op,source,publish=publish,semantic={'status':status,'basis':[f.fact_id for f in matches],
                                       'values':sorted({_claim_value(g,f) for f in found}),
                                       'as_of_turn':as_of})
    if op=='SOCIAL':
        act=p['act'].upper()
        last=next((x for x in reversed(r.dialogue_history) if x.get('speaker')=='C4'),None)
        last_id=last.get('event_id') if last else None
        # Require causal link for a continuation act; no imaginary prior turn.
        if act=='ACCEPT_THANKS' and (not last or last.get('text')!='Спасибо!'):
            msg='Пока не вижу предыдущей благодарности, к которой это относится.'
            label='UNRESOLVED_SOCIAL_REFERENCE'
        else:
            msg={'GREET':'Привет!','PRAISE':'Спасибо!','THANK':'Пожалуйста!',
                 'ACCEPT_THANKS':'Можем продолжить.','ACK':'Поняла.'}[act]
            label='SOCIAL_REPLY'
        _record(r,'COMMIT','NOOP',source,reason='SOCIAL_NOT_WORLD_FACT')
        _record(r,'DRIVE','SPEECH_CHOICE',source,choice=label,linked_event_id=last_id)
        return _reply(r,msg,op,source,publish=publish,semantic={'prior_reply_event_id':last_id,'status':label})
    if op=='TOPIC':
        subject=_atom(p['subject']);eid=g.resolve(subject)
        evidence=[f for f in g.facts.values() if eid and f.subject==eid and f.status in {'ADMITTED','REVISED','SOURCE_ASSERTED'}]
        if not evidence:
            # Existing G329 curiosity organ, NOT a second agenda. An entity label
            # is only an address for an unresolved topic, never evidence of truth.
            eid=eid or g.entity(subject)
            gap=r.register_gap('DEFINITION',eid,reason='USER_TOPIC_UNKNOWN',priority=.72,
                               cause_id=source,schedule=True)
            _record(r,'COMMIT','CURIOSITY_GAP',source,gap_id=gap.gap_id,status='OPEN',
                    basis='TOPIC_NOT_KNOWLEDGE')
        msg=(f'Есть {len(evidence)} записей о теме «{subject}». Что именно исследуем?' if evidence
             else f'Про «{subject}» пока недостаточно оснований. Что ты хочешь выяснить?')
        _record(r,'DRIVE','TOPIC_INQUIRY',source,topic=subject,basis=[x.fact_id for x in evidence])
        return _reply(r,msg,op,source,publish=publish,semantic={'topic':subject,'evidence_count':len(evidence)})
    if op=='GOAL':
        target=_fact(p['target'])
        if ctx['scope']!='SIM':
            _record(r,'COMMIT','GOAL_REJECTED',source,reason='ONLY_SIM_PLANNING_AT_THIS_STAGE')
            return _reply(r,'Планирование действий пока разрешено только в SIM.',op,source,publish=publish)
        gid='goal:'+source
        r.cognitive_goals[gid]={'goal_id':gid,'target':target,'context':ctx,'status':'OPEN','source_event_id':source}
        _record(r,'COMMIT','GOAL_CREATED',source,goal_id=gid,scope='SIM')
        _record(r,'DRIVE','GOAL_ACTIVATED',source,goal_id=gid)
        return _reply(r,'Цель в SIM поставлена: '+target['subject']+' '+target['relation']+' '+target['object']+'. Проверю доступные действия.',op,source,mutated=True,publish=publish,semantic={'goal_id':gid})
    if op=='DEMO':
        before=_fact(p['before']);after=_fact(p['after']);action=_atom(p['action'])
        # A teacher's example is not an independently executed experiment.
        item={'action':action,'before':before,'after':after,'context':ctx,'source_event_id':source,
              'status':'UNVERIFIED_TEACHER_EXAMPLE','source_root':'OTHER_CHAT_LINEAGE'}
        r.cognitive_demonstrations.append(item)
        _record(r,'COMMIT','EXAMPLE_CANDIDATE',source,status='UNVERIFIED',action=action,
                basis='USER_SAID_NOT_SIM_RECEIPT')
        _record(r,'DRIVE','EXPERIMENT_NEEDED',source,action=action)
        return _reply(r,'Сохранила пример как неподтверждённую гипотезу для SIM. Нужен реальный результат действия.',op,source,mutated=True,publish=publish)
    if op=='PLAN':
        selected=p.get('goal_id')
        goals=[g for g in r.cognitive_goals.values() if g['status']=='OPEN' and (selected is None or g['goal_id']==selected)]
        if not goals:
            _record(r,'DRIVE','NO_PLAN',source,reason='NO_OPEN_GOAL')
            return _reply(r,'Нет подходящей открытой цели.',op,source,publish=publish,semantic={'status':'NO_GOAL'})
        goal=goals[-1];ctx=goal['context'];target=goal['target']
        # Learnable: match by relational roles and effects, not object names.
        candidates=[d for d in r.cognitive_demonstrations if d['context']==ctx and
                    d['after']['relation']==target['relation'] and d['after']['object']==target['object'] and
                    d['status']=='UNVERIFIED_TEACHER_EXAMPLE']
        if not candidates:
            _record(r,'DRIVE','NO_PLAN',source,goal_id=goal['goal_id'],reason='NO_EFFECT_MODEL')
            return _reply(r,'Нет даже пробной стратегии. Надо исследовать действие или спросить об опыте.',op,source,publish=publish,semantic={'status':'NO_MODEL'})
        weights=Counter(d['action'] for d in candidates)
        # Verified SIM consequences dominate teacher reports, *for a strategy*;
        # disagreement does not change provenance/source trust or graph truth.
        outcomes={}
        for old in r.cognitive_actions.values():
            if old.get('context')!=ctx or old.get('action') not in weights:continue
            if old['status'] in {'SIM_SUCCESS','SIM_FAILURE'}:
                score=3 if old['status']=='SIM_SUCCESS' else -4
                outcomes[old['action']]=outcomes.get(old['action'],0)+score
        ranked=sorted(weights,key=lambda a:(-(outcomes.get(a,0)+min(weights[a],2)*.2),a))
        action=ranked[0]
        if outcomes and max(outcomes.get(a,0)+min(weights[a],2)*.2 for a in ranked)<=0:
            _record(r,'DRIVE','EXPERIMENT_NEEDED',source,goal_id=goal['goal_id'],reason='ALL_EVALUATED_STRATEGIES_FAILED')
            return _reply(r,'Из проверенных стратегий пока нет успешной. Нужен другой способ или новый эксперимент.',op,source,publish=publish,
                          semantic={'status':'NEEDS_NEW_STRATEGY'})
        aid='trial:'+source
        r.cognitive_actions[aid]={'action_id':aid,'goal_id':goal['goal_id'],'action':action,'context':ctx,
                                  'source_event_id':source,'status':'PROPOSED_NOT_EXECUTED',
                                  'candidate_example_ids':[d['source_event_id'] for d in candidates if d['action']==action]}
        _record(r,'DRIVE','ACTION_PROPOSED',source,action_id=aid,action=action,goal_id=goal['goal_id'],
                status='PROPOSED',basis=r.cognitive_actions[aid]['candidate_example_ids'])
        # NO MEDIATE claim of execution/delivery/result.
        return _reply(r,'Могу попробовать в SIM действие '+action+', но выполнения и результата ещё нет.',op,source,mutated=True,publish=publish,
                      semantic={'action_id':aid,'status':'PROPOSED_NOT_EXECUTED','action':action})
    if op=='REFLECT':
        # Re-evaluate experienced consequences, not a canned narrative.
        rows=list(r.cognitive_actions.values())
        observed=[x for x in rows if x['status'] in {'SIM_SUCCESS','SIM_FAILURE'}]
        candidates=[x for x in rows if x['status']=='PROPOSED_NOT_EXECUTED']
        _record(r,'EVAL','SELF_REVIEW',source,verified_sim_results=len(observed),unexecuted_proposals=len(candidates))
        _record(r,'DRIVE','SPEECH_CHOICE',source,choice='UNCERTAINTY_DISCLOSURE')
        return _reply(r,f'Предложений без результата: {len(candidates)}. Подтверждённых результатов симуляции: {len(observed)}. Не буду объявлять предложения успехом.',op,source,publish=publish,
                      semantic={'unexecuted':len(candidates),'confirmed_sim':len(observed)})
    raise ValueError('UNREACHABLE')


def verified_sim_receipt(r,p):
    """Called *only* by bound SIM host, never by USER_MESSAGE JSON.

    Receipt is still scoped to SIM. A host-bound event cannot become WORLD truth.
    """
    if not isinstance(p,dict):raise ValueError('INVALID_SIM_RECEIPT')
    aid=_atom(p.get('action_id'));action=r.cognitive_actions.get(aid)
    if action is None or action['status']!='PROPOSED_NOT_EXECUTED':raise ValueError('NO_PENDING_ACTION')
    if p.get('success') is not True and p.get('success') is not False:raise ValueError('BOOLEAN_SUCCESS_REQUIRED')
    # A receipt is external to C4's self-score. The host callback is an explicitly
    # delegated trust boundary; nobody should infer this is independent real world proof.
    action['status']='SIM_SUCCESS' if p['success'] else 'SIM_FAILURE'
    action['outcome_event_id']='hostsim:'+hashlib.sha256((aid+'|'+str(r.step)).encode()).hexdigest()[:18]
    goal=r.cognitive_goals[action['goal_id']]
    if p['success']:goal['status']='ACHIEVED_SIM'
    _record(r,'MEDIATE','SIM_RECEIPT',action['outcome_event_id'],status=action['status'],action_id=aid,goal_id=goal['goal_id'])
    _record(r,'EVAL','CONSEQUENCE_REVIEW',action['outcome_event_id'],action_id=aid,success=p['success'])
    _record(r,'COMMIT','STRATEGY_SCORE',action['outcome_event_id'],action_id=aid,
            reward=1 if p['success'] else -1,scope='SIM')
    r._autosave_tick(True)
    return {'accepted':True,'scope':'SIM','action_id':aid,'status':action['status'],'goal_status':goal['status']}
