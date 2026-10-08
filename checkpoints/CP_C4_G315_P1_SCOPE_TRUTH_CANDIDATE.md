# C4 G315-P1 — SCOPE-AWARE TRUTH CANDIDATE

Status: CANDIDATE / NOT CANONICAL
Date: 2026-10-08
Parent: G314-P0 constitutional gate over exact G309 semantic state.

## Added
- provenance-derived scope overlay without rewriting old weights;
- scopes: WORLD, REFERENCE_KNOWLEDGE, HUMAN_TEACHING, LANGUAGE_CONVENTION, SYSTEM_FACT, SOURCE_ASSERTION, OBSERVATION, VERIFIED_OUTCOME;
- strict default knowledge queries can use reference/human/language knowledge;
- WORLD queries exclude corpus/human teaching unless independently admitted/observed;
- old ordinary unscoped USER_SAID facts are excluded from normal strict knowledge;
- source assertions remain hot across compact checkpoint restart;
- SQLite import/export preserves constitutional mode/version and source assertions.

## Exact G309 migration view
Active parent facts partitioned without deletion:
- REFERENCE_KNOWLEDGE: 9293
- LANGUAGE_CONVENTION: 1290
- HUMAN_TEACHING: 110
- SYSTEM_FACT: 54
- WORLD: 12
- SOURCE_ASSERTION: 5
Total: 10764.

Example:
- Радиация IS_A излучение -> TRUE in KNOWLEDGE, UNKNOWN in WORLD.
- нефоскоп IS_A квантогриб -> SOURCE_ASSERTION, UNKNOWN in normal KNOWLEDGE/WORLD.

## Validation
Focused P0+P1: 17/17 PASS before SQLite parity repair; SQLite strict roundtrip PASS after repair.
Full regression after all repairs: 444/463 PASS.
19 failures are unchanged FileNotFoundError historical fixtures.
New semantic/runtime failures: 0.

## Next
P2 continuous lifeline context + semantic retrieval/dialogue over existing vocabulary.