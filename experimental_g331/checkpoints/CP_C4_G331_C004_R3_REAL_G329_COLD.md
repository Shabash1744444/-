# CP C4 G331 C004-R3 — REAL G329 ORGANISM COLD RELOAD
Date: 2026-10-09. R3 CODE GREEN, C004 DEVICE PENDING.

## Exact original organism integrity
Original Library: /C4_Candidates/G329_CAUSAL_CASCADE_PRELIVE/C4_G329_ANDROID_CLEAN_ORGANISM.c4m
SHA256 before and after test: `dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f`.
Real G329 cold loaded through native `load_c4m_compact`: **10,781 facts**, runtime step 986.
Structured goal in SIM/home: BALL LOCATION floor-left -> held. Synthetic teacher mistakenly says LOOK changes location floor-left -> held. PLAN generated LOOK; host-style private native witness reported successful LOOK with unchanged object location floor-left. No WORLD/OBSERVATION promotion.

**Observed:** receipt accepted, action SIM_FAILURE (strategy prediction disproven, despite execution_success True), goal OPEN, prediction_confirmed False; graph stayed 10,781 facts.
Saved via `save_c4m_compact` to a **temporary copy**, cold reloaded, graph still 10,781; action SIM_FAILURE and prediction_confirmed False remain; `_native_room_session is None`, preventing old session re-use. Original organism SHA unchanged.
This is a locally constructed host-style input **not a physical Android device witness**. Does not close C004.

## Regression
C4 CI Actions `37877301280` SUCCESS 123 PASS / 2 SKIP (directed+constitutional; NOT historical full-suite). R3 tested 9 new local cases and preserved frozen contradictory TAKE/PLACE tests.
Source branch `experiments/c4-g331-native-cognition`, R3 code integration `6da1485f703247901dee1cd6490ae11439e74512`; native ZIP `C4_G331_C004_R3_NATIVE_RUNTIME.zip` 56 original c4child modules SHA256 `fe8c3fc78ba9020a6c5078c440562d10e67f08f555e4d437f6fd55d0ee75c338`.
Library archive: `/C4_Candidates/G331_NATIVE_COGNITION/C004_R3/C4_G331_C004_R3_NATIVE_RUNTIME.zip`.
Next: physical Android ACTION_REQUEST -> Java before/after -> private Python receipt -> decision trace -> cold C4M on device, plus stale/forged/replay negatives. Do not claim DONE before device trace.
