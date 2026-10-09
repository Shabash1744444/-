# C004-R5 — Android HOST_SIM_RESULT diagnostic UI; CODE GREEN, device pending

Date: 2026-10-09. C004 remains NOT DONE. C003 last complete DONE.
Frozen RED: Emu Java `MainActivity.dispatchNativeC4RoomAction` emitted native `HOST_SIM_RESULT` with `room` and `c4Credit`, but WebView `window.C4RuntimeEvent` ignored event types absent from an allowlist. Thus the phone UI did not distinguish host actuator execution, C4 receipt acceptance and actual goal achievement. `buildTrainingBundle` already included native trace; issue was live visibility, not missing storage.

Implementation: in **existing Android app only**, branch `Shabash1744444/Emu@experiments/c4-c004-native-host`:
- `app/src/main/assets/index.html`: pure `c4HostSimDiagnostic(p)` summarizer and `HOST_SIM_RESULT` case render into existing `#traceLast` and `#runtimeStatus`; diagnostics only, `trainingEligible:false`. No .c4m/weights/core mutations.
- Goal achievement is shown only when room executed AND C4 receipt was accepted AND C4 status is SIM_SUCCESS AND C4 goal_status is ACHIEVED_SIM. A Java-room result alone cannot produce UI success.
- `tests/c004_host_sim_diagnostics.test.cjs`: Node VM tests for room credit/goal permutations, rejected receipt, SIM_FAILURE and OPEN, malformed event, no training lane, and Java->WebView native event path.
- `.github/workflows/build-apk.yml`: runs Node contract before compiling APK.

Verified: GitHub Actions `37887788310` SUCCESS on exact Emu commit `3b7ef023a6d687ab9b429eb6fbbf5e658e7765bb`; job logs `C004-R5 HOST_SIM_RESULT DIAGNOSTICS PASS 9 scenarios/contracts`, UI CONTRACT PASS (173 ids, 50 critical bindings), LAYOUT CONTRACT PASS (173 ids), BUILD SUCCESSFUL. APK artifact `C4-Nursery-0.64.3-trace-ru` from run; physical Android phone has NOT executed this build yet.
C4 native brain unchanged from C004-R4: C4 GitHub branch still pinning `C4_G331_C004_R4_NATIVE_RUNTIME.zip`, SHA256 `9dd72f1d5bfc57c6c1ad757503b46ec0dbde637fc4ded285e3e59c6d8173eaa3` (56 native c4child Python modules). Old G329 .c4m intact.

NEXT physical phone exam:
1. Download Emu experimental APK artifact from https://github.com/Shabash1744444/Emu/actions/runs/37887788310
2. Backup original G329 .c4m; import matched C4-R4 native runtime, start with a *copy* of existing organism.
3. In System > C4 Journal choose DECISIONS before issuing SIM/home typed goal/demo/plan commands from `experimental_g331/c004/C004_R4_PHONE_LIVE_PROTOCOL.txt`.
4. Observe native room before/after and new `SIM HOST` result with distinct executor / C4 accepted / goal achieved. Export `Выгрузить пакет для разбора`; it contains `nativeTransportTrace`, `cognitiveTrace`, diagnostic UI events, and conversation.
5. Test rejected public `@c4 RECEIPT`, replay, stale session, cold saved .c4m. Do NOT claim C004 DONE without real Android trace; no unverified WORLD promotions. If not run, stay DEVICE PENDING.

Constitution: EVAL/COMMIT/DRIVE/MEDIATE, SOURCE≠WORLD, ACTION≠VERIFIED_OUTCOME, NO G215 cascade trust penalty, no self-validating pseudo-success; mass autonomous pretrain BLOCKED, C005 not started. If hang, latest code C004-R5 finished, C004 device gate outstanding. Android code at `3b7ef023a6d687ab9b429eb6fbbf5e658e7765bb`.
