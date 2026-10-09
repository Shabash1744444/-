# CP C4 G331 C004-R3 — CODE GREEN, DEVICE PENDING
Date: 2026-10-09. STATUS: **R3 DONE (code-only); C004 NOT DONE, Android physical live NOT ATTESTED**.

## Why this repair exists
Frozen RED on original C004-R2 native runtime: action LOOK executes successfully, but C4's earlier synthetic example incorrectly predicts a location transition floor-left -> held. The host attests unchanged observed location. Original `verified_sim_receipt` threw `SIM_OBSERVATION_CONTRADICTS_SUCCESS`, lost adverse learning signal and retained action as PROPOSED_NOT_EXECUTED. Command locally: `python -m pytest -q test_r3_red.py` -> 1 FAIL in original source.

## Implemented inside existing C4
- `experimental_g331/native_c4child/structured_cognition.py` (existing graph and .c4m unchanged).
- `experimental_g331/native_c4child/runtime.py` (native receipt bridge).
- Separate `execution_success` from `prediction_confirmed` and effective strategy outcome. Keep observed state and SIM scope; no WORLD promotion.
- Default generic SIM receipts **continue to reject** claimed success with contradictory observations. A narrowly validated host LOOK with before==after is a legitimate example of actuator success while C4's *learned effect prediction* is wrong.
- No credit from bad TAKE/PLACE destination witness, repeated receipt, wrong before-location, or mismatched native session. No automatic source trust penalty (G215).
- `tests/test_c004_r3_outcome_distinction.py` contains 9 new attacks covering alternate object, valid success, invalid TAKE/PLACE, replay, cold reload, failed execution.

## Evidence and exact artifacts
- Frozen local RED 1 FAIL (ValueError), subsequent local R3 nine targeted PASS after protecting old regression.
- First GitHub CI (broader regression) detected two true old-contract regressions; repaired without modifying older tests.
- GitHub Actions run `37877301280`, branch commit `6da1485f703247901dee1cd6490ae11439e74512`: **SUCCESS 123 PASS, 2 SKIP**; checks source SHA256 `b388140e6311b3cf2d4b2315596801fea34f536fd37330226b381cd5b71a58a5` for cognition, `209977573522203d587f5a18d448bf9f1aceb9c4368d6df884b4235b2167104b` for runtime, overlays pinned full 56-module native C4 runtime, executes tests, builds tested runtime ZIP. Mass autonomous pretraining stays BLOCKED.
- Local runtime ZIP SHA256 `fe8c3fc78ba9020a6c5078c440562d10e67f08f555e4d437f6fd55d0ee75c338`, 56 Python files, zip verification clean. Library: `/C4_Candidates/G331_NATIVE_COGNITION/C004_R3/C4_G331_C004_R3_NATIVE_RUNTIME.zip`.
- Source code and tests in GitHub branch, no alternative brain/memory, no rewrite of user C4M. Android Java project `Shabash1744444/Emu` remains experimental branch `experiments/c4-c004-native-host`.

## Open work
1. **Real phone** run paired G331 R3 ZIP and latest experimental Emu APK with backup of original .c4m, and obtain native action trace with accepted host before/action/after and cognitive result. Include unexpected prediction (LOOK), replay and stale-session cases.
2. Observe .c4m cold reload after action and verify scope remains SIM and no forged WORLD/reward.
3. Re-run historical broad corpus with previously unavailable 27 fixture models if they become available. Current CI was the specified directed+constitutional set, NOT full empirical proof.
4. Do NOT declare C004 DONE or begin C005 before physical evidence or explicitly record device blocker. Actual free-Russian, human-level dialogue and autonomous learning remain NOT PROVEN.

If interrupted: last full DONE cycle C003; C004 integrated with completed code-only R1/R2/R3, Android live outstanding. Read work journal bottom and latest branch HEAD before writing.
