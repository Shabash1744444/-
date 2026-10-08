from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional
import hashlib, re, time

SPINE_VERSION = "C4_SEMANTIC_SPINE_V0_2"

_QUOTE_RE = re.compile(r'«([^»]*)»|“([^”]*)”|"([^"]*)"')


def quoted_fragments(text: str) -> List[Dict[str, Any]]:
    out=[]
    for m in _QUOTE_RE.finditer(str(text)):
        body=next((g for g in m.groups() if g is not None),"")
        out.append({"text":body,"start":m.start(),"end":m.end(),"depth":1})
    return out


def outside_quotes(text: str) -> str:
    return _QUOTE_RE.sub(" ",str(text))


def temporal_scope(text: str) -> str:
    t=str(text).lower()
    if re.search(r'\b(раньше|прежде|вчера|когда-то|ранее)\b',t): return "PAST"
    if re.search(r'\b(потом|позже|завтра|будущ|будет|буду|будешь|станет)\b',t): return "FUTURE"
    return "PRESENT"


def epistemic_mode(text: str) -> str:
    t=str(text).strip().lower()
    if re.match(r'^(?:может|может быть|возможно|наверное|вероятно)\b',t): return "POSSIBLE"
    if t.rstrip().endswith('?'): return "QUESTION"
    return "ASSERTED"


def social_role(token: str) -> Optional[str]:
    t=str(token).strip().lower()
    if t in {"я","меня","мне","мной"}: return "OTHER"  # speaker/user, from C4 perspective
    if t in {"ты","тебя","тебе","тобой"}: return "SELF"
    return None


@dataclass
class SpineEvent:
    event_id: str
    actor: str
    channel: str
    payload: str
    internal_step: int
    wall_time: float
    external_order: int = 0
    status: str = "OBSERVED"

@dataclass
class InterpretationCandidate:
    candidate_id: str
    event_id: str
    source: str
    speech_act: str
    subject_role: Optional[str] = None
    relation: Optional[str] = None
    object_value: Optional[str] = None
    temporal_scope: str = "PRESENT"
    epistemic_mode: str = "ASSERTED"
    quoted_depth: int = 0
    confidence: float = 0.5
    status: str = "CANDIDATE"
    note: Optional[str] = None

    def can_request_commit(self) -> bool:
        """Only eligibility to REQUEST COMMIT; never COMMIT authority itself."""
        if self.quoted_depth>0: return False
        if self.epistemic_mode in {"QUESTION","POSSIBLE","HYPOTHETICAL"}: return False
        if self.temporal_scope != "PRESENT" and self.relation in {"NAME","LOCATION","STATE"}: return False
        return self.speech_act in {"ASSERTION","CORRECTION","TEACHING"}


