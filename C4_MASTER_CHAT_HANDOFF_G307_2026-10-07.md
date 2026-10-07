# C4 MASTER CHAT HANDOFF — G307 — 2026-10-07

This is the recovery entrypoint for a new chat. Extended snapshot with the same name is stored in /C4_Canonical/.

## Exact canon

Weights:
child_g307_sound_grapheme_words_green.c4m
SHA256 648ba7eeaf1f1f1af038949e228b1e9a37afd115ff6920952533143bbda8350f

Runtime:
C4_RUNTIME_G307_SOUND_GRAPHEME_WORDS_GREEN_2026-10-07.zip
SHA256 b18c746f61fa9e4ec6af5323657ac6af0ede64b5b30a4ef4a51c5c1a1731c7ca

Combined:
C4_G307_RUNTIME_PLUS_G307_WEIGHTS_2026-10-07.zip
SHA256 4068e8c8c7a6128747433e3c92bb5795b1f33faed385784c27d3d3e095285f49

Regression:
409 passed + 16 FileNotFound environment failures in memory.
409 passed + 16 FileNotFound environment failures in SQLite.
New semantic failures: 0.

## Boundaries

C4 != Singularity OS.
Mobile app/body is separate.
Claude CL-Gxxx is runtime/R&D numbering, not C4 training-generation numbering.

## Current development line

G302 ROLE/MEANS/SUCCESSOR scope.
G303 event tense boundaries.
G304 event conjunction scope.
G305 durable sensory bridge.
G306 verified synthetic 3D spatial physics.
G307 sound/grapheme/word grounding.

## Critical current laws

UNKNOWN != FALSE
QUESTION != ASSERTION
DERIVED != OBSERVATION
SIMULATION != OBSERVATION
PREDICTION != EVIDENCE
ACTION_REQUEST != VERIFIED_OUTCOME
RECEIPT != CAUSAL PROOF
SIMILARITY != IDENTITY
RAW SIGNAL != TEACHER LABEL
PART_OF != TRANSITIVE BY DEFAULT
HAS != HAS_PART
MEANS != SYMMETRIC
ROLE != INHERITED BY DEFAULT
EVIDENCE HISTORY != CURRENT SOURCE STANCE
RETRACTION != RESURRECTION OF OLD STANCE
PAST EPISODE != CURRENT STATE
FUTURE CLAIM != CURRENT STATE
FUTURE CLAIM != VERIFIED OUTCOME
NEGATED CONJUNCTION != DISTRIBUTED NEGATION
VECTOR SIMILARITY != IDENTITY
RAW SENSORY OBSERVATION != GRAPH TRUTH
SINGLE UNKNOWN MODALITY != NEW ENTITY
WORLD AXIS != EGOCENTRIC DIRECTION
MOTOR PRIOR != EXTERNAL-WORLD FACT
PHONEME != GRAPHEME
SOUND ASSOCIATION != IDENTITY
SEQUENCE FORM != WORD ENTITY

Never weaken laws just to turn a benchmark GREEN.

## Recent results

G302:
44 novel lessons (MEANS16/ROLE16/SUCCESSOR12), 24/24 forbidden inference controls UNKNOWN.

G303:
negative past queries fixed; Russian future auxiliary no longer pollutes subject/current state; PAST != PRESENT != FUTURE; FUTURE != VERIFIED OUTCOME.

G304:
positive SET conjunction may create separately queryable proposition-events; negative conjunction does not distribute automatically; known multiword identity outranks split.

G305:
SCREEN/AUDIO/SYMBOL are distinct vector modalities inside durable living runtime.
Repeated supported grounding may converge on one sensory concept.
Single unknown modality does not create a graph entity.
Explicit naming binds sensory identity to graph entity.
Focused 54/54.

G306:
88 verified synthetic 3D interactions -> 10 learned SELF-relative effects.
10/10 novel-pose heldout.
Graph unchanged by motor-prior training.

G307:
6 phoneme concepts + 6 grapheme concepts.
24 repeated sound<->glyph alignments.
5 word entities grounded independently from sound and glyph sequences.
Heldout 5/5 noisy audio + 5/5 noisy glyph, memory and SQLite.
G306 spatial 10/10 retained.
G302 reasoning retained.

