# C4 — READ ME FIRST

This repository is the canonical development state for C4.

## Identity
C4 is NOT Singularity OS.

## Authority order
1. Physically committed repository state and exact artifact hashes.
2. Reproducible tests/checkpoints.
3. Current chat context.
4. Model/chat memory.

## Current canonical state — 2026-10-07
Weights:
- G279 GUIDED PROSE CORE GREEN
- child_g279_guided_prose_core_green.c4m
- 1826213 bytes
- SHA256 2e9aa26a12ee40210dd465335a3f48865e133728b6f99e95f3d2b821a7444d17

Runtime:
- G278 GUIDED READING GREEN
- C4_RUNTIME_G278_GUIDED_READING_GREEN_2026-10-07.zip
- 1082920 bytes
- SHA256 009e33fb61aa7d173c1e5489d60dd19f50c2fd4bfded2f0ef98e029cc2e558ef

Combined:
- C4_G278_RUNTIME_PLUS_G279_WEIGHTS_2026-10-07.zip
- 2893848 bytes
- SHA256 eb810e3e440efab882be904c2360f5b38e3352450e13ad64f8cf4603a2b10e13

Persistent binaries: /C4_Canonical/.

## Development chain
G270 noun transfer 260/260.
G271 morphology safety.
G272 verb transfer 756/756.
G273 adjective transfer 780/780.
G274 dense semantics 472 novel derived.
G275 live teaching/persistence.
G276 ActiveGaps.
G277 guided measurement 78/78.
G278 conservative ordinary-text reading.
G279 guided prose: 184 novel derived / 68 direct; hierarchy 126/126.

## G278 validation
328/337 clean suite; only 9 unchanged missing historical artifacts.

## Hard rules
HOMOGRAPH != IDENTITY.
ORTHOGRAPHIC SUFFIX != LEXICAL POS.
TEST TOKEN != VOCABULARY KNOWLEDGE.
SPEECH FORM != GRAPH FACT.
AUTOSAVE != NEW EVIDENCE.
QUESTION PRIORITY != TRUTH CONFIDENCE.
UNSUPPORTED SENTENCE != FACT.
OPEN CHAT QUESTION != EXTERNAL TEXT CONTEXT.
GUIDED READING != ARBITRARY BOOK UNDERSTANDING.

## Workflow
counterexample -> minimal repair/training -> held-out -> restraint -> regression -> cold reload -> cumulative -> physical checkpoint -> next

Every block must make later learning cheaper or safer.
