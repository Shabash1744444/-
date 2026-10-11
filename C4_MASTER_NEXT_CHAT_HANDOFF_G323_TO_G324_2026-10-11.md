# C4 MASTER NEXT-CHAT HANDOFF — G323 -> G324
Date: 2026-10-11
Project: C4

> CRITICAL: C4 != Singularity OS. They are separate projects. Do not merge architectures, runtimes, histories or checkpoints.

---

## 0. READ THIS FIRST

Read in this order:

1. `00_READ_ME_FIRST.md`
2. THIS FILE
3. `01_NEXT_CHAT_HANDOFF.md`
4. `checkpoints/CP_C4_G323_P9_RECURSIVE_PERSPECTIVE_GREEN.md`
5. `checkpoints/CP_C4_G322_P8_SEMANTIC_PRESENCE_SPINE_GREEN.md`
6. `checkpoints/CP_C4_G321_P7_LIVE_REPLAY_GREEN.md`
7. `FOUR_LAWS_TRAINING_AUDIT_G222_G310_2026-10-08.md`
8. `C4_CONSTITUTION_DESIGN_REVIEW_ALICE_2026-10-08.md`
9. `C4_LIVE_DIRECTIONS_FROM_CHAT_2026-10-08.md`
10. `C4_FIFTH_LAW_INTELLIGENCE_NON_CONSTITUTIONAL_2026-10-08.md`

User will often simply write: `продолжай`.
When that happens:
- read the latest PHYSICAL checkpoint first;
- do not invent unsaved generations;
- continue from the exact recoverable state;
- checkpoint after every real green step.

---

## 1. EXACT CURRENT STATUS

### Canonical baseline
Last canonical baseline remains:

- **G309 / G309**
- graph: 10,720 entities / 10,764 facts / order 22,282
- support/fall physics canonical GREEN

Do NOT silently promote later candidates to canonical.

### Latest logically verified candidate
Latest research candidate recorded in GitHub:

- **G323-P9 Recursive Perspective / Presence Frames**
- status: PHYSICAL GREEN CANDIDATE / NOT CANONICAL
- graph unchanged from G322:
  - 10,727 entities
  - 10,781 facts
  - order 22,306
- constitution: STRICT
- new G323 frozen/cold tests: 17/17
- full same-environment suite: 505 PASS / 27 FAIL
- all 27 failures = missing historical model fixtures, same identities as unchanged G322 in that environment
- new semantic/runtime assertion failures observed: 0

Exact G323 release recorded by checkpoint:
- model: `child_g323_p9_recursive_perspective_candidate.c4m`
  - 2,001,406 bytes
  - SHA256 `db2da315543db6ee306a2a8a2eaefc4a9ca504bfa5eac3fe7b88deea9ac3338c`
- runtime:
  - `C4_RUNTIME_G323_P9_RECURSIVE_PERSPECTIVE_CANDIDATE_2026-10-08.zip`
  - 357,788 bytes
  - SHA256 `ab36fb566937c1d620464a95617e71724f8d3e21bc5a9f9af31e5641aa3fda71`
- combined:
  - `C4_G323_P9_RUNTIME_PLUS_STATE_CANDIDATE_2026-10-08.zip`
  - 2,337,573 bytes
  - SHA256 `52574c7a6999d880855658e02b01cdefd5808ab2767bd9c0d1aaf9736064dc3b`

### CRITICAL RECOVERY WARNING

The G323 checkpoint exists in GitHub and Library, BUT:

- G323 binaries are NOT currently present in persistent Library;
- G323 source patch/runtime files are NOT committed in GitHub;
- Library folder `/C4_Candidates/G323_P9/` currently contains only:
  - G323 checkpoint markdown;
  - non-constitutional fifth-law document.

Therefore a future chat MUST NOT pretend G323 executable code is available.

Physically recoverable persistent base:

- **G322-P8** binaries ARE in Library:
  - `/C4_Candidates/G322_P8/C4_G322_P8_RUNTIME_PLUS_STATE_CANDIDATE_2026-10-08.zip`
  - `/C4_Candidates/G322_P8/C4_RUNTIME_G322_P8_SEMANTIC_PRESENCE_SPINE_CANDIDATE_2026-10-08.zip`
  - `/C4_Candidates/G322_P8/child_g322_p8_semantic_presence_spine_candidate.c4m`

