# C4 G331 C004 — native Android host action candidate

Status: **LOCAL_AND_ANDROID_CI_CANDIDATE / PHYSICAL_DEVICE_NOT_ATTESTED**.

This iteration preserves the original 56-module c4child runtime and existing C4M. Native Python changes: `c4child/structured_cognition.py`, `c4child/runtime.py`; Android companion branch changes: `app/src/main/python/c4_mobile_bridge.py` and `MainActivity.java` in `Shabash1744444/Emu`, branch `experiments/c4-c004-native-host`.

The typed goal `SIM home BALL LOCATION floor-left → held`, an unverified demonstration `TAKE`, and `PLAN` now produce both an ordinary REPLY and a host-only `ACTION_REQUEST` event. Only allowed room objects/actions are dispatchable; this does **not** add open-ended motor planning. The host must return an actual `SANDBOX/HOME` room receipt tied to the exact pending `requestId`, native session, action, and witnessed before/after location. Receipt is evaluated as SIM only; neither source nor world truth is promoted. Duplicate receipts and stale sessions cannot earn strategy credit. After cold restart a pending request is not automatically resent. Native Java dispatch handles C4 native requests directly and never routes these through WebView `ACTION_RECEIPT` as a substitute for the private host callback.

This is experimental and does not cryptographically authenticate a compromised Java/Python process. Actual phone LIVE and background service integration remain unverified. The background service drops these native requests rather than granting credit through an untrusted UI. In-process host session identifiers are not independent epistemic roots; G215 and distinct source roots still need holistic testing.

Install only as matched pair: C004 experimental APK from `Shabash1744444/Emu` Actions on branch `experiments/c4-c004-native-host`, plus this `C4_G331_C004_NATIVE_RUNTIME.zip` installed through **System → Import runtime ZIP**, with an **existing backed-up `.c4m`**. Do not install into canonical G309. Ordinary Russian dialogue remains its old route.

Core local regression tests: 83/83 passing from C001+C002+C003+C004 (no full 633-test sweep here). Real G329 C4M 10,781 facts preserved across simulated host receipt + compact C4M cold reload. Android Actions `assembleDebug` succeeded for companion commit `0ba500e28bb406a1a6fb391ae55f233fe1249f29`, but real phone wasn't exercised.

NEXT: physical Android trial + native cognitive trace + negative replay/session tests. Do not mark C004 DONE without physically verified logs.
