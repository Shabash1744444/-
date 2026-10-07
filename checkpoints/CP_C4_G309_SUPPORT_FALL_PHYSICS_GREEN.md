# CP C4 G309 SUPPORT / FALL PHYSICS GREEN

Status: CANONICAL GREEN
Date: 2026-10-07
Parent: exact G308 weights + G308 runtime.

## Training
104 verified synthetic interactions:
- 16 RELEASE;
- 48 uninterrupted FREE_NO_CONTACT;
- 16 CONTACT_BELOW stable;
- 16 CONTACT_ONSET / landing;
- 8 HELD stability controls.

Hidden simulator acceleration is never learner input.
The learner sees verified before/after position, velocity, held state, contact-below state, dt and receipt provenance.

## Learned regularities
RELEASE -> HELD_TO_FREE without fake instantaneous movement.
HELD -> POSITION_STABLE.
FREE_NO_CONTACT -> DOWNWARD_CHANGE + DOWNWARD_ACCELERATION.
CONTACT_BELOW -> POSITION_STABLE.
CONTACT_ONSET -> DOWNWARD_MOTION_STOPPED.

Estimated mean vertical acceleration from experienced velocity changes: -1.6.

## Frozen heldout
20/20:
- 12 unseen free-motion combinations with new dt/height/radius/initial vertical velocity;
- 4 unseen supported-contact configurations;
- 4 unseen contact-onset configurations.

Cold memory GREEN.
Cold SQLite GREEN.

## Retention
G306 spatial 10/10.
G307 sound-symbol 6/6; 10/10 chunks; 5 shared word entities.
G308 contact/collision + effort-response GREEN.

## Graph isolation
10,720 entities -> 10,720.
10,764 facts -> 10,764.
order 22,282 -> 22,282.
graph_hot.json unchanged.

## Regression
423 PASS.
18 FileNotFoundError only for the same unavailable historical fixtures.
0 new semantic/runtime assertion failures.

## Laws
RELEASE != MOTION.
HELD != FREE.
CONTACT_BELOW != HELD.
DOWNWARD REGULARITY != WORD GRAVITY.
SIMULATION != OBSERVATION.
ENVIRONMENT CHANGE != ACTION REQUEST.
ACTION_REQUEST != VERIFIED_OUTCOME.
AUDIO FORM != TEXT FORM.
PHONEME != GRAPHEME.
WORD FORM != CONCEPT / MEANING.

## Artifacts
Weights: child_g309_support_fall_physics_green.c4m
1,992,240 bytes
SHA256 ac396a927f3819ea38d1af5ed73b2e9ca3078b4cf0b5c4e4f276ef61aa81c197

Runtime: C4_RUNTIME_G309_SUPPORT_FALL_PHYSICS_GREEN_2026-10-07.zip
314,478 bytes
SHA256 01d7044d5fc64d86fa0a384c1ad005b1655f20bc9cbba1ddde1c645fd76232b4

Combined: C4_G309_RUNTIME_PLUS_G309_WEIGHTS_2026-10-07.zip
2,276,116 bytes
SHA256 aca30b080c2ba9e81a1d986121de545bda78495188f16ae3b25a5fb3c8fe0e6e
