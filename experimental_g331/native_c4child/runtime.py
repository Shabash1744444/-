from __future__ import annotations
import json
from dataclasses import dataclass,asdict
from collections import deque
from typing import Optional
import hashlib,time,re
from .dialogue import C4ChildDialogue
from .graph import norm
from .gaps import KnowledgeGapRegistry,OPEN,ASKED,RESOLVED
from .agenda import build_agenda, agenda_dicts
from .learning import LearningSessionRegistry,SUCCESS as LEARNING_SUCCESS
from .competency import CompetencyRegistry,MASTERED,OPEN as COMP_OPEN
from .bootstrap import BootstrapTeacher
from .rule_induction import RuleInductionOrgan
from .epistemic import EpistemicAdmissionOrgan
from .learned_constraints import EmpiricalConstraintLearner
from .discourse_ru import RussianDiscourseBridgeV1
from .guided_reading import GuidedReaderRU
from .sensory import NurseryState
from .spatial3d import SpatialEffectLearner,ContactEffortLearner,SupportFallLearner
from .lexical_grounding import SoundSymbolBridge
from .composition import SemanticComposition
from .semantic_spine import SemanticSpine, quoted_fragments, outside_quotes, temporal_scope, epistemic_mode, social_role
from .perspective_composition import chain_summary, perspective_entity_inquiry
from .metacognitive_probe import inspect_question
from .discourse_bridge import resolve_disposition
from .episodic_memory import index_event, is_query_batch, is_memory_query, is_inquiry_query, answer_batch, answer_memory_query
from .inquiry_link import evaluate_inquiry_link
from . import structured_cognition

@dataclass
class OutboundEvent:
    event_id:str
    kind:str             # REPLY|ASK|PUBLISH|STATUS
    text:str
    reason:str
    created_step:int
    urgency:float=0.5
    cause_id:Optional[str]=None
    requires_user:bool=False

