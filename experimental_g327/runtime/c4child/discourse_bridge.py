"""G327 experimental source-scoped discourse queries over recursive semantic frames.

This module is an EVAL-only view over the event/representation graph. It does
not write facts, mark sources independent, select actions, or verify the world.
Question forms are an interface to graph retrieval, never learning targets.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional
import re

_RUWORD = r'[А-ЯЁа-яёA-Za-z][А-ЯЁа-яёA-Za-z-]*'
_Q_ACT = re.compile(rf'^\s*(?:а\s+)?что\s+(?P<act>думает|думал[аи]?|считает|сказал[аи]?|говорил[аи]?|сообщил[аи]?)\s+(?P<who>{_RUWORD})\s*\?\s*$',re.I)
_Q_WHO = re.compile(r'^\s*(?:а\s+)?кто\s+(?P<act>думает|считает|сказал|говорил|сообщил)\s*(?:,?\s*что\s+|:\s*)(?P<claim>.+?)\s*\?\s*$',re.I)
_Q_TRUTH = re.compile(r'^\s*(?:а\s+)?(?:правда\s+ли|точно\s+ли|верно\s+ли|действительно\s+ли)\s*(?:,?\s*что\s+)?(?P<claim>.+?)\s*\?\s*$',re.I)
_Q_LAST_TRUTH = re.compile(r'^\s*(?:а\s+)?(?:это|так)\s+(?:правда|факт|доказано)\s*\?\s*$',re.I)
_Q_WHEN = re.compile(rf'^\s*(?:а\s+)?когда\s+(?P<who>{_RUWORD})\s+(?P<act>сказал[аи]?|говорил[аи]?|думал[аи]?|подумал[аи]?)\b.*\?$',re.I)
_Q_WHY = re.compile(r'^\s*(?:почему|на\s+каком\s+основании|откуда)\s+(?:ты\s+)?(?:так\s+)?(?:думаешь|считаешь|решила|решил|уверена|уверен|знаешь|говоришь|ответила|ответил)[^?]*\?\s*$',re.I)
_STOP = {'что','это','она','он','они','мне','меня','я','ты','тебя','там','уже','сказал','сказала','думает','думал','считает','говорил','говорила','был','была','было','ли'}


def _stem(word: str) -> str:
    """Conservative token reduction for matching claims, not morphological truth."""
    w = word.casefold().replace('ё','е')
    for end in ('ыми','ими','ного','ной','ого','ему','ами','ями','ает','ила','ила','или','ала','ало','али','его','иях','иях','ом','ой','ый','ий','ая','ое','ые','ов','ев','ам','ям','ах','ях','у','ю','а','я','ы','и','е'):
        if len(w)>len(end)+3 and w.endswith(end):
            return w[:-len(end)]
    return w


def _tokens(text: str):
    return {_stem(w) for w in re.findall(_RUWORD, str(text)) if w.casefold() not in _STOP and len(w)>2}


def _same_name(a: str, b: str) -> bool:
    a=str(a).casefold().replace('ё','е');b=str(b).casefold().replace('ё','е')
    return a==b or _stem(a)==_stem(b)


def _kind(act: str) -> str:
    return 'BELIEF' if str(act).casefold().startswith(('дум','счит','полага','вер')) else 'REPORTED_SPEECH'


@dataclass(frozen=True)
class Attributed:
    holder: str
    mode: str
    content: str
    root: str
    event_id: str
    depth: int
    hypothetical: bool


def attributed_frames(spine: Any) -> List[Attributed]:
    """Read-only derive nested attributions in true external receive order.

    Crucially, reporting someone's belief != confirming that belief in WORLD.
    """
    out=[]
    order={eid:(int(ev.get('external_order',0)),float(ev.get('wall_time',0)))
           for eid,ev in getattr(spine,'events',{}).items()}
    for eid, frame in sorted(spine.perspective_frames.items(),key=lambda p:order.get(p[0],(0,0))):
        node=frame;depth=0;hypo=False
        while isinstance(node,dict) and depth<32:
            act=node.get('act')
            hypo = hypo or act=='HYPOTHETICAL'
            if act in {'BELIEF','REPORTED_SPEECH'} and str(node.get('holder','')).casefold() not in {'кто','что'}:
                out.append(Attributed(str(node.get('holder','')),str(act),str(node.get('content','')),
                                      str((node.get('evidence_roots') or [eid])[0]),str(eid),depth,hypo))
            node=node.get('child');depth+=1
    return out


def _act_matches(asked: str,actual: str) -> bool:
    return _kind(asked)==actual


def resolve_disposition(text: str,spine: Any,history: Iterable[dict]|None=None) -> Optional[Dict[str,Any]]:
    """Precise follow-up over recorded attributed events, fail-closed on ambiguity.

    Replies express SOURCE_ASSERTION only. No physical-world verification implied.
    """
    t=str(text).strip()
    if '?' not in t:return None
    rows=attributed_frames(spine)
    history=list(history or [])
    if _Q_WHY.match(t):
        previous=next((x for x in reversed(history) if x.get('speaker')=='C4'),None)
        if previous is None:
            msg='Пока нет моего предыдущего ответа для проверки причин.'
        else:
            reason=previous.get('reason') or previous.get('kind') or 'не зарегистрирована'
            msg=('Это мой предыдущий вывод или ответ, а не независимое наблюдение. '
                 f'Записанный тип основания: {reason}. Без исходного проверяемого свидетельства я не могу гарантировать его истинность.')
        return {'kind':'DISCOURSE_SELF_AUDIT','reply':msg,'refs':[],'scope':'SYSTEM_REPORT'}
    m=_Q_ACT.match(t)
    if m:
        who=m['who'];matched=[r for r in rows if _same_name(r.holder,who) and _act_matches(m['act'],r.mode)]
        if not matched:
            return None
        distinct={(r.content,r.root) for r in matched}
        last=matched[-1]
        intro='считает' if last.mode=='BELIEF' else 'сообщил(а)'
        inner=last.content.strip()
        if inner.startswith(('«','\"')) and inner.endswith(('»','\"')):inner=inner[1:-1].strip()
        reply=(f'В этой беседе {last.holder} {intro}: «{inner}». '
               'Это приписанное высказывание, не доказанный факт внешнего мира.')
        if len(distinct)>1:reply+=' Есть и другие приписанные сообщения; контекст может быть неоднозначным.'
        if last.hypothetical:reply='В гипотетическом сценарии '+reply[0].lower()+reply[1:]
        return {'kind':'ATTRIBUTION_QUERY','reply':reply,'refs':[r.event_id for r in matched], 'scope':'SOURCE_ASSERTION'}
    m=_Q_WHO.match(t)
    if m:
        goal=_tokens(m['claim'])
        if not goal:return None
        matched=[r for r in rows if _act_matches(m['act'],r.mode) and goal<=_tokens(r.content)]
        if not matched:return None
        names=list(dict.fromkeys(r.holder for r in matched))
        return {'kind':'ATTRIBUTION_WHO','reply':
                'В этой беседе такое '+('убеждение' if _kind(m['act'])=='BELIEF' else 'высказывание')+
                ' приписано: '+', '.join(names)+'. Это атрибуция текста, не проверка внешнего мира.',
                'refs':[r.event_id for r in matched],'scope':'SOURCE_ASSERTION'}
    m=_Q_WHEN.match(t)
    if m:
        rows2=[r for r in rows if _same_name(r.holder,m['who']) and _act_matches(m['act'],r.mode)]
        if rows2:
            return {'kind':'SOURCE_TIME','reply':
                    f'В сообщениях есть утверждение, приписанное {rows2[-1].holder}, но реальное время действия не проверено. '
                    'В журнале есть время получения сообщения; его нельзя подменять временем самого события.',
                    'refs':[r.event_id for r in rows2],'scope':'SOURCE_ASSERTION'}
        return None
    m=_Q_TRUTH.match(t)
    goal=_tokens(m['claim']) if m else set()
    if m or _Q_LAST_TRUTH.match(t):
        if m:
            found=[r for r in rows if goal and goal<=_tokens(r.content)]
        else:
            # Elliptic 'Is this true?' must refer to the LAST ASSERTIVE external
            # event, not an unrelated older frame. Current question is not an
            # evidence root, and intervening normal messages reset deixis.
            events=sorted(spine.events.values(),
                          key=lambda e:(int(e.get('external_order',0)),float(e.get('wall_time',0))))
            recent=next((e for e in reversed(events)
                         if e.get('actor')=='OTHER' and not str(e.get('payload','')).strip().endswith('?')),None)
            found=[r for r in rows if recent and r.event_id==recent.get('event_id')]
        if found:
            scope='Гипотетический сценарий' if found[-1].hypothetical else 'Чужое сообщение или убеждение'
            return {'kind':'SOURCE_WORLD_BOUNDARY','reply':
                    f'{scope} зафиксированы как представление, но сами по себе не подтверждают истинность утверждения в WORLD.',
                    'refs':[r.event_id for r in found], 'scope':'SOURCE_ASSERTION'}
    return None