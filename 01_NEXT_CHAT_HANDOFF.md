# NEXT CHAT HANDOFF — C4 G309 WEIGHTS + G309 RUNTIME

Weights:
- child_g309_support_fall_physics_green.c4m
- 1,992,240 bytes
- SHA256 ac396a927f3819ea38d1af5ed73b2e9ca3078b4cf0b5c4e4f276ef61aa81c197

Runtime:
- C4_RUNTIME_G309_SUPPORT_FALL_PHYSICS_GREEN_2026-10-07.zip
- 314,478 bytes
- SHA256 01d7044d5fc64d86fa0a384c1ad005b1655f20bc9cbba1ddde1c645fd76232b4

Combined:
- C4_G309_RUNTIME_PLUS_G309_WEIGHTS_2026-10-07.zip
- 2,276,116 bytes
- SHA256 aca30b080c2ba9e81a1d986121de545bda78495188f16ae3b25a5fb3c8fe0e6e

## Latest developmental ladder

G306: SELF-relative space — 10/10 heldout.
G307: distinct AUDIO/GLYPH form pathways — noisy 5/5 + 5/5.
G308: contact/collision + effort-response — 96 training interactions, 12/12 heldout.
G309: release/free/support/contact-onset dynamics — 104 training interactions, frozen heldout 20/20.

G309 learned from verified transitions:
- RELEASE -> held-to-free, without fake instantaneous movement;
- HELD -> stable;
- FREE_NO_CONTACT -> downward change + inferred downward acceleration;
- CONTACT_BELOW -> stable;
- CONTACT_ONSET -> downward motion stops.

The synthetic acceleration constant is environment-private. The learner estimates it from observed velocity changes.
Proposition graph is unchanged.

Full regression:
- G309 423 PASS;
- same 18 historical missing-fixture FileNotFoundError failures;
- 0 new semantic/runtime assertion failures.

## Hard laws

AUDIO FORM != TEXT FORM.
PHONEME != GRAPHEME.
SEQUENCE FORM != WORD ENTITY.
WORD FORM != CONCEPT / MEANING.

CONTACT != COLLISION.
MOTOR EFFORT != OBJECT MASS.
RELEASE != MOTION.
HELD != FREE.
CONTACT_BELOW != HELD.
DOWNWARD REGULARITY != WORD GRAVITY.

RAW SIGNAL != TEACHER LABEL.
SIMULATION != OBSERVATION.
ACTION_REQUEST != VERIFIED_OUTCOME.
ENVIRONMENT CHANGE != ACTION REQUEST.

## Next

Continue physical development before naming:
1. multi-step falling trajectories and time-to-contact prediction;
2. horizontal + vertical collision dynamics / momentum-like continuity without prematurely naming momentum;
3. containment / inside-outside / support hierarchy;
4. only after stable physical concepts exist, attach Russian spoken and written labels through the separate G307 form channels;
5. bridge the same physical/sensory receipts into the Nursery room.

Do not solve vocabulary by collapsing modality or by installing semantic labels into low-level physics.
