C4 MASTER HANDOFF — G304 CANONICAL + G305 SENSORY IN PROGRESS
Date: 2026-10-07
Project: C4
IMPORTANT: C4 != Singularity OS. They are different projects and architectures.

================================================================
0. PURPOSE OF THIS FILE
================================================================

This is the emergency recovery / next-chat handoff for C4.

If the current chat ends, the next chat must:
1) treat G304 runtime + G302 weights as the last fully promoted canonical pair;
2) treat G305 sensory bridge as IN PROGRESS, not canonical;
3) continue training, not restart architecture design;
4) preserve all epistemic and causal laws;
5) keep physical checkpoints, hashes, regression results and repo state;
6) never mix C4 with Singularity OS;
7) keep Claude's runtime branch separate from the main C4 training generation numbers.

The user will often simply say "продолжай" / "ебош".
That means: continue actual training / implementation autonomously, with physical checkpointing.
Do not respond with a plan-only answer if work can be done.

================================================================
1. CURRENT CANONICAL STATE
================================================================

CANONICAL WEIGHTS:
G302 ROLE / MEANS / SUCCESSOR SCOPE GREEN

File:
child_g302_role_means_successor_scope_green.c4m

Size:
1,981,454 bytes

SHA256:
250625e164ffd6a7809f75129c2919a00a303cf97198cc27179ed9115f219ba7

CANONICAL RUNTIME:
G304 EVENT CONJUNCTION SCOPE GREEN

File:
C4_RUNTIME_G304_EVENT_CONJUNCTION_SCOPE_GREEN_2026-10-07.zip

Size:
301,378 bytes

SHA256:
59ca94c6dd2ab78c881e015eaf885ebbc1ca1407696ca0102707d1b032a51aae

COMBINED:
C4_G304_RUNTIME_PLUS_G302_WEIGHTS_2026-10-07.zip

Size:
2,261,376 bytes

SHA256:
02bd772d97edf43ff7c0bdfbc385aa1e746fa48a962e87f3ac3d029331bfd77b

Canonical recovery location:
Library /C4_Canonical/
GitHub repo: Shabash1744444/-
Branch: main

================================================================
2. LATEST CANONICAL DEVELOPMENT: G299 -> G304
================================================================

G299 — LEXICAL RELATION RESTRAINT
- 40 direct lexical lessons:
  SYNONYM 20
  ANTONYM 20
- 24/24 reverse symmetric readings after/cold/SQLite
- 0 direct leaks
- 16/16 non-transitivity / identity traps UNKNOWN
- core laws:
  SYNONYM != IDENTITY
  LEXICAL SYMMETRY != TRANSITIVITY

G300 — OPEN RELATION QUERY RUNTIME
- open/list questions can consume safe read-only inverse/symmetric relation algebra
- derived values are never persisted as direct facts
- direct contradiction blocks a derived list answer
- MEANS remains non-symmetric
- full regression at that point: 384/393 memory and SQLite
- the 9 failures were historical missing artifacts

G301 — RELATION LANGUAGE BRIDGE
Learned QUERY_RELATION vocabulary:
- синоним -> SYNONYM
- антоним -> ANTONYM
- противоположность -> OPPOSITE
- роль -> ROLE
- смысл -> MEANS
- преемник -> SUCCESSOR

Validation:
- 6/6 natural relation questions after/cold/SQLite
- questions are read-only
- G297 and G299 retention GREEN

G302 — ROLE / MEANS / SUCCESSOR SCOPE
44 novel direct lessons:
- MEANS 16
- ROLE 16
- SUCCESSOR 12

Important semantics:
- MEANS is SET-valued
- ROLE is SET-valued
- polysemy is not conflict
- multiple roles are not contradiction
- SUCCESSOR is one-step and non-transitive

Held-out restraint:
- reverse MEANS 8/8 UNKNOWN
- reverse ROLE 8/8 UNKNOWN
- transitive SUCCESSOR endpoints 8/8 UNKNOWN
Total 24/24 UNKNOWN

Retention:
- G301 natural queries GREEN
- G299 GREEN
- G297 GREEN
- memory == SQLite

G303 — EVENT TENSE BOUNDARIES RUNTIME
Counterexamples found and repaired:
1) negative PAST event was stored in event memory but query
   "Правда ли, что Антон не любил чай?"
   was rejected by the parser.
