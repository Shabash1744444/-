# NEXT CHAT HANDOFF — C4 G274 WEIGHTS + G275 RUNTIME

Read CURRENT_STATE.md and checkpoints/CP_C4_G275_RUNTIME_LIVE_TEACHING_MERGE_GREEN.md first.

## Exact canonical weights
- child_g274_dense_semantic_core_green.c4m
- 1805052 bytes
- SHA256 6e566b67e54504fbdb9f2924bdba0ed330dce5ce525acb97234d5dd33676c20e

## Exact canonical runtime
- C4_RUNTIME_G275_LIVE_TEACHING_MERGE_GREEN_2026-10-07.zip
- 324818 bytes
- SHA256 1c7243de518c12cff4a27572cf2e423bd77c5bd6cf70925748e86ce698ef9a68

## Combined recovery
- C4_G275_RUNTIME_PLUS_G274_WEIGHTS_2026-10-07.zip
- 2113082 bytes
- SHA256 10943a16639f4fa6b17eef0e107c1ccf16b864e1a616c0294153e515efde4c5d

Persistent recovery: personal Library /C4_Canonical/ first.

## G275
G275 is a three-way runtime merge, not a weight generation.

Adds:
- ordinary-dialogue teaching intent;
- structured definition decomposition;
- open teaching state that survives restart;
- Russian speech inflection/agreement;
- first/second-person dialogue;
- autosave on state change.

Preserves:
- G271 verb/POS morphology guard;
- discourse history and perspective;
- human-safe one-question initiative;
- public-label firewall;
- question-read-only behavior outside explicit teaching;
- G274 weights unchanged.

The external disposable acceptance-test token was not accepted as vocabulary and is absent from canonical weights/runtime package.

## Validation
- 317/326 full merged suite
- 9 known missing historical artifacts only
- 0 new assertion failures
- nouns 260/260
- verbs 756/756
- adjectives 780/780
- semantic derivations 472/472
- canonical G274 SHA unchanged

## Next objective
ActiveGaps / Teacher Cost.

Build a benchmark where C4:
1. reads a small unseen text;
2. identifies unresolved concepts/relations;
3. ranks them by downstream utility;
4. asks one highest-value question at a time;
5. learns the answer structurally;
6. re-evaluates remaining gaps;
7. is tested on held-out combinations.

Track:
- teacher questions;
- teacher relations/words;
- autonomous admissions;
- correctly UNKNOWN;
- false inference;
- held-out competency.

Do not bulk-ingest books/dictionaries before this loop is GREEN.