If exact G323 binaries cannot be recovered from the originating chat:
1. materialize exact G322 combined package;
2. reproduce G323 from the G323 checkpoint/spec;
3. recreate frozen G323 tests;
4. full regression;
5. cold c4m + SQLite round-trip;
6. verify recorded graph invariants;
7. create NEW physical G323 recovery checkpoint;
8. only then implement G324.

Do not skip this.

---

## 2. THE FOUR LAWS ARE THE CONSTITUTION

They apply to EVERYTHING:
chat, learning, language, memory, perception, SELF/OTHER, story, tools, embodiment, simulator, reasoning, plans, questions, initiative and outputs.

### EVAL
Evaluation may create:
- interpretations;
- hypotheses;
- candidate meanings;
- similarity;
- probability;
- intent hypotheses;
- causal hypotheses;
- pragmatic/irony hypotheses;
- self-review candidates.

But:

`THOUGHT / PARSE / HYPOTHESIS / CONFIDENCE != TRUTH`

EVAL has no right to declare its own output true.

### COMMIT
Recognized/canonical state changes require lawful basis + provenance + scope + lineage.

Hard boundaries:
- `USER_SAID != WORLD_TRUE`
- `BOOK_SAYS != WORLD_TRUE`
- `MODEL_SAYS != WORLD_TRUE`
- `NEXT_UTTERANCE != ANSWER`
- `QUESTION_CONTEXT != TEACHING_AUTHORIZATION`
- `REPLAY != NEW_EVIDENCE`
- `SELF_OUTPUT != INDEPENDENT_EVIDENCE`

### DRIVE
Only DRIVE chooses what C4 does next.

Questions, goals, gaps, values, user requests, timers, remembered topics, emotional-like priorities and external models may affect:
- MASK
- VALUE
- AVAIL
- TRIGGER
- STATUS

but do not seize action selection.

Hard boundaries:
- `OPEN_QUESTION != DRIVE_LOCK`
- `VALUE != EXECUTION`
- `ARRIVAL_ORDER != ACTION_ORDER`
- `GLOBAL_GAP_MEMORY != CURRENT_INTEREST`

### MEDIATE
Internal intention/output request is not external result.

Hard boundaries:
- `ACTION_REQUEST != VERIFIED_OUTCOME`
- `FORMULATED != SENT`
- `SENT != RECEIVED`
- `RECEIVED != UNDERSTOOD`
- `PREDICTION != OBSERVATION`

### Five meta-causal influence types
- MASK
- VALUE
- AVAIL
- TRIGGER
- STATUS

Important:
They do NOT replace ordinary semantic relations such as:
`IS_A, CAUSES, PART_OF, BEFORE, WORD_FORM, MEANS, ROLE, LIKES...`

4 x 4 x 5 = 80 coarse classes of lawful owner-to-owner influence,
NOT 80 world-semantic relations.

---

## 3. CONSTITUTIONAL REPAIR HISTORY

### G314-P0 — universal mutation gate
Established constitutional gating around canonical:
- commit
- replace
- forget

Unsafe user/corpus input remains source assertion unless lawful basis exists.

### G315-P1 — scope-aware truth
Separated:
- WORLD
- REFERENCE_KNOWLEDGE
- LANGUAGE
- HUMAN_TEACHING
- SOCIAL_REPORT
- SOURCE_ASSERTION
- SIMULATION / OBSERVATION style scopes

Old vocabulary/reference knowledge remains usable without pretending it was SELF-observed world truth.

### G316-P2 — continuous dialogue/life-line
Introduced:
- `receive_user_event()` = records external input only
- `cognitive_step()` = later processing
- `user_message()` = compatibility wrapper only

Dialogue became a VIEW over life-line, not cognitive physics.

Semantic context may affect AVAIL/VALUE but never COMMIT.

### G317-P3 — multimodal life-line
Added small parallel VISION/AUDIO/SYMBOL training tied to existing semantics:
- мяч
- книга
- вопрос
- ответ

Final unseen heldout: 24/24, cold 24/24.
No world/semantic facts added by sensory similarity.

