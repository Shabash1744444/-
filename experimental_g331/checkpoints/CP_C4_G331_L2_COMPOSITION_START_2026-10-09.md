# C4 L2 — START / FROZEN RED (2026-10-09)

Base HEAD verified **26aac785d7142899061f2023fc71499165e48ff1**; L1 model sha256 **bba87b3d1b7c48f929236868c2244d05153532b4b173c8d7768783dadc6ef7ce**; L1 native runtime sha256 **c9726f5a5645716b61d2ffe07ccb80d1fea48ceab3dbd76f384abcdc6344b9cc**. Tested exact Library binaries, not GitHub surrogate weights.

### Frozen RED (before L2 implementation)
24 separate two-clause holdouts: combinations of previously trained L1 verbs and new operands, with operator surfaces `и`, `но`, `однако`. Input examples include `Маркус предпочитает мандарин и Гайя ценит мираж.`. Initial L1 read-only `C4ChildDialogue.semantic_intent` recognized **0/24** as a composite or full claim (all UNKNOWN). Complete immutable generator will be committed at `training/l2/l2_frozen_data.py`; no full sentence may appear in train lessons.

Control cohorts: original L1 runtime + L1 model; patched *same native* runtime + **untrained** L1; patched runtime + L2 *copy* trained through existing BootstrapTeacher. Check cold loading, original 10,908 facts and all original organs/state, SOURCE_ASSERTED vs WORLD, unknown connectors/forms, story/question and ambiguous segmentation fail-closed; include novel reattack and source-root dependence. Freeze any new failures rather than skip.

L2 is independent supervised language-learning track. C003 remains last full DONE, Android C004 physical room host receipt still DEVICE PENDING, C005 NOT STARTED. Constitution EVAL/COMMIT/DRIVE/MEDIATE, 5 influences and mass-autonomous-pretraining ban unchanged. No claim of fluent dialogue or new grammar generalization beyond gated tests.
