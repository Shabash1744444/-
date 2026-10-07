# CURRENT STATE

Date: 2026-10-07
Canonical weights: G306
Canonical runtime: G306

Weights:
- child_g306_synthetic_spatial_physics_green.c4m
- 1,983,393 bytes
- SHA256 78d68b05845bd1b54cebc430d2b902d796b56b8efb9c7922328647989f8c5ded

Runtime:
- C4_RUNTIME_G306_SYNTHETIC_3D_PHYSICS_GREEN_2026-10-07.zip
- 304,847 bytes
- SHA256 c8f7a4605655984910d76735e8e4a6f7ab68e7d5ec43d281dc6df32aae8eddbb

Combined:
- C4_G306_RUNTIME_PLUS_G306_WEIGHTS_2026-10-07.zip
- 2,258,483 bytes
- SHA256 25aed1de0c7f3eda2d8937e748944e461856e5e1f7945c695a84cd31c9c9915e

## G305
Durable SCREEN/AUDIO/SYMBOL sensory grounding.

## G306
Synthetic embodied 3D physics:
- SELF-relative axes (+x right, +y up, +z forward);
- yaw changes egocentric frame;
- action request does not mutate world;
- stale request != success;
- only verified SANDBOX_RECEIPT can train spatial effects;
- 88 verified interactions;
- learned LEFT/RIGHT/UP/DOWN/FORWARD/BACKWARD, TURN_LEFT/RIGHT, TOWARD/AWAY;
- 10/10 novel-pose heldout;
- graph unchanged by simulated motor training;
- cold memory + SQLite GREEN.

Exact older cognition retained:
G302 44/44 direct + 24/24 restraint UNKNOWN; natural queries read-only.

Full runtime regression:
404 passed + 16 missing-file environment failures in memory;
404 passed + 16 missing-file environment failures in SQLite;
new semantic failures 0.

## Current objective
Build phoneme/grapheme/sound-symbol sequence grounding without collapsing sound into letter identity; then contact/collision and mass/effort physics.