2) "Антон будет любить чай" incorrectly produced subject "Антон будет"
   and wrote current LIKES(чай).

After repair:
- PAST EPISODE != PRESENT STATE
- FUTURE CLAIM != PRESENT STATE
- FUTURE CLAIM != VERIFIED OUTCOME
- negative EVENT_POLARITY is queryable
- Russian periphrastic future:
  буду / будешь / будет / будем / будете / будут + infinitive
  becomes FUTURE event structure
- the future auxiliary is not part of subject identity
- event questions remain read-only

Focused G303 tests: 17/17.

Exact G302 on G303:
- 44/44 direct
- 24/24 restraint UNKNOWN
- memory == SQLite

Full workspace at G303:
- semantic assertion regressions: 0
- failures were missing-file environment failures only

G304 — EVENT CONJUNCTION SCOPE RUNTIME
Counterexample:
"Антон любил чай и сок" was stored as one EVENT_OBJECT literal "чай и сок",
so "Правда ли, что Антон любил чай?" could remain UNKNOWN.

Safe repair:
- positive conjunction on SET-valued event predicate may distribute:
  "любил чай и сок" -> proposition-events for чай and сок
- NEGATED CONJUNCTION DOES NOT distribute automatically:
  "не любил чай и сок" is NOT silently converted into
  "не любил чай" + "не любил сок"
- exact known multiword entity / phrase identity wins over surface splitting

Law:
POSITIVE SET CONJUNCTION MAY DISTRIBUTE
NEGATED CONJUNCTION != DISTRIBUTED NEGATION
KNOWN PHRASE IDENTITY > SURFACE SPLIT

Focused G303+G304+older event pack:
22/22

Full workspace:
390/406 memory
390/406 SQLite

All 16 failures were FileNotFound environment failures only.
Semantic assertion failures: 0.

Exact G302 on G304:
- 44/44 direct
- 24/24 restraint UNKNOWN
- relation queries read-only
- memory == SQLite

================================================================
3. G305 SENSORY BRIDGE — IN PROGRESS, NOT CANONICAL
================================================================

IMPORTANT:
Do NOT promote G305 just because focused tests are green.
The full regression was not yet completed and checkpoint not finalized.

Motivation:
The mobile app / runtime body is beginning to outrun organism training.
Voice, screen, room, sensors and PC-use are becoming available, so C4 needs
a thin multimodal perception foundation now rather than waiting until G760.

Discovery:
The codebase already contains a SensoryGrounder from earlier generations.

Existing concepts in SensoryGrounder:
- VISION modality
- AUDIO modality
- SYMBOL modality
- vector prototypes
- cross-modal grounding
- novelty rejection
- stable unnamed concept -> curiosity / naming request
- synthetic worlds where labels are deliberately not handed to the grounder

Important insight:
The multimodal foundation does NOT need to be invented from zero.
It needs to be raised to current G304 epistemic laws and integrated into C4LivingRuntime.

G305 intended bridge:
RAW SIGNAL
-> features/vector
-> sensory candidate
-> cross-modal grounding
-> graph entity/event
-> epistemic admission
-> causal / action layer

Vectors are NOT truth.
Vectors are sensory address / similarity.

SIMILARITY != IDENTITY
RAW SIGNAL != TEACHER LABEL

An unknown single vector must NOT automatically create a world entity.

Multiple modalities may converge toward one entity only under stable evidence.

Proposed useful modalities for the app:
- VISION
- SCREEN
- AUDIO
- SYMBOL
Later:
- DEPTH
- PROPRIOCEPTION
- TOUCH / COLLISION
- possibly tool-specific embeddings

Focused G305 work already reached:
34/34

The focused pack included:
- older synthetic sensory tests
- naming curiosity
- embodiment
- streaming
- G303/G304 event laws
- new living-runtime sensory bridge tests

Observed harness issue:
one early RED was only a modality mismatch in the test harness:
synthetic world produced VISION/AUDIO/SYMBOL while a helper asked for SCREEN/AUDIO/SYMBOL.
This was a test issue, not a cognitive failure.

