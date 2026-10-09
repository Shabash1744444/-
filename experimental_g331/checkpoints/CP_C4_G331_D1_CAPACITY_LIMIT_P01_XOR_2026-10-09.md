# C4 D1 Capacity Limit — P0.1 XOR interaction (2026-10-09)

**Status:** standalone reproducible operator expressivity diagnostic. Original C4 L1/D1 .c4m files and native runtime untouched.

Real D1 narrative_policy._context_features and _fit from verified 57-module runtime (sha256 0125e17eb4e889b5de8dd4e9b4f657e89ba0e71f2c26324c4612dee975c8a52e).

Four synthetic frame configurations: two previous_reply_act × two goal values, fixed intent NEXT, mode STORY and focus. XOR target label says choose A iff the binary values differ.

- Original D1 featurizer and online perceptron: **2/4** after 400 epochs.
- Adding one generic prev_goal conjunctive feature to the SAME perceptron: **4/4** after 400 epochs.
- D1 has only additive terms for prev, goal, and each crossed with the FIXED intent. No prev×goal joint feature. Binary additive classifier cannot represent XOR, so **no training amount can reach 4/4 on this artificial XOR task**.
- This is a proof of a limit in the CURRENT D1 speech-policy readout, **not** a universal limit of C4Graph/four owners or humanlike language evidence.

Reproducible source/result/readme in artifact C4_CAPACITY_P01_XOR_2026-10-09.zip (SHA256 8a95d6e1c8577d1cd38784e9cb2141b0bdccff7692e2d77a366ce4d923661dde).
Previous P0 report+code ZIP stored in Library /C4_Candidates/G331_NATIVE_COGNITION/C4_CAPACITY_LIMIT_P0_2026_10_09/.

**Next:** native D2 trainable semantics via ordinary user_message, independent operation-family holdouts, same C4Graph provenance and cold reload; C004 Android device separately pending. No new D2 training in this checkpoint.