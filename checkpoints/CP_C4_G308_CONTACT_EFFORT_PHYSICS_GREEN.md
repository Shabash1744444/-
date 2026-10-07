# CP C4 G308 CONTACT / EFFORT PHYSICS GREEN

Status: GREEN
Date: 2026-10-07
Parent: exact G307 weights + G307 runtime.

## Goal
Extend G306 SELF-relative synthetic 3D experience into verified contact/collision and effort-response learning without semantic shortcuts such as "heavy" or "mass".

## Training
96 verified synthetic interactions:
- 12 near TOUCH;
- 4 far TOUCH no-contact controls;
- 64 movable PUSH interactions across four opaque targets;
- 8 far PUSH no-contact controls;
- 8 anchored PUSH interactions with verified contact/collision and zero displacement.

Hidden simulator response/anchoring values participate in environment physics but are never exposed to the learner.
Learner receives motor effort, verified contact/collision, before/after target position, measured displacement and provenance.

## Laws
CONTACT != COLLISION.
ACTION_SUCCESS != OBJECT_DISPLACEMENT.
MOTOR EFFORT != OBJECT MASS.
SIZE / APPEARANCE != PHYSICAL RESPONSE.
SIMULATION != OBSERVATION.

The learned response profile is empirical displacement-per-effort. It is not a semantic word meaning and is not asserted as physical mass.

## Anti-shortcut
A deliberately large target was more mobile than a deliberately small target.
The learner still ranked the small target as more resistant from receipts.
Size/name were not learner inputs.

## Held-out
12/12 novel effort/pose displacement predictions.
Cold memory GREEN.
Cold SQLite GREEN.

G306 spatial retained 10/10.
G307 retained 6/6 sound-symbol links, 10/10 sequence chunks and 5 shared word entities.

## Graph isolation
- entities 10,720 -> 10,720;
- facts 10,764 -> 10,764;
- order 22,282 -> 22,282;
- graph_hot.json unchanged.

## Regression
Exact G307 parent in same environment: 407 PASS + 18 historical-fixture FileNotFoundError.
G308: 415 PASS + same 18 FileNotFoundError.
New semantic/runtime assertion failures: 0.

## Artifacts
Weights:
- child_g308_contact_effort_physics_green.c4m
- 1,990,583 bytes
- SHA256 7514473482308858166670238b1bfbc946e223102443e22ec3c76e38fbf10ba5

Runtime:
- C4_RUNTIME_G308_CONTACT_EFFORT_PHYSICS_GREEN_2026-10-07.zip
- 319,082 bytes
- SHA256 88532c2963c0d3a7bc302ae9363ba48a6a4f7477304c2538555a154abf9053c3

Combined:
- C4_G308_RUNTIME_PLUS_G308_WEIGHTS_2026-10-07.zip
- 2,289,646 bytes
- SHA256 703dbba1666a2ea127c0bc4312e68f91c6b1971e8fa42c259a75b738fffe71ee

Status: CANONICAL GREEN.