Intended G305 safety:
- one novel vector alone -> no permanent entity
- stable cross-modal evidence -> candidate identity
- explicit naming binds sensory concept to graph entity
- sensory state persists in .c4m / .c4db
- naming and grounding survive restart
- sensor vector != action
- PC-use action remains separate:
  ACTION_REQUEST -> receipt -> VERIFIED_OUTCOME

G305 must be recreated/continued from G304 if the current process state is lost.
Do not assume it was physically promoted.

================================================================
4. WHY MULTIMODAL TRAINING SHOULD START NOW
================================================================

Do not postpone all multimodality to G760.

Use a thin "synthetic kindergarten" now:
1) controlled synthetic signals
2) known causal world transitions
3) multimodal identity grounding
4) explicit naming
5) negative / UNKNOWN controls
6) restart persistence
7) later real sensors

Then return to dirty language / discourse / pragmatics.

The full long-range G1000 plan still includes a larger multimodal band,
but the foundation can and should be trained earlier.

================================================================
5. 3D WORLD / BODY PHYSICS TRAINING VISION
================================================================

The mobile app includes / is planned to include a room / 3D environment and body.

The organism should learn physical concepts through world transitions,
not only through dictionary facts.

Important synthetic concepts:
- up / down
- left / right
- forward / backward
- toward self / away from self
- near / far
- above / below
- inside / outside
- front / behind
- light / heavy
- fast / slow
- moving / still
- reachable / unreachable
- collision
- support
- falling
- carrying
- grasp / release
- occlusion
- object permanence
- direction of sound
- self-body position
- object-relative vs self-relative coordinates

Preferred training form:
STATE_before
+ ACTION_REQUEST
+ simulator transition
+ OBSERVATION_after
+ verified delta
-> EVENT / relation / causal candidate

Do NOT train physics as only:
"вверх = положительное Y"

The meaningful unit is causal experience:
"подняла руку -> положение кисти стало выше относительно корпуса"

Useful laws:
ACTION_REQUEST != VERIFIED_OUTCOME
RECEIPT != CAUSAL PROOF
PREDICTION != OBSERVATION
SHARED EFFECT != CAUSAL RELATION BETWEEN CAUSES
GRAPH REACHABILITY != INTERVENTION SEMANTICS

The 3D room can become a controlled causal curriculum before real-world camera use.

================================================================
6. SOUND -> LETTER -> WORD -> CONCEPT LAYER
================================================================

User idea:
teach sounds, letters, fragments of words and words as distinct but connectable layers.

This is architecturally sound if boundaries are preserved.

Do NOT collapse:
sound == letter == word == concept

Preferred layers:
RAW AUDIO
-> acoustic features/vector
-> candidate phonetic unit
-> learned sound fragment / phoneme-like unit
-> symbol/letter candidate
-> word-form candidate
-> lexical entity
-> concept / graph relations

Important:
SOUND SIMILARITY != SAME SOURCE
RAW SIGNAL != TEACHER LABEL
SURFACE FORM != INTENDED LEXEME
WORD_FORM != WORLD FACT

The architecture already has WORD_FORM and morphology.
Audio should connect to that layer, not replace it.

Possible synthetic curriculum:
- generate clean isolated phonetic/letter examples
- associate multiple audio variants with one symbol
- negative examples with similar sounds
- concatenate sound fragments into word candidates
- bind recognized word form to existing lexical entity only when evidence is sufficient
- ambiguity -> alternatives / ASK / UNKNOWN

Later:
microphone / ASR / prosody can feed the same event bus,
but an external ASR output should remain a candidate interpretation,
not unquestioned truth.

================================================================
7. PC-USE / VOICE INTERACTION VISION
================================================================

Target:
User speaks naturally to C4 in the mobile/desktop app.
C4 sees screen, hears voice, finds UI entities, executes actions and verifies results.

Desired pipeline:
VOICE AUDIO
-> acoustic/speech candidate
-> lexical / intent interpretation
-> TASK / GOAL
-> SCREEN vector candidates
-> graph entity "button Save"
-> ACTION_REQUEST(click)
-> tool receipt
-> new SCREEN observation
-> VERIFIED_OUTCOME or unresolved state

Do not allow:
screen similarity -> action success

The vector layer helps locate / identify candidates.
The action layer stays epistemically separate.

