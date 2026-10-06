# RUNTIME CURRENT — G267 RUSSIAN DISCOURSE BRIDGE

Canonical weights remain G266.
Canonical runtime is G267.

## Files
Runtime:
C4_RUNTIME_G267_DIALOGUE_BRIDGE_GREEN_2026-10-07.zip
SHA256 87141d5a1cdee1fce555b300a295ac3ffc77d53df5f884ed9a61b4fe7f87c77a

Runtime + G266 weights:
C4_G267_RUNTIME_PLUS_G266_WEIGHTS_2026-10-07.zip
SHA256 c574850e1fc1a03233cc0ce9f70f782956f1df99ea59f27bb6c3696c6b4f8d50

## Runtime architectural change
Old:
user surface -> bounded parser -> UNKNOWN -> canned fallback

G267:
user surface
-> bounded exact semantic parser
-> if UNKNOWN: RussianDiscourseBridgeV1 + dialogue context
-> safe discourse response / transparent unresolved-language status

The bridge is conservative and read-only with respect to world facts.

## Initiative change
ASK creates an awaiting-response state.
Ticks cannot emit another ASK until a user/teacher turn arrives.
This prevents initiative bursts without deleting initiative itself.

## Compatibility
Runtime state keeps schema string C4_LIVING_RUNTIME_V0.2 for old consumers.
G267 adds optional fields:
- dialogue_history
- awaiting_response
- discourse_schema
Old G266 runtime state loads with defaults.

## Test status
7/7 new dialogue tests PASS.
261/270 full source tests PASS.
9 failures are unchanged missing historical artifact files.
