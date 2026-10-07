# C4 — READ ME FIRST

C4 is NOT Singularity OS.

## Canonical — 2026-10-07
Weights: G297 RELATION DIVERSITY GREEN
- child_g297_relation_diversity_green.c4m
- 1,960,675 bytes
- SHA256 0db410bc1ebf71aba05e7571c58e82e6cfb3d17f8c72faea6c09e77e38a6cae9

Runtime: G296 TEMPORAL ORDER GREEN
- C4_RUNTIME_G296_TEMPORAL_ORDER_GREEN_2026-10-07.zip
- 300,749 bytes
- SHA256 c12f86c80a61fe133cea1d62219d010886c523a434832fee27107fadbc5035e3

Combined:
- C4_G296_RUNTIME_PLUS_G297_WEIGHTS_2026-10-07.zip
- 2,238,816 bytes
- SHA256 9daf8aac6f1256543c925751da34c12f39089b6095d8d9914b693cc048bb8ab4

Recovery: /C4_Canonical/.

## Latest
G295:
- FUNCTIONAL slot source disagreement is visible even in a specific yes/no query;
- SET relations remain multi-valued and unaffected;
- no new truth is created by conflict reporting.

G296:
- BEFORE/AFTER are one strict directed temporal order;
- temporal paths compose transitively read-only;
- reverse proven order refutes a query read-only;
- temporal cycles and NEG-vs-positive-path disagreements become CONFLICT;
- temporal order does not imply CAUSES.

G297 weights:
- 40 direct relation lessons: PART_OF 12, OPPOSITE 8, MEANS 8, BEFORE 12;
- 32/32 strict derived held-out relations after + cold;
- 0 direct target leaks;
- 26/26 cross-relation traps remain UNKNOWN;
- exact SQLite validation also 32/32 + 26/26;
- all protected G270-G292 capabilities remain GREEN;
- growth vs G292: +7,746 bytes.

Quality > bytes > generation count.
