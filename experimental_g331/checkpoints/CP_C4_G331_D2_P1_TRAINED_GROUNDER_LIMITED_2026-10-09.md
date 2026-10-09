# C4 G331 — D2-P1 native trained grounded story candidate (2026-10-09)

**STATUS: LIMITED LEARNING PROVEN; FULL D2 REMAINS RED.** C4 is not Singularity OS. Four owners EVAL/COMMIT/DRIVE/MEDIATE and five influence classes remain unchanged. C004 Android physical action is still DEVICE_PENDING; do not mark it DONE.

## Immutable input / saved new artifacts
- Input model D1 native copy sha256: `86986428afd7bd6957f57bea30596a5ccbb361647c2bf0bd29cbc6d1ddd1aa01` (11,821 hydrated facts).
- New trained D2-P1 `C4_G329_D2_P1_GROUNDED_STORY_CANDIDATE.c4m`: 2,346,483 bytes, 12,767 cold facts, SHA256 `f8ed0e709b565ae0b437b8b273cd70c75762ed09ebb5cbe31bf099e6a412309c`.
- Companion full native runtime **58 Python modules**: `C4_D2_P1_NATIVE_RUNTIME_58_MODULES.zip` sha256 `5c86a156ec657bc6ea3f13db32bb114f6bea23363cbbbb47e5d4a114a978c6e4`.
- Reproducibility archive `C4_D2_P1_GROUNDED_STORY_PROOF_PACKAGE_2026-10-09.zip` SHA256 `d62347bea4ef0ba9dddc4cbb68c1dd35df182b446e7f4121e2541a0c495b2fe7`. Physical Library folder `/C4_Candidates/G331_NATIVE_COGNITION/D2_P1_GROUNDED_STORY_2026_10_09/` stores **all three** artifacts. ZIP contains actual c4m, full runtime, code/patch, test, frozen dataset, JSON report and README. The original G329/L1/D1 files are untouched.

## Exactly what was trained
Native organ `c4child/d2_grounder.py` uses a generic supervised multiclass intent learner and a structured first-order sequence tagger (Viterbi + perceptron) to infer typed input `INVITE/NEXT/OTHER` and a dynamic `FOCUS` span from raw text. **No hardcoded phrase routing in inference and no external frame at evaluation.** It stores 946 `D2_GROUNDER_WEIGHT` records through original `BootstrapTeacher` and strict graph admission as `LANGUAGE_CONVENTION`, all from **one dependent EXTERNAL_CORPUS/TEACHER root**. Inference in normal `C4LivingRuntime.user_message` proposes STORY interpretations through EVAL; no WORLD commits; outputs are delivered through original DRIVE public-act arbitration. Existing D1 trained speech-act policy and its **finite teacher-supplied reply patterns remain**. This is a *bounded* learned language organ, **not proof of unlimited semantic composition**.

## Frozen measurements (synthetic; distinct heldout categories)
- Teaching: 620 supervised episodes, 8 epochs. 300 INVITE, 160 NEXT, 160 OTHER built from finite training templates and 20 training focus terms. These are **not 620 independent natural-human conversations**.
- Same new runtime with original D1 model before D2 weights: 0 trained grounded story-input correct in heldout set.
- **Unseen referents, familiar training constructions:** 81/100 correct intent AND full extracted focus span.
- **Entirely withheld construction families:** 12/50. Strong failure; not a passed broad operator-transfer gate.
- **Out-of-domain negative phrases:** 8/8 properly declined/OTHER on a tiny heldout set. Abstention counted correctly as a negative success, NOT as positive understanding.
- **Known NEXT phrasings:** 3/3; **unseen NEXT phrasings:** 0/4.
- Cold C4M: all categories exactly retained; no semantic mutations or old-fact edits (946 new language-only facts); D1 old synthetic benchmark still 112/125.
- 4 independently runnable local native tests PASS.
- Shuffled intent labels **while retaining correct slot tags** (same training examples): familiar test 38/100, new construction 10/50, previously seen NEXT 0/3. Not a total teacher-shuffle control.
- Example actual `user_message` first utterance: `давай придумаем историю про космический чайник` -> learned `OPEN_SCENE` reply with dynamic focus, next `а что дальше` -> `ASK_GOAL` referring to the same focus. Before D2 same native code + D1 weights gives NOT_UNDERSTOOD. Current learned response still has Russian morphology error: `для космический чайник`.
- Eight-turn original D2 FREE TEXT remains RED: first invitation understood but fictional names, belief scopes, corrections, physical situation and several multi-question turns not; NO claim of general human dialogue or source-safe free learning.

## Hypothesis / next architecture exam
The D1 language readout has **representation-loss** and **linear interaction/XOR** limits. This new learnt sequence binder repairs only a narrow text-to-scene entry, NOT D1's nonlinear policy expressive limit. Next phase requires genuinely **trainable typed-relational composition**: variable binding for speaker/addressee/story subject, negation, modality, temporal/causal scope, perspective and source lineage, followed by a differentiable or structured graph message-passing mechanism, trained by operator-family-disjoint curricula. No per-phrase `if` handlers, no oracle frame, no independent LLM answering during eval.

Protocol next: freeze full multi-turn adversarial holdout; train COPY of D2-P1; compare code-identical untrained, shuffled labels, independent human judgments, unseen operator FAMILIES, cold and all previous constitutional regressions. No massive autonomous distillation before these gates.

**Note:** New runtime 58-module ZIP and new model are separate Android-importable artifacts, but actual on-phone invocation and C004 physical action were NOT tested in this cycle.