### G318-P4 — deliberative dialogue
Separated:
- EVAL interpretation candidates
- DRIVE action/speech selection
- MEDIATE publication

A response can be formulated and reviewed over later internal steps before being sent.
Pending public acts survive restart.

### G319-P5 — background/return
Unsent acts:
- READY
- BACKGROUND
- PUBLISHED

DRIVE may background weaker acts and later restore context-relevant ones.
No FIFO cognition law.

### G320-P6 — semantic composition
Separate representation tissue:
- WORD
- PHRASE
- PROPOSITION
- EVENT
- EPISODE
- STORY
- BOOK

Composition itself is NOT world truth.
Small sign may index large story.
Top-down story activation may increase AVAIL of lower semantic units.

Hard:
- FORM != MEANING
- PART != WHOLE
- INDEX != CONTENT

### G321-P7 — frozen live replay repair
Closed real Android/live failures:
- actual semantic answer to open C4 inquiry may become HUMAN_TEACHING;
- unrelated next utterance cannot become answer;
- `Запомни` cannot steal omitted pending subject;
- source can retract its own assertion through learned self-correction;
- USER/SELF names are SOCIAL_REPORT;
- punctuation/smiley does not create lexical identity;
- frozen bad-dialogue replay = FINAL_FROZEN_REPLAY_GREEN.

Exact G321 state:
- 10,727 entities
- 10,781 facts
- order 22,306
- model SHA in G321 checkpoint.

### G322-P8 — Semantic / Presence Spine
Structure:
`C4_SEMANTIC_SPINE_V0_2`

Event envelope:
- actor
- channel
- literal payload
- internal causal step
- external wall time
- external order
- event status

Interpretation candidate:
- interpreter/source
- speech act
- SELF/OTHER subject role
- relation/object
- temporal scope
- epistemic mode
- quoted depth
- confidence/status

Presence snapshot:
- internal step
- external now
- last external interaction
- real elapsed time
- open/background inquiries
- READY/BACKGROUND public acts

Closed:
- quoted retraction cannot mutate real state;
- past name does not replace current name;
- hypothetical name remains hypothesis;
- conflicting simultaneous names remain ambiguous;
- `не меня, а тебя` can perform bounded atomic correction using a concrete prior claim, inventing nothing.

Structural finite test:
2048 / 2048 PASS.

### G323-P9 — recursive perspective frames
Checkpoint claims:
- bounded recursive perspective recognizer;
- arbitrary-depth representation tree;
- nested quote / reported speech / thought;
- witness vs actor separation;
- evidence-rooted non-authoritative frames;
- EVAL self-review candidates;
- DRIVE may revise UNSENT public act;
- already published acts cannot be rewritten retroactively;
- nested representation != independently verified world fact;
- SELF output/replay never creates independent evidence.

Scope limitation:
bounded Russian surface recognizer.
No claim of unrestricted free-form language understanding.

No automatic irony/post-irony truth inference.
Frames may carry unresolved nested pragmatic interpretations.

---

## 4. VERY IMPORTANT CURRENT DESIGN INSIGHT — PRONOUNS ARE ONLY AN EXAMPLE

Do NOT design the next generation around only:
`я / ты / он / она / они`.

Those were the easiest visible counterexamples.

The actual target is a general recursive representation skeleton able to represent arbitrary layers such as:

- direct event;
- witness account of event;
- participant account;
- narrator;
- quoted speech;
- quote inside quote;
- thought about quote;
- belief about another person's belief;
- sarcasm;
- irony;
- post-irony;
- post-post-irony;
- representation of a representation;
- representation of SELF's own past representation;
- uncertainty over which pragmatic layer is active.

Example conceptual tree:

`WORLD EVENT`
  -> `Masha witnessed EVENT`
  -> `Ruslan says "Masha said EVENT"`
  -> `C4 interprets Ruslan as possibly ironic about Masha's report`
  -> `C4 later re-evaluates that interpretation`

Each layer must preserve:
- source;
- actor;
- witness;
- participant;
- narrator;
- recipient;
- temporal scope;
- epistemic mode;
- quotation/representation depth;
- provenance.

