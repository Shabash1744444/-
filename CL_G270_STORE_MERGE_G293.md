# CL-G270 STORE -> CANONICAL G293 MERGE

Date: 2026-10-07

Source:
Claude branch CL-G270 STORE, based on its older G266->G270 runtime lineage.

Decision:
DO NOT replace canonical runtime wholesale.
Cherry-pick only storage/query infrastructure onto canonical G289.

Reason:
CL-G270 predates later canonical cognition layers:
G275 live teaching,
G278 guided reading,
G281 lexical gaps,
G286 causal guided reading,
G289 mixed-chunk dependency and PROPERTY precedence.

Integrated:
- SQLiteGraph disk-backed graph
- streamed .c4m import/export
- indexed retrieval and reverse queries
- indexed rule coverage
- per-turn transaction persistence
- quick reopen without hydrating full graph
- USER_SAID carry-forward across changed weights with .bak backup
- memory-mode compatibility

Validation after merge:
- memory full suite 352/361
- SQLite full suite 352/361
- all nine failures are unchanged historical missing-artifact FileNotFoundError cases
- latest critical SQLite subset 45/45
- exact G292 semantic held-out 96/96
- exact G292 restraint 36/36 UNKNOWN
- unknown causal text -> zero graph mutation
- .c4m member contents survive store round-trip byte-identically; whole ZIP bytes may differ because of repacking
- USER_SAID migration verified on G292-derived checkpoint

Canonical result:
Runtime G293.
Weights remain exact G292.
