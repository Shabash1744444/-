# C4 — READ ME FIRST

This repository is the canonical development state for C4.

## Identity
C4 is NOT Singularity OS. They are separate architectures and separate projects.
Do not merge their runtime, memory, actors, laws or terminology by assumption.

## Authority order
1. Physically committed repository state and exact artifact hashes.
2. Reproducible tests/checkpoints.
3. Current chat context.
4. Model/chat memory.

If memory conflicts with repository state, repository wins.
Unsaved work is LOST work.

## Current canonical state — 2026-10-07
Weights:
- G274 DENSE SEMANTIC CORE GREEN
- child_g274_dense_semantic_core_green.c4m
- 1805052 bytes
- SHA256 6e566b67e54504fbdb9f2924bdba0ed330dce5ce525acb97234d5dd33676c20e

Runtime:
- G271 MORPHOLOGY VERB GUARD GREEN
- C4_RUNTIME_G271_MORPH_VERB_GUARD_GREEN_2026-10-07.zip
- 228891 bytes
- SHA256 5d7720e172017f0b32f2c0b92fcee3eb88e6a8be40580c454778eec6f6a76f31

Combined recovery:
- C4_G271_RUNTIME_PLUS_G274_WEIGHTS_2026-10-07.zip
- 2036899 bytes
- SHA256 e23bcff6cb54746d5aeda27b6d0477452eff81f6c291046706c00bdc97bd06d3

Persistent binary recovery: personal Library /C4_Canonical/.

## Latest Fast Curriculum chain
- G270 nouns: 260/260 held-out.
- G271 runtime safety: verb transforms require explicit verb evidence.
- G272 verbs: 756/756 held-out, transfer/direct 5.906.
- G273 adjectives: 780/780 held-out, transfer/direct 7.879.
- G274 semantics: 472 novel derived truths from 114 direct facts, transfer/direct 4.140.

Cumulative G274 re-attack is fully GREEN.

## New hard rule
HOMOGRAPH != IDENTITY.
If a new lemma collides with an existing useful surface, quarantine it until contextual POS/sense disambiguation exists.

## Non-negotiable workflow
counterexample -> minimal repair/training -> held-out re-attack -> restraint -> regression -> cold reload -> cumulative prior-skill re-attack -> PHYSICAL CHECKPOINT -> next

Do not optimize bytes or corpus volume.
Every new block must make later learning cheaper.

## Start here
1. 00_READ_ME_FIRST.md
2. 01_NEXT_CHAT_HANDOFF.md
3. CURRENT_STATE.md
4. curriculum/FAST_CURRICULUM_PROGRESS_G270_G274.md
5. TRAINING_LAWS.md
6. DEVELOPMENTAL_TRAINING_METHODOLOGY.md
7. RUNTIME_ARCHITECTURE_PRINCIPLES.md
8. MEMORY_CONSOLIDATION_COMPRESSION.md
9. latest checkpoint
