# C4 G321-P7 — LIVE REPLAY GREEN CANDIDATE

Status: **LIVE-TEST CANDIDATE / NOT CANONICAL**
Date: 2026-10-08
Parent: G320-P6 semantic composition candidate over G319-P5 / G317-P3 state.

## Purpose
Close the final frozen-live counterexamples before returning C4 to real Android conversation.

## Constitutional repairs
- Valid semantic answer to an actually open/published C4 inquiry may COMMIT only as `HUMAN_TEACHING` knowledge.
- `HUMAN_TEACHING != WORLD`: human teaching does not become direct physical-world observation.
- `NEXT_UTTERANCE != ANSWER`: unrelated later claims remain source assertions.
- `Запомни` / `помни` may express teaching intent but cannot select an omitted subject from a pending inquiry.
- A source may retract its own latest assertion by a learned semantic self-correction/retraction act; retraction never asserts the opposite.
- SELF/OTHER names are `SOCIAL_REPORT`, not WORLD facts.
- compound social speech may split into safe independent acts.
- chat smiley punctuation is stripped from lexical identity boundaries; `слон)` does not become an entity.

## Language-only state growth
12 LANGUAGE_CONVENTION relations were added for generic source-self-retraction semantics:
- `напиздеть` -> `отзыв утверждения`, forms `напиздил`, `напиздел`;
- `соврать` -> `отзыв утверждения`, forms `соврал`, `соврала`;
- `наврать` -> `отзыв утверждения`, forms `наврал`, `наврала`;
- `ошибиться` -> `самокоррекция утверждения`, forms `ошибся`, `ошиблась`.

No WORLD observation was added by this language training.

## Exact candidate state
- entities: 10,727
- facts: 10,781
- order: 22,306
- composition units/links at baseline: 6 / 5
- sensory concepts: 16

Model:
- `child_g321_p7_live_candidate.c4m`
- bytes: 2,001,317
- SHA256: `49d4b7c02f0dc3125ebe8536ad24afb940eb7a1e76a4f0a61a77ca9eb51af893`

Runtime:
- `C4_RUNTIME_G321_P7_LIVE_CANDIDATE_2026-10-08.zip`
- bytes: 344,015
- SHA256: `590297a3e81a9ba335df663c445f0584822ca9735b1f292fa4e27b78d002b5ed`

## Validation
Focused constitutional/dialogue/lifeline stack G310 + G314-G321: **67/67 PASS**.
Full workspace suite: **489 PASS / 19 FAIL**.
All 19 failures are FileNotFoundError for the same unavailable historical model/fixture paths.
New semantic/runtime assertion failures: **0**.

## Frozen live replay
Required results:
- `процесс -> изменение`: KNOWLEDGE TRUE / HUMAN_TEACHING TRUE / WORLD UNKNOWN;
- inquiry `что такое процесс?`: RESOLVED;
- `Запомни это Поговорить...` does not steal `изменение` as hidden subject;
- `кошка -> слон`: KNOWLEDGE UNKNOWN / WORLD UNKNOWN;
- false source claim can be RETRACTED by learned self-correction;
- USER social name: Руслан;
- SELF social name: Синька;
- no `слон)` entity;
- no opaque coordination-tail entity;
- cold reload preserves constitution, teaching scope, social names, retraction, inquiry status and composition.

Result: **FINAL_FROZEN_REPLAY_GREEN**.

## Live-test rule
Use a clean copy. Live failures become frozen counterexamples, then:
`counterexample -> minimal general repair -> re-attack -> regression -> cold reload -> physical checkpoint`.