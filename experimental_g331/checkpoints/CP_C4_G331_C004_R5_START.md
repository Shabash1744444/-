# C004-R5 START — observable host result ≠ cognitive credit ≠ goal achievement
Date: 2026-10-09.
C004-R4 code green; physical Android LIVE pending; last complete C003.
Frozen RED: Android Java emits `HOST_SIM_RESULT` with room witness and c4Credit; WebView `window.C4RuntimeEvent` filters it out. Therefore UI gives no diagnostics on whether C4 accepted/denied the private SIM outcome.
Scope: companion existing Android UI (`Shabash1744444/Emu`, branch `experiments/c4-c004-native-host`). No edits to .c4m, C4 graph, policy, core, weights. Nontraining UI event only; do not treat native room `executionSuccess=true` as cognitive credit, and do not treat `SIM_SUCCESS` as goal reached without `ACHIEVED_SIM`.
Repair: explicit HOST_SIM_RESULT UI case with pure summarizer, separate roomExecuted / c4CreditAccepted / goalAchieved, diagnostics only. Add Node test for schema permutations and CI static gate; run Android Actions and save checkpoint.
Proof gate: CI compilation and test then real phone export of native/owner log; code-only partial checkpoint until physical live. Do not close C004 or start C005.
