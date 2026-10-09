# CP_C4_G331_L1_TRAINED_ORGANISM_CODE_GREEN_2026-10-09

Date: 2026-10-09. First **actual supervised model-state training cycle** on a COPY of the native C4 G329 model. This is not C005, not mass autonomous pretraining and not proof of conversational fluency. C003 last FULL DONE; C004 actual room-actuator host-receipt device proof still pending.

## Frozen RED and source boundary
- Original source G329 `.c4m` SHA256 `dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f`, 2,065,628 bytes. Cold hydration exposes 10,789 total facts (10,781 hot from old tests plus eight cold); do not confuse cold count with an extra model.
- Native R6 parser BEFORE teaching: 0 / 48 held-out complete sentences could identify twelve selected new predicate forms. Main free-speech greeting still routed to episodic read-only; not addressed by this lexical experiment.
- Origin provenance RED: existing strict/hardened model would record EXTERNAL_CORPUS-origin language lessons as SOURCE_ASSERTED, so assistant-authored material would not become usable syntax. Never falsely label assistant synthetic examples as USER_SAID.

## Narrow generic repair, no new brain
- Exactly one-line R6 `c4child/graph.py` guard permits EXTERNAL_CORPUS + TEACHER + LANGUAGE_CONVENTION only when relation belongs to `LANGUAGE_RELATIONS`, preserves hardening of IS_A/LOCATION/world origins and MODEL self-elevation. Patch `training/l1/L1_EXTERNAL_LANGUAGE_ORIGIN.patch`.
- All learner logic remains original `BootstrapTeacher`, `C4Graph`, `RussianPredicateLexiconV1`, old 56-module C4 runtime, all four owners and five influence types. No new hardcoded sentence answers.
- Teacher dataset is **assistant-curated** `EXTERNAL_CORPUS`, ONE dependent source root `curated:assistant-teacher:c4-l1-lexical:2026-10-09`, not twelve independent confirmations. LANGUAGE_CONVENTION scopes only, no WORLD facts, no runtime-state mutation.
- 12 infinitive lexical concepts, 120 authorized teaching events, 119 newly admitted linguistic facts, 1 already present/duplicate (10,789 cold original -> 10,908 cold trained). Existing original 10,789 graph facts checked structurally unchanged by fact_id/data, original runtime_state and organs deep-equal after cold.
- 48 held-out complete Russian sentences with not-taught subject/object combinations but already-taught inflected verb surfaces: baseline **0/48**, trained **48/48**, cold reloaded **48/48**. Six unknown predicate negatives still ABSTAIN; this is **limited compositional lexical transfer**, NOT unseen-verb language acquisition.
- A direct C4LivingRuntime phone-like path on two novel utterances changed from NOT_UNDERSTOOD to parsed CLAIM, while external speaker propositions remained SOURCE_ASSERTED; multiquestion greeting unchanged and unresolved. No genuine human conversational competence claimed.
- Previously existing G329 original input hash preserved; output trained COPY is new `C4_G329_L1_LEARNED_ORGANISM_20261009.c4m`, SHA256 `bba87b3d1b7c48f929236868c2244d05153532b4b173c8d7768783dadc6ef7ce`, 2,080,308 bytes, Library `/C4_Candidates/G331_NATIVE_COGNITION/L1_SUPERVISED_LEXICAL_2026_10_09/`. Training report SHA256 `181414b72b174bff7fd92a3e55d08c29410a0f98b951bd60c258b2680fed7a30`. Reproducible script `training/l1/train_language_l1.py` and test `tests/test_c4_l1_teacher_lexicon.py`.
- Companion 56-module local patched runtime `C4_G331_C004_R6_L1_NATIVE_RUNTIME.zip` SHA256 `c9726f5a5645716b61d2ffe07ccb80d1fea48ceab3dbd76f384abcdc6344b9cc` in same Library folder; CI packs a separately zipped but source-matched runtime.

## Independent code gates
GitHub Actions `37895557084` on C4 branch **SUCCESS**: 139 PASS / 2 SKIP / 2 honest XFAIL (remaining multi-question greeting and nested perspective). Native R6 pinned original ZIP plus R6 source patches and L1 one-line origin guard, graph.py digest check `0e4eba5eb9abff5de206ec3faf58ce9d65196a18521d266f68f12eec64cc110e`; all old tests retained, 7 new tests passed. Autonomous pretrain BLOCKED. Uploaded CI artifact `C4-G331-C004-R6-L1-TESTED-RUNTIME`. Native 56-module ABI intact.
Read on next chat: this checkpoint, last Work Journal, C004-R6 real-life diagnosis. No C005 and no claims of finished natural-language dialogue.

## Next actual learning horizon
(1) Hold out entirely unseen lexical/construction classes; (2) train clause/perspective/temporal **composition** rather than word-table-only association, inside .c4m with stable provenance and no self-grading; (3) use outside teacher (Claude or other transformer) only to propose lessons, require independent valid supervised labels, heldout no-copy tests, counterexamples; (4) finish C004 real Android action/live-cold gate. No broad self-training without those checks.
