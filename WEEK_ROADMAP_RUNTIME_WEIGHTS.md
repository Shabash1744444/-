# C4 WEEK ROADMAP — RUNTIME + WEIGHTS

Planning document. Do not treat targets as achieved capabilities.

## Track A — Runtime
Preferred workflow: deep audit agent (Claude-style) + independent re-attack before promotion.

Priority:
1 WORD_FORM-aware retrieval
2 Russian morphology/agreement
3 compositional parsing beyond surface regex
4 new-word acquisition protocol
5 teacher-definition parsing
6 reference/ellipsis across turns
7 sentence planning + Russian generation
8 persistence/autosave/checkpoint on mobile
9 initiative utility/prioritization
10 consolidation/forgetting/compression
11 sensory organ interfaces without semantic oracle leakage

Runtime must remain a mechanism layer, not a fact dump.

## Track B — Weights
Continue from canonical G266 unless/until new weights checkpoint is produced.

Priority:
1 core Russian lexical graph
2 morphology
3 RU dialogue nursery
4 simple prose
5 varied literature
6 science/math
7 complex argument/philosophy
8 speech grounding
9 visual/audio grounding
10 game-world test curriculum

Target growth:
2 -> 5 -> 10 -> 30 -> 100 MB only when held-out transfer improves.

## Track C — Live developmental experiments
Keep them small and diagnostic.
Atomic lesson -> one gap -> one answer -> transfer example.
Use results to discover runtime/training defects.
Do not replace bulk curriculum with manual chat teaching yet.

## Track D — Long-horizon proof
When language/runtime is ready:
100-game-day resident test.
Persistent memory, rumor/source separation, learning, goals, relationships, self/history continuity, latency and storage.

## Promotion rule
No runtime or weights release becomes canonical without:
exact artifact/SHA
focused counterexample tests
full regression
cold reload where applicable
checkpoint
repo handoff update.


## Storage/runtime work is now prerequisite to 100-300MB
Before bulk growth reaches phone-breaking scale:
1. benchmark current graph/object expansion precisely;
2. design disk-backed graph schema;
3. preserve provenance and relation typing;
4. build lazy/indexed retrieval;
5. keep hot dialogue/SELF/current-world subset resident;
6. support atomic incremental learning;
7. checkpoint/export back to portable C4 artifact;
8. compare semantic behavior bit-for-bit/receipt-for-receipt against in-memory baseline.

Do not optimize by dropping provenance, UNKNOWN semantics or source independence.

## Claude G268 candidate merge
A newer external Claude runtime candidate adds acquaintance/deixis improvements and reduces lexical-index memory.
It is evidence/candidate, not canonical.
Next runtime agent should diff it against canonical G269 and produce a new merged generation only after combined regression.
