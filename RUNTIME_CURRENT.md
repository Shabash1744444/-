# RUNTIME CURRENT — G293 SQLITE STORE GREEN

Canonical runtime: G293.
Canonical weights: G292.

Runtime SHA256:
a2ccaa0ecd862657328338f1b5e87726d21753748152a1a8989a368f1ac251c5

Weights SHA256:
d5631373fbdf24f2bf7a8068ca768edc0a4e94765e5b43035c90c3712aa2d246

Combined SHA256:
c526d21fb0c1bf7aaa5390f84bdcc5fecc35fc11337d2f4d67ec4fd4a3295541

G293 = canonical G289 cognition plus disk-backed storage/query infrastructure from CL-G270.

Capabilities:
- SQLiteGraph lazy graph
- indexed retrieval/reverse queries/rule coverage
- streamed checkpoint import/export
- per-turn durable transactions
- USER_SAID carry-forward across changed weights
- memory mode still supported

Validation:
- memory 352/361
- SQLite 352/361
- same nine historical missing artifacts only

Boundary:
STORAGE CHANGE != COGNITIVE CHANGE.
