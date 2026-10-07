# NEXT CHAT HANDOFF — C4 G274 WEIGHTS + G271 RUNTIME

Read CURRENT_STATE.md and checkpoints/CP_C4_G274_DENSE_SEMANTIC_CORE_GREEN.md first.

## Exact canonical weights
- child_g274_dense_semantic_core_green.c4m
- 1805052 bytes
- SHA256 6e566b67e54504fbdb9f2924bdba0ed330dce5ce525acb97234d5dd33676c20e

## Exact canonical runtime
- C4_RUNTIME_G271_MORPH_VERB_GUARD_GREEN_2026-10-07.zip
- 228891 bytes
- SHA256 5d7720e172017f0b32f2c0b92fcee3eb88e6a8be40580c454778eec6f6a76f31

## Combined recovery
- C4_G271_RUNTIME_PLUS_G274_WEIGHTS_2026-10-07.zip
- 2036899 bytes
- SHA256 e23bcff6cb54746d5aeda27b6d0477452eff81f6c291046706c00bdc97bd06d3

Persistent recovery: personal Library /C4_Canonical/ first.

## What changed
G271 runtime:
- blocks verb suffix transforms from guessing noun lexical POS;
- exact aliases still win;
- full suite 289/298, same 9 missing historical artifact failures.

G272 weights:
- 84 target verbs, zero target paradigms;
- 756/756 held-out;
- transfer/direct 5.906.

G273 weights:
- 78 target adjectives, zero target paradigms;
- 780/780 held-out;
- transfer/direct 7.879;
- homograph quarantine introduced.

G274 weights:
- 92 semantic members;
- 114 direct facts;
- 472 novel derived truths;
- transfer/direct 4.140;
- 10 unrelated decoys, zero false transitions.

## Cumulative final re-attack
- G270 nouns 260/260
- G272 verbs 756/756
- G273 adjectives 780/780
- G274 semantics 472/472
- verb safety 10/10

## Current learning objective
Move from BOOTSTRAP toward GUIDED learning by reducing Teacher Cost.

Next:
1. build active-gap utility scoring;
2. measure which unresolved relation unlocks the most downstream queries;
3. small unseen-text guided-reading benchmark;
4. count teacher questions / teacher relations required for competency;
5. only then scale Dense Core further.

Do not bulk-ingest books or dictionaries.
Do not resolve homographs by destructive merge.
Do not train around runtime defects.
