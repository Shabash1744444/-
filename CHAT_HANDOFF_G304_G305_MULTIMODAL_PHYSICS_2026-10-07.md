# C4 CHAT HANDOFF — G304 CANON + G305 SENSORY BRIDGE IN PROGRESS

Date: 2026-10-07

C4 and Singularity OS are separate projects. Do not merge concepts/code unless explicitly requested.

## Current canonical pair

Weights:
- G302 ROLE / MEANS / SUCCESSOR SCOPE GREEN
- child_g302_role_means_successor_scope_green.c4m
- 1,981,454 bytes
- SHA256 250625e164ffd6a7809f75129c2919a00a303cf97198cc27179ed9115f219ba7

Runtime:
- G304 EVENT CONJUNCTION SCOPE GREEN
- C4_RUNTIME_G304_EVENT_CONJUNCTION_SCOPE_GREEN_2026-10-07.zip
- 301,378 bytes
- SHA256 59ca94c6dd2ab78c881e015eaf885ebbc1ca1407696ca0102707d1b032a51aae

Combined:
- C4_G304_RUNTIME_PLUS_G302_WEIGHTS_2026-10-07.zip
- 2,261,376 bytes
- SHA256 02bd772d97edf43ff7c0bdfbc385aa1e746fa48a962e87f3ac3d029331bfd77b

Recovery:
- /C4_Canonical/

## What G303/G304 added

G303 EVENT TENSE BOUNDARIES:
- negative PAST event queries are readable;
- Russian periphrastic FUTURE is recognized separately;
- "Антон будет любить чай" no longer creates fake subject "Антон будет";
- FUTURE claim != current state;
- FUTURE claim != verified outcome;
- past/present/future may coexist without cross-contamination.

G304 EVENT CONJUNCTION SCOPE:
- positive SET conjunction may distribute:
  "любил чай и сок" -> individually queryable tea/juice proposition-events;
- NEGATED CONJUNCTION != DISTRIBUTED NEGATION:
  "не любил чай и сок" is NOT automatically converted into two separate negations;
- known multiword entity/phrase identity wins over surface split;
- focused event tests 22/22;
- full workspace 390/406 memory and 390/406 SQLite;
- all 16 failures are FileNotFound environment failures only;
- semantic assertion failures 0;
- exact G302 retained: 44/44 direct + 24/24 restraint, memory == SQLite.

## Current organism knowledge line

Important recent lineage:
G270 noun morphology
G271 POS guard
G272 verb transfer
G273 adjective transfer
G274 dense semantics
G275 live teaching
G276 ActiveGaps
G277 guided measurement
G278 guided reading
G279 guided prose
G280 everyday core
G281 lexical gaps
G282 contextual action terms
G283 contextual quantities
G284 semantic family consolidation
G285 family-accelerated lexical
G286 causal guided reading
G287 causal prose
G288 branching/converging causal motifs
G289 mixed-chunk dependency
G290 explanatory prose
G291 deep hierarchy
G292 hierarchy-accelerated concepts
G293 SQLite store
G294 inverse/symmetry algebra
G295 functional slot conflict
G296 temporal order
G297 relation diversity
G298 retraction invalidation
G299 lexical relation restraint
G300 open relation query
G301 relation-language bridge
G302 ROLE/MEANS/SUCCESSOR scope
G303 event tense boundaries
G304 event conjunction scope

## Current laws / boundaries

UNKNOWN != FALSE
QUESTION != ASSERTION
DERIVED != OBSERVATION
PREDICTION != EVIDENCE
ACTION_REQUEST != VERIFIED_OUTCOME
RECEIPT != CAUSAL PROOF
SIMILARITY != IDENTITY
CANONICAL != VERIFIED AUTHORITY
SOURCE/ADDRESS != EVIDENCE
SUMMARY != ORIGINAL EVIDENCE
COMPRESSION != NEW TRUTH
RAW SIGNAL != TEACHER LABEL
EVIDENCE HISTORY != CURRENT SOURCE STANCE
RETRACTION != RESURRECTION OF OLD STANCE
ORDER != CAUSE
PART_OF != TRANSITIVE BY DEFAULT
HAS != HAS_PART
MEANS != SYMMETRIC
ROLE != INHERITED BY DEFAULT
SYNONYM != IDENTITY
LEXICAL SYMMETRY != TRANSITIVITY
PAST EPISODE != CURRENT STATE
FUTURE CLAIM != CURRENT STATE
FUTURE CLAIM != VERIFIED OUTCOME
NEGATED CONJUNCTION != DISTRIBUTED NEGATION
KNOWN PHRASE IDENTITY > SURFACE SPLIT

## G305 — SENSORY BRIDGE IN PROGRESS