Useful future modalities:
SCREEN vector prototype
UI element geometry
OCR/text candidate
icon visual vector
mouse/keyboard action
accessibility tree candidate
post-action screenshot
verified state delta

The user specifically wants "vector eyes / fly eyes" speed for games and PC-use.
Treat vectors as fast perception/retrieval, not as authority.

================================================================
8. C4 CORE ARCHITECTURE
================================================================

C4 is a compact trainable non-transformer cognitive architecture.

Core state:
typed graph
+ provenance
+ status
+ scope
+ history/receipts
+ learned morphology
+ event structures
+ causal contracts

Important organs / concepts:
- C4Graph
- EpistemicAdmissionOrgan
- StructuralReasoner
- RuleInductionOrgan
- ActiveGaps
- GuidedReaderRU
- RussianMorphologyV1
- SensoryGrounder
- C4LivingRuntime

High-level learning loop:
counterexample
-> minimal repair
-> re-attack
-> regression
-> physical checkpoint
-> continue

Main design goal:
self-learning without self-poisoning.

================================================================
9. THEORETICAL 4 x 4 x 5 MATRIX
================================================================

Theoretical coarse relation space:
4 owners:
- EVAL
- COMMIT
- DRIVE
- MEDIATE

5 influences:
- MASK
- VALUE
- AVAIL
- TRIGGER
- STATUS

4 x 4 x 5 = 80 coarse edge types.

This is theoretical architecture space.
Do not blindly turn all 80 into explicit runtime relation classes.

State cardinality concepts:
|S_struct| = aleph_0
|S_token| = |R|

The old "all states" counts 36,864 / 2,208 / 38,154 are obsolete.

================================================================
10. NORMATIVE LAWS / HARD BOUNDARIES
================================================================

Preserve these. Add only by counterexample.

UNKNOWN != FALSE
REPLAY != NEW EVIDENCE
DERIVED != OBSERVATION
SIMULATION != OBSERVATION
PREDICTION != EVIDENCE
ACTION_REQUEST != VERIFIED_OUTCOME
RECEIPT != CAUSAL PROOF
SIMILARITY != IDENTITY
MODEL CONFIDENCE != AUTHORITY
CANONICAL != VERIFIED AUTHORITY
different source labels != independent lineage
one model/many chats != many independent sources
explanation != evidence
DISCOURSE CONTEXT != WORLD EVIDENCE
LEXICAL RETRIEVAL != TRUTH
QUESTION != ASSERTION
ASK WAIT != GAP RESOLUTION
SUMMARY != ORIGINAL EVIDENCE
SCHEMA != OBSERVATION
COMPRESSION != NEW TRUTH
BOOK != TRUTH
AUTHOR != NARRATOR
CHARACTER != AUTHOR
FICTIONAL WORLD FACT != EXTERNAL WORLD FACT
C4 != Singularity
ORTHOGRAPHIC SUFFIX != LEXICAL POS
PRODUCTIVE VERB TRANSFORM REQUIRES EXPLICIT VERB EVIDENCE
HOMOGRAPH != IDENTITY
TEST TOKEN != VOCABULARY KNOWLEDGE
GENERATED/OUTPUT SPEECH FORM != GRAPH FACT
AUTOSAVE != NEW EVIDENCE
QUESTION PRIORITY != TRUTH CONFIDENCE
GUIDED SEMANTIC EXTRACTION != RAW READING
UNSUPPORTED SENTENCE != FACT
OPEN CHAT QUESTION != EXTERNAL TEXT CONTEXT
LEXICAL HYPOTHESIS != LEMMA FACT
UNKNOWN SURFACE != NEW ENTITY
GLOBAL GAP MEMORY != RUN-LOCAL TRAINING QUEUE
GENERATED HELD-OUT ITEM != VALID EVALUATION ITEM
SHARED EFFECT != CAUSAL RELATION BETWEEN CAUSES
SHARED CAUSE != CAUSAL RELATION BETWEEN EFFECTS
GRAPH REACHABILITY != INTERVENTION SEMANTICS
SECOND PASS != GUESSING
UNKNOWN CAUSAL ENDPOINT != NEW ENTITY
EXPLICIT PROPERTY GRAMMAR > GENERIC HAVE PREDICATE
SURFACE FORM != INTENT
PROFANITY != NEGATIVE AFFECT
PROSODY != EMOTION
INTONATION != TRUTH
SLANG != ERROR
UNDERSTAND != EMIT
EDIT DISTANCE != IDENTITY
UNKNOWN LEXEME != TYPO
TYPO HYPOTHESIS != LEXICAL FACT
SURFACE FORM != INTENDED LEXEME
NORMALIZATION != CORRECTION
NONSTANDARD != ERROR
RAW SIGNAL != TEACHER LABEL
IMAGE SIMILARITY != IDENTITY
SOUND SIMILARITY != SAME SOURCE
FRAME != EVENT
CORRELATION != CAUSE
STORE CHANGE != COGNITIVE LAW CHANGE
DISK INDEX != NEW EVIDENCE
INVERSE RELATION != NEW FACT
SYMMETRIC READING != NEW EVIDENCE
PART_OF != TRANSITIVE BY DEFAULT
HAS != HAS_PART
MEANS != SYMMETRIC
ROLE != INHERITED BY DEFAULT
EVIDENCE HISTORY != CURRENT SOURCE STANCE
RETRACTION != RESURRECTION OF OLD STANCE
DERIVED STATE MUST INVALIDATE WHEN SUPPORT DISAPPEARS
ORDER != CAUSE
SHARED PREDECESSOR != ORDER BETWEEN SIBLINGS
TEMPORAL DERIVATION != NEW EVIDENCE
PAST EPISODE != CURRENT STATE
FUTURE CLAIM != CURRENT STATE
FUTURE CLAIM != VERIFIED OUTCOME
NEGATED CONJUNCTION != DISTRIBUTED NEGATION
KNOWN PHRASE IDENTITY > SURFACE SPLIT

