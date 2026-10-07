# C4 — READ ME FIRST

This repository is the canonical development state for C4.

## Identity
C4 is NOT Singularity OS.

## Authority order
1. Physically committed repository state and exact artifact hashes.
2. Reproducible tests/checkpoints.
3. Current chat context.
4. Model/chat memory.

If memory conflicts with repository state, repository wins.

## Current canonical state — 2026-10-07
Weights:
- G277 GUIDED MEASUREMENT CORE GREEN
- child_g277_guided_measurement_core_green.c4m
- 1814566 bytes
- SHA256 84ab317de73d65b459447a31471715e69726d2df37122ea0352f6da38ca1f2c4

Runtime:
- G276 ACTIVE GAPS GREEN
- C4_RUNTIME_G276_ACTIVE_GAPS_GREEN_2026-10-07.zip
- 281120 bytes
- SHA256 6a8e174e0d3e79bd90c04d66e55964b9c22feb16f5eb9d83f0724278506d2a17

Combined:
- C4_G276_RUNTIME_PLUS_G277_WEIGHTS_2026-10-07.zip
- 2076668 bytes
- SHA256 ceb2149903ea6ef47cefbeb1caeaabe963ebde84458cd00c7fc72881093ccf35

Persistent binaries: personal Library /C4_Canonical/.

## Current developmental chain
- G270 nouns: 260/260.
- G271 verb/POS guard.
- G272 verbs: 756/756; transfer/direct 5.906.
- G273 adjectives: 780/780; transfer/direct 7.879.
- G274 semantics: 472 novel derived; transfer/direct 4.140.
- G275 live teaching/persistence.
- G276 ActiveGaps: utility-ranked Teacher Cost.
- G277 guided measurement core: 3 teacher relations -> 78/78 held-out hierarchy targets; 104 novel derived / 56 direct.

## G276 regression
321/330 clean-unzip PASS.
Only 9 unchanged missing historical artifact failures.
0 new assertion failures.

## Hard rules
HOMOGRAPH != IDENTITY.
ORTHOGRAPHIC SUFFIX != LEXICAL POS.
TEST TOKEN != VOCABULARY KNOWLEDGE.
SPEECH FORM != GRAPH FACT.
AUTOSAVE != NEW EVIDENCE.
QUESTION PRIORITY != TRUTH CONFIDENCE.
GUIDED SEMANTIC EXTRACTION != RAW READING.

## Workflow
counterexample -> minimal repair/training -> held-out re-attack -> restraint -> regression -> cold reload -> cumulative re-attack -> PHYSICAL CHECKPOINT -> next

Every new block must make later learning cheaper.

## Start here
1. 00_READ_ME_FIRST.md
2. 01_NEXT_CHAT_HANDOFF.md
3. CURRENT_STATE.md
4. checkpoints/CP_C4_G276_RUNTIME_ACTIVE_GAPS_GREEN.md
5. checkpoints/CP_C4_G277_GUIDED_MEASUREMENT_CORE_GREEN.md
6. curriculum/FAST_CURRICULUM_PROGRESS_G270_G277.md
