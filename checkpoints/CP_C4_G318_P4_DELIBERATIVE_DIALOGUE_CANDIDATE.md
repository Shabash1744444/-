# C4 G318-P4 — DELIBERATIVE DIALOGUE CANDIDATE

Status: CANDIDATE / NOT CANONICAL
Date: 2026-10-08
Parent state: exact G317-P3 model, unchanged.
Runtime: G318-P4.

## Purpose
Break the remaining hidden rule `COGNITIVE_PROCESS -> IMMEDIATE_PUBLIC_REPLY`.

## Added
- independent EVAL candidate set from kernel semantic parser + discourse bridge;
- `SPEECH_ACT_CANDIDATE` with VALUE, STATUS and provenance in the life-line;
- persistent `pending_public_acts`;
- DRIVE may review an act internally without sending it;
- DRIVE may publish the act on a later cognitive step;
- `FORMULATED != SENT`;
- a formulated question is not marked ASKED and does not open an external inquiry until publication;
- VALUE influences selection but cannot publish by itself;
- compatibility `user_message()` still chooses synchronous public output for the Android shell.

## Cold re-attack
On exact G317 state:
1. `Что ты знаешь про радиацию?` was processed with public output disabled.
2. Proposed speech act: `Радиация — излучение.`
3. Outbox remained empty.
4. Two later cognitive steps reviewed the act; still no public output.
5. Runtime was saved and restarted.
6. Pending act remained READY with review count 2.
7. A later DRIVE step published it.
8. Semantic graph stayed unchanged throughout.

## Multiple interpretations
`Привет` generated at least two EVAL candidates:
- KERNEL / UNKNOWN;
- DISCOURSE / GREETING.
DRIVE selected the speech act; neither candidate had COMMIT authority.

## Constitutional retention
On exact G317 state, `Кошка это слон` remains SOURCE_ASSERTED only; KNOWLEDGE is UNKNOWN.
G317 multimodal and G316 context tests remain green.

## Validation
Focused P0-P4 suite: 42/42 PASS.
Full regression: 469/488 PASS.
19 failures are unchanged FileNotFoundError historical fixtures/models.
New semantic/runtime assertion failures: 0.

## State
Weights/state are EXACT G317-P3:
- model bytes: 1998549;
- SHA256: `0c62250f7845df1a52ea080434ee6eba84771e8d6715611a0dad840ca6d83810`.

No new semantic facts or sensory weights were added in P4.

## Next
P5: multiple concurrent internal/public action candidates and background/return behavior under DRIVE, without converting chat turns into a FIFO queue.
