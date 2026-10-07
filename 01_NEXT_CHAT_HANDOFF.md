# NEXT CHAT HANDOFF — C4 G270 WEIGHTS + G269 RUNTIME

Read CURRENT_STATE.md and checkpoints/CP_C4_G270_FAST_LEMMA_TRANSFER_GREEN.md first.

## Exact canonical weights
- child_g270_fast_lemma_transfer_green.c4m
- 1756887 bytes
- SHA256 b081428bed0080f9982491247d98640009de4662d7f654c571946acd5e36fa1b

## Exact canonical runtime
- C4_RUNTIME_G269_KERNEL_FLOOR_DISCOURSE_GREEN_2026-10-07.zip
- SHA256 5541f67d56ec2cf0cd373cbff58801f0fa6d4445e333a229d34215813290475a

## Combined recovery
- C4_G269_RUNTIME_PLUS_G270_WEIGHTS_2026-10-07.zip
- SHA256 2b62bcd06bd588324fd7aa3ebc5b1ddf7f7b6744089cdf961ae135ef8e457dde

Persistent recovery: personal Library /C4_Canonical/ first.

## Critical distinction
G269 is the runtime generation.
G270 is a weights/persistent-state generation.
Runtime physics did not change in G270.

## G270 Fast Curriculum result
60 new noun lemmas were introduced with only noun type + grammatical gender.
Their paradigms were withheld.

Direct:
- 120 target typing facts
- 38 anchor WORD_FORM facts
- 0 target WORD_FORM facts
- 158 total admitted facts

Held-out:
- before new anchors: 140/260 correct
- after anchors: 260/260 correct
- 0 wrong
- 0 UNKNOWN
- 19/19 decoy restraint
- cold reload 260/260

Efficiency:
- transfer/direct = 1.646
- extra transfer unlocked by anchors = 120
- marginal transfer/anchor = 3.158

Regression:
- 288/297 PASS
- same 9 missing historical artifact FileNotFoundErrors
- 0 new semantic/runtime failures

## Current learning objective
Optimize teacher cost, not bytes.

A new curriculum block should report:
- direct lessons
- held-out transferable ability
- correctly UNKNOWN
- false inference
- teacher interventions
- bytes/RAM/latency
- cold reload
- regression

## Next
Continue Fast Curriculum from exact G270:
1. regular verb families and held-out conjugation;
2. adjective agreement families;
3. dense semantic cells for high-utility core lemmas;
4. active-gap prioritization;
5. repeat fixed developmental benchmark and track teacher burden.

Do not dump books or dictionaries into weights without transfer tests.
Do not train around runtime defects.
Do not hardcode corpus facts in runtime.

Mandatory reading:
- DEVELOPMENTAL_TRAINING_METHODOLOGY.md
- LEXICAL_GRAPH_SCALE_TARGETS.md
- RUSSIAN_CURRICULUM_BOOK_ROADMAP.md
- WEEK_ROADMAP_RUNTIME_WEIGHTS.md
- RUNTIME_ARCHITECTURE_PRINCIPLES.md
- MEMORY_CONSOLIDATION_COMPRESSION.md
