"""G326 experimental, conservative, recursive perspective/EVAL frame extraction.

Outputs candidates, not WORLD facts or authority. Surface-level grammar with abstention;
it does NOT claim to be general Russian language comprehension.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict, field
from typing import Optional, Tuple
import hashlib
import re
import json

_OPEN_CLOSE = {'«':'»', '“':'”', '"':'"'}
_WORD = r'[А-ЯЁа-яёA-Za-z][А-ЯЁа-яёA-Za-z-]*'
_REPORT = re.compile(rf'^\s*(?P<who>{_WORD})\s+(?P<verb>сказал[аи]?|говорил[аи]?|сообщил[аи]?|рассказал[аи]?|написал[аи]?|подумал[аи]?|думает|думал[аи]?|считает|считал[аи]?|полагает|полага[лла]+|верит|верил[аи]?)\s*(?P<sep>:|,?\s+что\s+)\s*(?P<body>.+)$',re.I|re.S)
_MODAL = re.compile(r'^\s*(?P<modal>представь|допустим|предположим|вообрази)\s*:\s*(?P<body>.+)$',re.I|re.S)
_REPORTED = re.compile(r'(?:говор|сказ|сообщ|рассказ|напис)',re.I)

@dataclass
class PerspectiveNode:
    holder: str
    act: str
    content: str
    mode: str
    child: Optional['PerspectiveNode'] = None
    referent: Optional[str] = None
    source_event: Optional[str] = None
    scope: str = 'SOURCE_ASSERTION'
    evidence_roots: Tuple[str,...] = field(default_factory=tuple)
    def as_dict(self):
        return json.loads(json.dumps(asdict(self),ensure_ascii=False))

def _unquote(t):
    t=t.strip()
    if len(t)>=2 and t[0] in _OPEN_CLOSE and t[-1]==_OPEN_CLOSE[t[0]]:
        return t[1:-1].strip(),True
    return t,False

def _deictic(content,holder,origin_speaker,origin_recipient):
    """First person in an *attributed* utterance refers to attributed speaker.
    Outside an attributed frame, these refer to the origin dialogue participants.
    No object/subject entity is created from the text.
    """
    m=re.search(r'\b(?:я|меня|мне|мной)\b',content,re.I)
    if m:return holder
    m=re.search(r'\b(?:ты|тебя|тебе|тобой)\b',content,re.I)
    if m:return origin_recipient if holder==origin_speaker else None
    return None

def _one(text, *, parent_holder, deictic_holder, origin_speaker, origin_recipient, source_event, depth, limit):
    if depth>limit:raise ValueError('PERSPECTIVE_DEPTH_LIMIT')
    text=text.strip()
    raw,was_quote=_unquote(text)
    if was_quote:
        child=_one(raw,parent_holder=parent_holder,deictic_holder=parent_holder,origin_speaker=origin_speaker,
                   origin_recipient=origin_recipient,source_event=source_event,depth=depth+1,limit=limit)
        return PerspectiveNode(parent_holder,'QUOTE',raw,'REPORTED',child,
                               source_event=source_event,evidence_roots=(source_event,))
    modal=_MODAL.match(raw)
    if modal:
        child=_one(modal['body'],parent_holder=parent_holder,deictic_holder=deictic_holder,origin_speaker=origin_speaker,
                   origin_recipient=origin_recipient,source_event=source_event,depth=depth+1,limit=limit)
        return PerspectiveNode(parent_holder,'HYPOTHETICAL',raw,'HYPOTHETICAL',child,
                               source_event=source_event,evidence_roots=(source_event,))
    report=_REPORT.match(raw)
    if report:
        token=report['who']; who=origin_speaker if token.lower()=='я' else origin_recipient if token.lower()=='ты' else token
        verb=report['verb']; mode='REPORTED_SPEECH' if _REPORTED.search(verb) else 'BELIEF'
        body=report['body'].strip()
        child=_one(body,parent_holder=who,deictic_holder=(who if report['sep'].strip()==':' else deictic_holder),origin_speaker=origin_speaker,
                   origin_recipient=origin_recipient,source_event=source_event,depth=depth+1,limit=limit)
        return PerspectiveNode(who,mode,body,mode,child,source_event=source_event,evidence_roots=(source_event,))
    return PerspectiveNode(parent_holder,'CONTENT',raw,'UNVERIFIED',None,
                           referent=_deictic(raw,deictic_holder,origin_speaker,origin_recipient),
                           source_event=source_event,evidence_roots=(source_event,))

def parse_perspective(text:str, *, source_event:str, origin_speaker='USER',origin_recipient='C4',depth_limit=10):
    """Conservative candidate: None if no perspective construction is found."""
    text=str(text).strip()
    # Strip leading 'imagine' wrapper only through the same recursive parser.
    if not (_MODAL.match(text) or _REPORT.match(text) or (len(text)>1 and text[0] in _OPEN_CLOSE and text[-1]==_OPEN_CLOSE[text[0]])):
        return None
    if not source_event:raise ValueError('source_event required')
    tree=_one(text,parent_holder=origin_speaker,deictic_holder=origin_speaker,origin_speaker=origin_speaker,
              origin_recipient=origin_recipient,source_event=str(source_event),depth=0,limit=depth_limit)
    return tree.as_dict()

def chain_summary(frame:dict)->str:
    """Generic human-readable trace; not a claim of external truth."""
    segments=[];cur=frame
    while isinstance(cur,dict):
        act=cur.get('act')
        if act=='BELIEF':segments.append(f"{cur.get('holder','?')} предполагает")
        elif act=='REPORTED_SPEECH':segments.append(f"{cur.get('holder','?')} сообщил(а)")
        elif act=='HYPOTHETICAL':segments.append('в воображаемой ситуации')
        elif act=='QUOTE':segments.append('цитата')
        else:
            segments.append('содержание: '+cur.get('content',''))
            break
        cur=cur.get('child')
    return ' → '.join(segments)

def perspective_entity_inquiry(text, event_frames):
    """Resolve 'who X' using ONLY prior attributed appearances, not world identity."""
    t=str(text).strip().rstrip('?!. ')
    patterns=(r'^(?:а\s+)?(?P<name>[А-ЯЁ][а-яё]+)\s+кто$',
              r'^(?:а\s+)?кто\s+(?:(?:такая|такой|это)\s+)?(?P<name>[А-ЯЁ][а-яё]+)$')
    who=None
    for p in patterns:
        m=re.match(p,t,re.I)
        if m:who=m['name'];break
    if not who:return None
    names=[]
    for v in event_frames.values():
        node=v
        while isinstance(node,dict):
            holder=node.get('holder')
            if holder and str(holder).casefold()==who.casefold():names.append(node.get('act'))
            node=node.get('child')
    if not names:return None
    return {'kind':'CONTEXT_PARTICIPANT','reply':
            f'В этой переписке {who} упоминалась или упоминался в чужой речи либо мысли. '
            f'По одному этому упоминанию я не могу установить, кто это в реальном мире.'}