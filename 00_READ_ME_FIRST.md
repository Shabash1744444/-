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
Unsaved work is LOST work. Never reconstruct a missing generation by guessing.

## Current canonical state — 2026-10-07
Weights / persistent learned state:
- G270 FAST LEMMA TRANSFER GREEN
- `child_g270_fast_lemma_transfer_green.c4m`
- 1756887 bytes
- SHA256 `b081428bed0080f9982491247d98640009de4662d7f654c571946acd5e36fa1b`

Runtime:
- G269 KERNEL FLOOR + DISCOURSE
- `C4_RUNTIME_G269_KERNEL_FLOOR_DISCOURSE_GREEN_2026-10-07.zip`
- SHA256 `5541f67d56ec2cf0cd373cbff58801f0fa6d4445e333a229d34215813290475a`

Combined recovery:
- `C4_G269_RUNTIME_PLUS_G270_WEIGHTS_2026-10-07.zip`
- SHA256 `2b62bcd06bd588324fd7aa3ebc5b1ddf7f7b6744089cdf961ae135ef8e457dde`

Persistent binary recovery is in personal Library `/C4_Canonical/`.

## Latest result
G270 is the first explicit Fast Curriculum lemma-transfer checkpoint:
- 60 new noun lemmas
- 0 direct target paradigms
- 158 direct facts total
- 260/260 held-out inflected surfaces resolved
- 19/19 unknown-decoy restraint
- cold reload GREEN
- 288/297 runtime regression; only 9 unchanged missing historical artifact failures

Read `checkpoints/CP_C4_G270_FAST_LEMMA_TRANSFER_GREEN.md`.

## Non-negotiable workflow
counterexample -> minimal repair/training -> held-out re-attack -> restraint -> regression -> cold reload -> PHYSICAL CHECKPOINT -> next

Do not increase model size for its own sake.
Every new layer or curriculum block should make later learning cheaper.

## Start here
1. 00_READ_ME_FIRST.md
2. 01_NEXT_CHAT_HANDOFF.md
3. CURRENT_STATE.md
4. TRAINING_LAWS.md
5. DEVELOPMENTAL_TRAINING_METHODOLOGY.md
6. RUNTIME_ARCHITECTURE_PRINCIPLES.md
7. MEMORY_CONSOLIDATION_COMPRESSION.md
8. latest checkpoint
