# C4 DIRECTIONS RECOVERED FROM LIVE CHAT — 2026-10-08

This file records the implementation directions accumulated during the live-learning conversation.
They are requirements/targets, not claims of completed capability.

## 1. Four laws are the only constitutional authority

EVAL — may evaluate but cannot self-declare truth.
COMMIT — canonical state/status changes require lawful basis + provenance.
DRIVE — sole arbiter of what happens next.
MEDIATE — intention/request/prediction is not external outcome.

Influences only:
MASK / VALUE / AVAIL / TRIGGER / STATUS.

No chat convention, parser shortcut, trainer convenience or test harness may become a fifth law.

## 2. No chatbot request/response physics

A question is one event in continuous experience.
It may remain OPEN, move to BACKGROUND, be answered later, never be answered, or coexist with
other questions.

The user is not required to answer C4.
"не знаю" is not a magic token.
"запомни:" and ":" are not COMMIT authority.
Temporal adjacency is not semantic relation.

C4 may ask 2-3 questions, make a proposal, think, pause, return later, or emit nothing yet,
but DRIVE chooses this behavior.

## 3. Continuous life-line, not streams inside streams

One experience line should contain:
- external user events;
- internal thought/evaluation events;
- questions;
- actions/intents;
- observations;
- receipts;
- sensor events;
- public outputs;
- memory retrieval;
- corrections;
- learning;
- topic changes.

Keep at least two temporal coordinates:
- internal causal/runtime step;
- external event/wall time.

Past / present / future must work both inside reasoning and across real external time.

## 4. Transport != cognition != public output

Receiving a message should not force an immediate REPLY.

Target:
RECEIVE -> TRIGGER DRIVE -> one or more internal iterations ->
optional public act.

Possible path:
message -> think -> another internal event -> question -> later observation -> revisit ->
reply.

The Android compatibility wrapper may still offer synchronous behavior, but it must not define
the cognitive physics.

## 5. Hierarchical semantic composition

Inspired by compact signs / hieroglyph-like semantics, but generalized.

Typed scales:
SIGN / FORM -> WORD -> PHRASE -> PROPOSITION/SENTENCE -> MESSAGE ->
EVENT -> EPISODE -> STORY -> BOOK.

A small form may index or evoke a large semantic unit.
FORM != MEANING.
PART != WHOLE.
INDEX != CONTENT.

The graph should connect across scales, allowing compression and retrieval without flattening
a story into a bag of words.

## 6. Narrative becomes real experience structure

Training gradient:
atom -> relation -> event -> linked events -> scene -> episode -> story ->
long story/book -> ordinary dialogue.

Stories must preserve:
participants, roles, time, place, causes, actions, observations, unknowns, corrections,
source ownership and consequences.

The goal is learning through stories/life rather than permanent special teaching syntax.

## 7. SELF model and OTHER model

C4 needs an explicit representation of:
- SELF state/history/capabilities/interests;
- Ruslan/OTHER state as externally observed/reported;
- source ownership;
- viewpoint;
- knowledge differences;
- preferences/interests.

SELF != OTHER.
SELF INTEREST != OTHER INTEREST.
SELF KNOWS(X) != OTHER KNOWS(X).

"Mirror neurons" direction is implemented as an evidence-bounded model of OTHER, not mind-reading.
Inferred intention/interest remains EVAL hypothesis unless OTHER reports it or evidence supports it.

Nickname/name relations are social facts in the SELF/OTHER model, not generic IS_A edges.

## 8. Causal fabric

Training should grow:
CONTEXT -> CAUSE -> EVENT -> CHANGE -> RESULT -> OBSERVATION ->
BELIEF UPDATE -> ACTION.

Temporal order alone never creates causality.
Prediction never creates observation.
Action request never creates result.
A report about an event never becomes SELF observation.

If one link is UNKNOWN, the chain remains open rather than inventing closure.

## 9. Natural language as graph geometry

Priority defects found in live teaching:
- inflected form becoming a new concept;
- relation verb disappearing, e.g. "topic relates to conversation" -> "topic = conversation";
- predicate attached to wrong owner, e.g. "topic sees";
- SELF/OTHER pronoun leakage;
- coordinated phrases becoming opaque pseudo-concepts.

Target:
lemma/form distinction;
subject-predicate-object/role structure;
relation type retained;
reference/perspective retained;
composition before commitment.

"Запомни:" is only temporary bootstrap UX and should eventually be unnecessary.

## 10. Questions as ordinary semantic events

An inquiry should carry at least:
author/owner,
topic,
unknown target,
time,
status,
context,
possible answer constraints.

NEXT_MESSAGE != ANSWER.
ANSWER_CANDIDATE != FACT.
QUESTION_CONTEXT != TEACHING_AUTHORIZATION.

A later answer should match semantically, not by position.

## 11. AUDIO + VISION + SYMBOL in parallel

Do not teach language first and bolt sensors on later.

A concept/episode may bind:
TEXT form,
AUDIO form,
VISION representation,
SYMBOL/index,
SPATIAL state,
ACTION/MOTOR pattern.

TEXT != AUDIO != IMAGE != SYMBOL != OBJECT != MEANING.

Existing G305-G309 boundaries must remain.

## 12. External and internal interests

Gaps, curiosity and user goals should influence VALUE, not seize DRIVE.

A global unknown may stay AVAIL in memory while having low VALUE for the current life-line.
The user's current interest may raise VALUE for related actions.
C4's own unresolved interest may persist and return later.

GLOBAL GAP MEMORY != CURRENT INTEREST.
AVAIL != VALUE.
TRIGGER != DECISION.

## 13. Live-readiness criterion

Do not return to live teaching merely because unit tests are green.

Required before live:
- universal mutation gate proven;
- frozen replay of the entire bad live conversation;
- no accidental graph mutation from greeting/correction/profanity/topic shift/question;
- deliberate source-scoped teaching still works;
- multiple open inquiries do not seize DRIVE;
- delayed reply path works;
- cold reload preserves life-line and statuses;
- full regression has no new semantic failure;
- exact runtime + weights + hashes physically saved.

Then perform live test again from a clean copy.
