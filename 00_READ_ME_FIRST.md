# C4 — READ ME FIRST

C4 is NOT Singularity OS.

## Canonical — 2026-10-07
Weights: G297 RELATION DIVERSITY GREEN
- child_g297_relation_diversity_green.c4m
- 1,960,675 bytes
- SHA256 0db410bc1ebf71aba05e7571c58e82e6cfb3d17f8c72faea6c09e77e38a6cae9

Runtime: G298 RETRACTION INVALIDATION GREEN
- C4_RUNTIME_G298_RETRACTION_INVALIDATION_GREEN_2026-10-07.zip
- 302,268 bytes
- SHA256 7ff72ff492ef247c18fe9d44a6927ca06434945c4c7254781930ce960221897f

Combined:
- C4_G298_RUNTIME_PLUS_G297_WEIGHTS_2026-10-07.zip
- 2,240,335 bytes
- SHA256 55c15d8f8dd03efb30074b4299037f932d07336ae899b32f3e8d4b06c0e61184

Recovery: /C4_Canonical/.

## Latest
G295:
- FUNCTIONAL slot disagreement is visible in specific yes/no queries.

G296:
- strict BEFORE/AFTER temporal order;
- transitive read-only temporal paths;
- reverse-path refutation;
- cycles and NEG-vs-positive-path -> CONFLICT;
- ORDER != CAUSE.

G297 weights:
- 40 direct relation lessons;
- 32/32 strict derived held-out after + cold;
- 0 direct target leaks;
- 26/26 cross-relation traps UNKNOWN;
- all protected G270-G292 capabilities GREEN;
- growth vs G292: +7,746 bytes.

G298:
- derived inverse/symmetric/temporal state invalidates immediately when support disappears;
- FUNCTIONAL source stance reconstruction now respects later retraction;
- retraction does not resurrect an older superseded value;
- NEG of another value does not erase the current positive stance;
- evidence history remains distinct from current source stance.

Validation:
- focused G294-G298: 32/32;
- full memory: 380/389;
- SQLite split: 380 pass + same 9 historical missing artifacts;
- streaming SQLite 5/5;
- exact G297 on G298: memory 32/32 + 26/26, SQLite 32/32 + 26/26, direct leaks 0;
- cumulative G270-G292 GREEN on G298.

Quality > bytes > generation count.
