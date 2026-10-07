# RUNTIME CURRENT — G309 SUPPORT / FALL PHYSICS GREEN

Canonical runtime: G309.
Canonical weights: G309.

Runtime SHA256:
01d7044d5fc64d86fa0a384c1ad005b1655f20bc9cbba1ddde1c645fd76232b4

Weights SHA256:
ac396a927f3819ea38d1af5ed73b2e9ca3078b4cf0b5c4e4f276ef61aa81c197

## New durable organ

SupportFallLearner:
- learns RELEASE as held-to-free without inventing motion at release time;
- learns free no-contact vertical dynamics from verified before/after state;
- estimates acceleration from velocity change / dt;
- learns stable contact-below condition;
- learns contact onset stopping downward motion;
- keeps all outputs SIMULATION-scoped.

Runtime-facing methods:
- learn_support_transition(...)
- support_effect(...)
- predict_free_vertical_step(...)

SyntheticSupportWorld is deterministic sandbox physics. Its acceleration constant is environment-private and absent from learner transitions.

## Retained organs
G306 SpatialEffectLearner.
G307 SoundSymbolBridge.
G308 ContactEffortLearner.

## Boundaries
AUDIO FORM != TEXT FORM.
PHONEME != GRAPHEME.
WORD FORM != CONCEPT / MEANING.
CONTACT != COLLISION.
MOTOR EFFORT != OBJECT MASS.
RELEASE != MOTION.
HELD != FREE.
CONTACT_BELOW != HELD.
DOWNWARD REGULARITY != WORD GRAVITY.
SIMULATION != OBSERVATION.
ACTION_REQUEST != VERIFIED_OUTCOME.
