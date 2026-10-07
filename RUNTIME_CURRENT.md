# RUNTIME CURRENT — G308 CONTACT / EFFORT PHYSICS GREEN

Canonical runtime: G308.
Canonical weights: G308.

Runtime SHA256:
88532c2963c0d3a7bc302ae9363ba48a6a4f7477304c2538555a154abf9053c3

Weights SHA256:
7514473482308858166670238b1bfbc946e223102443e22ec3c76e38fbf10ba5

## New durable physical organ

ContactEffortLearner:
- learns verified CONTACT / COLLISION / NO_CONTACT effects;
- records empirical motor-effort -> measured-displacement response;
- estimates displacement-per-effort;
- compares response without asserting semantic mass labels;
- persists through .c4m and SQLite runtime state.

Runtime-facing methods:
- learn_contact_transition(...)
- contact_effect(...)
- physical_response_profile(...)
- compare_physical_response(...)
- predict_push_displacement(...)

SyntheticContactWorld is deterministic SANDBOX physics. Hidden response/anchor parameters are environment-only and are not learner transition fields.

## Retained

G306 spatial APIs remain.
G307 SoundSymbolBridge remains.

AUDIO FORM != TEXT FORM.
PHONEME != GRAPHEME.
SOUND ASSOCIATION != IDENTITY.
SEQUENCE FORM != WORD ENTITY.
WORD FORM != CONCEPT / MEANING.

CONTACT != COLLISION.
MOTOR EFFORT != OBJECT MASS.
SIMULATION != OBSERVATION.
ACTION_REQUEST != VERIFIED_OUTCOME.
