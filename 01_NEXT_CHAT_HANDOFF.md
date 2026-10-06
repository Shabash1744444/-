# NEXT CHAT HANDOFF — C4 G266

Read CURRENT_STATE.md plus methodology files before training.

## Exact canonical baseline
- child_g266_object_permanence_green.c4m
- 1737251 bytes
- SHA256 1fbbf2c26c8253dab51c5e7555bbb0656a36ca0de98a7874a5589556017b3ea6
- generation G266

Verify bytes/SHA before training.
Recover from /C4_Canonical/ first if needed.

## Latest sequence
G263:
- OmniCaption abstraction pass 3
- 117/117, cold 14/14

G264:
- Russian transfer
- 84/84, cold 14/14

G265:
- 108 raw synthetic PNGs
- 72 train / 36 held-out
- 748/748, cold 10/10

G266:
- 18 motion sequences / 162 frames
- controlled occlusion and reappearance
- 220/220, cold 9/9
- runtime changes 0

Regression:
254 passed / 9 failed; same missing historical artifacts only.

## Hard sensory boundaries
RAW_IMAGE != DERIVED_FEATURE
DERIVED_FEATURE != TEACHER_LABEL
TEACHER_LABEL != AUTONOMOUS VISION
WORLD_STATE != OBSERVABILITY
OBSERVATION_MISSING != WORLD_OBJECT_MISSING
PREDICTION != OBSERVATION

Synthetic ENV_OBJECT_ID is a controlled-environment receipt.
Do not assume real video provides object identity.

## Language
Russian remains primary language-learning channel.
English teacher text remains quarantined from Russian lexicon/syntax.

## Next
Prefer genuine held-out visual transfer, then richer multi-object world physics and Russian speech grounding.