SoundSymbolBridge APIs:
learn_sound_symbol
glyphs_for_sound
sounds_for_glyph
observe_form_sequence
bind_sequence_name
resolve_form_sequence

## Multimodal/body direction

Correct path:
RAW SIGNAL
-> modality vector/features
-> candidate sensory identity
-> repeated cross-modal grounding
-> explicit entity/event binding
-> graph semantics
-> causal/temporal/world relation
-> ACTION_REQUEST
-> receipt
-> VERIFIED_OUTCOME.

Vectors are similarity/address evidence, never truth.

Sound/glyph/image/screen pattern/word/world object may refer to one entity but are not identical representations.

## 3D room physics next

The room is developmental infrastructure, not decoration.

Next curriculum:
1. contact/collision;
2. resistance/effort/mass-like behavior;
3. near/far + toward/away from SELF;
4. up/down/support/fall-like regularity;
5. containment/reachability;
6. object state across frames.

Train:
action -> verified sandbox outcome -> motor/world prior -> held-out world/pose test.

Simulation scope stays explicit.

## Sound/letter/word next

raw audio
-> acoustic vector
-> recurring sound concept
-> phoneme-side concept
-> learned sound<->glyph mapping
-> sequence
-> explicit word entity
-> meaning.

Many-to-many mapping is allowed.
Later: speaker/noise variation, syllables/fragments, ASR-like corruption, prosody.

## PC-use/voice target

speech -> AUDIO grounding -> language/goal -> SCREEN/VISION grounding -> target -> ACTION_REQUEST -> adapter -> receipt -> inspect resulting state -> VERIFIED_OUTCOME -> learning/credit.

Never assume action success from command or receipt alone.

## Claude branch

CL-G270 Storage: SQLite/disk graph, fast startup/low RAM, c4m import/export, carry-forward.
CL-G271 Reading: article -> unknown -> ask -> answer -> new gaps -> reread; persistent state/provenance; question count example 82 -> 48 -> 11.
CL-G272 Frames: typed clause/event-frame direction.

Claude branch is R&D/mutation. Cherry-pick proven organs; do not wholesale overwrite newer canonical cognition.

CLAUDE_FRIDAY_RUNTIME_TASK.md is already updated to exact G307/G307.

## App vision

Separate app line:
chat, mic/audio, VAD/ASR/TTS, barge-in, screen stream/screenshots, camera/video, files/network/weights, 3D room/body/avatar, sandbox physics, mini-games, later phone/PC control.

## AutoTrainer

Do not hand G307->G1000 to an unsupervised script yet.
Future trainer must automate routine work but know when to stop:
GREEN continue;
clear local RED bounded repair;
ambiguous RED quarantine/ask;
suspicious evaluation no promotion.

See C4_AUTOTRAINER_SPEC.md and C4_PRETRAINING_STANDARD_0_TO_1GB.md.

## Open issues

- COLOR/LOCATION/VALUE scope/cardinality needs context/time/scope.
- dirty language: typo/slang/reduction/ASR noise.
- discourse/deixis.
- pragmatics/prosody.
- source/conflict/retraction at scale.
- richer real multimodal grounding.
- long mixed material.
- persistent TASK lifecycle.

## Do not reintroduce

Rejected heuristic lemma guessing:
животные->животный
белое->белой
словом->словой

Do not auto-correct unknown lexemes permanently by edit distance.
Do not trust autogenerated held-out without validation.
Do not treat graph reachability as intervention.
Do not treat SYNONYM as identity.
Do not distribute negation blindly.
Do not equate vector/sound/glyph associations with identity.

## Recovery order

Read:
1. this file;
2. 00_READ_ME_FIRST.md;
3. CURRENT_STATE.md;
4. 01_NEXT_CHAT_HANDOFF.md;
5. RUNTIME_CURRENT.md;
6. G305/G306/G307 checkpoints;
7. C4_G1000_HUMAN_LIKE_PERCEPTION_TARGET.md;
8. C4_PRETRAINING_STANDARD_0_TO_1GB.md;
9. C4_AUTOTRAINER_SPEC.md;
10. CLAUDE_FRIDAY_RUNTIME_TASK.md.

If conversation text disagrees with repo state, repo/checkpoints win.

Exact next start:
G307 weights + G307 runtime.

Next:
synthetic contact/collision and resistance/effort physics.
