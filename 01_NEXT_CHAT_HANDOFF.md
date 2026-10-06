# NEXT CHAT HANDOFF — C4 G266 WEIGHTS + G267 RUNTIME

Read CURRENT_STATE.md first.

## Exact canonical weights
- child_g266_object_permanence_green.c4m
- 1737251 bytes
- SHA256 1fbbf2c26c8253dab51c5e7555bbb0656a36ca0de98a7874a5589556017b3ea6

## Exact canonical runtime
- C4_RUNTIME_G267_DIALOGUE_BRIDGE_GREEN_2026-10-07.zip
- SHA256 87141d5a1cdee1fce555b300a295ac3ffc77d53df5f884ed9a61b4fe7f87c77a

Combined recovery package:
- C4_G267_RUNTIME_PLUS_G266_WEIGHTS_2026-10-07.zip
- SHA256 c574850e1fc1a03233cc0ce9f70f782956f1df99ea59f27bb6c3696c6b4f8d50

Persistent recovery: personal Library /C4_Canonical/ first.

## Critical distinction
G267 is a RUNTIME generation, not a new weight generation.
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
