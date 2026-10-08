# C4 G331 C004 START — Android host action / C4 credit trust boundary
Date: 2026-10-09. Status: START ONLY, not DONE.
Base branch HEAD: c953dcddcc26f2382945ca7da62a05294375bc3f
Previous verified C003: latest journal DONE, 97 directed PASS, 633 broad PASS / 27 unavailable historic fixtures; GitHub Actions run 37836471938 success.
Task: audit and connect actual native C4 ACTION_REQUEST -> Android room actuation -> Java host-generated receipts -> original C4LivingRuntime.sim_action_receipt, excluding JS/USER_MESSAGE receipt forgery and cross-session or replayed receipt.
Frozen initial RED hypotheses:
- Existing c4_mobile_bridge.py lacks SIM host-bound action receipt ABI.
- Existing C4 PLAN emits REPLY/proposal rather than an executable ACTION_REQUEST outbox for the app.
- Android JS currently sends ACTION_RECEIPT via runtimeCommand exposed to the UI; this is not an independently authenticated host-to-core gate.
- Room action receipt describes room object locations etc., whereas cognitive SIM receipt requires typed observed_before/after + matching pending action ID; blind conversion is unsafe.
Do not downgrade host-origin trust, SIM to WORLD, action proposal to execution. No new memory or model, do not change user C4M. Preserve existing C4Graph, C4LivingRuntime and Android event ABI.
Workflow: freeze RED test; enforce host callback ABI that cannot be triggered by user text; action and session binding; independent Java observation before/after; defensive no-result state for unsupported actions; reattack, regression and cold C4M; CI and physical checkpoint. Physical device Android not yet attested.
If interrupted: C003 remains latest DONE. Continue C004 only after consulting this START and current branch HEAD. Never report Android live PASS without a device log.
