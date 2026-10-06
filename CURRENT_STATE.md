# CURRENT STATE

Date: 2026-10-06
Canonical GREEN generation: G266
Current organism: child_g266_object_permanence_green.c4m
Size: 1737251 bytes
SHA256: 1fbbf2c26c8253dab51c5e7555bbb0656a36ca0de98a7874a5589556017b3ea6

## Active direction
Russian-first language + multimodal abstraction + raw synthetic sensory nursery.

## G263
OmniCaption abstraction pass 3:
- 117/117 admitted
- cold 14/14
- 1602113 bytes
- SHA256 8267844a7169641ea52382cc122c08a223e2eaf7f7f53ad4eec2853a30dd5b7c
- runtime changes 0

## G264
Russian sensory-reasoning transfer:
- 84/84 admitted
- cold 14/14
- 1619770 bytes
- SHA256 aef1f49725358a46915955affe0e4c5ac58ad6055a735e576990fb818e072b3a
- runtime changes 0

## G265
Controlled raw-image nursery:
- 108 physical PNG images 128x128
- 72 train / 36 held-out
- 748/748 admitted
- cold 10/10
- 1707998 bytes
- SHA256 6e62f3839ea41a13a9f420f0e579f549d3b1c95a766d93de01c076ea19a0d8de
- runtime changes 0

Hard boundaries:
RAW_IMAGE != DERIVED_FEATURE
DERIVED_FEATURE != TEACHER_LABEL
TEACHER_LABEL != C4_AUTONOMOUS_RECOGNITION
SYNTHETIC SUCCESS != REAL-PHOTO GENERALIZATION

G265 RED note:
First held-out test polluted itself by calling _eid on the held-out label. RED was not promoted. Harness-only fix; clean rerun from G264.

## G266 — SYNTHETIC OBJECT PERMANENCE — CURRENT GREEN
Parent: G265.
- 18 controlled motion sequences
- 162 physical PNG frames
- moving shape with fixed occluder
- environment maintains exact ENV_OBJECT_ID
- 220/220 admitted
- 0 rejected
- cold 9/9
- 1737251 bytes
- SHA256 1fbbf2c26c8253dab51c5e7555bbb0656a36ca0de98a7874a5589556017b3ea6
- runtime changes 0

Core:
WORLD_STATE != OBSERVABILITY
OBSERVATION_MISSING != WORLD_OBJECT_MISSING
PREDICTION != OBSERVATION
object may remain in world while hidden from current sensor
reappearance may support persistence
synthetic ENV_OBJECT_ID is environment ground truth and must NOT be assumed available in real video
real-video post-occlusion identity remains a hypothesis unless independently grounded

SELF/world:
external object identity remains separate from C4 internal representation
sensory gap != C4 SELF disappearance
internal prediction does not rewrite external history

## Regression after G266
254 passed / 9 failed in 6.57s.
All 9 are unchanged missing historical G207/G137/G151/G153 artifact FileNotFoundErrors.
No new semantic/runtime assertion failures.

## Language policy
Russian remains active natural-language learning channel.
English OmniCaption lexical/syntactic form remains quarantined.
Only language-independent abstractions may cross that firewall.

## Normative loop
counterexample -> minimal repair -> re-attack -> regression -> cold reload -> physical checkpoint -> next

RED never canonical.
No runtime repair merely to fit curriculum.
No byte padding.

## Next
Continue from exact G266.
High-value next:
- held-out shape/category generalization without teacher labels
- richer multi-object synthetic scenes and containment/support/contact
- real Russian speech/audio grounding
- real-video persistence tests with uncertainty instead of ENV_OBJECT_ID
- continue complex Russian discourse in parallel