Engineering maxim:
Everything may be represented as hypothesis/candidate/source claim.
Nothing may be promoted to proven truth without grounds.

================================================================
11. TRAINING METHODOLOGY
================================================================

Core metric:
new transferable abilities / direct lessons

Maxim:
Every new C4 layer should make later learning cheaper.

Preferred progression:
Morphological Substrate
-> Dense Semantic Core
-> Composition
-> Structural Transfer
-> Active Gap Selection
-> Guided Reading
-> Consolidation
-> Autonomous Learning

Training unit:
rule + positive + negative + unseen transfer

Modes:
BOOTSTRAP
-> GUIDED
-> AUTONOMOUS

Always measure:
- memorized
- inferred
- correctly UNKNOWN
- false inference
- teacher burden
- teacher cost to competence
- question efficiency
- autonomy ratio
- Error Amplification Factor
- bytes/RAM/latency
- cold reload
- cumulative regression

Do not train by bulk dumping books/dictionaries.
Use texts to expose gaps.
Ask high-value questions.
Deduplicate known structure.
Consolidate repeated semantics.

Quality > bytes > generation number.

================================================================
12. IMPORTANT EARLIER TRAINING LINE
================================================================

G270 nouns:
260/260

G271:
verb/POS guard; protects noun "сеть" from false verb morphology

G272 verbs:
756/756

G273 adjectives:
780/780

G274 dense semantics:
472/472

G275:
live teaching three-way merge

G276:
ActiveGaps / teacher cost

G277:
guided measurement

G278:
guided reading

G279:
guided prose

G280:
guided everyday

G281:
unknown surface -> lexical gap, no entity guess

G282:
guided action terms

G283:
contextual quantities

G284:
semantic family consolidation

G285:
family-accelerated lexical
Important historical RED:
autogenerated invalid form "глянецом" was caught and candidate rebuilt.
Lesson:
GENERATED HELD-OUT != VALID EVALUATION ITEM

G286:
causal guided reading

G287:
linear causal prose

G288:
branching/converging causal motifs
Historical harness bug:
capitalization issue falsely broke motif-local checks; candidate was not blindly promoted.

G289:
mixed-chunk dependency runtime
- one bounded deterministic second pass
- SECOND PASS != GUESSING
- explicit PROPERTY grammar priority over generic HAVE

G290:
mixed explanatory prose

G291:
deep explanatory hierarchy

G292:
hierarchy-accelerated concepts
16 direct concept classifications -> 96/96 inherited relations
leverage = 6.0
36/36 negative controls UNKNOWN
0 semantic target copies
0 target WORD_FORM
0 teacher questions

