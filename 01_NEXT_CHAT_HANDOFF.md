# NEXT CHAT HANDOFF — C4 G297 WEIGHTS + G296 RUNTIME

Weights:
child_g297_relation_diversity_green.c4m
1,960,675 bytes
SHA256 0db410bc1ebf71aba05e7571c58e82e6cfb3d17f8c72faea6c09e77e38a6cae9

Runtime:
C4_RUNTIME_G296_TEMPORAL_ORDER_GREEN_2026-10-07.zip
SHA256 c12f86c80a61fe133cea1d62219d010886c523a434832fee27107fadbc5035e3

Combined:
C4_G296_RUNTIME_PLUS_G297_WEIGHTS_2026-10-07.zip
SHA256 9daf8aac6f1256543c925751da34c12f39089b6095d8d9914b693cc048bb8ab4

## G295
Functional relation yes/no answers now surface slot-level source disagreement.
Focused 6/6.
Full memory 366/375; SQLite split 366 pass + same 9 historical missing artifacts.

## G296
Strict temporal order algebra:
BEFORE/AFTER inverse + transitive positive paths.
Reverse positive order refutes query read-only.
Cycle or explicit NEG vs positive path -> CONFLICT.
Shared predecessor does not order siblings.
Temporal order != causality.
Focused G294+G295+G296 25/25.
Full memory 373/382; SQLite 373 pass + same 9 historical missing artifacts; streaming 5/5.

## G297
40 sparse direct lessons:
PART_OF 12 / OPPOSITE 8 / MEANS 8 / BEFORE 12.

Strict held-out:
32/32 derived after and cold:
- HAS_PART inverse 12
- reverse OPPOSITE 8
- temporal transitive/inverse endpoint 12

Restraint:
26/26 UNKNOWN after and cold:
- HAS != HAS_PART
- MEANS not symmetric
- temporal order != CAUSES

0 direct target leaks.
SQLite exact G297: 32/32 + 26/26.
All prior cumulative G270-G292 GREEN.

## Next
Continue G1000 relation-algebra/trap coverage:
retraction/correction invalidation, functional cardinality by relation family, LOCATION/VALUE/COLOR traps, ROLE/MEANS context, and mixed source conflict.
