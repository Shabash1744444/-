"""C4 M1-M3: executable four-owner cognitive state machine, source-bounded.

This is an experimental *structured* cognition substrate, not general Russian NLU,
AGI, or a reinvention of the established C4 learned organism.
"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict, replace
from enum import Enum
from typing import Any, Callable, Iterable, Mapping
from pathlib import Path
import hashlib
import json
import os


class Scope(str, Enum):
    WORLD = 'WORLD'                # verified external observation only
    SOURCE = 'SOURCE_ASSERTION'    # source said a proposition
    STORY = 'NARRATIVE'            # true *inside* named fictional scene
    SIM = 'SIMULATION'             # simulator state, never physical-world receipt
    SELF = 'SELF_REPORT'
    LANGUAGE = 'LANGUAGE'


class Act(str, Enum):
    ANSWER = 'ANSWER'
    ASK = 'ASK'
    THINK = 'THINK'
    WAIT = 'WAIT'
    REVISE = 'REVISE'
    SEND = 'SEND'
    SENSE = 'SENSE'


class Verdict(str, Enum):
    ADMIT = 'ADMIT'
    DOWNGRADE = 'DOWNGRADE_TO_SOURCE'
    REJECT = 'REJECT'


class CommitDenied(ValueError):
    pass


@dataclass(frozen=True)
class Proposition:
    predicate: str
    args: tuple[str, ...]

    def __post_init__(self):
        object.__setattr__(self, 'args', tuple(self.args))
        if (not isinstance(self.predicate, str) or not self.predicate or not self.args
                or any(not isinstance(x, str) or not x for x in self.args)):
            raise ValueError('Predicate and all arguments must be nonempty strings')


@dataclass(frozen=True)
class Perspective:
    """Arbitrary finite nested holder frames: nested thoughts/quotes/beliefs."""
    holder: str
    mode: str
    content: Proposition | 'Perspective'

    def __post_init__(self):
        if not self.holder or not self.mode:
            raise ValueError('Perspective holder and mode required')


Meaning = Proposition | Perspective


@dataclass(frozen=True)
class Event:
    id: str
    actor: str
    kind: str
    payload: Meaning | str | None
    scope: Scope
    scene: str
    roots: tuple[str, ...]
    parents: tuple[str, ...]
    step: int
    received_at: float
    claimed_at: float | None
    receipt_id: str | None = None


@dataclass(frozen=True)
class Candidate:
    event_id: str
    content: Meaning
    scope: Scope
    scene: str
    roots: tuple[str, ...]
    status: str = 'HYPOTHESIS'
    id: str = ''  # EVAL-generated registration; unregistered data cannot be admitted


@dataclass(frozen=True)
class Claim:
    id: str
    content: Meaning
    scope: Scope
    scene: str
    roots: tuple[str, ...]
    event_ids: tuple[str, ...]
    status: str
    committed_step: int
    claimed_at: float | None
    retracted_at: float | None = None


@dataclass(frozen=True)
class Query:
    predicate: str
    args: tuple[str | None, ...]  # None = variable binding
    scope: Scope
    scene: str = 'default'
    perspective: tuple[tuple[str, str], ...] = ()  # outer -> inner holder,mode
    as_of: float | None = None # event-time bound, not reception time

    def __post_init__(self):
        object.__setattr__(self, 'args', tuple(self.args))
        object.__setattr__(self, 'perspective', tuple(tuple(x) for x in self.perspective))


@dataclass(frozen=True)
class Answer:
    status: str
    bindings: tuple[tuple[str, ...], ...]
    claim_ids: tuple[str, ...]
    roots: tuple[str, ...]
    scope: Scope
    scene: str
    reason: str


@dataclass(frozen=True)
class Action:
    id: str
    kind: Act
    subject: str
    utility: float
    proposed_by: str = 'EVAL'


@dataclass(frozen=True)
class Authorization:
    id: str
    action_id: str
    kind: Act
    decision_step: int


@dataclass(frozen=True)
class Receipt:
    id: str
    action_id: str
    state: str
    verified: bool
    boundary: str
    event_id: str


@dataclass(frozen=True)
class Demonstration:
    premises: tuple[Proposition, ...]
    consequence: Proposition
    successful: bool


@dataclass(frozen=True)
class Example:
    premises: tuple[Proposition, ...]
    consequence: Proposition
    scope: Scope
    scene: str
    root: str
    successful: bool


@dataclass(frozen=True)
class Rule:
    """Restricted unary relational generalization, gained from distinct demonstrations.

    This rule learner is deliberately small, explicit, counterexample-aware;
    it cannot discover arbitrary causal laws or universal language grammar.
    """
    premises: tuple[str, ...]
    consequence: str
    scope: Scope
    supporting_roots: tuple[str, ...]
    exceptions: tuple[str, ...] = ()
    active: bool = True
    scene: str = 'default'  # local simulation/story scope; no cross-scene leakage


class C4:
    VERSION = 'C4_EXECUTABLE_SPINE_M1_M3_V2_GUARDS'
    LEGACY_VERSIONS = ('C4_EXECUTABLE_SPINE_M1_M3_V1',)
    MAX_PERSPECTIVE_DEPTH = 64
    MAX_TRACE_EVENTS = 5000
    INFLUENCES = ('MASK', 'VALUE', 'AVAIL', 'TRIGGER', 'STATUS')
    OWNERS = ('EVAL', 'COMMIT', 'DRIVE', 'MEDIATE')

    def __init__(self, *, trusted_sensors: Mapping[str, Callable[[], tuple[Proposition, bool]]] | None = None):
        # Only host code may supply adapters; user events cannot register one.
        self._trusted_sensors = dict(trusted_sensors or {})
        self._events: dict[str, Event] = {}
        self._claims: dict[str, Claim] = {}
        self._candidates: dict[str, Candidate] = {}
        self._actions: dict[str, Action] = {}
        self._auth: dict[str, Authorization] = {}
        self._receipts: dict[str, Receipt] = {}
        self._trace: list[dict[str, Any]] = []
        self._questions: dict[str, dict[str, Any]] = {}
        self._examples: list[Example] = []
        self._rules: dict[str, Rule] = {}
        self._step = 0
        self._seq = 0
        self._hyp_seq = 0  # ephemeral EVAL proposals do not change canonical state
        self._trace_enabled = True
        self._pending: list[Action] = []

    @property
    def events(self) -> tuple[Event, ...]:
        return tuple(self._events.values())

    @property
    def claims(self) -> tuple[Claim, ...]:
        return tuple(self._claims.values())

    @property
    def rules(self) -> tuple[Rule, ...]:
        return tuple(self._rules.values())

    @property
    def trace(self) -> tuple[dict[str, Any], ...]:
        return tuple(dict(row) for row in self._trace)

    @property
    def step(self) -> int:
        return self._step

    def _id(self, prefix: str) -> str:
        self._seq += 1
        return f'{prefix}{self._seq:09d}'

    def _record(self, owner: str, influence: str, operation: str, **kw):
        if owner not in self.OWNERS or influence not in self.INFLUENCES:
            raise ValueError('Invalid constitutional owner or influence')
        if self._trace_enabled:
            self._trace.append({'step': self._step, 'owner': owner,
                                'influence': influence, 'operation': operation, **kw})
            if len(self._trace) > self.MAX_TRACE_EVENTS:
                del self._trace[:len(self._trace) - self.MAX_TRACE_EVENTS]

    def set_trace(self, enabled: bool):
        self._trace_enabled = bool(enabled)

    @staticmethod
    def _meaning_depth(p: Meaning) -> int:
        return 1 if isinstance(p, Proposition) else 1 + C4._meaning_depth(p.content)

    def receive(self, actor: str, content: Meaning | str | None, *,
                kind='ASSERT', scope: Scope = Scope.SOURCE, scene='default',
                parents: Iterable[str] = (), roots: Iterable[str] | None = None,
                received_at: float = 0, claimed_at: float | None = None,
                receipt_id: str | None = None) -> Event:
        """INGEST: no truth admission. roots of relayed events MUST be inherited.
        Fake received-at/claimed-at never count as verified-world receipt.
        """
        if not actor or not scene: raise ValueError('actor/scene required')
        # Enforce a resource budget at ingest, not after deep recursive decoding.
        if isinstance(content, (Proposition, Perspective)):
            cursor, depth = content, 0
            while isinstance(cursor, Perspective):
                depth += 1
                if depth > self.MAX_PERSPECTIVE_DEPTH:
                    raise CommitDenied('PERSPECTIVE_DEPTH_BUDGET_EXCEEDED')
                cursor = cursor.content
            if not isinstance(cursor, Proposition):
                raise TypeError('Nested meaning must terminate at a typed proposition')
        if actor == 'C4':
            raise CommitDenied('C4-origin public events require MEDIATE authorization')
        parents = tuple(parents)
        if any(x not in self._events for x in parents):
            raise ValueError('Unknown causal parent')
        if roots is not None and not parents:
            raise CommitDenied('Unparented event cannot claim arbitrary independent roots')
        if roots is not None and not tuple(roots):
            raise CommitDenied('Evidence lineage cannot be erased by a relayed event')
        if roots is not None and parents:
            parent_roots = set().union(*(set(self._events[x].roots) for x in parents))
            if not set(roots).issubset(parent_roots):
                raise CommitDenied('Relayed evidence cannot mint its own roots')
        if roots is None and parents:
            roots = tuple(sorted(set().union(*(set(self._events[x].roots) for x in parents))))
        eid = self._id('ev')
        if roots is None:
            roots = (eid,)
        roots = tuple(sorted(set(roots)))
        self._step += 1
        ev = Event(eid, actor, kind, content, Scope(scope), scene, roots,
                   parents, self._step, float(received_at), claimed_at, receipt_id)
        self._events[eid] = ev
        self._record('EVAL', 'TRIGGER', 'INGEST', event_id=eid, kind=kind,
                     root_ids=list(roots), actor=actor)
        return ev

    def replay_source(self, source_event_id: str, *, actor='RELAY') -> Event:
        src = self._events[source_event_id]
        return self.receive(actor, src.payload, kind='REPLAY', scope=src.scope,
                            scene=src.scene, parents=(source_event_id,))

    def evaluate(self, event_id: str) -> Candidate | None:
        """EVAL hypotheses can be evaluated repeatedly; they are not facts."""
        ev = self._events[event_id]
        if not isinstance(ev.payload, (Proposition, Perspective)):
            self._record('EVAL', 'STATUS', 'NO_SEMANTIC_CANDIDATE', event_id=event_id)
            return None
        self._hyp_seq += 1
        cid = f'cand{self._hyp_seq:09d}'
        candidate = Candidate(event_id, ev.payload, ev.scope, ev.scene, ev.roots, id=cid)
        self._candidates[cid] = candidate
        self._record('EVAL', 'AVAIL', 'CANDIDATE', candidate_id=cid,
                     event_id=event_id, roots=list(ev.roots), depth=self._meaning_depth(ev.payload))
        return candidate

    def commit(self, candidate: Candidate, *, target: Scope | None = None,
               world_receipt_id: str | None = None) -> tuple[Verdict, Claim]:
        """COMMIT is the *only* way to create a recognized Claim.
        Unverified WORLD proposals are downgraded to sourced claims.
        """
        if not candidate.id or self._candidates.get(candidate.id) != candidate:
            raise CommitDenied('Unregistered or modified EVAL candidate')
        if candidate.event_id not in self._events:
            raise CommitDenied('Candidate event not in the causal life-line')
        source = self._events[candidate.event_id]
        if (candidate.content != source.payload or candidate.roots != source.roots
                or candidate.scope != source.scope or candidate.scene != source.scene
                or candidate.status != 'HYPOTHESIS'):
            raise CommitDenied('Candidate does not match original event content/scope/scene')
        scope = Scope(target or candidate.scope)
        verdict = Verdict.ADMIT
        if scope == Scope.WORLD:
            r = self._receipts.get(world_receipt_id or '')
            if not (r and r.verified and r.boundary == 'EXTERNAL_SENSOR'
                    and r.event_id == source.id):
                scope = Scope.SOURCE
                verdict = Verdict.DOWNGRADE
        elif scope != candidate.scope:
            # Prevent a source/fiction assertion being reassigned to another truth scope.
            raise CommitDenied('Scope escalation or change without a lawful basis')
        # Same root, same semantic content and scope -> provenance remains dependent.
        for old in self._claims.values():
            if (old.content == candidate.content and old.scope == scope
                and old.scene == candidate.scene and old.status == 'ACTIVE'
                and old.roots == candidate.roots):
                self._record('COMMIT', 'STATUS', 'DEPENDENT_DUPLICATE', claim_id=old.id)
                return verdict, old
        self._step += 1
        claim = Claim(self._id('cl'), candidate.content, scope, candidate.scene,
                      candidate.roots, (source.id,), 'ACTIVE', self._step, source.claimed_at)
        self._claims[claim.id] = claim
        self._record('COMMIT', 'STATUS', verdict.value, claim_id=claim.id,
                     scope=scope.value, event_id=source.id, roots=list(source.roots))
        return verdict, claim

    def teach(self, actor: str, content: Meaning, *, scope=Scope.SOURCE,
              scene='default', claimed_at: float | None = None) -> tuple[Verdict, Claim]:
        ev = self.receive(actor, content, scope=scope, scene=scene, claimed_at=claimed_at)
        candidate = self.evaluate(ev.id)
        assert candidate is not None
        return self.commit(candidate)

    def retract(self, claim_id: str, *, basis_event_id: str) -> Claim:
        if claim_id not in self._claims or basis_event_id not in self._events:
            raise CommitDenied('Retraction needs existing claim and source event')
        old = self._claims[claim_id]
        basis = self._events[basis_event_id]
        # A correction by same original actor or externally verified evidence only.
        first_source = self._events[old.event_ids[0]]
        if basis.actor != first_source.actor:
            raise CommitDenied('Only original source may retract its claim via this API')
        same_slot = (isinstance(basis.payload, Proposition)
                     and isinstance(old.content, Proposition)
                     and basis.payload.predicate == old.content.predicate
                     and basis.payload.args[:1] == old.content.args[:1])
        explicit_target = (basis.kind == 'CORRECTION' and first_source.id in basis.parents)
        if not (basis.scene == old.scene and basis.scope == old.scope
                and (same_slot or explicit_target)):
            raise CommitDenied('Retraction basis does not identify the original claim or its slot')
        if old.status != 'ACTIVE': return old
        self._step += 1
        new = replace(old, status='RETRACTED', retracted_at=basis.claimed_at)
        self._claims[claim_id] = new
        self._record('COMMIT', 'STATUS', 'RETRACT', claim_id=claim_id,
                     basis_event_id=basis_event_id, old_status='ACTIVE', new_status='RETRACTED')
        return new

    @staticmethod
    def _unwrap(content: Meaning, perspective: tuple[tuple[str, str], ...]) -> Proposition | None:
        x = content
        for holder, mode in perspective:
            if not isinstance(x, Perspective) or x.holder != holder or x.mode != mode:
                return None
            x = x.content
        return x if isinstance(x, Proposition) else None

    def query(self, query: Query) -> Answer:
        """Read-only semantically typed matching, not lexical retrieval.
        Rule inferences stay candidates, not admitted WORLD facts.
        """
        bindings: list[tuple[str, ...]] = []
        refs: list[str] = []
        roots: set[str] = set()
        for c in self._claims.values():
            if c.scope != query.scope or c.scene != query.scene:
                continue
            if query.as_of is not None and (c.claimed_at is None or c.claimed_at > query.as_of):
                continue
            if c.status == 'RETRACTED':
                if query.as_of is None or c.retracted_at is None or c.retracted_at <= query.as_of:
                    continue
            elif c.status != 'ACTIVE':
                continue
            p = self._unwrap(c.content, query.perspective)
            if p is None or p.predicate != query.predicate or len(p.args) != len(query.args):
                continue
            if all(q is None or q == a for q, a in zip(query.args, p.args)):
                bindings.append(p.args); refs.append(c.id); roots.update(c.roots)
        if bindings:
            ans = Answer('SUPPORTED', tuple(bindings), tuple(refs),
                         tuple(sorted(roots)), query.scope, query.scene, 'MATCHED_SCOPED_CLAIMS')
        else:
            ans = self._infer(query)
        self._record('EVAL', 'AVAIL', 'QUERY', predicate=query.predicate,
                     scope=query.scope.value, scene=query.scene, status=ans.status,
                     claim_ids=list(ans.claim_ids), root_ids=list(ans.roots))
        return ans

    def _infer(self, query: Query) -> Answer:
        if query.perspective or len(query.args) != 1 or query.args[0] is None:
            return Answer('UNKNOWN', (), (), (), query.scope, query.scene, 'NO_SUPPORTED_RELATION')
        entity = query.args[0]
        for rule in self._rules.values():
            if (not rule.active or rule.scope != query.scope or rule.scene != query.scene
                    or rule.consequence != query.predicate):
                continue
            if entity in rule.exceptions: continue
            matches: list[Claim] = []
            for pred in rule.premises:
                options = [c for c in self._claims.values()
                           if c.status == 'ACTIVE' and c.scope == query.scope
                           and c.scene == query.scene
                           and isinstance(c.content, Proposition)
                           and c.content.predicate == pred and c.content.args == (entity,)]
                if not options: break
                matches.append(options[0])
            else:
                roots = set(rule.supporting_roots)
                for c in matches: roots.update(c.roots)
                return Answer('INFERRED', ((entity,),), tuple(c.id for c in matches),
                              tuple(sorted(roots)), query.scope, query.scene,
                              'GENERALIZATION_CANDIDATE_NOT_OBSERVATION')
        return Answer('UNKNOWN', (), (), (), query.scope, query.scene, 'NO_SUPPORTED_RELATION')

    def propose(self, kind: Act, subject: str, utility: float) -> Action:
        if not isinstance(kind, Act): kind = Act(kind)
        if not subject: raise ValueError('Action subject required')
        action = Action(self._id('act'), kind, subject, float(utility))
        self._actions[action.id] = action
        self._pending.append(action)
        self._record('EVAL', 'VALUE', 'ACTION_CANDIDATE', action_id=action.id, kind=kind.value)
        return action

    def arbitrate(self) -> Authorization:
        if not self._pending:
            self.propose(Act.WAIT, 'NO_PENDING_ACTION', utility=0.0)
        # deterministic sole DRIVE arbitration, no special pending-ASK lock
        best = max(self._pending, key=lambda a: (a.utility, -int(a.id[3:])))
        self._pending.remove(best)
        self._step += 1
        a = Authorization(self._id('auth'), best.id, best.kind, self._step)
        self._auth[a.id] = a
        self._record('DRIVE', 'STATUS', 'SELECT', authorization=a.id,
                     action_id=best.id, kind=best.kind.value,
                     remaining=[x.id for x in self._pending])
        return a

    def mediate(self, auth_id: str, *, delivered=False, boundary='PUBLIC_CHAT') -> Receipt:
        """SENT never implies DELIVERED. Internal THINK/WAIT are not outside events."""
        if auth_id not in self._auth: raise CommitDenied('DRIVE authorization required')
        if delivered:
            raise CommitDenied('Delivery requires an external verified boundary receipt; boolean is not evidence')
        auth = self._auth.pop(auth_id)
        action = self._actions[auth.action_id]
        if auth.kind in (Act.THINK, Act.WAIT, Act.REVISE):
            state = 'INTERNAL'
        else:
            state = 'DELIVERED' if delivered else 'SENT'
        # Only this MEDIATE path can emit C4-origin public/internal events.
        eid_value = self._id('ev')
        self._step += 1
        eid = Event(eid_value, 'C4', auth.kind.value, action.subject, Scope.SELF,
                    'self', (eid_value,), (), self._step, 0.0, None)
        self._events[eid.id] = eid
        self._record('MEDIATE', 'TRIGGER', 'SELF_EVENT_INGEST', event_id=eid.id,
                     authorization=auth.id, kind=auth.kind.value)
        rid = self._id('rcpt')
        receipt = Receipt(rid, action.id, state, bool(delivered), boundary, eid.id)
        self._receipts[rid] = receipt
        self._record('MEDIATE', 'STATUS', state, receipt_id=rid, auth_id=auth_id,
                     event_id=eid.id, verified=receipt.verified)
        return receipt

    def sense(self, sensor_id: str, observe: Callable[[], tuple[Proposition, bool]] | None = None, *,
              scene='default', received_at: float = 0, claimed_at: float | None = None):
        """MEDIATE requires host-bound sensor adapters. Callback verification is
        host attestation, NOT cryptographic certainty about external reality.
        No ordinary user message can forge this receipt through COMMIT.
        """
        if sensor_id not in self._trusted_sensors:
            raise CommitDenied('Unregistered sensor is not a trusted WORLD observation boundary')
        if observe is not None and observe is not self._trusted_sensors[sensor_id]:
            raise CommitDenied('Cannot replace host-bound sensor callback at runtime')
        action = self.propose(Act.SENSE, f'READ:{sensor_id}', 2.0)
        auth = self.arbitrate()
        if auth.action_id != action.id:
            raise CommitDenied('DRIVE did not authorize this sensory action')
        self._auth.pop(auth.id)
        proposition, adapter_verified = self._trusted_sensors[sensor_id]()
        if not isinstance(proposition, Proposition):
            raise TypeError('Sensor adapter must return a Proposition')
        scope = Scope.WORLD if adapter_verified else Scope.SOURCE
        ev = self.receive(sensor_id, proposition, kind='SENSOR_RECEIPT', scope=scope,
                          scene=scene, received_at=received_at, claimed_at=claimed_at)
        receipt = Receipt(self._id('rcpt'), action.id, 'OBSERVED' if adapter_verified else 'UNVERIFIED',
                          bool(adapter_verified), 'EXTERNAL_SENSOR', ev.id)
        self._receipts[receipt.id] = receipt
        self._record('MEDIATE','STATUS',receipt.state, receipt_id=receipt.id,
                     event_id=ev.id, sensor=sensor_id)
        candidate = self.evaluate(ev.id)
        assert candidate is not None
        verdict, claim = self.commit(candidate, world_receipt_id=receipt.id)
        return receipt, verdict, claim

    def respond(self, query: Query) -> tuple[Answer, Receipt]:
        ans = self.query(query)
        if ans.status == 'UNKNOWN':
            text = f'Не установлено ({query.scope.value}/{query.scene}); нужен источник.'
        else:
            text = f'{ans.status} {query.predicate}: {ans.bindings} ({query.scope.value}/{query.scene})'
        outgoing = self.propose(Act.ANSWER, text, utility=1.0)
        a = self.arbitrate()
        # DRIVE may lawfully choose a different higher-value action: no fake answer.
        if a.action_id != outgoing.id:
            receipt = self.mediate(a.id, delivered=False)
            deferred = Answer('DEFERRED', (), ans.claim_ids, ans.roots, ans.scope,
                              ans.scene, 'DRIVE_SELECTED_DIFFERENT_ACTION')
            return deferred, receipt
        # External transport receipt has not been supplied.
        return ans, self.mediate(a.id, delivered=False)

    def open_gap(self, topic: str, human_question: str, *, utility=0.6) -> str:
        qid = self._id('gap')
        self._questions[qid] = {'topic': topic, 'question': human_question,
                                'status': 'OPEN', 'utility': utility, 'asked_event': None}
        self._record('EVAL', 'TRIGGER', 'GAP_OPEN', gap_id=qid)
        return qid

    def receive_gap_answer(self, gap_id: str, actor: str, proposition: Proposition):
        if gap_id not in self._questions: raise KeyError(gap_id)
        gap = self._questions[gap_id]
        topic = gap['topic'].casefold()
        if topic not in (proposition.predicate.casefold(), *(x.casefold() for x in proposition.args)):
            self.receive(actor, proposition, kind='UNRELATED_GAP_MESSAGE', scope=Scope.SOURCE)
            self._record('EVAL','STATUS','UNRELATED_GAP_ANSWER',gap_id=gap_id)
            return None
        _, cl = self.teach(actor, proposition, scope=Scope.SOURCE)
        gap['candidate_claim'] = cl.id
        gap['status'] = 'ANSWER_CANDIDATE'  # not automatically verified or resolved
        self._record('COMMIT', 'STATUS', 'GAP_ANSWER_CANDIDATE', gap_id=gap_id,
                     claim_id=cl.id)
        return cl

    def tick(self) -> Receipt:
        """Can independently initiate ASK, or spend a cycle thinking/waiting."""
        already = {self._events[q['asked_event']].payload for q in self._questions.values()
                   if q.get('asked_event') in self._events}
        for qid, q in self._questions.items():
            if q['status'] == 'OPEN' and not q['asked_event'] and q['question'] not in already:
                self.propose(Act.ASK, q['question'], q['utility'])
                action = self.arbitrate()
                receipt = self.mediate(action.id)
                if action.kind == Act.ASK:
                    q['asked_event'] = receipt.event_id
                return receipt
        self.propose(Act.THINK, 'REFLECT_ON_OPEN_GAPS', utility=0.1)
        action = self.arbitrate()
        return self.mediate(action.id)

    def own_asks(self) -> tuple[str, ...]:
        return tuple(ev.payload for ev in self._events.values()
                     if ev.actor == 'C4' and ev.kind == 'ASK' and isinstance(ev.payload, str))

    def learn_example(self, actor: str, premises: Iterable[Proposition],
                      consequence: Proposition, *, scope=Scope.SIM, scene='default',
                      successful=True) -> Rule | None:
        ps = tuple(premises)
        if Scope(scope) == Scope.WORLD:
            raise CommitDenied('WORLD rules require independently verified evidence; teaching is not observation')
        ev = self.receive(actor, Demonstration(ps, consequence, bool(successful)),
                          kind='DEMONSTRATION', scope=scope, scene=scene)
        return self.add_example(ps, consequence, ev.id, successful=successful)

    def add_example(self, premises: Iterable[Proposition], consequence: Proposition,
                    event_id: str, *, successful=True) -> Rule | None:
        """Generalize same-subject unary predicate regularity across independent demos.
        Two distinct roots and subjects required; exceptions deactivate a rule.
        Never commits a predicted consequent as a world observation.
        """
        event = self._events[event_id]
        if event.scope == Scope.WORLD:
            raise CommitDenied('Unverified demonstrations cannot train WORLD rules')
        ps = tuple(premises)
        if (event.kind != 'DEMONSTRATION' or not isinstance(event.payload, Demonstration)
            or event.payload != Demonstration(ps, consequence, bool(successful))):
            raise CommitDenied('Learning example must be backed by its exact source demonstration event')
        if not ps or any(len(p.args) != 1 for p in ps) or len(consequence.args) != 1:
            raise ValueError('Current learner accepts unary examples only')
        subject = consequence.args[0]
        if any(p.args[0] != subject for p in ps):
            raise ValueError('Demonstration subject must agree')
        example = Example(ps, consequence, event.scope, event.scene, event.roots[0], bool(successful))
        self._examples.append(example)
        key = (tuple(sorted(p.predicate for p in ps)), consequence.predicate, event.scope, event.scene)
        positive = [x for x in self._examples
                    if x.successful and (tuple(sorted(p.predicate for p in x.premises)),
                                         x.consequence.predicate, x.scope, x.scene) == key]
        negative = [x for x in self._examples
                    if not x.successful and (tuple(sorted(p.predicate for p in x.premises)),
                                             x.consequence.predicate, x.scope, x.scene) == key]
        support_roots = tuple(sorted({x.root for x in positive}))
        subjects = {x.consequence.args[0] for x in positive}
        rid = ':'.join((*key[0], key[1], event.scope.value, event.scene))
        exceptions = tuple(sorted({x.consequence.args[0] for x in negative}))
        active = len(support_roots) >= 2 and len(subjects) >= 2
        rule = Rule(key[0], key[1], event.scope, support_roots, exceptions, active, event.scene)
        self._rules[rid] = rule
        self._record('EVAL', 'STATUS', 'INDUCTIVE_RULE_CANDIDATE',
                     rule_id=rid, active=active, independent_example_roots=len(support_roots),
                     exception_count=len(exceptions))
        return rule if active else None

    # Persistence: no pickle, check content hash; public state fully derived from snapshot.
    @staticmethod
    def _encode(x: Any) -> Any:
        if isinstance(x, Enum): return x.value
        if isinstance(x, Proposition): return {'_type': 'P', 'predicate': x.predicate, 'args': list(x.args)}
        if isinstance(x, Perspective): return {'_type': 'F', 'holder': x.holder, 'mode': x.mode, 'content': C4._encode(x.content)}
        if isinstance(x, Demonstration): return {'_type':'D','premises':C4._encode(x.premises),'consequence':C4._encode(x.consequence),'successful':x.successful}
        if isinstance(x, tuple): return [C4._encode(v) for v in x]
        if isinstance(x, list): return [C4._encode(v) for v in x]
        if isinstance(x, dict): return {k:C4._encode(v) for k,v in x.items()}
        if hasattr(x, '__dataclass_fields__'):
            return {k:C4._encode(getattr(x,k)) for k in x.__dataclass_fields__}
        return x

    @staticmethod
    def _decode_meaning(x: Any):
        if isinstance(x, dict) and x.get('_type') == 'P':
            return Proposition(x['predicate'], tuple(x['args']))
        if isinstance(x, dict) and x.get('_type') == 'F':
            return Perspective(x['holder'], x['mode'], C4._decode_meaning(x['content']))
        if isinstance(x, dict) and x.get('_type') == 'D':
            return Demonstration(tuple(C4._decode_meaning(y) for y in x['premises']), C4._decode_meaning(x['consequence']),x['successful'])
        return x

    def _snapshot(self) -> dict[str, Any]:
        return {'version': self.VERSION, 'step': self._step, 'seq': self._seq,
                'events': [self._encode(e) | {'payload': self._encode(e.payload)} for e in self._events.values()],
                'claims': [self._encode(c) | {'content': self._encode(c.content)} for c in self._claims.values()],
                'questions': self._questions,
                'examples': [self._encode(e) for e in self._examples],
                'rules': [self._encode(r) for r in self._rules.values()],
                'actions': [self._encode(a) for a in self._actions.values()],
                'auth': [self._encode(a) for a in self._auth.values()],
                'receipts': [self._encode(r) for r in self._receipts.values()],
                'pending': [x.id for x in self._pending]}

    def snapshot_hash(self) -> str:
        data = json.dumps(self._snapshot(), sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()
        return hashlib.sha256(data).hexdigest()

    def save(self, path: str | Path) -> str:
        p = Path(path)
        obj = self._snapshot()
        raw = json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
        checksum = hashlib.sha256(raw).hexdigest()
        wrapper = json.dumps({'sha256': checksum, 'payload': obj}, ensure_ascii=False, sort_keys=True).encode('utf-8')
        tmp = p.with_suffix(p.suffix+'.tmp')
        with open(tmp, 'wb') as f:
            f.write(wrapper); f.flush(); os.fsync(f.fileno())
        os.replace(tmp,p)
        return checksum

    @classmethod
    def load(cls, path: str | Path, *, trusted_sensors: Mapping[str, Callable[[], tuple[Proposition, bool]]] | None = None) -> 'C4':
        doc = json.loads(Path(path).read_text('utf-8'))
        obj = doc['payload']
        raw = json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
        if hashlib.sha256(raw).hexdigest() != doc['sha256']:
            raise ValueError('CHECKPOINT_INTEGRITY_FAILURE')
        if obj['version'] not in (cls.VERSION, *cls.LEGACY_VERSIONS):
            raise ValueError('UNSUPPORTED_STATE_VERSION')
        c = cls(trusted_sensors=trusted_sensors); c._step=obj['step']; c._seq=obj['seq']
        for v in obj['events']:
            e = Event(v['id'],v['actor'],v['kind'],cls._decode_meaning(v['payload']),Scope(v['scope']),
                      v['scene'],tuple(v['roots']),tuple(v['parents']),v['step'],v['received_at'],v['claimed_at'],v['receipt_id'])
            c._events[e.id] = e
        for v in obj['claims']:
            z = Claim(v['id'],cls._decode_meaning(v['content']),Scope(v['scope']),v['scene'],tuple(v['roots']),
                      tuple(v['event_ids']),v['status'],v['committed_step'],v['claimed_at'],v.get('retracted_at'))
            c._claims[z.id]=z
        c._questions=obj['questions']
        for v in obj['examples']:
            c._examples.append(Example(tuple(cls._decode_meaning(p) for p in v['premises']),
                                       cls._decode_meaning(v['consequence']),Scope(v['scope']),
                                       v['scene'],v['root'],v['successful']))
        for v in obj['rules']:
            r=Rule(tuple(v['premises']),v['consequence'],Scope(v['scope']),tuple(v['supporting_roots']),
                   tuple(v['exceptions']),v['active'],v.get('scene','default'))
            c._rules[':'.join((*r.premises,r.consequence,r.scope.value,r.scene))]=r
        for v in obj['actions']:
            a=Action(v['id'],Act(v['kind']),v['subject'],v['utility'],v['proposed_by']);c._actions[a.id]=a
        for v in obj['auth']:
            a=Authorization(v['id'],v['action_id'],Act(v['kind']),v['decision_step']);c._auth[a.id]=a
        for v in obj['receipts']:
            r=Receipt(v['id'],v['action_id'],v['state'],v['verified'],v['boundary'],v['event_id']);c._receipts[r.id]=r
        c._pending=[c._actions[a] for a in obj['pending']]
        return c