class C4LivingRuntime:
    """Stable app-facing organism interface.

    The app is not request/response-only. User messages are inbound events;
    cognition may later emit ASK/PUBLISH events into an outbox without a new
    user message. The shell delivers events but never invents them.
    """
    def __init__(self,dialogue:Optional[C4ChildDialogue]=None,initiative_cooldown:int=8,strict_world_admission:bool=False,hardened_truth_gate:bool=False):
        self.dialogue=dialogue or C4ChildDialogue()
        self.step=0
        self.outbox=deque()
        self.pending_questions=deque()  # (entity_id, reason, cause_id)
        self.pending_conflicts=deque()  # (subject_id, target_id, cause_id)
        self.asked=set()
        self.asked_conflicts=set()
        self.initiative_cooldown=max(1,int(initiative_cooldown))
        self.last_initiative_step=-10**9
        self.last_user_step=0
        self._seq=0
        self.gaps=KnowledgeGapRegistry()
        self.learning=LearningSessionRegistry()
        self.competencies=CompetencyRegistry()
        self.rule_induction=RuleInductionOrgan()
        self.epistemic=EpistemicAdmissionOrgan(strict_world=strict_world_admission)
        # G324-P3: experiments only; never writes WORLD knowledge.
        self.causal_studies={}
        self.discourse=RussianDiscourseBridgeV1()
        # G305: durable post-codec sensory state. Vectors are weak perceptual evidence, never graph truth by themselves.
        self.nursery=NurseryState()
        # G306: SIMULATION-scoped action-effect learner; verified receipts only.
        self.spatial_effects=SpatialEffectLearner()
        # G307: phoneme/glyph alignment is association, never sensory identity.
        self.sound_symbol=SoundSymbolBridge()
        # G308: verified contact/collision and effort->displacement response; no hidden mass labels.
        self.contact_physics=ContactEffortLearner()
        # G309: release/free-motion/contact regularities from verified sandbox transitions.
        self.support_physics=SupportFallLearner()
        self.dialogue_history=deque(maxlen=64)
        # G316: one continuous life-line. Transport events, cognition and public
        # acts coexist but are not the same event. Dialogue history remains a
        # compatibility/public-discourse view over this richer line.
        self.life_events=deque(maxlen=512)
        self.inbound_events=deque()
        self.external_seq=0
        # G316: semantic anchors over the life-line. These records affect only
        # contextual AVAIL/VALUE/EVAL; they are never COMMIT evidence.
        self.semantic_context=deque(maxlen=96)
        # G320: non-truth composition across representational scales.
        self.composition=SemanticComposition()
        # G322: non-authoritative semantic/presence spine. Events and EVAL
        # candidates live here; the spine never grants COMMIT authority.
        self.semantic_spine=SemanticSpine()
        # G328: immutable-source transcript episode index. No admission authority.
        self.episode_index={}
        self.last_inquiry_evaluation=None
        # Observational telemetry is opt-in, non-persistent, and distinct from
        # cognition. The host receives actual event records, never a fake chain.
        self._trace_mode='OFF'
        self._trace_scope='CONTINUOUS'
        self._trace_outbox=deque(maxlen=1024)
        self._trace_included=[]
        # G318: cognition may formulate a public act without sending it yet.
        # READY/BACKGROUND/PUBLISHED are communication STATUS, never truth status.
        self.pending_public_acts=deque()
        # G310: internal causal order (step) and external wall time coexist.
        # A question is an event in the life-line, never a transport lock.
        self.awaiting_response=False          # compatibility/status only; DRIVE never delegates to it
        self.human_active=False
        self._asked_since_user=False          # compatibility telemetry; not an arbitration gate
        self.inquiries={}                     # event_id -> OPEN/BACKGROUND/RESOLVED inquiry record
        self.inquiry_order=deque(maxlen=128)
        self.max_foreground_inquiries=3       # presentation budget, not epistemic law
        self.dialogue.reasoner.rule_induction=self.rule_induction
        # G331 is an input organ on this SAME runtime and C4Graph; no second memory.
        self.cognitive_goals={}
        self.cognitive_demonstrations=[]
        self.cognitive_actions={}
        self._sim_receipt_adapter=None  # binding is host-only, not user message JSON.
        if hardened_truth_gate:self.enable_hardened_truth()

    def enable_hardened_truth(self):
        """Experimental fail-closed gate for ALL graph commit/replace/forget APIs."""
        self.dialogue.g.set_constitutional_mode('STRICT')
        self.dialogue.g.hardened_gate=True
        self.epistemic.strict_world=True
        return True

    def _event(self,kind,text,reason,urgency=0.5,cause_id=None,requires_user=False):
        self._seq+=1
        raw=f"{self.step}|{self._seq}|{kind}|{text}|{reason}".encode('utf-8')
        eid="evt:"+hashlib.blake2s(raw,digest_size=8).hexdigest()
        ev=OutboundEvent(eid,kind,text,reason,self.step,float(urgency),cause_id,bool(requires_user))
        self.outbox.append(ev)
        if kind=="ASK":
            self.awaiting_response=True  # observable status only; tick() does not use it as DRIVE authority
            rec={"event_id":eid,"text":str(text),"status":"OPEN","created_step":int(self.step),
                 "created_wall_time":time.time(),"cause_id":cause_id,"reason":str(reason),
                 "requires_user":bool(requires_user)}
            self.inquiries[eid]=rec;self.inquiry_order.append(eid)
            self._record_turn("C4",text,kind=kind,reason=reason,requires_user=bool(requires_user),event_id=eid)
        return ev

    def _record_life_event(self,actor,kind,*,text=None,status=None,event_id=None,source_event_id=None,extra=None):
        if event_id is None:
            self._seq+=1
            raw=f"{self.step}|{self._seq}|{actor}|{kind}|{text or ''}".encode('utf-8')
            event_id="life:"+hashlib.blake2s(raw,digest_size=8).hexdigest()
        row={"event_id":str(event_id),"actor":str(actor),"kind":str(kind),"step":int(self.step),
             "wall_time":time.time(),"external_order":int(getattr(self,'external_seq',0))}
        if text is not None:row["text"]=str(text)
        if status is not None:row["status"]=str(status)
        if source_event_id is not None:row["source_event_id"]=str(source_event_id)
        if extra:row.update(dict(extra))
        self.life_events.append(row)
        if getattr(self,'_trace_mode','OFF')!='OFF':
            # These are materialized runtime events, not generated explanations.
            channel='COMMIT' if ('COMMIT' in kind or 'TRANSACTION' in kind) else (
                'DRIVE' if ('DRIVE' in kind or 'PUBLIC' in kind) else (
                'EVAL' if ('EVAL' in kind or 'INTERPRETATION' in kind) else (
                'MEDIATE' if ('RECEIPT' in kind or 'SENSORY' in kind) else 'EVENT')))
            if self._trace_mode!='EVENTS' or channel in {'COMMIT','DRIVE','MEDIATE'}:
                event={'type':'TRACE_'+channel,'kind':'TRACE_'+channel,'schema':'C4_COGNITIVE_TRACE_V1',
                       'eventId':row['event_id'],'step':row['step'],'owner':channel,
                       'sourceEventId':row.get('source_event_id'), 'record':dict(row),
                       'epistemic':'INTERNAL_PROCESS_RECORD_NOT_WORLD_EVIDENCE'}
                self._trace_outbox.append(event)
        return row

    def _record_turn(self,speaker,text,*,kind=None,reason=None,requires_user=False,event_id=None,parsed=None,semantic_eids=None):
        row={"speaker":str(speaker),"text":str(text),"step":int(self.step),"wall_time":time.time()}
        if kind is not None:row["kind"]=str(kind)
        if reason is not None:row["reason"]=str(reason)
        if requires_user:row["requires_user"]=True
        if event_id is not None:row["event_id"]=str(event_id)
        if parsed is not None:row["parsed"]=parsed
        if semantic_eids:row["semantic_eids"]=list(dict.fromkeys(semantic_eids))
        self.dialogue_history.append(row)
        # Published C4 speech is a witnessed utterance, not a world receipt.
        # Store it with speaker provenance so an old ASK can be retrieved as ASK.
        if str(speaker)=='C4' and event_id and kind in {'ASK','ASK_EMBEDDED','REPLY'}:
            entry=index_event(str(event_id),self.external_seq,str(text))
            entry['source_kind']='C4_ASK' if kind in {'ASK','ASK_EMBEDDED'} else 'C4_REPLY'
            entry['scope']='SPOKEN_INQUIRY' if kind in {'ASK','ASK_EMBEDDED'} else 'C4_PUBLIC_REPLY'
            self.episode_index[str(event_id)]=entry
        extra={}
        if reason is not None:extra["reason"]=reason
        if semantic_eids:extra["semantic_eids"]=list(dict.fromkeys(semantic_eids))
        self._record_life_event(speaker,kind or "TURN",text=text,status="RECORDED",event_id=event_id,extra=extra or None)
        return row

    def _remember_context(self,eid,*,role="MENTION",source_event_id=None):
        """Remember a known semantic anchor without creating knowledge.

        Context changes AVAIL/VALUE for retrieval only. It carries no COMMIT basis.
        """
        if not eid or eid not in self.dialogue.g.entities:return
        if eid in {self.dialogue.user_eid,self.dialogue.self_eid}:return
        self.semantic_context.append({"eid":eid,"step":int(self.step),"role":str(role),
                                      "source_event_id":source_event_id,"wall_time":time.time()})

    def activate_composition(self,unit_id,*,role="COMPOSITION_CONTEXT"):
        """Make semantic referents from a phrase/episode/story contextually AVAIL.

        Top-down composition affects retrieval context only; it never creates or
        commits semantic facts.
        """
        refs=[]
        for eid in self.composition.semantic_refs(unit_id):
            if eid in self.dialogue.g.entities:
                self._remember_context(eid,role=role,source_event_id=unit_id);refs.append(eid)
        self.dialogue.set_context_entities(self._recent_context_eids())
        self._record_life_event('C4','COMPOSITION_ACTIVATION',status='AVAIL',extra={'unit_id':unit_id,'semantic_eids':refs})
        return refs

    def _recent_context_eids(self,limit=12):
        out=[]
        for row in reversed(self.semantic_context):
            eid=row.get("eid") if isinstance(row,dict) else None
            label=norm(self.dialogue.g.label(eid)) if eid in self.dialogue.g.entities else ""
            if label in {"я","ты","мы","вы","он","она","оно","они","меня","тебя","его","ее","её","их","этот","эта","это"}:continue
            if eid in self.dialogue.g.entities and eid not in out:
                out.append(eid)
                if len(out)>=int(limit):break
        return list(reversed(out))

    def _known_mentions(self,text,parsed=None,limit=8):
        """Resolve only EXISTING concepts mentioned by a surface. Never creates entities."""
        g=self.dialogue.g;ret=self.dialogue.retriever;out=[]
        deictic={"я","ты","мы","вы","он","она","оно","они","меня","тебя","мне","тебе","его","ее","её","ей","ему","их","нам","вам","этот","эта","это","эти","него","нее","неё","ней","них"}
        def add_label(label):
            if not label:return
            raw=str(label).strip()
            if norm(raw) in deictic:return
            eid=g.resolve(raw) or self.dialogue.morphology.resolve(raw) or ret.lemma(raw)
            if eid in g.entities and eid not in out and eid not in {self.dialogue.user_eid,self.dialogue.self_eid}:out.append(eid)
        if parsed is not None:
            add_label(getattr(parsed,"subject",None))
            rel=getattr(parsed,"relation",None)
            obj=getattr(parsed,"object",None)
            if obj and rel and g.relation_spec(rel).object_mode in {"entity","either"}:add_label(obj)
        # Longest-first phrase scan catches known multiword concepts while remaining read-only.
        words=re.findall(r"[0-9A-Za-zА-Яа-яЁё_-]+",str(text))
        for n in range(min(5,len(words)),0,-1):
            for i in range(0,len(words)-n+1):
                add_label(" ".join(words[i:i+n]))
                if len(out)>=int(limit):return out
        return out

    def _receipt_entities(self,fact_ids,limit=8):
        out=[];g=self.dialogue.g
        for fid in fact_ids or ():
            f=g.facts.get(fid)
            if f is None:continue
            for eid in (f.subject, f.object_value if f.object_kind=="entity" else None):
                if eid in g.entities and eid not in out and eid not in {self.dialogue.user_eid,self.dialogue.self_eid}:out.append(eid)
                if len(out)>=int(limit):return out
        return out

    def _track_embedded_inquiry(self,text,reason,cause_id=None,requires_user=True):
        """Record a question spoken inside a larger reply as its own life-line event.

        Presentation may remain one chat bubble, but cognition receives a distinct
        event/status object.  MESSAGE PACKAGING != COGNITIVE EVENT BOUNDARY.
        """
        self._seq+=1
        raw=f"{self.step}|{self._seq}|ASK_EMBEDDED|{text}|{reason}".encode('utf-8')
        eid="evt:"+hashlib.blake2s(raw,digest_size=8).hexdigest()
        rec={"event_id":eid,"text":str(text),"status":"OPEN","created_step":int(self.step),
             "created_wall_time":time.time(),"cause_id":cause_id,"reason":str(reason),
             "requires_user":bool(requires_user),"embedded":True}
        self.inquiries[eid]=rec;self.inquiry_order.append(eid)
        self._record_turn("C4",text,kind="ASK_EMBEDDED",reason=reason,requires_user=requires_user,event_id=eid)
        return rec

    def register_gap(self,kind,subject,*,relation=None,object_value=None,reason='UNKNOWN',priority=0.5,cause_id=None,schedule=False):
        g=self.gaps.register(kind,subject,relation=relation,object_value=object_value,reason=reason,step=self.step,priority=priority,cause_id=cause_id)
        if schedule:
            if kind=='DEFINITION':
                tup=(subject,reason,cause_id)
                if tup not in self.pending_questions:self.pending_questions.append(tup)
            elif kind=='CONTRADICTION' and object_value is not None:
                tup=(subject,object_value,cause_id)
                if tup not in self.pending_conflicts:self.pending_conflicts.append(tup)
        return g

    def _gid(self,x):
        """G267: a gap may name a surface the graph does not know yet ('surface:...'); re-resolve it, never create it."""
        if isinstance(x,str) and x.startswith('surface:'):
            return self.dialogue._rid(x[len('surface:'):]) or x
        return x

    def _glabel(self,x):
        if x is None:return None
        if isinstance(x,str) and x.startswith('surface:'):return x[len('surface:'):]
        return self.dialogue.g.label(x)

    def _surface_id(self,label):
        return self.dialogue._rid(label) or ('surface:'+str(label or '').strip())

    _GRAMMATICAL_CLASS_LABELS={'существительное','глагол','прилагательное','наречие','местоимение','слово','часть речи'}

    def _semantic_definition_known(self,eid):
        if eid not in self.dialogue.g.entities:return False
        rows=self.dialogue.g.get_all(eid,'IS_A',viewer=self.dialogue.principal,principal=self.dialogue.principal,polarity='POS')
        for f in rows:
            if f.object_kind!='entity':continue
            if norm(self.dialogue.g.label(f.object_value)) not in self._GRAMMATICAL_CLASS_LABELS:
                return True
        foundational=self.dialogue.g.get(eid,'FOUNDATIONAL',viewer=self.dialogue.principal,principal=self.dialogue.principal)
        return bool(foundational and foundational.object_value=='true')

    # ------------------------------------------------------------------ G305: sensory bridge
    def observe_sensory(self,bundle,*,origin="SENSOR",allow_create=True):
        """Observe one synchronized post-codec multimodal bundle.

        A vector match is only a perceptual candidate. It never creates graph facts,
        and an unresolved single modality cannot create a persistent concept.
        """
        before=(len(self.nursery.grounder.concepts),len(self.nursery.grounder.audit))
        row=self.nursery.grounder.observe_bundle(bundle,origin=origin,allow_create=allow_create)
        cid=row.get("concept_id")
        row=dict(row)
        row["entity_id"]=None if cid is None else self.nursery.grounder.concepts[cid].named_entity
        # G317: sensory processing joins the same continuous life-line as dialogue.
        # Only modality names / resolved identity are journaled; raw vectors stay in the
        # sensory organ. A recognized entity changes contextual AVAIL/VALUE only.
        # It is never a COMMIT basis merely because a vector matched.
        sev=self._record_life_event(
            "SENSOR","SENSORY_OBSERVATION",
            status=("UNRESOLVED" if cid is None else ("GROUNDED" if row.get("entity_id") else "PERCEPTUAL_CANDIDATE")),
            extra={
                "modalities":sorted(str(x).upper() for x in bundle),
                "origin":str(origin),
                "sensory_concept_id":cid,
                "entity_id":row.get("entity_id"),
                "created":bool(row.get("created")),
                "score":float(row.get("score",-1.0)),
            })
        row["life_event_id"]=sev["event_id"]
        if row.get("entity_id") in self.dialogue.g.entities:
            self._remember_context(row["entity_id"],role="SENSORY_GROUNDED",source_event_id=sev["event_id"])
            self.dialogue.set_context_entities(self._recent_context_eids())
        after=(len(self.nursery.grounder.concepts),len(self.nursery.grounder.audit))
        self._autosave_tick(mutated=after!=before)
        return row

    def bind_sensory_name(self,concept_id,label,*,kind="concept",origin="USER_SAID",source_ref=None):
        """Explicitly bind a stable sensory concept to a graph entity.

        Naming is a teaching act, not similarity inference. If the label is new,
        entity identity is created only here (never by raw sensor observation).
        """
        gd=self.nursery.grounder
        if concept_id not in gd.concepts:raise KeyError(concept_id)
        g=self.dialogue.g
        eid=g.resolve(str(label),kind=kind) or g.entity(str(label),kind=kind)
        gd.name(concept_id,eid,origin=origin,source_ref=source_ref)
        # Naming binds a sensory representation to an already explicit semantic
        # identity; it does not turn the sensory vectors into graph truth.
        ev=self._record_life_event(
            "OTHER" if str(origin).upper() in {"USER_SAID","CREATOR_REPORTED","TEACHER"} else "C4",
            "SENSORY_NAMING",status="BOUND",
            extra={"sensory_concept_id":concept_id,"entity_id":eid,"label":g.label(eid),
                   "origin":str(origin),"source_ref":source_ref})
        self._remember_context(eid,role="SENSORY_NAMED",source_event_id=ev["event_id"])
        self.dialogue.set_context_entities(self._recent_context_eids())
        self._autosave_tick(mutated=True)
        return {"concept_id":concept_id,"entity_id":eid,"label":g.label(eid),"life_event_id":ev["event_id"]}

    def sensory_resolve(self,modality,vec):
        """Return a named entity only after sensory identity has explicit grounding."""
        eid,score,cid=self.nursery.grounder.entity_for(modality,vec)
        return {"entity_id":eid,"concept_id":cid,"score":float(score)}

    # ------------------------------------------------------------------ G306: embodied 3D learning bridge
    def learn_spatial_transition(self,receipt,transition):
        """Learn a SIMULATION-scoped motor/world effect from a verified sandbox receipt."""
        row=self.spatial_effects.observe(receipt,transition)
        self._autosave_tick(mutated=True)
        return self.spatial_effects.effect(receipt.action)

    def spatial_effect(self,action):
        return self.spatial_effects.effect(action)

    # ------------------------------------------------------------------ G308: contact / collision / effort-response bridge
    def learn_contact_transition(self,receipt,transition):
        row=self.contact_physics.observe(receipt,transition)
        self._autosave_tick(mutated=True)
        return self.contact_physics.interaction_effect(receipt.action)

    def contact_effect(self,action):
        return self.contact_physics.interaction_effect(action)

    def physical_response_profile(self,target_id):
        return self.contact_physics.response_profile(target_id)

    def compare_physical_response(self,a,b):
        return self.contact_physics.compare_response(a,b)

    def predict_push_displacement(self,target_id,effort):
        return self.contact_physics.predict_displacement(target_id,effort)


    # ------------------------------------------------------------------ G309: support / release / fall dynamics bridge
    def learn_support_transition(self,receipt,transition):
        keys=self.support_physics.observe(receipt,transition)
        self._autosave_tick(mutated=True)
        return {k:self.support_physics.effect(k) for k in keys}

    def support_effect(self,condition):
        return self.support_physics.effect(condition)

    def predict_free_vertical_step(self,pre_vy,dt):
        return self.support_physics.predict_free_step(pre_vy,dt)

    # ------------------------------------------------------------------ G307: sound / glyph / word-form bridge
    def learn_sound_symbol(self,sound_concept_id,glyph_concept_id,*,provenance="USER_TEACHING"):
        if sound_concept_id==glyph_concept_id:raise ValueError("sound/glyph identity collapse forbidden")
        row=self.sound_symbol.observe(sound_concept_id,glyph_concept_id,provenance=provenance)
        self._autosave_tick(mutated=True)
        return {"sound_concept":row.sound_concept,"glyph_concept":row.glyph_concept,"support":row.support}

    def glyphs_for_sound(self,sound_concept_id):
        return self.sound_symbol.glyphs_for(sound_concept_id)

    def sounds_for_glyph(self,glyph_concept_id):
        return self.sound_symbol.sounds_for(glyph_concept_id)

    def observe_form_sequence(self,constituents):
        before=len(self.nursery.composer.chunks)
        chunk=self.nursery.composer.observe(constituents)
        self._autosave_tick(mutated=(len(self.nursery.composer.chunks)!=before or chunk is not None))
        return chunk

    def bind_sequence_name(self,chunk_id,label,*,kind="word"):
        c=self.nursery.composer.chunk_by_id(chunk_id)
        if c is None:raise KeyError(chunk_id)
        eid=self.dialogue.g.resolve(str(label),kind=kind) or self.dialogue.g.entity(str(label),kind=kind)
        self.nursery.composer.name(chunk_id,eid);self._autosave_tick(mutated=True)
        return {"chunk_id":chunk_id,"entity_id":eid,"label":self.dialogue.g.label(eid)}

    def resolve_form_sequence(self,constituents):
        cid=self.nursery.composer.recognize(constituents)
        return {"chunk_id":cid,"entity_id":None if cid is None else self.nursery.composer.entity_for_chunk(cid)}

    def guided_read(self,text:str,*,source_ref='guided',source_group=None,priority=0.72):
        """Read a short Russian passage conservatively as EXTERNAL_CORPUS.

        Only structures recognized by existing deterministic language organs are
        admitted. Unsupported sentences are returned as skipped, never guessed.
        """
        return asdict(GuidedReaderRU(self).read(text,source_ref=source_ref,source_group=source_group,priority=priority))

    def _gap_resolved_now(self,g):
        d=self.dialogue;graph=d.g
        if g.kind=='LEXICAL_TERM':
            raw=self._glabel(g.subject)
            eid=d.morphology.resolve(raw) or graph.resolve(raw,kind='concept')
            return bool(eid and self._semantic_definition_known(eid))
        if g.kind in {'DEFINITION','RELATION','CAUSAL_RELATION','CAUSE_OF','EFFECT_OF'} and (
                str(g.subject).startswith('surface:') or str(g.object_value or '').startswith('surface:')):
            sid,oid=self._gid(g.subject),self._gid(g.object_value)
            if str(sid).startswith('surface:') or str(oid or '').startswith('surface:'):return False
            from types import SimpleNamespace
            g=SimpleNamespace(kind=g.kind,subject=sid,object_value=oid,relation=g.relation,reason=getattr(g,'reason','UNKNOWN'))
        if g.kind=='DEFINITION':
            if g.reason=='GUIDED_READING':
                return self._semantic_definition_known(g.subject)
            defined=graph.get_all(g.subject,'IS_A',viewer=d.principal,principal=d.principal)
            foundational=graph.get(g.subject,'FOUNDATIONAL',viewer=d.principal,principal=d.principal)
            return bool(defined or (foundational and foundational.object_value=='true'))
        if g.kind=='RELATION':
            return graph.truth(g.subject,g.relation,g.object_value,object_kind='entity',viewer=d.principal,principal=d.principal)!='UNKNOWN'
        if g.kind=='COMPETENCY_RELATION':
            return graph.truth(g.subject,g.relation,g.object_value,object_kind='entity',viewer=d.principal,principal=d.principal)=='TRUE'
        if g.kind=='COMPETENCY_RELATION_TRUE':
            return graph.truth(g.subject,g.relation,g.object_value,object_kind='entity',viewer=d.principal,principal=d.principal)=='TRUE'
        if g.kind=='COMPETENCY_RELATION_FALSE':
            return graph.truth(g.subject,g.relation,g.object_value,object_kind='entity',viewer=d.principal,principal=d.principal)=='FALSE'
        if g.kind=='CAUSAL_RELATION':
            return d.reasoner.evaluate_causes(g.subject,g.object_value,principal=d.principal,viewer=d.principal).value!='UNKNOWN'
        if g.kind=='CAUSE_OF':
            return bool(d.reasoner.direct_causes_of(g.subject,principal=d.principal,viewer=d.principal))
        if g.kind=='EFFECT_OF':
            return bool(d.reasoner.direct_effects_of(g.subject,principal=d.principal,viewer=d.principal))
        if g.kind=='CONTRADICTION':
            return d.reasoner.evaluate_is_a(g.subject,g.object_value,principal=d.principal,viewer=d.principal).value!='CONFLICT'
        if g.kind=='LANGUAGE_RELATION':
            eid=graph.resolve(g.subject) or d.morphology.resolve(g.subject)
            return bool(eid and graph.get(eid,'QUERY_RELATION',viewer=d.principal,principal=d.principal))
        if g.kind=='RULE_EXAMPLE':
            if g.subject not in self.rule_induction.studies:return True
            st=self.rule_induction.study_status(g.subject)
            return st.get('next_need')!=g.object_value
        if g.kind=='EPISTEMIC_VALIDATION':
            c=self.epistemic.candidates.get(g.object_value)
            return c is None or c.status not in {'NEEDS_CHALLENGE','NEEDS_REVALIDATION'}
        return False

    def refresh_gaps(self):
        self.rule_induction.refresh_supports(self.dialogue.g,principal=self.dialogue.principal,viewer=self.dialogue.principal)
        self.sync_rule_studies()
        for g in self.gaps.open():
            if self._gap_resolved_now(g):self.gaps.resolve(g.gap_id)
        self._recheck_learning_sessions()

    def _recheck_learning_sessions(self):
        for sess in self.learning.sessions.values():
            if sess.status==LEARNING_SUCCESS:continue
            gap=self.gaps.gaps.get(sess.gap_id)
            resolved=bool(gap and gap.status==RESOLVED)
            self.learning.evaluate(sess.session_id,step=self.step,resolved=resolved)

    def begin_learning_session(self,gap_id):
        if gap_id not in self.gaps.gaps:raise KeyError(gap_id)
        return asdict(self.learning.begin(gap_id,self.step))

    def learning_session(self,session_id):
        s=self.learning.sessions.get(session_id);return asdict(s) if s else None

    def teach_event(self,event,learning_session_id=None):
        # A teacher event is evidence input; whether it resolves an inquiry is decided
        # by gap/semantic state below, not by arrival alone.
        before=len(self.dialogue.g.facts)
        m=BootstrapTeacher(self.dialogue.g,principal=self.dialogue.principal).ingest([event])
        self.refresh_gaps();self.sync_competencies()
        # A structured teacher answer can resolve the same definition that tick()
        # exposed through dialogue.pending_ask. Do not persist a stale conversational
        # question after the graph gap is already resolved.
        pa=getattr(self.dialogue,'pending_ask',None)
        if pa and pa.get('eid'):
            gid=self.gaps.make_id('DEFINITION',pa['eid'],'IS_A',None)
            gap=self.gaps.gaps.get(gid)
            if (gap is not None and gap.status==RESOLVED) or self._semantic_definition_known(pa['eid']):
                self.dialogue.pending_ask=None
        if learning_session_id is not None:
            self.learning.note_lesson(learning_session_id,step=self.step,admitted=m.admitted,dedup=m.dedup,rejected=m.rejected)
            self._recheck_learning_sessions()
        self._autosave_tick(len(self.dialogue.g.facts)!=before)
        return {'events':m.events,'admitted':m.admitted,'dedup':m.dedup,'rejected':m.rejected,'mutated':len(self.dialogue.g.facts)!=before,'learning_session':self.learning_session(learning_session_id) if learning_session_id else None}

    def define_competency(self,label,requirements):
        rows=[]
        for r in requirements:
            sid=r.get('subject') if r.get('subject') in self.dialogue.g.entities else self.dialogue._eid(r['subject'])
            oid=r.get('object_value') if r.get('object_value') in self.dialogue.g.entities else self.dialogue._eid(r['object_value'])
            rows.append({'kind':r.get('kind','RELATION'),'subject':sid,'relation':r['relation'],'object_value':oid,'priority':r.get('priority',0.8),'expected':r.get('expected','TRUE')})
        c=self.competencies.create(label,rows);self.sync_competencies();return c.competency_id

    def sync_competencies(self):
        d=self.dialogue
        for c in self.competencies.contracts.values():
            all_met=True
            for r in c.requirements:
                truth=d.reasoner.evaluate_relation(r.subject,r.relation,r.object_value,object_kind='entity',viewer=d.principal,principal=d.principal).value
                met=(truth==r.expected)
                gkind='COMPETENCY_RELATION_TRUE' if r.expected=='TRUE' else 'COMPETENCY_RELATION_FALSE'
                gid=self.gaps.make_id(gkind,r.subject,r.relation,r.object_value)
                if met:
                    if gid in self.gaps.gaps:self.gaps.resolve(gid)
                else:
                    all_met=False
                    self.gaps.ensure(gkind,r.subject,relation=r.relation,object_value=r.object_value,reason='COMPETENCY_REQUIREMENT',step=self.step,priority=r.priority,cause_id=c.competency_id)
            c.status=MASTERED if all_met else COMP_OPEN
        return {cid:c.status for cid,c in self.competencies.contracts.items()}


    def _rule_study_gap(self,study_id,need):
        st=self.rule_induction.studies[study_id]
        return self.gaps.ensure('RULE_EXAMPLE',study_id,relation=st.target_relation,object_value=need,reason='RULE_STUDY_NEED',step=self.step,priority=0.82,cause_id=study_id)

    def sync_rule_studies(self):
        active={}
        for sid,st in self.rule_induction.studies.items():
            status=self.rule_induction.study_status(sid)
            need=status.get('next_need')
            for gap in self.gaps.gaps.values():
                if gap.kind=='RULE_EXAMPLE' and sid in gap.cause_ids and (need is None or gap.object_value!=need):
                    self.gaps.resolve(gap.gap_id)
            if need is not None:
                g=self._rule_study_gap(sid,need);active[sid]=g.gap_id
        return active

    def begin_rule_study(self,relation,object_value,*,object_kind='literal',polarity='POS',seed_from_graph=True):
        st=self.rule_induction.begin_study(relation,object_value,object_kind=object_kind,polarity=polarity)
        if seed_from_graph:self.rule_induction.seed_study_from_graph(self.dialogue.g,st.study_id,principal=self.dialogue.principal,viewer=self.dialogue.principal)
        self.sync_rule_studies()
        return self.rule_induction.study_status(st.study_id)

    def rule_study_status(self,study_id):
        return self.rule_induction.study_status(study_id)

    def teach_rule_example(self,study_id,entity,*,expected,split,source_group,source_class='HUMAN'):
        self.awaiting_response=False
        eid=entity if entity in self.dialogue.g.entities else self.dialogue.g.resolve(entity)
        if eid is None:raise KeyError(entity)
        before_need=self.rule_induction.study_status(study_id).get('next_need')
        out=self.rule_induction.add_study_example(self.dialogue.g,study_id,eid,expected=bool(expected),split=split,source_group=source_group,source_class=source_class,principal=self.dialogue.principal,viewer=self.dialogue.principal)
        self.sync_rule_studies()
        after_need=self.rule_induction.study_status(study_id).get('next_need')
        # If the same evidence bucket still needs more examples, a real new example
        # is the event that re-opens the ASK. Ticks alone never do this.
        if after_need is not None and after_need==before_need:
            gid=self.gaps.make_id('RULE_EXAMPLE',study_id,self.rule_induction.studies[study_id].target_relation,after_need)
            gap=self.gaps.gaps.get(gid)
            if gap is not None and gap.status==ASKED:
                gap.status=OPEN;gap.last_step=self.step
        return out

    def begin_causal_study(self, study_id, features, *, frame='ROOT', epoch='E0', max_parents=3):
        """Experimental simulation-scoped association study (not world truth)."""
        if study_id in self.causal_studies:
            raise ValueError('study already registered')
        self.causal_studies[study_id]=EmpiricalConstraintLearner(features,
            scope='SIMULATION',frame=frame,epoch=epoch,max_parents=max_parents)
        return {'study_id':study_id,'scope':'SIMULATION','status':'CREATED'}

    def learn_simulated_constraint(self, study_id, inputs, outcome, *, root, receipt, frame=None, epoch=None):
        """A trusted simulator adapter must supply the receipt and dependency root.

        The method rejects missing receipts but cannot itself authenticate a caller.
        """
        study=self.causal_studies[study_id]
        status=study.observe(inputs,outcome,root=root,receipt=receipt,
            frame=frame or study.frame,epoch=epoch or study.epoch)
        if status in {'LEARNABLE','ROOT_CONFLICT_QUARANTINED'}:
            self._autosave_tick(mutated=True)
        return {'status':status,'study_id':study_id,'world_committed':False}

    def fit_causal_study(self, study_id):
        result=self.causal_studies[study_id].fit()
        self._autosave_tick(mutated=True)
        return result

    def predict_causal_study(self, study_id, inputs):
        return self.causal_studies[study_id].predict(inputs)

    def register_epistemic_source(self,source_id,source_family,source_class,source_lineage=None):
        return self.epistemic.register_source(source_id,source_family,source_class,source_lineage)

    def epistemic_source_identity(self,source_id):
        return self.epistemic.source_identity(source_id)

    def register_epistemic_evidence_origin(self,evidence_id,dependency_root):
        return self.epistemic.register_evidence_origin(evidence_id,dependency_root)

    def submit_epistemic_claim(self,subject,relation,object_value,*,object_kind='entity',polarity='POS',
                               source_id,source_family,source_class,source_lineage=None,evidence_id=None,dependency_root=None,phase='PROPOSAL',confidence=1.0):
        # Untrusted proposals must not create graph entities before admission.
        sid=subject if subject in self.dialogue.g.entities else str(subject)
        if object_kind=='entity':
            oval=object_value if object_value in self.dialogue.g.entities else str(object_value)
        else:oval=str(object_value)
        out=self.epistemic.submit(self.dialogue.g,sid,relation,oval,object_kind=object_kind,polarity=polarity,principal=self.dialogue.principal,
                                  source_id=source_id,source_family=source_family,source_class=source_class,source_lineage=source_lineage,evidence_id=evidence_id,dependency_root=dependency_root,phase=phase,confidence=confidence)
        cid=out.get('candidate_id')
        if cid and out.get('status') in {'NEEDS_CHALLENGE','NEEDS_REVALIDATION'}:
            reason='EPISTEMIC_REVALIDATION' if out.get('status')=='NEEDS_REVALIDATION' else 'EPISTEMIC_CHALLENGE'
            priority=0.93 if out.get('status')=='NEEDS_REVALIDATION' else 0.88
            self.gaps.ensure('EPISTEMIC_VALIDATION',sid,relation=str(relation).upper(),object_value=cid,reason=reason,step=self.step,priority=priority,cause_id=cid)
        elif cid and out.get('status') in {'ADMITTED','CONFLICT','QUARANTINED','REJECTED'}:
            gid=self.gaps.make_id('EPISTEMIC_VALIDATION',sid,str(relation).upper(),cid)
            if gid in self.gaps.gaps:self.gaps.resolve(gid)
        return out

    def epistemic_status(self,candidate_id):
        return self.epistemic.status(candidate_id)

    def _schedule_repeated_unknown(self,g,cause):
        # The immediate reply already says 'I do not know'. Autonomous follow-up is
        # reserved for repeated unresolved need, preventing one-shot query spam.
        if g.evidence_count<2:return
        marker=(g.gap_id,'GAP_FOLLOWUP',cause)
        # reuse pending_questions only for definition-style UI compatibility; other
        # gap kinds emit from tick directly.
        return marker

    def _split_user_surfaces(self,text:str):
        """Conservative speech-act segmentation for one transport message.

        Sentence punctuation always splits. A comma splits only when the right
        side is independently recognizable as a new speech act (contrastive
        copula, modal question, or first-person preference). This prevents a
        coordinated clause from becoming one opaque pseudo-concept.
        """
        text=str(text)
        # Segment only *outside* nested quote delimiters. Transport punctuation in
        # attributed speech is not a new independent user speech act.
        coarse=[];start=0;stack=[];pairs={'«':'»','“':'”','"':'"'}
        i=0
        while i<len(text):
            c=text[i]
            if stack and c==stack[-1]:stack.pop()
            elif c in pairs and (not stack or c!='"'):
                stack.append(pairs[c])
            if not stack and (c=='\n' or (c in '.!?' and (i+1==len(text) or text[i+1].isspace()))):
                end=i+1
                while end<len(text) and text[end] in '.!?':end+=1
                seg=text[start:end].strip()
                if seg:coarse.append(seg)
                start=end;i=end;continue
            i+=1
        tail=text[start:].strip()
        if tail:coarse.append(tail)
        out=[]
        for seg in coarse:
            # Chat emoticon tails are surface punctuation, not lexical identity.
            seg=re.sub(r'(?<=[\wА-Яа-яЁё])[)）]+(?=\s*$)', '', seg).strip()
            # Contrastive independent copula: «A это X, а B это Y».
            parts=re.split(r',\s*а\s+(?=[^,]{1,100}\s+(?:это|—|-)\s+)',seg,maxsplit=1,flags=re.IGNORECASE)
            if len(parts)==2:
                out.extend(x.strip() for x in parts if x.strip());continue
            # A recognized statement followed by an independent modal/question act.
            m=re.match(r'^(.+?),\s*((?:можно|можешь|можно\s+ли)\b.+)$',seg,flags=re.IGNORECASE)
            if m:
                left,right=m.group(1).strip(),m.group(2).strip()
                lit=self.dialogue.semantic_intent(left)
                if lit.kind!='UNKNOWN':out.extend([left,right]);continue
            # A naming/declaration followed by a first-person preference is also two acts.
            m=re.match(r'^(.+?),\s*(мне\s+нравится\b.+)$',seg,flags=re.IGNORECASE)
            if m:
                out.extend([m.group(1).strip(),m.group(2).strip()]);continue
            out.append(seg)
        return out

    def receive_user_event(self,text:str):
        """Receive transport without forcing cognition or a public reply.

        MESSAGE_RECEIVED is an external event. It TRIGGERs future DRIVE arbitration
        but performs no parsing, graph mutation or reply generation by itself.
        """
        self.external_seq+=1
        raw=f"{self.external_seq}|{time.time_ns()}|{text}".encode('utf-8')
        eid="in:"+hashlib.blake2s(raw,digest_size=8).hexdigest()
        wall=time.time()
        ev={"event_id":eid,"actor":"OTHER","kind":"MESSAGE_RECEIVED","text":str(text),
            "status":"PENDING","external_order":int(self.external_seq),"wall_time":wall,"channel":"CHAT_TEXT"}
        self.inbound_events.append(ev)
        self.life_events.append(dict(ev,step=int(self.step)))
        self.semantic_spine.record_event(event_id=eid,actor="OTHER",channel="CHAT_TEXT",payload=str(text),
                                         internal_step=int(self.step),wall_time=wall,external_order=int(self.external_seq),status="RECEIVED")
        self.semantic_spine.analyze_surface(eid,str(text))
        indexed=index_event(eid,self.external_seq,str(text))
        self.episode_index[eid]=indexed
        # Indexing never creates WORLD facts or SELF autobiography.
        return dict(ev)

    def _speech_value(self,parsed,reply_kind,decision=None):
        """Heuristic VALUE for DRIVE arbitration, not an execution rule."""
        kind=str(getattr(parsed,'kind','') or '')
        if kind in {'QUERY','TRUTH_QUERY','CAUSE_QUERY','EFFECT_QUERY','CAUSAL_TRUTH_QUERY','ABOUT'}:return 0.86
        if reply_kind in {'ANSWER','FLOOR'}:return 0.82
        if decision is not None and getattr(decision,'handled',False):
            dk=str(getattr(decision,'kind',''))
            if dk in {'ASK_CLARIFICATION','CHALLENGE'}:return 0.84
            if dk in {'TOPIC_CHOICE','PROPOSE_TOPIC'}:return 0.68
            if dk=='GREETING':return 0.46
        if reply_kind=='NOT_UNDERSTOOD':return 0.72
        if reply_kind=='ACK':return 0.42
        return 0.60

    def _queue_public_act(self,text,*,reason,cause_id,parsed=None,reply_kind=None,semantic_eids=None,requires_user=False,
                          value=0.6,asked_now=None,prompt_transition=None,source_event_id=None):
        self._seq+=1
        raw=f"{self.step}|{self._seq}|PUBLIC_ACT|{text}|{cause_id}".encode('utf-8')
        aid='act:'+hashlib.blake2s(raw,digest_size=8).hexdigest()
        context_eids=list(dict.fromkeys(list(self._recent_context_eids())+list(semantic_eids or [])))
        act={"act_id":aid,"text":str(text),"reason":str(reason),"cause_id":cause_id,"status":"READY",
             "created_step":int(self.step),"created_wall_time":time.time(),"external_order":int(self.external_seq),
             "value":float(value),"reply_kind":reply_kind,"parsed":parsed,"semantic_eids":list(semantic_eids or []),
             "context_eids":context_eids,"requires_user":bool(requires_user),"asked_now":list(asked_now or []),"reviews":0,
             "source_event_id":source_event_id,"prompt_transition":prompt_transition}
        # G319 / DRIVE STATUS: a stronger new candidate may background weaker
        # unsent candidates. They are preserved, not deleted or marked false.
        for old in self.pending_public_acts:
            if old.get('status')=='READY' and float(value)>=float(old.get('value',0.0))+0.15:
                old['status']='BACKGROUND';old['background_step']=int(self.step);old['background_reason']='LOWER_CURRENT_VALUE'
                self._record_life_event('C4','DRIVE_ACT_STATUS',status='BACKGROUND',source_event_id=old.get('act_id'),
                                        extra={"basis":"NEW_HIGHER_VALUE_ACT","new_act_id":aid,
                                               "old_value":float(old.get('value',0.0)),"new_value":float(value)})
        self.pending_public_acts.append(act)
        self._record_life_event('C4','SPEECH_ACT_CANDIDATE',status='READY',event_id=aid,source_event_id=source_event_id,
                                extra={"value":float(value),"reply_kind":reply_kind,"cause_id":cause_id,"context_eids":context_eids})
        return act

    def _publish_public_act(self,act):
        if not act or act.get('status') not in {'READY','BACKGROUND'}:return None
        # A delayed question becomes a user-facing inquiry only now. Formulation != sending.
        trans=act.get('prompt_transition') or {}
        safe_prompt=True
        if trans:
            cur_a=getattr(self.dialogue,'pending_ask',None);cur_c=getattr(self.dialogue,'pending_confirm',None)
            if cur_a==trans.get('before_ask') and cur_c==trans.get('before_confirm'):
                self.dialogue.pending_ask=trans.get('after_ask');self.dialogue.pending_confirm=trans.get('after_confirm')
            else:
                safe_prompt=False
        if act.get('requires_user') and trans and not safe_prompt:
            act['status']='BACKGROUND';act['background_reason']='PROMPT_CONTEXT_CHANGED'
            self._record_life_event('C4','DRIVE_PUBLICATION',status='BACKGROUND',source_event_id=act.get('act_id'),
                                    extra={"reason":"PROMPT_CONTEXT_CHANGED"})
            return None
        ev=self._event('REPLY',act.get('text',''),act.get('reason','DELIBERATED'),float(act.get('value',.6)),act.get('cause_id'),False)
        for eid in act.get('asked_now') or []:
            if eid in self.dialogue.g.entities:
                self.asked.add(eid);gid=self.gaps.make_id('DEFINITION',eid,'IS_A',None);self.gaps.mark_asked(gid)
                self._track_embedded_inquiry(f"А что такое {self.dialogue.g.label(eid)}?","TEACHING_FOLLOWUP",gid,True)
        self._record_turn('C4',act.get('text',''),kind='REPLY',reason=act.get('reason','DELIBERATED'),
                          requires_user=bool(act.get('requires_user')),event_id=ev.event_id,parsed=act.get('parsed'),
                          semantic_eids=act.get('semantic_eids') or [])
        act['status']='PUBLISHED';act['published_step']=int(self.step);act['reply_event_id']=ev.event_id
        self._record_life_event('C4','DRIVE_PUBLICATION',status='PUBLISHED',source_event_id=act.get('act_id'),
                                extra={"reply_event_id":ev.event_id,"value":float(act.get('value',.6))})
        return {'reply':act.get('text',''),'mutated':False,'event':asdict(ev),'parsed':act.get('parsed'),
                'public_act':dict(act)}

    def _select_public_act(self):
        ready=[x for x in self.pending_public_acts if x.get('status')=='READY']
        if not ready:return None
        # VALUE influences selection; DRIVE remains the sole selector.
        return max(ready,key=lambda x:(float(x.get('value',0.0)),int(x.get('created_step',0)),x.get('act_id','')))

    def _reconsider_background_acts(self):
        """DRIVE may return a background act to READY when current context supports it.

        This is an explicit arbitration step. BACKGROUND does not auto-publish.
        """
        current=set(self._recent_context_eids())
        rows=[]
        for act in self.pending_public_acts:
            if act.get('status')!='BACKGROUND':continue
            ctx=set(x for x in act.get('context_eids') or [] if x in self.dialogue.g.entities)
            overlap=len(current & ctx)
            age=max(0,int(self.step)-int(act.get('created_step',self.step)))
            effective=float(act.get('value',0.0))+min(.18,.06*overlap)-min(.20,.005*age)
            # Low-value social leftovers do not resurface merely because the queue emptied.
            if not overlap and effective<.75:continue
            rows.append((effective,overlap,-age,act.get('act_id',''),act))
        if not rows:return None
        _,overlap,_,_,act=max(rows,key=lambda z:z[:4])
        act['status']='READY';act['resumed_step']=int(self.step);act['resume_count']=int(act.get('resume_count',0))+1
        self._record_life_event('C4','DRIVE_ACT_STATUS',status='READY',source_event_id=act.get('act_id'),
                                extra={"basis":"BACKGROUND_RECONSIDERATION","context_overlap":int(overlap),
                                       "value":float(act.get('value',0.0))})
        return act

    def _review_public_acts(self):
        act=self._select_public_act()
        if act is None:return None
        act['reviews']=int(act.get('reviews',0))+1
        self._record_life_event('C4','DELIBERATION_REVIEW',status='OPEN',source_event_id=act.get('act_id'),
                                extra={"reviews":act['reviews'],"value":float(act.get('value',.6))})
        return act

    def cognitive_step(self,*,allow_initiative=True,allow_public_output=True,allow_background_return=False):
        """Run one cognitive iteration; public output is a separate DRIVE decision.

        MESSAGE_RECEIVED may be interpreted and learned from without forcing SEND.
        With no inbound event, DRIVE may publish a READY act, review it internally,
        or perform ordinary initiative.
        """
        if self.inbound_events:
            ev=self.inbound_events.popleft();ev["status"]="PROCESSING"
            self._record_life_event("C4","COGNITIVE_PROCESS",status="STARTED",source_event_id=ev["event_id"],extra={"external_order":ev.get("external_order")})
            before_facts=set(self.dialogue.g.facts)
            before_entities=set(self.dialogue.g.entities)
            before_order=self.dialogue.g.order
            before_tx=len(self.semantic_spine.transactions)
            before_inquiries={qid:(q.get('status'),len(q.get('answer_candidates',[]))) for qid,q in self.inquiries.items()}
            # All open questions are compared; no latest-ASK lock, no automatic truth/closure.
            link=evaluate_inquiry_link(ev.get('text',''),list(self.inquiries.values()),ev['event_id'])
            self.last_inquiry_evaluation=link
            self._record_life_event('C4','EVAL_INQUIRY_LINK',status=link['status'],source_event_id=ev['event_id'],
                                    extra={'influence':'AVAIL','candidates':link['candidates']})
            # Legacy dialogue.pending_ask was a single-answer shortcut. It may
            # contextualize an answer only if EVAL matched its actual ASK ID.
            # Suspending the pointer changes AVAIL, not the underlying inquiry.
            old_pa=self.dialogue.pending_ask
            chosen=link['candidates'][0]['question_event_id'] if link['status']=='CANDIDATE' else None
            pending_ids=[q['event_id'] for q in self.inquiries.values()
                         if q.get('status') in {'OPEN','BACKGROUND'}]
            matched_last=bool(chosen and pending_ids and chosen==pending_ids[-1])
            # Anaphora remains lawful when there is exactly one unresolved focus.
            # An older ASK which already received a candidate answer may stay OPEN
            # epistemically, but it is not a competing foreground referent.
            competing=[self.inquiries[qid] for qid in pending_ids[:-1]
                       if qid in self.inquiries and not self.inquiries[qid].get('answer_candidates')]
            unambiguous_focus=bool(not pending_ids or len(pending_ids)==1 or not competing)
            suspend=bool(self.inquiries and old_pa and not (matched_last or unambiguous_focus))
            if suspend:
                self.dialogue.pending_ask=None
                self._record_life_event('C4','EVAL_LEGACY_ANSWER_POINTER',status='SUSPENDED',
                                        source_event_id=ev['event_id'],
                                        extra={'influence':'MASK','reason':'NO_SUPPORTED_ASK_ID_MATCH',
                                               'legacy_subject_eid':old_pa.get('eid') if isinstance(old_pa,dict) else None})
            try:
                try:
                    pseudo=structured_cognition.parse(ev.get('text',''))
                except (ValueError,TypeError,KeyError) as ex:
                    # Untrusted text must not crash Android's foreground organism.
                    self._record_life_event('C4','EVAL_STRUCTURED_REJECT',status='REJECTED',
                                            source_event_id=ev['event_id'],extra={'reason':type(ex).__name__+':'+str(ex)[:120]})
                    self._record_life_event('C4','COMMIT_NOOP',status='BLOCKED',source_event_id=ev['event_id'],
                                            extra={'reason':'INVALID_STRUCTURED_EVENT'})
                    out=structured_cognition._reply(self,'Отклонено: неверная структура когнитивного события.',
                                         'REJECT',ev['event_id'],publish=bool(allow_public_output),
                                         semantic={'status':'REJECTED','error':str(ex)[:120]})
                else:
                    if pseudo is not None:
                        out=structured_cognition.process(self,pseudo,ev['event_id'],publish=bool(allow_public_output))
                    else:
                        out=self._process_user_message_now(ev.get("text",""),source_event_id=ev["event_id"],publish=bool(allow_public_output))
            finally:
                if suspend and self.dialogue.pending_ask is None:
                    self.dialogue.pending_ask=old_pa
            if link['status']=='CANDIDATE':
                qid=link['candidates'][0]['question_event_id']
                q=self.inquiries.get(qid)
                if q is not None and q.get('status') in {'OPEN','BACKGROUND'}:
                    # A human message is evidence of words received, not evidence
                    # the question was accurately answered. Keep OPEN until lawful resolution.
                    q.setdefault('answer_candidates',[]).append({'source_event_id':ev['event_id'],
                                                                  'shared_features':link['candidates'][0]['shared_features'],
                                                                  'status':'UNVERIFIED'})
                    self._record_life_event('C4','COMMIT_INQUIRY_CANDIDATE',status='RECORDED',source_event_id=ev['event_id'],
                                            extra={'influence':'STATUS','question_event_id':qid,
                                                   'evidence_scope':'USER_SAID_NOT_WORLD','resolved':False})
            added_facts=sorted(set(self.dialogue.g.facts)-before_facts)
            removed_facts=sorted(before_facts-set(self.dialogue.g.facts))
            added_entities=sorted(set(self.dialogue.g.entities)-before_entities)
            changed_q=[{'question_event_id':qid,'before':before_inquiries.get(qid),
                        'after':(q.get('status'),len(q.get('answer_candidates',[])))}
                       for qid,q in self.inquiries.items()
                       if before_inquiries.get(qid)!=(q.get('status'),len(q.get('answer_candidates',[])))]
            self._record_life_event('C4','CASCADE_OUTCOME',status='OBSERVED',source_event_id=ev['event_id'],
                                    extra={'influence':'STATUS','graph_delta':{'added_fact_ids':added_facts,
                                        'removed_fact_ids':removed_facts,'added_entity_ids':added_entities,
                                        'order_before':before_order,'order_after':self.dialogue.g.order},
                                        'inquiry_changes':changed_q,
                                        'new_transaction_ids':[t.get('transaction_id') for t in self.semantic_spine.transactions[before_tx:]],
                                        'selected_public_event_id':((out.get('event') or {}).get('event_id') if isinstance(out,dict) else None)})
            # G320 composition: represent what the message expressed without
            # turning representation into truth.
            parsed=out.get('parsed') if isinstance(out,dict) else None
            semantic_eids=[]
            if isinstance(parsed,dict):
                semantic_eids=self._known_mentions(ev.get('text',''),type('P',(),parsed)())
            self.composition.record_message(ev.get('text',''),step=self.step,source_event_id=ev["event_id"],
                                            parsed=parsed if isinstance(parsed,dict) else None,semantic_eids=semantic_eids)
            ev["status"]="PROCESSED";ev["processed_step"]=int(self.step)
            self._record_life_event("C4","COGNITIVE_PROCESS",status="DONE",source_event_id=ev["event_id"],extra={"reply_event_id":((out.get("event") or {}).get("event_id") if isinstance(out,dict) else None),"public_output":bool(out.get('reply') if isinstance(out,dict) else False)})
            out["inbound_event"]=dict(ev)
            if self._trace_mode!='OFF' and self._trace_scope=='NEXT_INTERACTION':
                # End after the input's actual cognitive step. Already emitted
                # trace events remain readable in the trace outbox.
                self._trace_mode='OFF';self._trace_scope='CONTINUOUS'
            return out
        act=self._select_public_act()
        if act is None and allow_background_return:
            act=self._reconsider_background_acts()
        if act is not None:
            if allow_public_output:
                out=self._publish_public_act(act)
                if out is not None:return out
            reviewed=self._review_public_acts()
            return {"reply":None,"mutated":False,"initiative":[],"event":None,"parsed":None,
                    "public_act":None if reviewed is None else dict(reviewed)}
        if allow_initiative:
            emitted=self.tick(1)
            return {"reply":None,"mutated":False,"initiative":emitted,"event":None,"parsed":None}
        return {"reply":None,"mutated":False,"initiative":[],"event":None,"parsed":None}

    def user_message(self,text:str):
        """Compatibility surface: receive one message and immediately run one cognitive step.

        Android may keep using this API, but the runtime physics no longer requires
        message receipt and cognition/reply to be synchronous.
        """
        self.receive_user_event(text)
        return self.cognitive_step(allow_initiative=False,allow_public_output=True)

    def _process_user_message_now(self,text:str,source_event_id=None,publish=True):
        self.human_active=True;self._asked_since_user=False
        # Receiving a human event is a TRIGGER for DRIVE, not proof that any
        # outstanding inquiry was answered.  Do not clear inquiry state here.
        # G328: a long exam/question sheet is one READ-ONLY event family.
        # Splitting 20 questions and sending each through dialogue.say() allowed
        # test premises, quotes and simulated events to become teaching attempts.
        # This applies to all topics/names, not to a fixed answer key.
        indexed=self.episode_index.get(source_event_id) if source_event_id else None
        if indexed is None:
            indexed=index_event(source_event_id or ('internal:%s'%self.step),self.external_seq,str(text))
        episodes=indexed['episodes']
        candidate=None
        if is_query_batch(episodes):
            candidate=answer_batch(episodes,self.episode_index,current_event_id=source_event_id,inquiries=list(self.inquiries.values()))
        elif len(episodes)==1 and (is_memory_query(episodes[0]['text']) or is_inquiry_query(episodes[0]['text'])):
            candidate=answer_memory_query(episodes[0]['text'],self.episode_index,current_event_id=source_event_id,inquiries=list(self.inquiries.values()))
        if candidate is not None:
            self.step+=1;self.last_user_step=self.step
            self._record_life_event('C4','EVAL_SOURCE_EPISODES',status='CANDIDATE',
                                    source_event_id=source_event_id,extra={
                                       'scope':'READ_ONLY_TRANSCRIPT', 'episode_count':len(episodes),
                                       'basis_event_ids':list(dict.fromkeys(x['event_id'] for x in candidate.get('refs',[]))),
                                       'candidate_status':candidate['status']})
            self._record_life_event('C4','COMMIT_NOOP',status='BLOCKED',
                                    source_event_id=source_event_id,
                                    extra={'reason':'EXAM_OR_TRANSCRIPT_QUERY_NOT_TEACHING'})
            self._record_life_event('C4','DRIVE_SPEECH_ACT',status='SELECTED',
                                    source_event_id=source_event_id,
                                    extra={'speech_act':'EVIDENCE_BOUNDED_RECALL','basis':'READ_ONLY_EPISODES'})
            self._record_turn('USER',text,kind='QUERY_BATCH' if is_query_batch(episodes) else 'MEMORY_QUERY')
            reply=candidate['reply'];ev=None
            if publish:
                ev=self._event('REPLY',reply,'SOURCE_RECALL',0.9,source_event_id,False)
                self._record_turn('C4',reply,kind='REPLY',reason='SOURCE_RECALL',event_id=ev.event_id)
            self._record_life_event('C4','SOURCE_RECALL_RESULT',status=candidate['status'],
                                    source_event_id=source_event_id,extra={
                                         'found_references':len(candidate.get('refs',[])),
                                         'question_count':candidate.get('question_count',1)})
            self._autosave_tick(False)
            return {'reply':reply if publish else None,'proposed_reply':None if publish else reply,
                    'mutated':False,'event':asdict(ev) if ev is not None else None,
                    'parsed':{'kind':'READ_ONLY_EPISODIC_QUERY'},
                    'reply_kind':'EVIDENCE_BOUNDED_RECALL','basis_event_ids':list(dict.fromkeys(x['event_id'] for x in candidate.get('refs',[]))),
                    'episode_count':len(episodes),'status':candidate['status']}
        surfaces=self._split_user_surfaces(text)
        if not surfaces:
            surfaces=[str(text).strip()] if str(text).strip() else ['']
        if len(surfaces)==1:
            out=self._user_surface(surfaces[0],emit_public=bool(publish),source_event_id=source_event_id);self._autosave_tick(out['mutated'])
            if publish:return out
            act=self._queue_public_act(out['reply'],reason='USER_EVENT',cause_id=f"user:{self.step}",parsed=out.get('parsed'),
                                       reply_kind=out.get('reply_kind'),semantic_eids=out.get('action_context_eids'),
                                       requires_user=out.get('requires_user',False),value=float(out.get('speech_value',.6)),
                                       asked_now=out.get('asked_now'),prompt_transition=out.get('prompt_transition'),source_event_id=source_event_id)
            return {'reply':None,'proposed_reply':out['reply'],'mutated':out['mutated'],'event':None,'parsed':out.get('parsed'),
                    'reply_kind':out.get('reply_kind'),'public_act':dict(act)}
        parts=[];reply_event_ids=set();mutated=False
        first_step=self.step+1
        for surface in surfaces:
            r=self._user_surface(surface,emit_public=bool(publish),source_event_id=source_event_id);parts.append(r);mutated=mutated or bool(r['mutated'])
            if r.get('event'):reply_event_ids.add(r['event']['event_id'])
        # UI submission is transport. Internal surfaces were processed separately, but
        # the shell gets one aggregate REPLY rather than N artificial chat bubbles.
        if publish:self.outbox=deque(ev for ev in self.outbox if ev.event_id not in reply_event_ids)
        # G267: a later surface that repeats the same related knowledge (same receipts) or the same text
        # supersedes the earlier one, so «Мяч закрыли коробкой. Он исчез?» is answered once.
        keep=[True]*len(parts);seen_ids=set();seen_txt=set()
        for i in range(len(parts)-1,-1,-1):
            r=parts[i];txt=r['reply']
            if txt in seen_txt:keep[i]=False;continue
            seen_txt.add(txt)
            if r.get('reply_kind')=='FLOOR' and r.get('receipts'):
                ids=set(r['receipts'])
                if ids<=seen_ids:keep[i]=False
                seen_ids|=ids
        texts=[r['reply'] for r in parts]
        kinds=[r.get('reply_kind') for r in parts]
        for i in range(len(parts)):
            # G268: «Хорошо.» echoed back adds nothing when the message has content; a statement that only served
            # as context for a later answered question («Мяч закрыли коробкой. Он исчез?») needs no reply of its own.
            if kinds[i]=='ACK' and any(k!='ACK' for j,k in enumerate(kinds) if j!=i):keep[i]=False
            if kinds[i]=='NOT_UNDERSTOOD' and any(k in ('ANSWER','FLOOR') for k in kinds[i+1:]):keep[i]=False
        nu=[i for i,r in enumerate(parts) if keep[i] and r.get('reply_kind')=='NOT_UNDERSTOOD']
        if len(nu)>=2:   # several not-understood surfaces -> one honest sentence, not N copies
            words=list(dict.fromkeys(w for i in nu for w in parts[i].get('unknown_words',[])))
            for i in nu[:-1]:keep[i]=False
            texts[nu[-1]]="Я пока не понимаю эти фразы. Скажи проще — по одной мысли."
        reply=' '.join(texts[i] for i in range(len(parts)) if texts[i] and keep[i]).strip()
        self._autosave_tick(mutated)
        cause=f'user-stream:{first_step}:{self.step}'
        if publish:
            ev=self._event('REPLY',reply,'USER_STREAM',0.9,cause,False)
            return {'reply':reply,'mutated':mutated,'event':asdict(ev),'parsed':parts[-1]['parsed'],
                    'surface_count':len(parts),'surfaces':[{'text':surfaces[i],'reply':parts[i]['reply'],'parsed':parts[i]['parsed']} for i in range(len(parts))]}
        sem=[];asked=[]
        for r in parts:
            sem.extend(r.get('reply_mentions') or []);asked.extend(r.get('asked_now') or [])
        value=max([float(r.get('speech_value',.6)) for r in parts] or [.6])
        act=self._queue_public_act(reply,reason='USER_STREAM',cause_id=cause,parsed=parts[-1]['parsed'],
                                   reply_kind='STREAM',semantic_eids=list(dict.fromkeys(sem)),value=value,asked_now=list(dict.fromkeys(asked)),source_event_id=source_event_id)
        return {'reply':None,'proposed_reply':reply,'mutated':mutated,'event':None,'parsed':parts[-1]['parsed'],
                'public_act':dict(act),'surface_count':len(parts),
                'surfaces':[{'text':surfaces[i],'reply':parts[i]['reply'],'parsed':parts[i]['parsed']} for i in range(len(parts))]}

    def _user_surface(self,text:str,*,emit_public=True,source_event_id=None):
        self.step+=1
        self.last_user_step=self.step
        before=len(self.dialogue.g.facts)
        pre_pending_ask=dict(self.dialogue.pending_ask) if isinstance(getattr(self.dialogue,'pending_ask',None),dict) else getattr(self.dialogue,'pending_ask',None)
        pre_pending_confirm=dict(self.dialogue.pending_confirm) if isinstance(getattr(self.dialogue,'pending_confirm',None),dict) else getattr(self.dialogue,'pending_confirm',None)
        parsed=self.dialogue.semantic_intent(text)
        # Build EVAL/AVAIL context from existing semantic anchors. Current mentions
        # may focus retrieval but cannot become evidence or create facts.
        current_mentions=self._known_mentions(text,parsed)
        context_before=self._recent_context_eids()
        self.dialogue.set_context_entities(list(dict.fromkeys(context_before+current_mentions)))

        # G275 merge: contextual discourse acts are allowed to intercept only
        # conversational/meta language.  A pending self-check belongs to the
        # teaching organ, so short yes/no answers must reach C4ChildDialogue.
        decision=self.discourse.interpret(text,parsed,list(self.dialogue_history),self.dialogue)
        # Explicit lexical teaching announcements belong to the teaching organ,
        # not to the generic conversational "I will teach/explain" act.
        if decision.handled and getattr(self.dialogue,'_announcement',lambda _x:None)(text):
            decision=type(decision)(False)
        pending_confirm=bool(getattr(self.dialogue,'pending_confirm',None))
        if pending_confirm and decision.handled and decision.kind in {
                'ANSWER_ACK','ACK','ANSWER_REJECT','REJECT'}:
            decision=type(decision)(False)
        # Kernel dialogue owns evidence-aware "Почему?" and can expose the
        # actual inference chain.  The discourse bridge is only a fallback.
        if decision.handled and decision.kind=='WHY_FOLLOWUP':
            decision=type(decision)(False)

        # G318: independent interpreters contribute EVAL candidates; no candidate
        # gains COMMIT or action authority by existing.
        icands=[{"source":"KERNEL","kind":str(parsed.kind),"relation":getattr(parsed,'relation',None),
                 "subject":getattr(parsed,'subject',None),"object":getattr(parsed,'object',None),
                 "confidence":0.72 if str(parsed.kind)!='UNKNOWN' else 0.15}]
        if decision.handled:
            icands.append({"source":"DISCOURSE","kind":str(decision.kind),
                           "confidence":float(decision.confidence),"reason":decision.reason})
        if source_event_id:
            for c in icands:
                self.semantic_spine.add_candidate(source_event_id,source=c.get("source","RUNTIME"),speech_act=c.get("kind","UNKNOWN"),
                                                  subject_role=None,relation=c.get("relation"),object_value=c.get("object"),
                                                  temporal_scope=temporal_scope(text),epistemic_mode=epistemic_mode(text),
                                                  quoted_depth=0,confidence=float(c.get("confidence",.5)),note=c.get("reason"))
        self._record_life_event('C4','EVAL_INTERPRETATION_SET',status='CANDIDATE',
                                extra={"candidates":icands,"count":len(icands)})

        # G326: if the old language organ cannot understand a perspective frame,
        # preserve the recursive semantics as a candidate instead of flattening it
        # into a WORLD fact. Acknowledgment is generated from structure, not a
        # phrase-specific chatbot answer. The existing intent/dialogue path wins
        # when it has a recognized interpretation.
        frame = self.semantic_spine.perspective_frames.get(source_event_id or '')
        self_audit = inspect_question(text, self.dialogue_history, self.semantic_spine.events)
        participant_info=perspective_entity_inquiry(text,self.semantic_spine.perspective_frames)
        # G327: a single read-only discourse query layer traverses ALL attributed
        # events before ordinary lexical retrieval. Interpretation != WORLD truth.
        scoped_query=resolve_disposition(text,self.semantic_spine,self.dialogue_history)
        # In fallback-only situations, source-aware metacognitive EVAL supersedes
        # generic topic overlap, which otherwise misassigns «ты» to the user.
        # Any attributed statement, even one recognized by the old copula parser,
        # is a SOURCE-REPRESENTATION. It must never fall into direct WORLD teaching.
        perspective_fallback = bool(frame)
        if scoped_query:
            self._record_life_event('C4','EVAL_DISCOURSE_GRAPH_QUERY',status='CANDIDATE',
                                    source_event_id=source_event_id,
                                    extra={'query_kind':scoped_query['kind'],'basis_events':scoped_query['refs'],
                                           'scope':scoped_query['scope']})
            self._record_life_event('C4','DRIVE_SPEECH_ACT',status='SELECTED',
                                    source_event_id=source_event_id,
                                    extra={'speech_act':scoped_query['kind'],'basis':'READ_ONLY_SOURCE_GRAPH'})
            reply=scoped_query['reply'];reply_kind=scoped_query['kind'];receipts=[];unknown_words=[]
            gap_requests=[];asked_now=[];deferred=[]
            self.dialogue.last_used=[];self.dialogue.last_unknown_words=[]
        elif participant_info and not decision.handled and parsed.kind=='UNKNOWN':
            self._record_life_event('C4','EVAL_CONTEXT_PARTICIPANT',status='CANDIDATE',
                                    extra={'source_event_id':source_event_id})
            self._record_life_event('C4','DRIVE_SPEECH_ACT',status='SELECTED',
                                    extra={'speech_act':'CONTEXT_PARTICIPANT','basis':'EVAL_CONTEXT'})
            reply=participant_info['reply'];reply_kind='CONTEXT_PARTICIPANT';receipts=[];unknown_words=[]
            gap_requests=[];asked_now=[];deferred=[]
            self.dialogue.last_used=[];self.dialogue.last_unknown_words=[]
        elif self_audit and not decision.handled:
            self._record_life_event('C4','EVAL_SOURCE_SELF_AUDIT',status='CANDIDATE',
                                    extra={'kind':self_audit['kind'],'source_event_id':source_event_id})
            self._record_life_event('C4','DRIVE_SPEECH_ACT',status='SELECTED',
                                    extra={'speech_act':'SOURCE_SELF_AUDIT','basis':'EVAL_SOURCE_META'})
            reply=self_audit['reply'];reply_kind='SOURCE_SELF_AUDIT';receipts=[];unknown_words=[]
            gap_requests=[];asked_now=[];deferred=[]
            self.dialogue.last_used=[];self.dialogue.last_unknown_words=[]
        elif perspective_fallback:
            self._record_life_event('C4','EVAL_RECURSIVE_PERSPECTIVE',status='CANDIDATE',
                                    extra={'source_event_id':source_event_id,'frame':frame})
            self._record_life_event('C4','DRIVE_SPEECH_ACT',status='SELECTED',
                                    extra={'speech_act':'PERSPECTIVE_ACK','basis':'STRUCTURAL_EVAL'})
            reply = 'Различаю вложенные точки зрения: ' + chain_summary(frame) + '. Это представление чужой речи или мысли, а не подтверждённый факт мира.'
            reply_kind='PERSPECTIVE_ACK';receipts=[];unknown_words=[]
            gap_requests=[];asked_now=[];deferred=[]
            self.dialogue.last_used=[];self.dialogue.last_unknown_words=[]
        elif decision.handled:
            # The discourse organ proposes an interpretation (EVAL). Runtime DRIVE
            # selects the public speech act; this selection carries no COMMIT power.
            self._record_life_event('C4','EVAL_INTERPRETATION',status='CANDIDATE',extra={
                'speech_act':decision.kind,'confidence':float(decision.confidence),'reason':decision.reason})
            self._record_life_event('C4','DRIVE_SPEECH_ACT',status='SELECTED',extra={
                'speech_act':decision.kind,'basis':'DISCOURSE_EVAL','confidence':float(decision.confidence)})
            reply=decision.reply or ''
            reply_kind='ACK' if decision.kind in {'ACK','ANSWER_ACK'} else 'DISCOURSE';receipts=list(getattr(self.dialogue,'last_used',[]) or []);unknown_words=[]
            gap_requests=[];asked_now=[];deferred=[]
            self.dialogue.last_used=[];self.dialogue.last_unknown_words=[]
        else:
            reply=self.dialogue.say(text)
            reply_kind=self.dialogue.last_reply_kind
            tx=getattr(self.dialogue,'last_spine_transaction',None)
            if tx and source_event_id:
                self.semantic_spine.record_transaction(tx_kind='ATOMIC_SOCIAL_CORRECTION',source_event_id=source_event_id,status='COMMITTED',details=dict(tx))
                self.dialogue.last_spine_transaction=None
            receipts=list(self.dialogue.last_used)
            unknown_words=list(getattr(self.dialogue,'last_unknown_words',[]))
            gap_requests=list(getattr(self.dialogue,'gap_requests',[]))
            asked_now=list(getattr(self.dialogue,'asked_in_reply',[]))
            deferred=list(getattr(self.dialogue,'deferred_asks',[]));self.dialogue.deferred_asks=[]
            self._record_life_event('C4','DRIVE_SPEECH_ACT',status='SELECTED',extra={
                'speech_act':reply_kind,'basis':'KERNEL_EVAL','parsed_kind':str(parsed.kind)})

        after=len(self.dialogue.g.facts)
        cause=f"user:{self.step}"
        # Derived objects used in the reply remain context, but an entity explicitly
        # mentioned by OTHER has the stronger discourse focus for later deixis.
        reply_mentions=self._receipt_entities(receipts)
        for eid in reply_mentions:self._remember_context(eid,role="C4_USED_FACT")
        for eid in current_mentions:self._remember_context(eid,role="USER_MENTION")
        self.dialogue.set_context_entities(self._recent_context_eids())
        self._record_turn('USER',text,kind='USER',parsed=asdict(parsed),semantic_eids=current_mentions)
        post_pending_ask=dict(self.dialogue.pending_ask) if isinstance(getattr(self.dialogue,'pending_ask',None),dict) else getattr(self.dialogue,'pending_ask',None)
        post_pending_confirm=dict(self.dialogue.pending_confirm) if isinstance(getattr(self.dialogue,'pending_confirm',None),dict) else getattr(self.dialogue,'pending_confirm',None)
        requires_user=bool(post_pending_ask or post_pending_confirm)
        prompt_transition={"before_ask":pre_pending_ask,"before_confirm":pre_pending_confirm,
                           "after_ask":post_pending_ask,"after_confirm":post_pending_confirm}
        ev=None
        if emit_public:
            ev=self._event('REPLY',reply,'USER_EVENT',0.9,cause,False)
            self._record_turn('C4',reply,kind='REPLY',reason='USER_EVENT',requires_user=requires_user,event_id=ev.event_id,parsed=asdict(parsed),semantic_eids=reply_mentions)
        else:
            # Formulated but not sent: restore user-facing prompt state until DRIVE publishes it.
            self.dialogue.pending_ask=pre_pending_ask;self.dialogue.pending_confirm=pre_pending_confirm

        # Explicit gap accounting: discourse/context acts are not world evidence.
        if not decision.handled:
            if parsed.kind=='QUERY' and reply.startswith('Не знаю'):
                sid=self.dialogue.g.resolve(parsed.subject) or self.dialogue.morphology.resolve(parsed.subject) or ('surface:'+str(parsed.subject).strip())
                self.register_gap('DEFINITION' if parsed.relation=='IS_A' else 'RELATION',sid,relation=parsed.relation,reason='USER_QUERY_UNKNOWN',priority=0.55,cause_id=cause,schedule=False)
            elif parsed.kind=='TRUTH_QUERY' and reply.startswith('Не знаю.'):
                sid=self._surface_id(parsed.subject);oid=self._surface_id(parsed.object)
                self.register_gap('RELATION',sid,relation=parsed.relation,object_value=oid,reason='USER_TRUTH_UNKNOWN',priority=0.6,cause_id=cause,schedule=False)
            elif parsed.kind=='CAUSAL_TRUTH_QUERY' and reply=='Не знаю.':
                sid=self._surface_id(parsed.subject);oid=self._surface_id(parsed.object)
                self.register_gap('CAUSAL_RELATION',sid,relation='CAUSES',object_value=oid,reason='USER_CAUSAL_UNKNOWN',priority=0.65,cause_id=cause,schedule=False)
            elif parsed.kind=='CAUSE_QUERY' and reply.startswith('Не знаю'):
                sid=self._surface_id(parsed.subject)
                self.register_gap('CAUSE_OF',sid,relation='CAUSES',reason='USER_CAUSE_UNKNOWN',priority=0.6,cause_id=cause,schedule=False)
            elif parsed.kind=='EFFECT_QUERY' and reply.startswith('Не знаю'):
                sid=self._surface_id(parsed.subject)
                self.register_gap('EFFECT_OF',sid,relation='CAUSES',reason='USER_EFFECT_UNKNOWN',priority=0.6,cause_id=cause,schedule=False)
            elif parsed.kind=='UNKNOWN' and reply.startswith('Я пока не понимаю'):
                shape=self.dialogue.relation_queries.question_shape(text)
                if shape is not None:
                    self.register_gap('LANGUAGE_RELATION',shape['relation_surface'],reason='UNBOUND_RELATION_NOUN',priority=0.7,cause_id=cause,schedule=False)

            # Curiosity comes from admitted bindings, not from discourse heuristics.
            if parsed.kind in {'CLAIM','REMEMBER_CLAIM','CORRECT_CLAIM'} and parsed.relation=='IS_A':
                oid=self.dialogue.g.resolve(parsed.object)
                sid=self.dialogue.g.resolve(parsed.subject) if parsed.subject else None
                if oid and oid not in self.asked:
                    defined=self.dialogue.g.get_all(oid,'IS_A',viewer=self.dialogue.principal,principal=self.dialogue.principal)
                    foundational=self.dialogue.g.get(oid,'FOUNDATIONAL',viewer=self.dialogue.principal,principal=self.dialogue.principal)
                    if not defined and not (foundational and foundational.object_value=='true'):
                        self.register_gap('DEFINITION',oid,relation='IS_A',reason='UNRESOLVED_DEFINITION',priority=0.65,cause_id=cause,schedule=True)
                if sid and oid:
                    rr=self.dialogue.reasoner.evaluate_is_a(sid,oid,principal=self.dialogue.principal,viewer=self.dialogue.principal)
                    ck=f"{sid}|{oid}"
                    if rr.value=='CONFLICT' and ck not in self.asked_conflicts:
                        self.register_gap('CONTRADICTION',sid,relation='IS_A',object_value=oid,reason='UNRESOLVED_CONTRADICTION',priority=0.9,cause_id=cause,schedule=True)
                    elif rr.value!='CONFLICT':
                        self.asked_conflicts.discard(ck)

            # Teaching dialogue may open explicit gaps; questions already spoken in
            # the reply are marked asked so tick does not echo them.
            for req in gap_requests:
                subj=req['subject']
                self.register_gap(req['kind'],subj,relation=req.get('relation'),reason='TEACHING_DIALOGUE',priority=req.get('priority',0.7),cause_id=cause,schedule=False)
            if emit_public:
                for eid in asked_now:
                    self.asked.add(eid)
                    gid=self.gaps.make_id('DEFINITION',eid,'IS_A',None)
                    self.gaps.mark_asked(gid)
                    # The question becomes an external inquiry only when actually sent.
                    label=self.dialogue.g.label(eid) if eid in self.dialogue.g.entities else str(eid)
                    self._track_embedded_inquiry(f"А что такое {label}?","TEACHING_FOLLOWUP",gid,True)
            for eid in deferred:
                # UNKNOWN/deferral changes conversational availability, not truth.
                # Keep the semantic gap open but do not immediately recycle the same
                # public question.  A future DRIVE trigger may surface it again.
                for qid in reversed(self.inquiry_order):
                    q=self.inquiries.get(qid)
                    if q and q.get('status')=='OPEN':
                        q['status']='BACKGROUND';q['background_step']=int(self.step);break

        self.refresh_gaps()
        return {'reply':reply,'mutated':after!=before,'event':(asdict(ev) if ev is not None else None),'parsed':asdict(parsed),
                'reply_kind':reply_kind,'receipts':receipts,'unknown_words':unknown_words,
                'discourse':decision.to_dict(),'reply_mentions':reply_mentions,
                'action_context_eids':list(dict.fromkeys(current_mentions+reply_mentions)),'asked_now':list(asked_now),
                'requires_user':requires_user,'prompt_transition':prompt_transition,
                'speech_value':self._speech_value(parsed,reply_kind,decision)}

    def presence_snapshot(self,now=None):
        """Read-only engineering presence: internal/external time and unfinished structures.

        This is not a metaphysical self claim and it has no COMMIT authority.
        """
        opens=[dict(self.inquiries[qid]) for qid in self.inquiry_order if qid in self.inquiries and self.inquiries[qid].get('status') in {'OPEN','BACKGROUND'}]
        acts=[{k:a.get(k) for k in ('act_id','status','text','value','created_step','created_wall_time')} for a in self.pending_public_acts if a.get('status') in {'READY','BACKGROUND'}]
        return self.semantic_spine.presence_snapshot(now=now,internal_step=self.step,open_inquiries=opens,pending_acts=acts)

    def add_learning_goal(self,label:str,reason="EXPLICIT_LEARNING_GOAL",cause_id=None):
        eid=self.dialogue._eid(label)
        if eid not in self.asked:self.pending_questions.append((eid,reason,cause_id))
        return eid

    def learning_agenda(self,limit:int=5):
        self.refresh_gaps()
        return agenda_dicts(self.gaps.open(),self.step,limit)

    # G269: initiative arbitration. With a person in the conversation the child asks ONE question per turn and only
    # about human-meaningful things; curriculum needs (competency / rule study / epistemic validation) stay on the
    # learning agenda for the teacher pipeline instead of being asked in chat.
    TEACHER_REASONS={'COMPETENCY_REQUIREMENT','RULE_STUDY_NEED','EPISTEMIC_CHALLENGE','EPISTEMIC_REVALIDATION'}
    _MACHINE_LABEL=re.compile(r"\b[a-zа-я]?\d{2,}\b|\bnode\b|\bworld\s+\d+|[_:]",re.IGNORECASE)

    def set_audience(self,audience:str):
        """'HUMAN' — initiative talks to a person; 'TEACHER' — every learning need is an ASK (curriculum pipeline)."""
        self.human_active=str(audience).upper()=='HUMAN'

    def _machine_label(self,x):
        return bool(x) and bool(self._MACHINE_LABEL.search(str(self._glabel(x))))

    def _human_ok(self,g):
        return g.reason not in self.TEACHER_REASONS and not self._machine_label(g.subject) and not self._machine_label(g.object_value)

    def _sync_inquiries(self):
        """Project inquiry STATUS from underlying semantic state without inventing answers.

        Cause-linked gaps resolve inquiries only when COMMIT/gap state says RESOLVED.
        Mere message arrival, elapsed time or model confidence never resolves one.
        """
        for qid in list(self.inquiry_order):
            q=self.inquiries.get(qid)
            if not q or q.get('status') not in {'OPEN','BACKGROUND'}:continue
            cid=q.get('cause_id')
            gap=self.gaps.gaps.get(cid) if cid else None
            if gap is not None and gap.status==RESOLVED:
                q['status']='RESOLVED';q['resolved_step']=int(self.step)
        self.awaiting_response=any(q.get('status')=='OPEN' and q.get('requires_user') for q in self.inquiries.values())

    def tick(self,n:int=1):
        emitted=[]
        hm=bool(getattr(self,'human_active',False))   # (not `human`: the RULE_EXAMPLE text below reuses that name)
        for _ in range(max(1,int(n))):
            self.step+=1
            # G310 / DRIVE: an outstanding question cannot seize arbitration.
            # New external/internal events merely TRIGGER reconsideration.
            ready=(self.step-self.last_initiative_step>=self.initiative_cooldown and self.step-self.last_user_step>=self.initiative_cooldown)
            self.refresh_gaps();self._sync_inquiries()
            foreground=sum(1 for q in self.inquiries.values() if q.get("status")=="OPEN" and q.get("requires_user"))
            if foreground>=self.max_foreground_inquiries:
                ready=False
            if ready:
                # G276 ActiveGaps: rank current needs.  HUMAN mode filters machine-only
                # curriculum, but there is no one-question request/response contract.
                eligible=[g for g in self.gaps.open() if g.status==OPEN and (
                    g.evidence_count>=2 or g.reason in {'COMPETENCY_REQUIREMENT','RULE_STUDY_NEED','EPISTEMIC_CHALLENGE','EPISTEMIC_REVALIDATION','GUIDED_READING','GUIDED_READING_TERM'}
                ) and g.kind!='CONTRADICTION']
                if hm:
                    eligible=[g for g in eligible if g.kind!='DEFINITION' and self._human_ok(g)]
                else:
                    eligible=[g for g in eligible if g.reason in self.TEACHER_REASONS or g.reason in {'GUIDED_READING','GUIDED_READING_TERM'} or (not self._machine_label(g.subject) and not self._machine_label(g.object_value))]
                ranked=build_agenda(eligible,self.step,1)
                if ranked:
                    target=ranked[0];g=self.gaps.gaps[target.gap_id]
                    if g.kind=='LEXICAL_TERM':
                        raw=self._glabel(g.subject)
                        text=f"В тексте встретилась форма «{raw}». Какая у неё словарная форма и что она означает?"
                    elif g.kind=='DEFINITION':
                        text=f"Какое определение у «{self._glabel(g.subject)}»?"
                        self.dialogue.pending_ask={'label':self._glabel(g.subject),'eid':self._gid(g.subject)}
                    elif g.kind in {'RELATION','COMPETENCY_RELATION','COMPETENCY_RELATION_TRUE','COMPETENCY_RELATION_FALSE'}:
                        obj=self._glabel(g.object_value) if g.object_value else None
                        if g.kind=='COMPETENCY_RELATION_FALSE' and obj:
                            text=f"Мне нужно проверить, что неверно: {self._glabel(g.subject)} — {obj}. Можешь уточнить?"
                        else:
                            text=(f"Я всё ещё не знаю, верно ли: {self._glabel(g.subject)} — {obj}. Можешь уточнить?" if obj else f"Мне не хватает знания о {self._glabel(g.subject)}. Можешь объяснить?")
                    elif g.kind=='CAUSAL_RELATION':
                        text=f"Я всё ещё не знаю, есть ли причинная связь: {self._glabel(g.subject)} → {self._glabel(g.object_value)}. Можешь объяснить?"
                    elif g.kind=='CAUSE_OF':
                        text=f"Я не знаю причины для «{self._glabel(g.subject)}». Можешь объяснить?"
                    elif g.kind=='EFFECT_OF':
                        text=f"Я не знаю последствий «{self._glabel(g.subject)}». Можешь объяснить?"
                    elif g.kind=='LANGUAGE_RELATION':
                        text=f"Я не понимаю, какую связь обозначает «{g.subject}». Что это означает здесь?"
                    elif g.kind=='EPISTEMIC_VALIDATION':
                        text='У меня есть правдоподобная гипотеза, но источники, которые её предложили, не могут сами её подтвердить. Нужна независимая проверка из другого семейства источников.'
                    elif g.kind=='RULE_EXAMPLE':
                        st=self.rule_induction.studies.get(g.subject);need=g.object_value
                        obj=self.dialogue.g.label(st.target_object_value) if st and st.target_object_kind=='entity' else (st.target_object_value if st else '?')
                        pol='не ' if st and st.target_polarity=='NEG' else ''
                        human={'TRAIN_POSITIVE':'положительный обучающий пример','TRAIN_NEGATIVE':'контрпример для обучения','VALIDATION_POSITIVE':'независимый положительный проверочный пример','VALIDATION_NEGATIVE':'независимый отрицательный проверочный пример','INDEPENDENT_SOURCE':'пример из независимого источника','DISTINGUISHING_FEATURE':'новый различающий признак, потому что текущие признаки не отделяют правило от контрпримера','NO_SURVIVING_RULE':'новый различающий пример или контрпример','NONMODEL_TRAIN_POSITIVE':'положительный обучающий пример из немодельного источника','NONMODEL_VALIDATION_POSITIVE':'независимый положительный проверочный пример из немодельного источника','NONMODEL_VALIDATION_NEGATIVE':'независимый контрпример из немодельного источника'}.get(need,str(need))
                        text=f"Я проверяю правило про {st.target_relation if st else '?'} → {obj}. Мне нужен {human}, чтобы не принять ложную закономерность."
                    else:text=f"Мне не хватает знания о {self._glabel(g.subject)}. Можешь объяснить?"
                    self.gaps.mark_asked(g.gap_id);self.last_initiative_step=self.step
                    if hm:self._asked_since_user=True
                    emitted.append(self._event('ASK',text,'KNOWLEDGE_GAP',g.priority,g.gap_id,True));continue
            if self.pending_conflicts and ready:
                sid,oid,cause=self.pending_conflicts.popleft();ck=f"{sid}|{oid}"
                rr=self.dialogue.reasoner.evaluate_is_a(sid,oid,principal=self.dialogue.principal,viewer=self.dialogue.principal)
                if rr.value=="CONFLICT" and ck not in self.asked_conflicts and not (hm and (self._machine_label(sid) or self._machine_label(oid))):
                    self.asked_conflicts.add(ck);self.last_initiative_step=self.step
                    if hm:self._asked_since_user=True
                    gid=self.gaps.make_id('CONTRADICTION',sid,'IS_A',oid);self.gaps.mark_asked(gid)
                    text=f"У меня противоречие: {self.dialogue.g.label(sid)} — {self.dialogue.g.label(oid)}. Что считать верным?"
                    emitted.append(self._event("ASK",text,"UNRESOLVED_CONTRADICTION",0.9,cause,True))
                    continue
            if self.pending_questions and ready:
                eid,reason,cause=self.pending_questions.popleft()
                if eid in self.asked:continue
                # Resolve again at emission time: the user may have taught it meanwhile.
                if self.dialogue.g.get_all(eid,"IS_A",viewer=self.dialogue.principal,principal=self.dialogue.principal):
                    continue
                foundational=self.dialogue.g.get(eid,"FOUNDATIONAL",viewer=self.dialogue.principal,principal=self.dialogue.principal)
                if foundational and foundational.object_value=="true":
                    continue
                if hm and self._machine_label(eid):continue
                self.asked.add(eid);self.last_initiative_step=self.step
                if hm:self._asked_since_user=True
                gid=self.gaps.make_id('DEFINITION',eid,'IS_A',None);self.gaps.mark_asked(gid)
                self.dialogue.pending_ask={'label':self.dialogue.g.label(eid),'eid':eid}   # G269: the answer may be elliptic
                emitted.append(self._event("ASK",f"А что такое {self.dialogue.g.label(eid)}?",reason,0.65,gid,True))
        if emitted:self._autosave_tick()
        return [asdict(x) for x in emitted]

    # ------------------------------------------------------------------ G269: persistence
    def attach_checkpoint(self,*,h3=None,meta=None,organs=None):
        """Keep what was loaded with the weights, so saving does not drop it."""
        self._ckpt_h3=h3;self._ckpt_meta=dict(meta or {});self._ckpt_organs=organs

    def save(self,path=None):
        """Atomic compact checkpoint: graph (hot + cold history), runtime state, H3 template, organs.

        G270: with the graph on disk (.c4db) saving is one transaction commit; a .c4m path exports the weights file."""
        import os,tempfile
        g=self.dialogue.g
        if getattr(g,'store_kind','memory')=='sqlite':
            self._flush_disk()
            if path is not None and not str(path).endswith('.c4db') and os.path.abspath(str(path))!=os.path.abspath(g.path):
                from .store_sqlite import export_c4m
                meta=dict(getattr(self,'_ckpt_meta',None) or json.loads(g.meta_get('ckpt_meta','{}') or '{}'))
                meta.update({'saved_by':'C4LivingRuntime.save','runtime_step':self.step})
                export_c4m(g,path,runtime_state=self.runtime_state(),h3=getattr(self,'_ckpt_h3',None),meta=meta,
                           organs=getattr(self,'_ckpt_organs',None))
            self._autosave_pending=0;self._saved_sig=self._persist_signature()
            return path or g.path
        from .checkpoint import save_c4m_compact
        path=str(path);folder=os.path.dirname(os.path.abspath(path))
        fd,tmp=tempfile.mkstemp(prefix='.c4m-',suffix='.tmp',dir=folder);os.close(fd)
        try:
            meta=dict(getattr(self,'_ckpt_meta',{}) or {});meta.update({'saved_by':'C4LivingRuntime.save','runtime_step':self.step})
            save_c4m_compact(tmp,self.dialogue.g,getattr(self,'_ckpt_h3',None),meta=meta,runtime_state=self.runtime_state(),
                             organs=getattr(self,'_ckpt_organs',None))
            os.replace(tmp,path)
        finally:
            if os.path.exists(tmp):os.remove(tmp)
        self._autosave_pending=0;self._saved_sig=self._persist_signature()
        return path

    def flush(self):
        """Commit everything now (a disk graph also commits at the end of every turn by itself)."""
        if getattr(self.dialogue.g,'store_kind','memory')=='sqlite':self._flush_disk()
        elif getattr(self,'_autosave_path',None):self.save(self._autosave_path)

    def close(self):
        """App exit: commit and release the file."""
        self.flush()
        if getattr(self.dialogue.g,'store_kind','memory')=='sqlite':self.dialogue.g.db.close()

    @classmethod
    def open(cls,path,*,autosave:bool=False,audience:Optional[str]=None,principal:str="USER",hydrate_cold:bool=False,
             store:str="auto",progress=None,db_path:Optional[str]=None):
        """One call for an app: load weights + runtime state, keep H3/meta/organs for saving, optionally autosave.

        G270: store='sqlite' (or a .c4db path) keeps the graph on disk: a .c4m is imported once into a sibling .c4db
        (re-imported only if the .c4m changes), start-up does not depend on the model size, and every user turn ends
        with a commit — autosave is always on."""
        path=str(path)
        if store=="sqlite" or (store=="auto" and path.endswith(".c4db")):
            from .store_sqlite import open_or_import
            g=open_or_import(path,progress=progress,db_path=db_path)     # db_path: a writable place if the .c4m is not
            rt=cls(C4ChildDialogue(g,principal=principal))
            rt.load_runtime_state(rt._read_disk_state(g))
            rt._disk_state_hash={}
            if audience:rt.set_audience(audience)
            rt._saved_sig=rt._persist_signature()
            return rt
        from .checkpoint import load_c4m_compact
        g,h,man,rs,organs=load_c4m_compact(path,with_runtime=True,with_organs=True,hydrate_cold=hydrate_cold)
        rt=cls(C4ChildDialogue(g,principal=principal));rt.load_runtime_state(rs)
        rt.attach_checkpoint(h3=h,meta=man.get('meta'),organs=organs or None)
        if autosave:rt.enable_autosave(path)
        if audience:rt.set_audience(audience)
        return rt

    def enable_autosave(self,path,*,every:int=1):
        """Save after every `every` user turns or lessons that changed durable state: facts, entities, the open
        teaching exchange, the question queue (what was taught, and what the child is waiting for, survive a crash)."""
        self._autosave_path=str(path);self._autosave_every=max(1,int(every));self._autosave_pending=0
        self._saved_sig=self._persist_signature()

    # G270: the runtime's own state is stored per part, so a turn writes only the parts that changed
    def _read_disk_state(self,g):
        return g.runtime_state()

    def _flush_disk(self):
        g=self.dialogue.g
        st=self.runtime_state();hashes=getattr(self,'_disk_state_hash',None)
        if hashes is None:hashes=self._disk_state_hash={}
        for k,v in st.items():
            b=json.dumps(v,ensure_ascii=False,separators=(',',':'),sort_keys=True)
            h=hash(b)
            if hashes.get(k)!=h:
                g.meta_put('rs:'+k,b);hashes[k]=h
        if g.meta_get('runtime_state') is not None:     # the imported block is fully superseded by the parts
            g.db.execute("DELETE FROM meta WHERE key='runtime_state'")
        g.flush()

    def _autosave_tick(self,mutated=False):
        g=self.dialogue.g;path=getattr(self,'_autosave_path',None)
        if getattr(g,'store_kind','memory')=='sqlite' and (path is None or str(path).endswith('.c4db') or str(path)==g.path):
            sig=self._persist_signature()
            if mutated or sig!=getattr(self,'_saved_sig',None):self._flush_disk();self._saved_sig=sig
            else:self.dialogue.g.flush()
            return
        if not getattr(self,'_autosave_path',None):return
        if not mutated and self._persist_signature()==getattr(self,'_saved_sig',None):return
        self._autosave_pending=getattr(self,'_autosave_pending',0)+1
        if self._autosave_pending>=self._autosave_every:self.save(self._autosave_path)

    def trace_config(self,config=None,**kwargs):
        """Real runtime-side instrumentation accepted by Emu/Chaquopy adapter.

        Recording is strictly observational, no graph writes. OFF drops pending
        trace rows. NEXT_INTERACTION automatically turns itself off after input.
        """
        c=dict(config or {});c.update(kwargs)
        mode=str(c.get('mode','OFF')).upper()
        scope=str(c.get('scope','CONTINUOUS')).upper()
        if mode not in {'OFF','EVENTS','DECISIONS','DEEP'}:raise ValueError('UNKNOWN_TRACE_MODE')
        if scope not in {'CONTINUOUS','NEXT_INTERACTION'}:raise ValueError('UNKNOWN_TRACE_SCOPE')
        self._trace_mode=mode;self._trace_scope=scope
        self._trace_included=[str(x) for x in (c.get('include') or [])]
        if mode=='OFF':self._trace_outbox.clear()
        return {'accepted':True,'schema':'C4_COGNITIVE_TRACE_V1','mode':mode,'scope':scope,
                'structured':True,'freeFormMonologue':False,
                'availableOwners':['EVAL','COMMIT','DRIVE','MEDIATE'],
                'warning':'Instrumented event ledger, not introspective hidden reasoning'}

    def trace_snapshot(self,request=None,**kwargs):
        """Non-mutating snapshot of actual causal and provenance records."""
        req=dict(request or {});req.update(kwargs)
        cap=max(1,min(80,int(req.get('limit',40))))
        items=list(self.life_events)[-cap:]
        return {'accepted':True,'schema':'C4_COGNITIVE_TRACE_V1',
                'mode':self._trace_mode,'scope':self._trace_scope,
                'internalStep':self.step,'lastExternalEventId':self.semantic_spine.last_external_event_id,
                'actualEventRows':items, 'episodeIndexEvents':len(self.episode_index),
                'graphFacts':len(self.dialogue.g.facts),'worldTruthNotInferred':True,
                'transactions':list(self.semantic_spine.transactions[-min(cap,10):]),
                'pendingInquiries':[dict(q) for q in self.inquiries.values() if q.get('status') in ('OPEN','BACKGROUND')][-10:],
                'lastInquiryEvaluation':self.last_inquiry_evaluation,
                'lastCascade':next((dict(e) for e in reversed(self.life_events) if e.get('kind')=='CASCADE_OUTCOME'),None)}

    def poll(self,limit:int=100):
        out=[];budget=max(0,int(limit))
        for _ in range(min(budget,len(self.outbox))):out.append(asdict(self.outbox.popleft()))
        for _ in range(min(budget-len(out),len(self._trace_outbox))):out.append(self._trace_outbox.popleft())
        return out

    def pending_count(self):return len(self.pending_questions)+len(self.pending_conflicts)

    def bind_sim_receipt_adapter(self,adapter):
        """Host-owned handler; not persisted or callable through user text."""
        if not callable(adapter):raise TypeError('CALLABLE_SIM_HOST_REQUIRED')
        self._sim_receipt_adapter=adapter

    def handle_runtime_command(self,type_,payload):
        """Android typed host channel. Never infer a receipt from USER_MESSAGE."""
        if type_=='SIM_ACTION_RECEIPT' and self._sim_receipt_adapter is not None:
            # The host must confirm that this is its own action receipt.
            confirmed=self._sim_receipt_adapter(dict(payload))
            if confirmed is None:return {'accepted':False,'error':'SIM_HOST_UNCONFIRMED'}
            return structured_cognition.verified_sim_receipt(self,confirmed)
        return {'accepted':False,'error':'CAPABILITY_UNAVAILABLE','command':type_}

    def runtime_state(self):
        self._sync_inquiries()
        return {"schema":"C4_LIVING_RUNTIME_V0.3","step":self.step,"seq":self._seq,
                "pending_questions":list(self.pending_questions),"pending_conflicts":list(self.pending_conflicts),"asked":sorted(self.asked),"asked_conflicts":sorted(self.asked_conflicts),
                "knowledge_gaps":self.gaps.to_dict(),"learning_agenda":self.learning_agenda(8),
                "nursery":self.nursery.to_dict(),
                "spatial_effects":self.spatial_effects.to_dict(),
                "sound_symbol":self.sound_symbol.to_dict(),
                "contact_physics":self.contact_physics.to_dict(),
                "support_physics":self.support_physics.to_dict(),
                "causal_studies":{k:v.to_dict() for k,v in self.causal_studies.items()},
                "hardened_truth_gate":bool(getattr(self.dialogue.g,"hardened_gate",False)),
                "learning_sessions":self.learning.to_dict(),"competencies":self.competencies.to_dict(),"rule_induction":self.rule_induction.to_dict(),"epistemic":self.epistemic.to_dict(),
                "last_initiative_step":self.last_initiative_step,"last_user_step":self.last_user_step,"initiative_cooldown":self.initiative_cooldown,
                "dialogue_focus_eid":self.dialogue.focus_eid,"dialogue_focus_stack":list(getattr(self.dialogue,"focus_stack",[])),
                "dialogue_history":list(self.dialogue_history),"discourse_schema":self.discourse.SCHEMA,
                "semantic_context":list(self.semantic_context),
                "semantic_composition":self.composition.to_dict(),
                "semantic_spine":self.semantic_spine.to_dict(),
                "episode_index":list(self.episode_index.values()),
                "last_inquiry_evaluation":self.last_inquiry_evaluation,
                "life_events":list(self.life_events),"inbound_events":list(self.inbound_events),"external_seq":int(self.external_seq),
                "pending_public_acts":list(self.pending_public_acts),
                "inquiries":[self.inquiries[qid] for qid in self.inquiry_order if qid in self.inquiries],
                "awaiting_response":bool(self.awaiting_response),"human_active":bool(getattr(self,'human_active',True)),
                # An open teaching exchange survives a restart.
                "dialogue_teaching":self._teaching_state(),
                "cognitive_g331":{"goals":self.cognitive_goals,
                     "demonstrations":self.cognitive_demonstrations,"actions":self.cognitive_actions}}

    def _teaching_state(self):
        d=self.dialogue
        return {"teach_root":getattr(d,'teach_root',None),"pending_ask":getattr(d,'pending_ask',None),
                "pending_confirm":getattr(d,'pending_confirm',None),"deferred_asks":list(getattr(d,'deferred_asks',[]))}

    def _restore_teaching_state(self,t):
        d=self.dialogue;ents=d.g.entities
        if not t:return
        d.teach_root=t.get("teach_root") if t.get("teach_root") in ents else None
        pa=t.get("pending_ask")
        d.pending_ask=dict(pa) if isinstance(pa,dict) and (pa.get('eid') is None or pa.get('eid') in ents) else None
        pc=t.get("pending_confirm")
        d.pending_confirm=dict(pc) if isinstance(pc,dict) and pc.get('subject') in ents and pc.get('object') in ents else None
        d.deferred_asks=[x for x in t.get("deferred_asks",[]) if x in ents]

    def _persist_signature(self):
        g=self.dialogue.g
        return (len(g.facts),len(g.entities),g.order,repr(self._teaching_state()),len(self.pending_questions),len(self.asked),
                tuple((q.get('event_id'),q.get('status')) for q in self.inquiries.values()),len(self.inbound_events),self.external_seq,
                tuple((a.get('act_id'),a.get('status'),a.get('reviews',0)) for a in self.pending_public_acts),
                len(self.composition.units),len(self.composition.links),len(self.semantic_spine.events),len(self.semantic_spine.transactions),
                len(self.episode_index),len(self.cognitive_goals),len(self.cognitive_demonstrations),
                tuple((k,v.get('status')) for k,v in self.cognitive_actions.items()),
                self.life_events[-1].get('event_id') if self.life_events else None)

    def load_runtime_state(self,d):
        if not d:return
        self.step=int(d.get("step",0));self._seq=int(d.get("seq",0))
        cog=d.get('cognitive_g331') or {}
        self.cognitive_goals=dict(cog.get('goals') or {})
        self.cognitive_demonstrations=list(cog.get('demonstrations') or [])
        self.cognitive_actions=dict(cog.get('actions') or {})
        self.pending_questions=deque(tuple(x) for x in d.get("pending_questions",[]))
        self.pending_conflicts=deque(tuple(x) for x in d.get("pending_conflicts",[]))
        self.asked=set(d.get("asked",[]));self.asked_conflicts=set(d.get("asked_conflicts",[]));self.last_initiative_step=int(d.get("last_initiative_step",-10**9))
        self.gaps=KnowledgeGapRegistry.from_dict(d.get('knowledge_gaps'))
        self.learning=LearningSessionRegistry.from_dict(d.get('learning_sessions'))
        self.competencies=CompetencyRegistry.from_dict(d.get('competencies'))
        self.rule_induction=RuleInductionOrgan.from_dict(d.get('rule_induction') or {})
        self.epistemic=EpistemicAdmissionOrgan.from_dict(d.get('epistemic') or {})
        if d.get("hardened_truth_gate",False):self.enable_hardened_truth()
        self.causal_studies={str(k):EmpiricalConstraintLearner.from_dict(v) for k,v in (d.get('causal_studies') or {}).items()}
        self.nursery=NurseryState.from_dict(d['nursery']) if d.get('nursery') else NurseryState()
        self.spatial_effects=SpatialEffectLearner.from_dict(d.get('spatial_effects') or {})
        self.sound_symbol=SoundSymbolBridge.from_dict(d.get('sound_symbol') or {})
        self.contact_physics=ContactEffortLearner.from_dict(d.get('contact_physics') or {})
        self.support_physics=SupportFallLearner.from_dict(d.get('support_physics') or {})
        self.dialogue.reasoner.rule_induction=self.rule_induction
        self.sync_competencies()
        self.last_user_step=int(d.get("last_user_step",0))
        self.initiative_cooldown=int(d.get("initiative_cooldown",self.initiative_cooldown))
        self.dialogue.focus_eid=d.get("dialogue_focus_eid")
        self.dialogue.focus_stack=[x for x in d.get("dialogue_focus_stack",[]) if x in self.dialogue.g.entities][-12:]
        self.dialogue_history=deque((x for x in d.get("dialogue_history",[]) if isinstance(x,dict)),maxlen=64)
        self.life_events=deque((x for x in d.get("life_events",[]) if isinstance(x,dict)),maxlen=512)
        self.semantic_context=deque((dict(x) for x in d.get("semantic_context",[]) if isinstance(x,dict) and x.get("eid") in self.dialogue.g.entities),maxlen=96)
        self.composition=SemanticComposition.from_dict(d.get("semantic_composition") or {})
        self.semantic_spine=SemanticSpine.from_dict(d.get("semantic_spine") or {})
        self.last_inquiry_evaluation=d.get("last_inquiry_evaluation")
        self.episode_index={str(e['event_id']):dict(e) for e in d.get('episode_index',[])
                            if isinstance(e,dict) and e.get('event_id')}
        # Backfill upgraded G327 checkpoints from recorded non-authoritative
        # external transport events; no teaching/reasoning is replayed.
        for eid,ev in self.semantic_spine.events.items():
            if ev.get('actor')=='OTHER' and eid not in self.episode_index:
                self.episode_index[eid]=index_event(eid,ev.get('external_order',0),ev.get('payload',''))
        self.dialogue.set_context_entities(self._recent_context_eids())
        self.inbound_events=deque((dict(x) for x in d.get("inbound_events",[]) if isinstance(x,dict)))
        self.pending_public_acts=deque((dict(x) for x in d.get("pending_public_acts",[]) if isinstance(x,dict)))
        self.external_seq=int(d.get("external_seq",0))
        self.inquiries={};self.inquiry_order=deque(maxlen=128)
        for q in d.get("inquiries",[]):
            if isinstance(q,dict) and q.get('event_id'):
                q=dict(q);self.inquiries[q['event_id']]=q;self.inquiry_order.append(q['event_id'])
        self.awaiting_response=bool(d.get("awaiting_response",False))
        self._sync_inquiries()
        self.human_active=bool(d.get("human_active",getattr(self,'human_active',False)))
        self._restore_teaching_state(d.get("dialogue_teaching"))