class SemanticSpine:
    """Non-authoritative event/interpretation spine.

    It records what happened and what EVAL considered. It cannot mutate truth.
    """
    def __init__(self):
        self.version=SPINE_VERSION
        self.events: Dict[str, Dict[str,Any]]={}
        self.interpretations: Dict[str, List[Dict[str,Any]]]={}
        self.transactions: List[Dict[str,Any]]=[]
        self.last_external_event_id: Optional[str]=None

    def record_event(self, *, event_id:str, actor:str, channel:str, payload:str,
                     internal_step:int, wall_time:Optional[float]=None, external_order:int=0,
                     status:str="OBSERVED") -> Dict[str,Any]:
        ev=SpineEvent(event_id=str(event_id),actor=str(actor),channel=str(channel),payload=str(payload),
                      internal_step=int(internal_step),wall_time=float(time.time() if wall_time is None else wall_time),
                      external_order=int(external_order),status=str(status))
        row=asdict(ev);self.events[ev.event_id]=row
        if actor=="OTHER": self.last_external_event_id=ev.event_id
        return row

    def add_candidate(self,event_id:str,*,source:str,speech_act:str,subject_role=None,relation=None,
                      object_value=None,temporal_scope="PRESENT",epistemic_mode="ASSERTED",
                      quoted_depth=0,confidence=.5,status="CANDIDATE",note=None):
        raw=f"{event_id}|{source}|{speech_act}|{subject_role}|{relation}|{object_value}|{len(self.interpretations.get(event_id,[]))}".encode()
        cid="ic:"+hashlib.blake2s(raw,digest_size=8).hexdigest()
        c=InterpretationCandidate(cid,str(event_id),str(source),str(speech_act),subject_role,relation,
                                  None if object_value is None else str(object_value),str(temporal_scope),
                                  str(epistemic_mode),int(quoted_depth),float(confidence),str(status),note)
        self.interpretations.setdefault(str(event_id),[]).append(asdict(c))
        return asdict(c)

    def mark_selected(self,event_id:str,candidate_id:str,*,operation=None):
        for c in self.interpretations.get(str(event_id),[]):
            if c.get("candidate_id")==candidate_id:
                c["status"]="SELECTED";c["selected_operation"]=operation;return c
        return None

    def record_transaction(self, *, tx_kind:str, source_event_id:str, status:str, details:Dict[str,Any]):
        raw=f"{tx_kind}|{source_event_id}|{len(self.transactions)}".encode()
        row={"transaction_id":"tx:"+hashlib.blake2s(raw,digest_size=8).hexdigest(),
             "kind":str(tx_kind),"source_event_id":str(source_event_id),"status":str(status),
             "details":dict(details),"wall_time":time.time()}
        self.transactions.append(row);return row

    def analyze_surface(self,event_id:str,text:str):
        """Cheap structural EVAL candidates. No truth mutation and no final parse authority."""
        txt=str(text).strip();out=[];ts=temporal_scope(txt);emode=epistemic_mode(txt)
        qs=quoted_fragments(txt)
        for q in qs:
            out.append(self.add_candidate(event_id,source="QUOTE_LAYER",speech_act="QUOTED_SPEECH",
                                          temporal_scope=temporal_scope(q["text"]),epistemic_mode=epistemic_mode(q["text"]),
                                          quoted_depth=q["depth"],confidence=.99,note=q["text"]))
        # Structural quarantine: the outer event must not acquire a claim
        # extracted from text nested inside quotation marks. This is a single
        # generic boundary rule, NOT a special case for any name or phrase.
        outer=outside_quotes(txt)
        # NAME surface, including past/hypothetical interpretations.
        m=re.search(r'\b(меня|тебя)\s+(?:зовут|звали)\s+([^?.!,;]+)',outer,flags=re.IGNORECASE)
        if m:
            role=social_role(m.group(1));obj=m.group(2).strip()
            out.append(self.add_candidate(event_id,source="SPINE_SOCIAL",speech_act="ASSERTION",
                                          subject_role=role,relation="NAME",object_value=obj,temporal_scope=ts,
                                          epistemic_mode=emode,confidence=.86))
        # Bare zero-copula naming: «Ты Синька» / «Я Руслан».
        m=re.match(r'^\s*(я|ты)\s+([А-ЯЁA-Z][\w-]*(?:\s+[А-ЯЁA-Z][\w-]*)?)\s*[.!)]*$',txt)
        if m:
            out.append(self.add_candidate(event_id,source="SPINE_SOCIAL",speech_act="ASSERTION",
                                          subject_role=social_role(m.group(1)),relation="NAME",object_value=m.group(2),
                                          temporal_scope=ts,epistemic_mode=emode,confidence=.8))
        # Contrast correction does not carry a new value; it points to a previous claim.
        m=re.match(r'^\s*не\s+(меня|тебя)\s*,?\s*а\s+(меня|тебя)\s*[.!?]*$',txt,flags=re.IGNORECASE)
        if m and social_role(m.group(1))!=social_role(m.group(2)):
            out.append(self.add_candidate(event_id,source="SPINE_CORRECTION",speech_act="CORRECTION",
                                          subject_role=social_role(m.group(2)),relation="NAME",object_value=None,
                                          temporal_scope="PRESENT",epistemic_mode="ASSERTED",confidence=.9,
                                          note=f"FROM:{social_role(m.group(1))}"))
        return out

    def presence_snapshot(self,*,now:Optional[float]=None,internal_step:int=0,open_inquiries=None,pending_acts=None):
        now=float(time.time() if now is None else now)
        last=self.events.get(self.last_external_event_id or "")
        return {"version":self.version,"internal_step":int(internal_step),
                "external_now":now,"last_external_event_id":self.last_external_event_id,
                "seconds_since_external_event":None if not last else max(0.0,now-float(last.get("wall_time",now))),
                "interaction_actor":None if not last else last.get("actor"),
                "open_inquiries":list(open_inquiries or []),"pending_acts":list(pending_acts or [])}

    def to_dict(self):
        return {"version":self.version,"events":list(self.events.values()),"interpretations":self.interpretations,
                "transactions":self.transactions,"last_external_event_id":self.last_external_event_id}

    @classmethod
    def from_dict(cls,d):
        s=cls();d=d or {}
        for ev in d.get("events",[]):
            if isinstance(ev,dict) and ev.get("event_id"):s.events[str(ev["event_id"])]=dict(ev)
        s.interpretations={str(k):[dict(x) for x in v if isinstance(x,dict)] for k,v in (d.get("interpretations") or {}).items() if isinstance(v,list)}
        s.transactions=[dict(x) for x in d.get("transactions",[]) if isinstance(x,dict)]
        s.last_external_event_id=d.get("last_external_event_id")
        return s