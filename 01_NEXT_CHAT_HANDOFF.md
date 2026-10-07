# NEXT CHAT HANDOFF — C4 G308 WEIGHTS + G308 RUNTIME

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

## GREEN lineage

G306:
- 88 verified 3D interactions;
- 10 learned SELF-relative effects;
- 10/10 novel-pose heldout.

G307:
- separate phoneme and grapheme sensory concepts;
- repeated many-to-many sound/glyph alignment;
- sound and glyph sequences may converge on one explicit word entity;
- noisy heldout 5/5 AUDIO + 5/5 GLYPH in memory and SQLite.

G308:
- 96 verified synthetic interactions;
- TOUCH can yield CONTACT without COLLISION;
- PUSH can yield CONTACT + COLLISION;
- far attempts remain NO_CONTACT;
- anchored object can yield verified contact with zero displacement;
- response learned from displacement per motor effort, not object name or size;
- large/mobile vs small/resistant anti-shortcut pair passed;
- 12/12 novel effort/pose heldout;
- graph unchanged;
- cold memory + SQLite GREEN;
- G306/G307 retained.

Regression in same environment:
- exact G307 parent: 407 PASS + 18 historical-fixture FileNotFoundError;
- G308: 415 PASS + same 18;
- new semantic/runtime assertion failures: 0.

## Hard laws

AUDIO FORM != TEXT FORM.
PHONEME != GRAPHEME.
SOUND ASSOCIATION != IDENTITY.
SEQUENCE FORM != WORD ENTITY.
WORD FORM != CONCEPT / MEANING.

CONTACT != COLLISION.
ACTION_SUCCESS != OBJECT_DISPLACEMENT.
MOTOR EFFORT != OBJECT MASS.
RESPONSE INDEX != WORD MEANING.
SIZE / APPEARANCE != PHYSICAL RESPONSE.

RAW SIGNAL != TEACHER LABEL.
SIMULATION != OBSERVATION.
ACTION_REQUEST != VERIFIED_OUTCOME.

## Next

Continue developmental physics without semantic shortcuts:
1. support / release / fall regularities;
2. richer collision/contact dynamics and relative velocity;
3. bind already-grounded physical concepts to spoken and written forms without collapsing modalities;
4. bridge the same receipt/sensory contracts into the Nursery application room.

Do not teach the word "heavy" by writing a mass label into the learner. Let physical response exist first; naming comes later as a teaching/binding act.
