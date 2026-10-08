# CP C004 — INTEGRATION CANDIDATE / DEVICE PENDING (NOT DONE)
Date: 2026-10-09.
START commit: 29722916a5ff9c5ce5db450d7c2c9f9afa2271a3.
Previous DONE: C003 at c953dcddcc26f2382945ca7da62a05294375bc3f.
Frozen RED: native SIM PLAN gave only REPLY, not ACTION_REQUEST (1 FAIL / 1 PASS).
Repair in ORIGINAL 56-module c4child: native runtime.py and structured_cognition.py.
Typed SIM home plans now issue an ACTION_REQUEST carrying exact action ID and no success claim; only whitelist room actions are dispatchable.
Android experimental companion: Shabash1744444/Emu branch experiments/c4-c004-native-host, commits 0cbed7eff269c0941da249084290895b76c99f9c and 0ba500e28bb406a1a6fb391ae55f233fe1249f29. Java dispatch calls actual room executor then private Python callback; WebView ACTION_RECEIPT cannot earn C4 SIM reward. Native session is ephemeral and never reloaded.
Android Actions run 37844344905 SUCCESS (APK assembly), but no real phone test. Python local 83/83 C001–C004 tests PASS. Existing G329 C4M: SHA256 dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f, fact count 10781 before/cold, original not overwritten, SIM achieved only after locally modeled native receipt. Incomplete broad full suite: NOT RUN in C004.
Native ZIP: SHA256 eefcd7c89706357aafc5c5bae59ce3522ccdf2619817858b48cff5f90426d641; code SHA256: runtime fbb5f7bab5c0318ecba089ee8afa6b149dce9c6f52ecfb69169142d541fff1fb; structured 289ed311509b27d26ed04d19c522f8ac00706dbb8bc5cb3690aae8073631e311.
Four owners, five influences, SOURCE/SIM/REPLAY!=WORLD, prediction!=observation, action!=verified outcome and G215 remain non-negotiable. CI training gate autonomous_pretrain BLOCKED until evidence.
C004 NOT DONE: verify matched experimental APK + ZIP physically on Android, causal host trace with request/receipt IDs, duplicate/stale/session attack and cold reload. Background service native actions intentionally blocked for safety; not yet general autonomous embodied action. C005 NOT STARTED.
On resume: read journal latest, this checkpoint, GitHub Actions latest CI and READ_ME_FIRST; do not discard G329 C4M or create parallel runtime.
