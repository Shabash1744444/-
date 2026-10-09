# C4 D1 — real graph-backed dialogue-policy trainability experiment
**Date:** 2026-10-09. **Status:** PARTIAL LEARNABILITY DEMONSTRATED / HUMAN CONVERSATION NOT PROVEN.  C4 ≠ Singularity OS.

## Start + exact binary evidence
- GitHub C4 branch: `experiments/c4-g331-native-cognition`. Original L1 native C4 organism `C4_G329_L1_LEARNED_ORGANISM_20261009.c4m`, SHA256 `bba87b3d1b7c48f929236868c2244d05153532b4b173c8d7768783dadc6ef7ce`, 2,080,308 bytes, 10,908 facts.
- Original unchanged L1 56-module runtime ZIP SHA256 `c9726f5a5645716b61d2ffe07ccb80d1fea48ceab3dbd76f384abcdc6344b9cc`.
- D1 new trained COPY `.c4m`: `C4_G329_D1_DIALOGUE_POLICY_20261009.c4m`, SHA256 `86986428afd7bd6957f57bea30596a5ccbb361647c2bf0bd29cbc6d1ddd1aa01`, 2,212,190 bytes, 11,821 facts. Input unchanged; 913 new *LANGUAGE_CONVENTION* policy facts (single dependent teacher root).
- Same native C4 runtime with one added organ `c4child/narrative_policy.py`, small additions to original `runtime.py` and `scope.py`, **57 Python modules**. Packaged `C4_G331_R6_L1_D1_NATIVE_RUNTIME.zip`, SHA256 `0125e17eb4e889b5de8dd4e9b4f657e89ba0e71f2c26324c4612dee975c8a52e`. Original 56 modules retained.
- These final binaries and reproducibility artifacts stored in Library `/C4_Candidates/G331_NATIVE_COGNITION/D1_DIALOGUE_POLICY_2026_10_09/`.

## What actually learned
One deterministic multiclass online perceptron learns two *different* mappings within the **existing `C4Graph`**: Russian surface n-gram → user speech-intent; and (intent + typed STORY context + previous C4 act + narrative goal + focus) → selected C4 speech-act. Feature/action weights and surface patterns are persisted as C4 native `LANGUAGE_CONVENTION` facts through existing `BootstrapTeacher` and survive cold `.c4m` reload. No `if surface == phrase` response lookup exists in inference, and no secondary graph/core/memory is created. Synthetic teacher labels originate in one EXTERNAL_CORPUS dependent root; they never prove facts about WORLD.

`C4LivingRuntime.learned_narrative_turn(text, frame)` is an **explicitly experimental method of the same C4LivingRuntime**, not a replacement for ordinary `user_message`. It emits EVAL/COMMIT_NOOP/DRIVE life events and appends a spoken reply to the existing conversation history. It refuses WORLD frames. A caller must provide typed STORY context (`focus`, `place`, `goal`, `previous_reply_act`, etc). Frame grounding from arbitrary Russian messages IS NOT LEARNED OR PROVEN. A few taught phrase patterns render responses with dynamic entity slots; arbitrary novel grammar generation not shown.

## Frozen benchmark (synthetic; no human judges)
Training: 256 labelled scene/message episodes (only 30 distinct training utterance texts repeated in different contexts). Heldout: 125 scenario turns **using only 15 distinct withheld utterance texts**; unseen object/place names and shuffled scenario contexts. This is not 125 independent language expressions. `frozen_d1_cases.json` immutable input sha256 `26f1e35b286045b394088136f9184bbe99389257bedb4f8c9fd7dfcaff5f6e71`.

- Same new code + original L1 untrained `.c4m`: 0/125.
- Newly trained D1 `.c4m`: 112/125. Cold reload: 112/125.
- Permute reply labels in lessons, without changing runtime: 0/125.
- Repeat with three training shuffle seeds, same fixed test: **112/125, 102/125, 111/125**. Not independent splits of the test corpus.
- Learning curve over episode count (16,32,64,128,256): **21,96,101,113,112** /125, respectively; training wall-clock seconds measured in full JSON (Python-only training operations, excludes I/O, loading, Android and teacher generation).
- 4 directed safety/feasibility tests passed locally (see `test_d1_native.py`). Original L1 facts structurally identical; all 913 new facts admitted only to `LANGUAGE_CONVENTION`, shared source root, no WORLD promotion. Nonsense input abstains, WORLD frame rejected. Same exact input text with different previous C4 speech-acts leads to different learned follow-ups and novel object labels are inserted.
- Initial exploratory pass yielded 0/125 because new policy weight relations were mistakenly excluded from the strict `LANGUAGE_RELATIONS` gate. Repaired by admitting only `DIALOGUE_POLICY_WEIGHT` and `DIALOGUE_REPLY_PATTERN` under TEACHER/EXTERNAL_CORPUS/LANGUAGE_CONVENTION, NOT arbitrary knowledge. Retained failed attempt in history, not mislabeled as architectural impossibility.

## What this does NOT prove
1. Human-like dialogue, agency, free conversation, semantic understanding of arbitrary Russian, open-ended grammatical composition, causal planning, unseen speech-act classes, emotional/narrative creativity, free turn-taking, or conversation across many topics.
2. The synthetic rubric used *hardcoded labels* to **generate training supervision** (not hardcoded inference). Limited taught Russian response patterns still yield templated replies, not learned unconstrained generation. The model currently depends on externally supplied semantic frames.
3. No independent person assessed the 125 labels, and test phrases are only 15 unique utterances. The benchmark may heavily overestimate real dialogic competence.
4. These 4 directed tests are NOT the old 139-case GitHub CI suite; the previous C004 Android host physical action-credit-cold proof remains DEVICE PENDING. Last FULL DONE C003, C005 not started.

## Next decisively falsifiable D2: no externally supplied semantic frame
Integrate natural-language semantic/frame induction **inside original C4** as trainable operators. Freeze multi-turn narratives where **user_message(text)**, not a structured oracle or a separate experimental entrypoint, must extract perspective, referents and scene changes, choose acts and construct semantic response content. No teacher-generated STORY fact may become WORLD; unknown/ambiguous → clarification. Compare new native runtime with old L1 vs trained `.c4m` *using the same code*, no phrase-specific hand-coded answers. Withhold *entire dialogue operation families*, not just texts; novel history dependencies; train on synthetic + externally audited labels and an independent human evaluation of >100 **different** utterances. **D1 does not settle whether C4 should replace a language model; until D2 passes, Singularity OS component remains an option, not a forced conclusion.**

## Files / continuation
Read this file, `narrative_policy.py`, `D1_NATIVE_DELTA.patch`, `d1_experiment.py`, `frozen_d1_cases.json`, `test_d1_native.py`, `D1_REPORT.json`, `D1_MULTISEED.json`. Use original immutable L1 and create a **copy** for D2; preserve weights, source provenance, four owners and five influence classes. Actual `.c4m` is in Library; GitHub contains source/tests/checkpoint only if successfully committed. Never claim new trained model without hash/cold evidence.