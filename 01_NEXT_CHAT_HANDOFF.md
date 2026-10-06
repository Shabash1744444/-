# NEXT CHAT HANDOFF — C4 G266 WEIGHTS + G268 RUNTIME

Read CURRENT_STATE.md first.

## Exact canonical weights
- child_g266_object_permanence_green.c4m
- 1737251 bytes
- SHA256 1fbbf2c26c8253dab51c5e7555bbb0656a36ca0de98a7874a5589556017b3ea6

## Exact canonical runtime
- C4_RUNTIME_G268_SURFACE_VERBALIZER_GREEN_2026-10-07.zip
- SHA256 db02d7f9c4da15cfbcc38ef4a3110e696e611eaaef90e3612effa84761cf60bb

Combined recovery package:
- C4_G268_RUNTIME_PLUS_G266_WEIGHTS_2026-10-07.zip
- SHA256 ad93604fb662da091e696a31e7f66cf7794ea51a6fd71efaa32892cea69dc1aa

Persistent recovery: personal Library /C4_Canonical/ first.

## Critical distinction
G268 is a RUNTIME generation, not a new weight generation.
Do not call the weights G267.
Do not retrain G266 to memorize app fallback examples.

## Why G267 exists
The Android conversation exposed a global language gateway bottleneck.
Exact fallback string:
`Я пока не понимаю эту фразу. Попробуй сказать проще или научи меня.`
was found in runtime `c4child/dialogue.py`.

The bounded Russian parser was rejecting ordinary context-dependent dialogue before the organism's richer state could be used.

## G267 repair
`RussianDiscourseBridgeV1` sits above the old exact parser.
It adds:
- persisted compact dialogue context
- adjacency pairs
- ellipsis/context for short replies
- meta-language/meta-capability questions
- transparent unresolved-language handling
- language UNKNOWN != world-knowledge UNKNOWN
- initiative ASK waits for response before another ASK

It does NOT:
- add an external LLM
- change G266 weights
- commit guessed world facts
- weaken epistemic invariants

## Validation
New tests: 7/7 PASS.
Full suite: 261 PASS / 9 unchanged missing historical artifact failures.
Real G266 tests confirm:
`Какие фразы ты знаешь?` no longer hits fallback.
C4 ASK -> `Научу` yields `Хорошо. Я слушаю.`
No ASK burst without an intervening user/teacher response.

## Next
First test G267 in the Android app with G266 weights.
Collect real dialogue counterexamples.
Do not patch isolated phrases unless they expose a reusable discourse class.
Continue Russian-first policy.


## G268 additional fixes
- `Привет` is a GREETING, not unknown language.
- `Я не понимаю тебя` is interpreted from USER perspective; no SELF leakage.
- opaque internal labels (g223/node/internal IDs) are never verbalized as teacher questions.
- human-readable knowledge gaps can still initiate normally.
- 14/14 dialogue adversarial tests PASS; full suite 268 PASS / 9 unchanged missing artifacts.
