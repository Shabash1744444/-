# C004 Android host action / C4 receipt linkage — frozen audit

**Status:** C004 START / RED, NOT DONE. C003 remains last DONE.
**Date:** 2026-10-09. Native C003 baseline ZIP: SHA256 cc3fd869d9133fe9180a277d134c3c736d613c35d0e0306ee4202a0e9b430664.

## Verified causal break
- The real original C003 `C4LivingRuntime` accepts GOAL/DEMO/PLAN and stores a pending `PROPOSED_NOT_EXECUTED` action in its own cognitive state.
- Its public outbox contains only REPLY for PLAN; it does NOT dispatch a typed `ACTION_REQUEST` event to Android. This is independently reproduced in `frozen_red/test_c004_android_receipt_red.py` (1 FAIL / 1 PASS).
- Its `sim_action_receipt()` correctly refuses bare receipt input while host adapter is unbound (`SIM_HOST_NOT_BOUND`).
- In connected Android `Shabash1744444/Emu` (main), WebView's `C4RuntimeEvent` handles `ACTION_REQUEST` by calling `executeC4RoomAction()`, which invokes Java `executeRoomAction()`. Java generates actual sandbox before/after and `ACTION_RECEIPT`; WebView also forwards it using `runtimeCommand('ACTION_RECEIPT')`.
- Android's Python `app/src/main/python/c4_mobile_bridge.py` does not bind a C003 SIM receipt adapter or route verified Java location/state transitions through `C4LivingRuntime.sim_action_receipt()`; currently legacy `ACTION_RECEIPT` forwarding is not the required host-only proof for C003. Thus a C4 planned action is not connected to its causal learning loop on the actual device.

## Atomic integration contract
1. DRIVE selects proposal with exact action_id, object, context; MEDIATE may issue HOST_ACTION_REQUEST but must not treat it as completed execution.
2. Java host checks request against native pending C4 action and sandbox capability; obtain **actual** before/action/after under host ownership. Never derive verified consequence from an arbitrary JSON supplied in USER_MESSAGE or from WebView `runtimeCommand('ACTION_RECEIPT')`.
3. Private Java→Python bridge must bind C003 host adapter and translate Java receipt to C4 typed `observed_before` / `observed_after`. Match session, action_id, action, object, before/after. Reject stale and duplicate receipts, failure to persist and mismatch without advancing plan.
4. Host-origin SIM root is not independently authenticated WORLD evidence. Keep SOURCE!=WORLD, SIM!=WORLD, action!=outcome, G215 and provenance invariants. Unverified data cannot increase strategy reward.
5. Cold-restart in-flight requests cannot automatically replay physical side effects. Save exact pending state and reconcile with host.
6. Do not replace C4Graph, trained G329 .c4m, existing event lifeline or original Android app. Use a separate experimental app branch until tests.
7. Reattack different actions/scenes, replay, old session, failed native execution and contradictory native state; directed/full native tests, same .c4m cold, separate Android device proof and full checkpoint required for DONE.

## Frozen executable evidence
`PYTHONPATH=<extracted C003 native zip> python -m pytest -q experimental_g331/c004/frozen_red/test_c004_android_receipt_red.py`
Observed on unchanged C003 (test result / raw log retained by creator):
`1 failed, 1 passed in 0.12s`, failure `NO_NATIVE_HOST_ACTION_REQUEST: PLAN emitted REPLY only`.
Source SHA256 `f82c7a8c41ebfcd1081ac53136876180a7dae4b471cd1d78da2dc63e6f3ffa18`.

## Handoff
C003 DONE. C004 START saved; audit and frozen RED saved; **no Android bridge repair yet**. Next: implement end-to-end hosted native receipt path jointly across existing `Emu` and original `c4child`, then green reattack and device verification. Do not claim C004 done from this audit.