G293:
SQLite storage/query infrastructure

G294:
conservative relation algebra

G295:
functional-slot conflict visibility

G296:
strict temporal order

G297:
relation diversity

G298:
retraction invalidation

G299-G304:
see latest section above

================================================================
13. RELATION ALGEBRA CURRENT SAFE RULES
================================================================

PART_OF(A,B) <-> HAS_PART(B,A) read-only inverse

BEFORE(A,B) <-> AFTER(B,A)

BEFORE temporal paths may compose transitively read-only.

SYNONYM symmetric read-only
ANTONYM symmetric read-only
OPPOSITE symmetric read-only

No derived inverse/symmetric/temporal fact becomes direct evidence.

Forbidden:
PART_OF transitivity by default
HAS -> HAS_PART
reverse MEANS
ROLE inheritance/symmetry by default
SUCCESSOR transitivity
SYNONYM -> identity
lexical relation transitivity

Functional source conflict:
specific truth query must not hide disagreement in a functional slot.

Retraction:
current source stance must reflect later retraction.
Retraction must not resurrect old superseded values.

Open unresolved architecture note:
COLOR / LOCATION / VALUE cardinality cannot be solved by a blind
FUNCTIONAL -> SET switch.
They require scope/context/time.

Example:
an object may be red and white simultaneously,
or red at one time and blue later.
Location also depends on time / frame / scale.

================================================================
14. DIRTY LANGUAGE / HUMAN SPEECH FUTURE
================================================================

Do not treat unknown as typo.

Pipeline:
raw surface
-> candidate intended lexical interpretation
-> semantic claim
-> source/evidence admission

UNKNOWN LEXEME != TYPO
TYPO REPAIR != TRUTH ADMISSION
SURFACE IDENTITY != CONCEPT IDENTITY

Use:
surface similarity
+ keyboard neighborhood
+ morphology
+ neighboring words
+ sentence semantics
+ discourse/topic
+ speaker history

Dominant candidate may stay transient.
Ambiguity -> ASK / UNKNOWN.

Russian pragmatics examples:
"пиздец"
"нахуй"
"блять"
"заебииииись"
"да заебал"

Meaning depends on:
lexical content
speech act
valence
arousal
stance
target
prosody
duration/stress
discourse
world context
social register
confidence

PROFANITY != NEGATIVE AFFECT
PROSODY != EMOTION
UNDERSTAND != EMIT

Colloquial forms such as:
щя / ща / че / чет / хз
must not be automatically classified as errors.

================================================================
15. GUIDED READING / CLAUDE RUNTIME BRANCH
================================================================

Claude branch numbering is separate.

IMPORTANT:
C4 Gxxx = organism/training generation.
CL-Gxxx = Claude's runtime/R&D iteration number.
Do not compare the numbers directly.

Claude's branch:
CL-G270 storage
-> CL-G271 reading
-> CL-G272 frames

CL-G270 STORAGE:
Synthetic ~541k facts probe:
old in-memory:
- load 33.6 s
- RAM 3.4 GB, peak 5.6 GB
- first search question 38.8 s
- save after message 28.5 s

SQLite:
- open 0.2-0.3 s
- ~25 MB RAM, peak 67-92 MB
- first indexed search 0.13-0.20 s
- ordinary query ~8-10 ms
- write after learned reply ~68-95 ms
- explicit save ~0.04 s

.c4m remains exchange format.
.c4db is operational disk store.

Disk bloat:
819 MB for 541k facts vs ~79 MB archive weights.
Compression is useful later, not the immediate blocker.

CL-G271 READING:
article
-> unknown words
-> ask teacher
-> read explanation
-> unknown words in explanation become new questions
-> reread source

Reproducible avalanche example:
Ёж questions 82
Белка 48
Медведь 11

CL-G272 FRAMES:
Claude began turning literal verb phrases into structured event/predicate frames.
Treat his work as R&D/cherry-pickable organs.
Do not wholesale overwrite later canonical cognition.

Claude runtime branch mission:
- reading
- task lifecycle
- Windows adapters
- streaming
- tool/plugin boundaries
- persistence/migration
- multimodal readiness

Friday task file exists in repo:
CLAUDE_FRIDAY_RUNTIME_TASK.md

