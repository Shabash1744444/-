# CP_C4_G331_D1_GRAPH_POLICY_TRAINED_LIMITED_TRANSFER_2026-10-09

**Status: D1 LIMITED LEARNED POLICY PROVEN IN SYNTHETIC TEST; HUMAN CONVERSATION NOT PROVEN.**
C4 is an independent project, **not Singularity OS**. Four constitutional owners EVAL/COMMIT/DRIVE/MEDIATE and influence types MASK/VALUE/AVAIL/TRIGGER/STATUS preserved. C003 last fully DONE, C004 Android action/Java receipt/cold DEVICE PENDING, C005 not started.

## Frozen initial baseline and trained model
- Source immutable L1 native model SHA256 `bba87b3d1b7c48f929236868c2244d05153532b4b173c8d7768783dadc6ef7ce`; 2,080,308 bytes, 10,908 cold-hydrated facts.
- L1 source-matched 56-module original runtime ZIP SHA256 `c9726f5a5645716b61d2ffe07ccb80d1fea48ceab3dbd76f384abcdc6344b9cc`.
- New D1 trained COPY `C4_G329_D1_DIALOGUE_POLICY_20261009.c4m`, SHA256 `86986428afd7bd6957f57bea30596a5ccbb361647c2bf0bd29cbc6d1ddd1aa01`; **2,212,190 bytes, 11,821 cold facts**, exactly 913 added language-convention/policy weight and surface-pattern facts, one dependent EXTERNAL_CORPUS teacher source root. All original L1 facts compared unchanged, original input hash preserved; original runtime state/organs retained. No SOURCE/STORY/teacher-to-WORLD promotion.
- Companion **same native organism** with one additional `c4child/narrative_policy.py` and a narrow delta to `runtime.py` / `scope.py`: `C4_G331_R6_L1_D1_NATIVE_RUNTIME.zip` SHA256 `0125e17eb4e889b5de8dd4e9b4f657e89ba0e71f2c26324c4612dee975c8a52e`, 57 .py modules (original 56 intact).
- All binaries, raw JSON report, source/test scripts and detailed handoff physically saved in **Library** `/C4_Candidates/G331_NATIVE_COGNITION/D1_DIALOGUE_POLICY_2026_10_09/`. GitHub source: `experimental_g331/training/d1/` and regression `experimental_g331/tests/test_d1_policy_learning_ci.py`.

## Direct measurements (not speculative)
125 held-out scenario turns but **only 15 distinct withheld surface utterances**, plus new story objects and changed dialogue contexts. Synthetic labels, no human judges. 256 training episodes use only 30 distinct surface utterances, each in varying situations. Source test-data SHA256 `26f1e35b286045b394088136f9184bbe99389257bedb4f8c9fd7dfcaff5f6e71`.
- Same new native code without learned weights: **0/125**.
- Graph-learned D1 copy: **112/125**; cold reload: **112/125**.
- Deliberately shuffled teacher reply-act labels, same runtime: **0/125**.
- Three curriculum shuffle seeds on same fixed heldout: 112, 102, 111 /125. Not independent heldout splits.
- Learning-curve episodes 16→21/125; 32→96/125; 64→101/125; 128→113/125; 256→112/125. These are measured within this synthetic experiment, NOT estimates of human fluency.
- 7 directed tests **PASS** locally (4 exact-weight/native, 3 fresh-graph CI tests).
- Same text `а что дальше` leads to `ASK_GOAL` versus `PROPOSE_NEXT` solely by changing prior context with unchanged code, and dynamically inserts a new story referent. Nonsense abstains; WORLD frame rejected. EVAL_D1_POLICY/COMMIT_NOOP/DRIVE_D1_SPEECH produced on the original `C4LivingRuntime`.

## Important forensic correction and limitations
One *earlier* trial yielded 0/125 because new D1 relations were not whitelisted as LANGUAGE_CONVENTION by the strict mutation boundary: all new facts remained SOURCE_ASSERTED and were rightly unusable. This was a correct fail-closed boundary, **not proof that graph learning was impossible**. Exact scope-limited repair admitted only `DIALOGUE_POLICY_WEIGHT` and `DIALOGUE_REPLY_PATTERN` under EXTERNAL_CORPUS/TEACHER/LANGUAGE_CONVENTION (never arbitrary WORLD facts).

**D1 is NOT proof of humanlike/free Russian dialogue.** Contextual typed STORY frames are still supplied from outside; open-ended text-to-frame understanding is not taught. Response surfaces are a small finite set of teacher-provided templates, not a general decoder. Teacher data supervision is synthetically labelled by a rule rubric for *training*, while inference uses learned graph parameters. Entirely unseen speech-act operator families, multi-turn unscripted narrative, independent human raters and physical Android actions remain unproven. Do not expand the claim beyond **learned, context-sensitive, limited-domain speech-act selection**.

## Next D2 mandatory falsification
Run raw free-text `C4LivingRuntime.user_message` (no supplied typed frame), freeze independent multi-turn stories before training, learn text→frame, actual referent memory and semantic reply construction through original c4child and persist in same .c4m. Tests must withhold whole dialogue operation families and verify stranger/third-person beliefs, corrections without unrelated retractions, time, plans, initiative, hostile paraphrases and novels. Disable trained edges / permute teacher labels / code-only comparison. Unverified mass pretraining remains BLOCKED. Gemma is teacher proposing episodes only; not evidence for its own claims.

## CI gate
Native GitHub Actions workflow `.github/workflows/c4-native-constitution-gate.yml` updated to run original suite before D1, then apply exact patch, SHA-check changed modules, run `test_d1_policy_learning_ci.py`, and produce D1 native ZIP artifact. Inspect **latest workflow run conclusion**, not any earlier successful run. If new CI fails, record it as RED until fixed; D1 local evidence remains local only.
