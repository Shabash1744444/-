# C4 D1 to D2 TRANSFER VERIFIED — 2026-10-09

This is a transfer/verification checkpoint, NOT new D2 training.

- Complete handoff: experimental_g331/06_NEXT_CHAT_FULL_HANDOFF_D1_D2_2026-10-09.md; covers original architecture, code paths, saved training weights, measured tests, Android physical gate, Claude/Gemma teacher and next D2 experiment.
- D1 proof portable ZIP in Library: /C4_Candidates/G331_NATIVE_COGNITION/D1_DIALOGUE_POLICY_2026_10_09/C4_D1_LEARNABILITY_PROOF_PACKAGE_20261009.zip; SHA256 e81b0385e609a963f8fe1e0734df6db670f01c237d9c5b4e038b06dbccaa0ad2.
- D1 trained target C4M SHA256 86986428afd7bd6957f57bea30596a5ccbb361647c2bf0bd29cbc6d1ddd1aa01; D1 57-module runtime SHA256 0125e17eb4e889b5de8dd4e9b4f657e89ba0e71f2c26324c4612dee975c8a52e.
- L1 source trained C4M SHA256 bba87b3d1b7c48f929236868c2244d05153532b4b173c8d7768783dadc6ef7ce.
- D1 learned 913 LANGUAGE_CONVENTION graph facts after L1; heldout with externally supplied frames 112/125 (15 distinct withheld utterances). This is not free human conversation.
- Verified physical files with SHA checks. Extracted native runtime, re-ran seven actual directed tests: 7 PASS.
- Re-ran D2 frozen eight-turn raw C4LivingRuntime.user_message: 8/8 IDENTICAL outputs L1 vs D1. D2 RED, actual free-text route not integrated with learned policy.
- Existing GitHub CI 37903537950 SUCCESS: 139 historic PASS/2 SKIP/2 XFAIL +3 D1 tests.
- C004 Android room real Java private action/credit/cold evidence still DEVICE PENDING, though human free-text LIVE was run; last full DONE C003; C005 not started.
- No mutation of original G329/L1/D1 model. Mass autonomous pretraining remains BLOCKED, source provenance and four owners preserved.

NEXT: freeze D2 RED before modifying original runtime, train a new copied model's semantic/frame induction using one C4Graph and existing four owners, compare same code + untrained baseline and ablations, novel operator-family heldouts, human audit, cold reload, SHA and journal. Do not hardcode canned responses or synthesize false WORLD evidence.
