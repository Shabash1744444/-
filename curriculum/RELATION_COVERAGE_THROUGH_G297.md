# C4 RELATION COVERAGE — THROUGH G301

Status: living coverage ledger for the G1000 perception target.

## Strongly tested
IS_A: direct, multi-hop transitivity, negative/path conflict, inheritance, source disagreement.
CAN / PROPERTY / USED_FOR: typed inheritance, exclusions, conflict, multi-level reuse.
CAUSES: direct, multi-hop, branching/convergence, reverse/cross restraint, source-aware reading, ORDER != CAUSE.
PART_OF / HAS_PART: read-only inverse, polarity/conflict, HAS != HAS_PART, non-transitive PART_OF, support-removal invalidation, open-list inverse query.
BEFORE / AFTER: inverse, transitive read-only path, reverse refutation, NEG/path conflict, cycles, sibling restraint, invalidation.
OPPOSITE: symmetric read-only, invalidation, natural query path.
SYNONYM / ANTONYM: symmetric read-only, G299 real lexical experience, 24/24 reverse held-out, non-transitive traps, SYNONYM != IDENTITY/IS_A/MEANS, G300 open queries, G301 language bridge.
FUNCTIONAL slots: same-source revision, independent-source disagreement, specific conflict visibility, SET isolation, retraction/current-source stance.
QUERY_RELATION: G301 adds синоним, антоним, противоположность, роль, смысл, преемник; natural queries are read-only.

## Partially tested / next
MEANS: direct, reverse restrained, query noun «смысл»; needs source conflict/retraction/contextual sense.
ROLE: not inherited/symmetric, query noun «роль»; needs time/context/source scope.
SUCCESSOR: query noun «преемник»; needs non-transitivity, correction/conflict, predecessor/cycle traps.
LOCATION / COLOR / VALUE: generic functional conflict/retraction works, but world cardinality is context/scope-sensitive; see CARDINALITY_SCOPE_NOTE.md.
WHEELS / HAS_SIDES / HAS_CORNERS: functional storage exists; needs family-specific correction/source/language tests.
HAS: SET cardinality, HAS != HAS_PART; needs possession/containment/attribute ambiguity.
EVENT_*: needs event-frame cardinality, temporal/context identity, correction and mixed-source traps.

## Rule
A relation is not done because a direct query passes.
Promotion requires positive, negative, UNKNOWN, source/conflict, correction/retraction, cold persistence, valid composition, invalid-composition traps and cross-relation confusion tests where applicable.
