# C4 D0 — Dialogue learnability gate / forensic audit (2026-10-09)

**RESULT: STILL NOT PROVEN.** Knowledge and event memory are not evidence that the G331 organism can *learn to conduct coherent dialogue*. This is a separate C4 architecture, not Singularity OS. Four constitutional owners (EVAL/COMMIT/DRIVE/MEDIATE) and five influence classes remain untouched; these govern authority and causality but do not themselves learn human speech.

## Read-only empirical probe
- Start/reference GitHub HEAD: `26aac785d7142899061f2023fc71499165e48ff1`. Verified physical source: Library `/C4_Candidates/G331_NATIVE_COGNITION/L1_SUPERVISED_LEXICAL_2026_10_09/`.
- Exact L1 .c4m SHA256 `bba87b3d1b7c48f929236868c2244d05153532b4b173c8d7768783dadc6ef7ce`, 10,908 hydrated facts; tested native 56-module R6-L1 runtime ZIP SHA256 `c9726f5a5645716b61d2ffe07ccb80d1fea48ceab3dbd76f384abcdc6344b9cc`.
- Ten ordinary prompts via existing `C4ChildDialogue.semantic_intent`: **6 UNKNOWN, 3 CLAIM, 1 PREDICT_QUERY**. Two CLAIM tags were semantic misframings, *not* proof of understanding.
- Seven sequential prompts through actual `C4LivingRuntime.user_message`: greeting + two questions got `READ_ONLY_EPISODIC_QUERY`; fictional names got `NOT_UNDERSTOOD`; fictional perspective only got an acknowledgment; why-Masha-was-mistaken got a false CLAIM and `NOT_UNDERSTOOD`; cube-fall got bounded ignorance plus fact retrieval; invitations to invent story or something interesting got `NOT_UNDERSTOOD`. No multi-turn narrative continuation.
- L1 0/48→48/48 trained already-known morphological predicate forms/lexemes on new operands, not a dialogue policy. A **local exploratory** connector-only L2 0/24→24/24 uses a newly coded bounded clause splitter and three graph-taught link words; NOT accepted as general speech learning, and not a released stage without native regressions.
- This probe used loaded real weights; no model file was modified, no Android LIVE retest, no Gemma training. Reproducible script & raw JSON created in the working session; final working files are not automatically GitHub artifacts.

## Mechanism audit
- `c4child/predicate_ru.py:parse_claim`: fixed predicate-between-nominals shape, with graph-trained predicate lexemes.
- `c4child/language_ru.py:RussianChildLanguageV0.parse`: many explicit regular-expression patterns for input.
- `c4child/discourse_ru.py:RussianDiscourseBridgeV1.interpret`: social/follow-up response handling uses explicit literal reply strings, although factual content can also be dynamically retrieved.
- `c4child/bootstrap.py:BootstrapTeacher`: safely writes graph claims and LANGUAGE_CONVENTION mappings; **does not train a conversational response policy**.
- `c4child/rule_induction.py:RuleInductionOrgan` learns bounded structural feature rules, **not** general conversational operator generation.
- `c4child/composition.py` + `C4LivingRuntime` maintain semantic representation, history, goals and initiative, giving useful substrate. But no demonstrated learnable pipeline `discourse_state → speech_act → reply_semantics → linguistic_realization → outcome_credit`.

**Feasibility distinction:** A stateful typed graph with executable, iterative operators can in principle implement a conversation learner. This C4 implementation has **not** empirically demonstrated that. Neither 'graph makes dialogue impossible' nor 'four laws guarantee dialogue' follows from the evidence.

## Pre-registered next experiment D1 (BEFORE mass Gemma distillation)
Use **one tiny narrative domain**: home room, ball/cube/table/basket, optional second character, changing fictional names, actions and corrections. Start from COPY of L1; do not create second brain or overwrite original. Freeze RED and split scenes *before* lesson generation.

Supervision schema: `(scene/speaker/perspective/time, preceding turns, user intention, current goal) -> (typed reply act, semantic content, referents, optional question/action, surface realization, external feedback)`. Teacher (Gemma ~4B) proposes labeled trajectories; it is one dependent EXTERNAL_CORPUS origin, **never independently proves its own facts or progress**. C4 must learn operator applicability/selection, not memorise sample replies.

Initial **planned trial counts, NOT measured**: 0 / 16 / 32 / 64 / 128 / 256 distinct supervised episodes, with baseline, training time, heldout scores, failure logs, exact SHA and cold reload at each step. Freeze multi-turn tests containing entirely withheld story/object/role combinations; contrastive opposite feedback; correction that must not erase unrelated SOURCE assertion; ambiguous reference -> clarify; STORY/REPLAY not WORLD.

**Decisive anti-hardcode ablations:** compare L1 original runtime, same patched native runtime with untrained copy, and patched runtime with trained copy. Disabling learned operator edges should reduce heldout performance; permuting teacher act labels should break it; renaming subjects and changing prior conversation should alter the right act without requiring code changes. If code-only beats baseline as much as trained model, mark FAIL: mechanism was coded, not learned.

Preregister a *target* (not a result): independently verified appropriateness on >=100 unseen conversational turns, for example >=70% typed-act relevance, working multistep story continuity and zero critical SOURCE→WORLD violations. A pass would prove limited-domain native learned dialogue, **not** human-level free conversation.

## Current gates and handoff
C003 last fully DONE. C004 Android room host execution/private Java receipt/C4 credit/cold .c4m still DEVICE PENDING; C005 NOT STARTED. Separate linguistic L2 explored locally but is **not accepted**, do not silently continue learning vocabulary as if that proves dialogue. Prior START: `checkpoints/CP_C4_G331_L2_COMPOSITION_START_2026-10-09.md`. Next action is D1 frozen tests and learned response policy in the SAME native `c4child` and persisted .c4m; do not silently bypass 4 laws or contaminate provenance.