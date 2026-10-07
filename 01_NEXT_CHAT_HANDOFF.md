# NEXT CHAT HANDOFF — C4 G297 WEIGHTS + G298 RUNTIME

Weights:
child_g297_relation_diversity_green.c4m
1,960,675 bytes
SHA256 0db410bc1ebf71aba05e7571c58e82e6cfb3d17f8c72faea6c09e77e38a6cae9

Runtime:
C4_RUNTIME_G298_RETRACTION_INVALIDATION_GREEN_2026-10-07.zip
302,268 bytes
SHA256 7ff72ff492ef247c18fe9d44a6927ca06434945c4c7254781930ce960221897f

Combined:
C4_G298_RUNTIME_PLUS_G297_WEIGHTS_2026-10-07.zip
2,240,335 bytes
SHA256 55c15d8f8dd03efb30074b4299037f932d07336ae899b32f3e8d4b06c0e61184

## G295
Functional-slot source conflict is visible in specific truth queries without mutating truth.

## G296
Strict temporal algebra:
BEFORE/AFTER inverse + bounded read-only transitivity.
Reverse path refutes.
Cycle and explicit NEG vs positive path -> CONFLICT.
ORDER != CAUSE.

## G297
40 sparse relation lessons:
PART_OF 12 / OPPOSITE 8 / MEANS 8 / BEFORE 12.

Held-out:
32/32 derived after and cold.
0 direct target leaks.
26/26 cross-relation controls UNKNOWN after and cold.
Exact SQLite 32/32 + 26/26.
All prior G270-G292 cumulative GREEN.

## G298
Counterexample:
source B could assert a FUNCTIONAL value X, later negate X, yet functional conflict reconstruction still treated B as supporting X.

Repair:
functional_source_stances reconstructs current stance in evidence order:
- later POS selects/revises;
- later NEG of selected value retracts;
- NEG of another value does not erase current positive;
- retracting a revised value does not resurrect old superseded value.

Derived invalidation:
PART_OF/HAS_PART, OPPOSITE symmetry and temporal chains disappear when their support is removed.

Validation:
focused G294-G298 32/32.
Full memory 380/389.
SQLite 380 pass + same 9 historical missing artifacts.
Streaming 5/5.
Exact G297 on G298: memory and SQLite 32/32 derived + 26/26 restraint, direct leaks 0.

## Next
Continue G1000 relation coverage:
LOCATION/COLOR/VALUE family semantics, ROLE/MEANS context/source traps, SUCCESSOR and event-frame boundaries, then dirty-language curriculum when relation algebra coverage is sufficiently broad.