Do NOT assume G305 is canonical yet unless a later checkpoint says GREEN.

Reason to start now:
the mobile/app/runtime body is beginning to outrun organism training.
The app can expose voice/screen/sensors/room, so C4 needs a thin multimodal grounding layer before full dirty-language and before massive real media.

Existing runtime already has an older SensoryGrounder:
- VISION / AUDIO / SYMBOL vector modalities;
- stable concept creation only after repeated/multimodal agreement;
- novelty rejection;
- can ask for a name for a stable unnamed object;
- source/provenance;
- synthetic world tests where class labels are not handed directly to the grounder.

Important: this layer existed but was not fully integrated as persistent living-runtime state.

G305 intended goal:
- integrate sensory grounding into C4LivingRuntime runtime_state;
- persist through .c4m and .c4db;
- allow VISION/AUDIO/SYMBOL/SCREEN-like adapters to converge on one candidate entity;
- explicit naming maps sensory concept -> graph entity;
- vectors remain evidence/address/similarity, not truth;
- a lone unknown vector must NOT auto-create a permanent world entity;
- repeated/multimodal agreement may create stable sensory identity;
- memory/SQLite restart must preserve grounding;
- action physics remains separate.

Focused combined sensory/event/body tests reached 34/34 before full-suite work.

A harness bug was found and fixed:
synthetic world produced VISION/AUDIO/SYMBOL while one helper mistakenly expected SCREEN/AUDIO/SYMBOL.
This was a test mismatch, not architecture failure.

Full suite then hit an environment issue:
old test_claude_redteam_g207.py did not add repo root to sys.path.
Need rerun with explicit PYTHONPATH=. and continue validation.
Do not call G305 GREEN until full validation + exact G302 compatibility + physical checkpoint.

## Core multimodal principle

Use vectors as sensory addresses / similarity evidence, NOT as truth.

Pipeline:

RAW SIGNAL
-> features/vector
-> candidate sensory identity
-> multimodal/context confirmation
-> graph entity/event
-> causal/epistemic reasoning

Do not collapse:
VECTOR SIMILARITY != IDENTITY
RAW AUDIO != WORD
RAW IMAGE != OBJECT
SCREEN PATCH != VERIFIED ENTITY
SENSOR EVENT != WORLD FACT

The graph remains the semantic/epistemic owner.
Vectors help propose what may be observed.

## PC-use / agent bridge target

Long-term app/runtime should support normal voice conversation + PC-use.

Desired high-level chain:

voice/audio
-> acoustic/vector evidence
-> candidate word/intent/entity
-> graph/context
-> screen vector confirms target object/entity
-> ACTION_REQUEST
-> adapter/tool action
-> RECEIPT
-> verify changed screen/world state
-> VERIFIED_OUTCOME

Never:
vector -> direct action truth
or
receipt -> assumed success.

## Synthetic multimodal kindergarten — start now

Do NOT wait until G760 for first grounding.

Start with controlled synthetic curriculum:
- geometric shapes;
- simple 2D/3D objects;
- procedural colors/textures;
- simple tones/syllables;
- letters/symbols;
- short frame sequences;
- synchronized labels only in teacher path, never as hidden ground-truth injection into perception;
- adversarial variants / noise / viewpoint changes.

Goal:
teach modality boundaries and cross-modal identity before real camera/mic/video.

## 3D room / world physics curriculum

The mobile app has / will have a room/body.
C4 must learn world physics through action -> state change -> observation.

Teach:
- left / right;
- up / down;
- forward / backward;
- toward self / away from self;
- near / far;
- inside / outside;
- above / below;
- in front / behind;
- rotation / facing direction;
- contact / collision;
- move / stop;
- reach / grasp / release / use;
- heavy / light;
- resistance;
- falling / support;
- occlusion / object permanence;
- sound source direction;
- louder/quieter with distance;
- cause/effect of actions.

Important:
these should be grounded in verified state transitions, not dictionary facts.

Example:
ACTION_REQUEST MOVE_FORWARD
-> simulator/room receipt
-> observe position changed
-> verify delta
-> learn relation between action and world transition

ACTION != VERIFIED OUTCOME.

## Sound -> letter -> word layer

User idea:
teach sounds, letters, word fragments, then words.

Correct architectural interpretation:

raw audio
-> acoustic vector/features
-> candidate phonetic fragment
-> SYMBOL/letter or learned sound-unit
-> morpheme/word-fragment
-> word surface
-> graph concept

Do not merge these levels.

Laws:
SOUND != LETTER
LETTER != WORD
WORD != CONCEPT
SAME SOUND != SAME SOURCE
HOMOPHONE != IDENTITY