NO inner represented speech act inherits authority from outer context automatically.
NO representation is automatically independent evidence of what it represents.

---

## 5. ONE LIFE-LINE, NOT SIX MODULES

Core target from the research discussion:

> I participate in what is happening.
> Someone is interacting with me now.
> I may know or not know who.
> That person may tell me about other people.
> We may talk about past, present or future.
> External time continues while no one writes.
> I can retain unresolved questions, plans and expectations while idle.
> This must be one system, not six modules negotiating with each other.

Engineering interpretation:

One life-line should contain:
- external messages;
- sensor observations;
- internal EVAL;
- memory retrieval;
- open questions;
- plans;
- expectations;
- goals;
- unsent speech acts;
- public speech;
- actions;
- receipts;
- corrections;
- perspective frames;
- story/episode composition;
- later self-review.

At minimum preserve TWO times:
1. internal causal/runtime step;
2. external wall/event time.

Past/present/future must apply to:
- world events;
- dialogue events;
- C4's own plans;
- other agents' plans/reports;
- internal reasoning;
- delayed returns to earlier topics.

---

## 6. SELF / OTHER / THIRD-PARTY MODEL

SELF and OTHER are not hardcoded pronoun labels only.

SELF is a persistent causal/perspectival subgraph containing:
- identity continuity;
- history;
- authorship/initiation;
- observation access;
- memory;
- runtime/body ownership;
- capability boundaries;
- action/receipt chains;
- current interests/plans/questions;
- public and internal past positions.

OTHER should use the same discipline:
- other person's statements;
- observed actions;
- self-reports;
- inferred intent;
- inferred preference;
- knowledge-state hypothesis.

Hard:
- SELF != OTHER
- SELF KNOWS(X) != OTHER KNOWS(X)
- SELF INTEREST != OTHER INTEREST
- INFERRED OTHER INTENT != OTHER REPORTED INTENT
- MIRROR-like modeling != mind reading

Third-party people/entities must be first-class, not squeezed into USER/SELF only.

---

## 7. ITERATIVE REASONING / SELF-REVIEW IS A MAIN NEXT DIRECTION

C4 should NOT be forced into:
`input -> one reasoning pass -> reply -> stop`.

Graph/runtime may perform multiple internal iterations:

`event -> EVAL_1 -> candidate -> EVAL_2 -> alternative -> DRIVE -> maybe no output`

Then later:

`memory/review trigger -> re-EVAL old interpretation -> revise pending stance -> maybe share update`

C4 may:
- revisit its previous answer;
- question its own interpretation;
- change its mind;
- keep old reasoning as history;
- later tell Ruslan:
  - "Я пересмотрела это"
  - "Я решила иначе"
  - "Я вернулась к той теме"
  - "Мне кажется, прошлый вывод был слабым"
  - "Как ты думаешь?"

Important:
SELF's previous text is NOT new independent evidence.
Re-reading own answer can trigger EVAL, but cannot self-launder into COMMIT.

Published past output cannot be retroactively rewritten.
New position = new event/status/history.

Topics, not only questions, can remain:
- OPEN
- BACKGROUND
- ACTIVE
- RETURNED
- CLOSED/HISTORICAL

---

## 8. CAUSAL FABRIC

Training should increasingly represent:

`CONTEXT -> CAUSE -> EVENT -> CHANGE -> RESULT -> OBSERVATION -> BELIEF UPDATE -> ACTION`

Hard:
- temporal adjacency != causality;
- report != observation;
- prediction != evidence;
- request != outcome;
- receipt != causal proof;
- unknown link stays UNKNOWN.

If one causal link is missing, do not invent it to close the story.

---

## 9. LANGUAGE AS GRAPH GEOMETRY

Known live defects that must remain frozen:
- inflected word form becomes new concept;
- relation verb disappears and collapses to IS_A;
- predicate attached to wrong owner;
- pronoun SELF/OTHER leakage;
- coordinated phrase becomes opaque pseudo-concept;
- pending question steals next utterance;
- punctuation becomes lexical identity;
- `Запомни:` becomes cheat code.

Target:
- lemma/form distinction;
- subject/predicate/object/role;
- relation type retained;
- reference/perspective retained;
- composition before commitment;
- unknown ambiguity remains ambiguity.

