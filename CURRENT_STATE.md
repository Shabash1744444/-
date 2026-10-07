# CURRENT STATE

Date: 2026-10-07
Canonical weights: G308
Canonical runtime: G308

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

## G306
Verified synthetic SELF-relative 3D motor priors.

## G307
Cross-channel lexical-form grounding:
- phoneme-side and grapheme-side concepts remain distinct;
- many-to-many sound/glyph association;
- sound and glyph sequences can converge on one explicit word entity;
- AUDIO FORM != TEXT FORM;
- WORD FORM != CONCEPT / MEANING.

## G308
Verified contact / collision / effort-response physics:
- 96 verified synthetic interactions;
- CONTACT and COLLISION learned as distinct effects;
- NO_CONTACT controls retained;
- anchored zero-displacement contact retained;
- response learned from displacement per motor effort, not name or visual size;
- hidden simulator response parameter never exposed to learner;
- 12/12 heldout on new efforts/poses;
- proposition graph unchanged;
- cold memory and SQLite GREEN.

Protected retention:
- G306 spatial 10/10;
- G307 sound-symbol 6/6;
- G307 sequence chunks 10/10 / 5 shared word entities.

Regression:
- parent G307: 407 PASS + 18 historical missing-fixture FileNotFoundError;
- G308: 415 PASS + same 18;
- new semantic failures 0.

## Current objective
Continue synthetic developmental physics with support/release/fall and richer contact dynamics. Only after physical concepts are grounded should spoken/written labels be attached as separate learned forms.
