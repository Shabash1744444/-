# RUNTIME CURRENT — G293 SQLITE STORE GREEN

Canonical runtime: G293.
Canonical weights: G292.

Runtime:
C4_RUNTIME_G293_SQLITE_STORE_GREEN_2026-10-07.zip
1,010,691 bytes
SHA256 a2ccaa0ecd862657328338f1b5e87726d21753748152a1a8989a368f1ac251c5

Weights SHA256:
d5631373fbdf24f2bf7a8068ca768edc0a4e94765e5b43035c90c3712aa2d246

Combined:
C4_G293_RUNTIME_PLUS_G292_WEIGHTS_2026-10-07.zip
SHA256 c526d21fb0c1bf7aaa5390f84bdcc5fecc35fc11337d2f4d67ec4fd4a3295541

G293 = canonical G289 cognition + cherry-picked CL-G270 storage/query infrastructure:
- SQLiteGraph disk-backed graph
- streamed c4m import/export
- indexed retrieval and reverse queries
- indexed morphology/rule coverage paths
- per-turn transaction persistence
- fast reopen without hydrating full graph
- USER_SAID carry-forward when replacing base weights
- memory-store compatibility

Boundaries:
STORE CHANGE != COGNITIVE LAW CHANGE.
DISK INDEX != NEW EVIDENCE.
.c4m = exchange/canonical checkpoint.
.c4db = operational disk store.

Validation:
memory 352/361; SQLite 352/361; same nine historical missing artifacts only.