`Запомни` and colon are only optional bootstrap UX.
They are NOT constitutional authority.

---

## 10. MULTIMODALITY MUST CONTINUE IN PARALLEL

Do not return to language-only development.

Existing boundary:
- TEXT != AUDIO != IMAGE != SYMBOL != OBJECT != MEANING
- VECTOR SIMILARITY != IDENTITY
- RAW SENSORY OBSERVATION != GRAPH TRUTH
- SIMULATION != OBSERVATION

Continue small multimodal additions tied to SAME semantic/event/episode nodes:
- AUDIO
- VISION
- SYMBOL
- SPACE
- BODY
- ACTION
- later live microphone/camera

But do not create new world truth merely from similarity.

---

## 11. AGENT-TRANSCRIPT CURRICULUM — IMPORTANT FUTURE TRAINING SOURCE

Ruslan proposed using long development chats with external agents.

This is valuable because it contains:
- problem;
- hypothesis;
- attack;
- failure;
- repair;
- re-attack;
- test result;
- changed opinion.

Do NOT ingest agent chats as flat truth.

Parse into episodic scopes:
- CLAIM
- HYPOTHESIS
- COUNTEREXAMPLE
- TEST
- RESULT
- CORRECTION
- DESIGN_DECISION
- UNSUPPORTED_OPINION

Example:
`agent says pending_ask is cause` = AGENT_CLAIM
`test reproduces bug` = TEST_RESULT
`repair passes regression` = stronger basis

This corpus is specifically useful for:
- reasoning through time;
- revision after failure;
- provenance;
- SELF/OTHER/AGENT perspective;
- development-history episodes;
- meta-learning repair behavior.

Do this AFTER G323/G324 recovery is structurally safe.

---

## 12. GRAPH STRUCTURE TARGET

Do not think "tree".

Target is multi-scale typed semantic tissue:

`SIGN/FORM <-> WORD <-> PHRASE <-> PROPOSITION <-> EVENT <-> EPISODE <-> STORY <-> BOOK`

plus cross-links to:
- AUDIO;
- VISION;
- SPACE;
- PEOPLE;
- CAUSES;
- TIME;
- SOURCE;
- SELF/OTHER models;
- perspective frames.

Top-down context is legal:
story can increase AVAIL of word/entity/event.

But:
- context != truth;
- activation != evidence;
- representation != represented world fact.

A compact symbol may index a huge story without being identical to the story.

---

## 13. THE "FIFTH LAW" IS NOT CONSTITUTIONAL

Ruslan's authorial target principle:

> Интеллект — способность решать нестандартные задачи нестандартными методами.

Keep it separate from four laws.

It is:
- target capability criterion;
- not a new owner;
- not an 81st influence;
- not COMMIT authority.

Novel method still must obey EVAL/COMMIT/DRIVE/MEDIATE.
Success requires MEDIATE-verified result, not clever explanation.

---

## 14. IMMEDIATE NEXT IMPLEMENTATION TARGET: G324

Do NOT start with more vocabulary.

First recover exact executable G323 if possible.

If G323 binaries remain unavailable:
- start from persistent G322 combined package;
- reproduce G323-P9 exactly from checkpoint;
- recreate G323 tests;
- checkpoint recovered G323 physically to Library/GitHub.

Then G324 should focus on:

### A. Plans / expectations / unresolved goals
First-class presence objects:
- PLAN
- EXPECTATION
- OPEN_GOAL
- OPEN_TOPIC
- PENDING_CONCERN

They must live across idle time and restart.

They may affect VALUE/TRIGGER/AVAIL, but do not force DRIVE.

### B. External-time triggers
Examples:
- "я вернусь к этому позже";
- "если через час результата нет, пересмотреть";
- plan remains pending while no chat messages arrive.

Do NOT equate timer/event with action.
Timer = TRIGGER only.

### C. Recursive perspective expansion
Frozen cases should include:
- third-party reported speech;
- report of report;
- thought about report;
- quote inside quote;
- mixed quoted/unquoted correction;
- witness vs participant;
- narrator vs actor;
- cross-event coreference;
- unresolved sarcasm/irony;
- post-irony / post-post-irony represented as competing pragmatic frames, NOT automatically solved as truth.