It was refreshed to current main-line pair:
G304 runtime + G302 weights.

================================================================
16. AGENT TASK LIFECYCLE
================================================================

Target first-class structures:
TASK
GOAL
TRIGGER
STATUS
PLAN
ACTION_REQUEST
RECEIPT
VERIFIED_OUTCOME
NEXT_CHECK

Lifecycle:
TASK
-> trigger
-> goal
-> plan
-> action request
-> receipt
-> verify
-> status
-> continue / finish

Statuses:
OPEN
WAITING
RUNNING
BLOCKED
DONE
CANCELLED

Laws:
TASK MEMORY != TASK EXECUTION
TASK SCHEDULING != ACTION
ACTION_REQUEST != VERIFIED OUTCOME
RECEIPT != CAUSAL PROOF

Tasks should survive restart and remain inspectable/cancellable.

================================================================
17. MOBILE APP / BODY VISION
================================================================

Separate mobile-app/runtime-shell work exists.

User target:
Android app first, later broader platform.

Desired:
- chat with C4
- voice
- VAD / ASR / TTS
- barge-in
- microphone
- screenshots / screen stream
- camera
- sensors
- file/network selection
- freeze protection
- 3D room / sandbox
- avatar/body
- mini-games
- filesystem / reader / constructor
- phone UI access
- level unlocking
- progress diary
- later VTuber / LLM teacher support

The app/body should be a sensor/action shell.
It must not bypass cognitive epistemic admission.

The room is useful as a synthetic causal world for training body physics.

================================================================
18. G1000 TARGET
================================================================

"Human-like perception" is an engineering target, not a consciousness claim.

Target pipeline:
raw input
-> candidate interpretations
-> context
-> meaning
-> pragmatics
-> epistemic status
-> response/action

Planned bands originally:
G293-380 relation algebra/traps
G381-480 dirty language/surface resolution
G481-580 discourse/deixis
G581-680 pragmatics/prosody
G681-760 source/conflict/correction/uncertainty
G761-840 multimodal grounding
G841-920 long mixed material
G921-1000 adversarial integration

IMPORTANT ROUTE ADJUSTMENT:
start a thin synthetic multimodal foundation earlier than G761,
because app/runtime body is already becoming usable.

Do not abandon later large-scale multimodal band.
The early foundation is:
sensory identity + vectors + persistence + naming + causal synthetic world.

Near G1000 require:
- no critical relation family untested
- cumulative retention
- low false inference on mixed attacks
- dirty input without graph pollution
- topic/discourse narrowing
- ambiguity preservation
- source/retraction integrity
- multimodal disambiguation
- comprehension separate from emission
- falling teacher cost

================================================================
19. NEXT RECOMMENDED STEPS FROM THIS EXACT HANDOFF
================================================================

FIRST:
Finish G305 SENSORY BRIDGE.
Do not promote until:
- full regression
- memory
- SQLite
- cold restart
- exact G302 compatibility
- no graph pollution
- physical checkpoint/hash
- Library upload
- repo promotion

G305 intended minimum:
- SensoryGrounder owned by C4LivingRuntime
- runtime_state persistence
- .c4m and .c4db survival
- VISION/AUDIO/SYMBOL and possibly SCREEN bridge
- explicit naming into graph
- one unknown vector does not create entity
- cross-modal stable identity
- sensory vectors never imply action success

SECOND:
G306-ish synthetic multimodal kindergarten:
- simple shapes
- tones/sounds
- symbols
- controlled cross-modal pairs
- adversarial near-neighbors
- naming
- identity vs similarity

THIRD:
3D room physics kindergarten:
- body-relative coordinates
- directional movement
- distance
- collision
- gravity
- support
- object permanence
- reach/grasp/release
- action -> observed delta -> verified outcome

FOURTH:
sound/letter/word fragment layer:
- acoustic vector
- symbol
- WORD_FORM
- word
- concept
without collapsing them.

FIFTH:
return to dirty-language curriculum with multimodal context now available.

Keep event-frame work going in parallel:
- tense
- polarity
- subject/predicate/object
- safe conjunction scope
- no timeless-property contamination

================================================================
20. REJECTED / DANGEROUS SHORTCUTS
================================================================

