# CURRENT STATE

Date: 2026-10-07
Canonical weights: G309
Canonical runtime: G309

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

## G306
Verified SELF-relative 3D motor priors.

## G307
Cross-channel lexical-form grounding with strict separation:
AUDIO FORM != TEXT FORM.
PHONEME != GRAPHEME.
WORD FORM != CONCEPT / MEANING.

## G308
Verified contact/collision and effort-to-displacement response learning.
96 interactions. Heldout 12/12.
Large/mobile vs small/resistant anti-shortcut passed.
Graph unchanged.

## G309
Verified support/release/free vertical dynamics.
104 interactions:
- 16 RELEASE;
- 48 FREE_NO_CONTACT;
- 16 CONTACT_BELOW;
- 16 CONTACT_ONSET;
- 8 HELD controls.

Frozen heldout 20/20.
Mean synthetic vertical acceleration inferred from velocity changes: -1.6.
The simulator constant itself was not learner input.
Cold memory + SQLite GREEN.
Graph unchanged.

Protected retention:
- G306 spatial 10/10;
- G307 sound-symbol 6/6 and 10/10 chunks / 5 word entities;
- G308 contact/effort-response GREEN.

Full regression:
423 PASS + same 18 historical missing-fixture FileNotFoundError.
New semantic/runtime failures: 0.

## Current objective
Continue developmental world physics: multi-step trajectories, richer collision dynamics, containment/support hierarchy; name grounded concepts only later through separate spoken/written form channels.
