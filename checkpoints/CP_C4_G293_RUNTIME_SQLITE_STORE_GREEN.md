# CP C4 G293 RUNTIME SQLITE STORE GREEN

Parent runtime: G289.
Canonical weights: G292 unchanged.

Source: CL-G270 storage infrastructure cherry-picked onto canonical G289.

Validation:
- memory full suite 352/361
- SQLite full suite 352/361
- same nine historical missing artifacts only
- latest critical SQLite subset 45/45
- G292 semantic 96/96
- G292 restraint 36/36 UNKNOWN
- unknown causal text causes zero graph mutation
- checkpoint members round-trip byte-identically
- USER_SAID carry-forward survives changed weights and keeps .bak

Runtime artifact:
C4_RUNTIME_G293_SQLITE_STORE_GREEN_2026-10-07.zip
SHA256 a2ccaa0ecd862657328338f1b5e87726d21753748152a1a8989a368f1ac251c5

Combined:
C4_G293_RUNTIME_PLUS_G292_WEIGHTS_2026-10-07.zip
SHA256 c526d21fb0c1bf7aaa5390f84bdcc5fecc35fc11337d2f4d67ec4fd4a3295541

Boundaries:
STORAGE CHANGE != COGNITIVE CHANGE.
DISK INDEX != NEW EVIDENCE.
DB REPACK != MODEL LEARNING.
USER_SAID CARRY-FORWARD != REPLAY AS NEW EVIDENCE.