Do not reintroduce scored lemma guessing.

A tested heuristic against 343 attested WORD_FORM was rejected.
Bad examples included:
животные -> животный
белое -> белой
словом -> словой

Do not:
- bulk admit grammatically clean statements as truth
- treat unknown word as typo
- distribute negation over conjunction without scope evidence
- turn future claim into current truth
- turn past episode into timeless property
- persist derived relation algebra as evidence
- let vectors create truth
- let ASR create truth
- let tool receipt equal verified outcome
- let LLM teacher write directly into graph
- hardcode benchmark answers
- import nonce/test vocab into canonical weights
- advance generation number without new transferable capability

================================================================
21. AUTOMATION / REMINDER
================================================================

A reminder exists for Friday evening to give Claude:
- CLAUDE_FRIDAY_RUNTIME_TASK.md
- current canonical pair

The reminder was updated to:
G304 runtime + G302 weights.

If main line advances before Friday:
update the current canonical references again before sending.

================================================================
22. REPO / IMPORTANT FILES
================================================================

Repo:
Shabash1744444/-
main

Core recovery files:
00_READ_ME_FIRST.md
01_NEXT_CHAT_HANDOFF.md
CURRENT_STATE.md
RUNTIME_CURRENT.md
ARTIFACT_MANIFEST.md
CHECKPOINT_JOURNAL.md

Theory/methodology:
C4_PRETRAINING_STANDARD_0_TO_1GB.md
C4_AUTOTRAINER_SPEC.md
C4_PRETRAINING_AGENT_TASK.md
C4_TRAINING_RUN_MANIFEST_TEMPLATE.json
C4_G1000_HUMAN_LIKE_PERCEPTION_TARGET.md
PRAGMATICS_PROSODY_ATOMIC_CURRICULUM_NOTE.md
CONTEXTUAL_SURFACE_RESOLUTION_NOTE.md
AGENT_TASK_LIFECYCLE_NOTE.md

Recent checkpoints:
checkpoints/CP_C4_G299_LEXICAL_RELATION_RESTRAINT_GREEN.md
checkpoints/CP_C4_G300_RUNTIME_OPEN_RELATION_QUERY_GREEN.md
checkpoints/CP_C4_G301_RELATION_LANGUAGE_BRIDGE_GREEN.md
checkpoints/CP_C4_G302_ROLE_MEANS_SUCCESSOR_SCOPE_GREEN.md
checkpoints/CP_C4_G303_RUNTIME_EVENT_TENSE_BOUNDARIES_GREEN.md
checkpoints/CP_C4_G304_RUNTIME_EVENT_CONJUNCTION_SCOPE_GREEN.md

Recent canonical artifacts in Library:
/C4_Canonical/child_g302_role_means_successor_scope_green.c4m
/C4_Canonical/C4_RUNTIME_G304_EVENT_CONJUNCTION_SCOPE_GREEN_2026-10-07.zip
/C4_Canonical/C4_G304_RUNTIME_PLUS_G302_WEIGHTS_2026-10-07.zip
/C4_Canonical/README_G304.md
/C4_Canonical/PATCH_G303_TO_G304.diff
/C4_Canonical/g304_g302_validation.json

================================================================
23. USER WORKING STYLE / OPERATIONAL EXPECTATION
================================================================

User wants actual work, not endless planning.

When user says:
"продолжай"
"ебош"
"делай"
=> continue autonomously.

Use checkpoint discipline:
counterexample
-> minimal repair
-> re-attack
-> regression
-> physical artifact
-> hash
-> repo
-> next

If RED:
do not force GREEN.
Keep counterexample.
Repair minimally or discard candidate.

If benchmark itself is wrong:
fix benchmark, do not mutate organism to satisfy invalid test.

Physical checkpointing is mandatory because chats can end or state can reset.

================================================================
24. ONE-SENTENCE RECOVERY SUMMARY
================================================================

Continue C4 from G304 runtime + exact G302 weights; finish the unpromoted G305 living-runtime sensory bridge with vectors as non-authoritative multimodal evidence, then build a synthetic multimodal/3D physics kindergarten while preserving strict epistemic, causal, event-time, scope and UNKNOWN boundaries, and keep Claude's CL-Gxxx runtime branch separate and cherry-pickable.