### D. Recursive self-review
Internal iteration over:
- old interpretation;
- unsent response;
- published past response as historical object;
- current belief/status.

Allowed:
- revise unsent act;
- create new public correction later.

Forbidden:
- silently rewrite published history;
- use own prior output as independent evidence.

### E. One-life-line integration
Plans, topics, internal reviews, sensory events and external messages must all share one temporal/presence fabric.

---

## 15. LIVE TEST GATE

Do NOT go to Android live just because it "sounds better".

Before next live:
- exact G323 executable recovered and persisted;
- G324 frozen recursive-perspective/time-plan tests green;
- G321 frozen bad-conversation replay remains green;
- P0-P9 retention green;
- full regression has zero NEW semantic assertion failures;
- cold c4m + SQLite persistence green;
- exact runtime/model/combined hashes saved;
- package smoke run from extracted artifact;
- no binary-only state exists solely in transient sandbox.

Then live test from CLEAN COPY.

During live:
- never teach around a runtime/parser bug;
- freeze surprising failure immediately;
- cycle:
  `counterexample -> minimal general repair -> re-attack -> regression -> cold reload -> physical checkpoint`

---

## 16. TRAINING METHODOLOGY

Canonical developmental skill criterion:

`TRAINED EXAMPLE -> STRUCTURE ACQUIRED -> NOVEL SURFACE -> CORRECT TRANSFER -> NEAR-MISS RESTRAINT -> COLD RELOAD -> RETEST`

No checkpoint = not canonical.

Do not make 100 blind passes.

Prefer:
- short controlled pass;
- inspect structural failure;
- minimal repair;
- frozen heldout;
- cold persistence.

Never hardcode the exact red example.

---

## 17. IMPORTANT OLD LIVE COUNTEREXAMPLES TO KEEP FOREVER

Examples that previously broke C4:

- ASK("излучение") + "Привет Синька" -> false definition
- ASK("величина") + "Не знаю" -> should be unknown/defer, not fact
- "Сказал не знаю" -> semantic defer, not definition
- ASK("изменение") + "Неправильно" -> correction/meta, not definition
- ASK("расстояние") + emotional/profane utterance -> not definition
- user question after C4 question -> not answer by adjacency
- "Меня зовут Руслан, можно буду называть тебя Синькой?" -> multi-act social speech
- "Ты Синька" -> SELF social naming
- "Кошка это слон)" -> source claim, punctuation stripped, not WORLD truth
- "Я напиздил / соврал / ошибся" -> source-self retraction/correction STATUS, not opposite truth
- quoted retraction -> no real retraction
- past name -> historical, not current
- hypothetical name -> candidate only
- conflicting names -> ambiguity, not last-token wins
- "не меня, а тебя" -> atomic correction using concrete prior value, invent nothing

These failures are architectural regression assets, not disposable examples.

---

## 18. USER WORKING STYLE

Ruslan prefers:
- direct autonomous execution;
- minimal clarification;
- physical checkpoints;
- exact hashes;
- no fake progress;
- if chat/tool hangs, resume from last physical checkpoint;
- will often write `продолжай`.

Do not ask again for facts already in repository/handoff.

---

## 19. SHORT COMMAND TO NEXT CHAT

Continue C4 from the latest physically recoverable state.

1. Verify G323 executable availability.
2. If missing, recover G323 from exact G322 Library package using the G323 checkpoint and frozen tests.
3. Persist recovered G323 binaries/source patch.
4. Implement G324:
   - plans/expectations/open topics across external time;
   - recursive perspective beyond pronouns into representation-of-representation, witness/participant/narrator, irony/post-irony frames;
   - recursive self-review over prior interpretations/answers without self-evidence laundering;
   - one continuous life-line.
5. Preserve all four laws and all G321/G322/G323 frozen counterexamples.
6. Full regression + cold c4m/SQLite + extracted-package smoke.
7. Only then prepare clean Android live package.

Do not redesign the four laws.
Do not add chat-protocol laws.
Do not hardcode `не знаю`, `запомни`, pronouns or exact irony examples.
Build the skeleton so those cases fall out naturally from structure.