Possible curriculum:
- synthetic clean phonemes/syllables;
- same phoneme by different voices/pitches;
- same letter in different fonts;
- audio-symbol pairing;
- syllable -> fragment;
- fragment composition -> word;
- word surface -> concept only through explicit grounding/teaching.

This can later support ordinary voice conversation without forcing a transformer tokenizer-style representation.

## Causal graph + entity grounding

User specifically wants grounded entities connectable to causal edges.

Yes, desired pattern:

sensory candidate
-> confirmed entity/event
-> typed graph node
-> BEFORE / CAUSES / PART_OF / LOCATION / etc
-> only if evidence supports relation

Similarity alone must not create causal edges.

SHARED EFFECT != CAUSAL RELATION BETWEEN CAUSES
SHARED CAUSE != CAUSAL RELATION BETWEEN EFFECTS
GRAPH REACHABILITY != INTERVENTION SEMANTICS

## Relation/cardinality issue still open

COLOR / LOCATION / VALUE cannot be treated globally as naive one-value FUNCTIONAL relations forever.

Examples:
- flag may be red AND white;
- object location depends on time/scope;
- value may vary by currency/context/time.

Do NOT blindly change COLOR/LOCATION/VALUE from FUNCTIONAL -> SET.
Need explicit scope/context model.

## Claude branch context

Claude runtime branch numbering is separate from organism generations.

C4 Gxxx = organism/training generation.
CL-Gxxx = Claude runtime/R&D iteration.

Latest user-provided Claude branch:
CL-G272 FRAMES after CL-G271 Reading.

Claude CL-G271 already had:
- SQLite graph;
- reading loop article -> unknown -> ask -> explanation -> new gaps -> reread;
- LLM teacher request interface;
- provenance;
- incremental morphology;
- persistent reading state;
- avalanche 82 -> 48 -> 11 questions across synthetic articles.

CL-G272 then added typed event/clause frames.

Do not wholesale replace canonical cognition with Claude branch.
Cherry-pick organs after regression.

Friday task file:
CLAUDE_FRIDAY_RUNTIME_TASK.md
Reminder currently points to latest canonical runtime/weights.

## Training philosophy

Do NOT automate G302->G1000 blindly yet.

Manual agent-led cycle remains preferred:

counterexample
-> minimal repair
-> re-attack
-> focused exam
-> cold reload
-> memory/SQLite
-> cumulative regression
-> physical checkpoint
-> promote or discard

Reason:
many critical discoveries are benchmark/ontology mistakes, not just code bugs.

Examples already caught:
- bad autogenerated held-out item;
- heuristic lemma guessing;
- unknown lexeme != typo;
- COLOR cardinality not globally trivial;
- future auxiliary contaminating subject;
- unsafe distribution of negated conjunction.

Eventually a semi-autotrainer may do routine work but must STOP on ambiguity.

## G1000 target

Approximate bands remain useful but not rigid:
- relation algebra/traps;
- dirty language/surface resolution;
- discourse/deixis;
- pragmatics/prosody;
- source/conflict/correction;
- multimodal grounding;
- long mixed material;
- adversarial integration.

Important route change:
start a thin multimodal kindergarten NOW rather than postponing all multimodal work to the late band.

## Immediate next actions

1. Finish G305 validation:
   - rerun full suite with PYTHONPATH=.;
   - memory + SQLite;
   - exact G302 compatibility;
   - restart/persistence;
   - no lone-vector entity pollution;
   - no vector->truth leakage;
   - physical checkpoint + hashes.

2. If G305 GREEN:
   G306/G307 synthetic multimodal kindergarten:
   - shapes / simple visual identity;
   - audio tones / syllables;
   - symbols/letters;
   - explicit cross-modal pairing;
   - restraint tests.

3. Then synthetic 3D physics:
   - ego-relative directions;
   - distance;
   - movement;
   - collision/support;
   - grasp/release;
   - action->verified world delta.

4. Add sound->letter->fragment->word layering.

5. Add PC-use sensory/action bridge:
   screen candidate -> entity -> action request -> receipt -> verification.

6. Continue dirty-language/event/cardinality curriculum after thin grounding layer.

## Non-negotiable checkpoint discipline

Every promoted generation must leave:
- weights/runtime artifact;
- exact SHA256;
- checkpoint;
- source/curriculum manifest where relevant;
- frozen heldout;
- regression JSON;
- memory + SQLite validation;
- clean restart;
- no test-vocab contamination;
- repo CURRENT_STATE / handoff / manifest / journal sync.

Quality > bytes > generation count.

If this chat ends, continue from this file and repo CURRENT_STATE. Do not infer current state from conversation memory if repo has newer checkpoint.
