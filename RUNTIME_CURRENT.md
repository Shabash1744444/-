# RUNTIME CURRENT — G296 TEMPORAL ORDER GREEN

Canonical runtime: G296.
Canonical weights: G297.

Runtime:
C4_RUNTIME_G296_TEMPORAL_ORDER_GREEN_2026-10-07.zip
300,749 bytes
SHA256 c12f86c80a61fe133cea1d62219d010886c523a434832fee27107fadbc5035e3

Weights SHA256:
0db410bc1ebf71aba05e7571c58e82e6cfb3d17f8c72faea6c09e77e38a6cae9

Combined SHA256:
9daf8aac6f1256543c925751da34c12f39089b6095d8d9914b693cc048bb8ab4

Lineage:
G293 SQLite store
-> G294 inverse/symmetry algebra
-> G295 functional-slot source conflict visibility
-> G296 strict temporal order algebra

G296 safe temporal semantics:
- BEFORE <-> AFTER
- positive temporal paths compose transitively
- reverse proven order refutes read-only
- cycle -> CONFLICT
- direct NEG vs positive path -> CONFLICT
- derived order never persists

Hard boundaries:
ORDER != CAUSE.
SHARED PREDECESSOR != ORDER BETWEEN SIBLINGS.
TEMPORAL DERIVATION != NEW EVIDENCE.
