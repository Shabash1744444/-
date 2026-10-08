# C4 G331 C003 — native causal-step learning and host-root feedback

**Experimental.** Changes only the original `c4child/structured_cognition.py` of G331/C002. Uses the same 56-module Android Python runtime, existing `C4LivingRuntime`, semantic graph, episodic memory and `.c4m` weights. No second engine, no replacement of user memory.

## What materially changed

- A `SIM GOAL` can specify a typed initial state as well as the target. The program finds a bounded (up to 6 steps), compositional path using typed `before -> action -> after` teacher demonstrations, rather than selecting any action that happens to match the final result. Names of objects/actions are not hardcoded.
- Each `PLAN` proposes at most one next step; a second request while a receipt is pending yields `PENDING_RECEIPT`. Planning waits for an actual host callback. A failure does not advance the current state.
- For a multi-step goal, the host must supply an action ID, an observed action, an observed before-state, an observed after-state, a receipt ID, and a provenance root; a bare `success=True` produces only `SIM_UNVERIFIED_TRANSITION`, not completion. Contradictory or duplicate receipts are rejected before mutation. This remains **SIM** evidence and **host-claimed**, not real-world truth.
- Different outcomes with the same `root_id` are not independently weighted for strategy choice. Repeated teacher examples all share `OTHER_CHAT_LINEAGE` and are never converted to independently verified knowledge. The distinct-host-root count is only a host-declared provenance proxy; it cannot authenticate the real independence of experiments.
- A staged goal's current state, proposed actions, consequence roots and status are persisted in the **existing** `runtime_state.cognitive_g331` inside the previous native `.c4m`. The underlying model's facts remain unchanged by SIM claims.

## Input experiment (one line per chat message)

```text
@c4 {"op":"GOAL","scope":"SIM","scene":"bench","initial":{"subject":"fresh","relation":"PHASE","object":"raw"},"target":{"subject":"fresh","relation":"PHASE","object":"ready"}}
@c4 {"op":"DEMO","scope":"SIM","scene":"bench","action":"fold","before":{"subject":"training","relation":"PHASE","object":"raw"},"after":{"subject":"training","relation":"PHASE","object":"shape"}}
@c4 {"op":"DEMO","scope":"SIM","scene":"bench","action":"seal","before":{"subject":"training","relation":"PHASE","object":"shape"},"after":{"subject":"training","relation":"PHASE","object":"ready"}}
@c4 {"op":"PLAN","scope":"SIM","scene":"bench"}
@c4 {"op":"REFLECT","scope":"SIM","scene":"bench"}
```

The chat may *propose* `fold`, but does NOT execute the action. To complete the example, an actual host simulator must be wired through `C4LivingRuntime.bind_sim_receipt_adapter()` and `sim_action_receipt()`. The **current Android app does not yet implement this C003 host feedback bridge**. Sending a forged receipt in text must fail.

## Evidence

- Initial frozen test: 5/5 RED on C002. One test was subsequently corrected because it expected an `action` even when a safe no-strategy refusal is valid; a source-root test was also revised to create real separate GOAL episodes rather than mutating private status directly. Original RED log is retained, and the revisions are explicit.
- Native C003 tests: 18/18 PASS, including 12 held-out three-step new-symbol tasks. Directed C003+prior: 97/97 PASS. Broad locally: **633 PASS / 27 historical missing-file FAIL** — NOT full GREEN.
- Real G329 model: 10,781 facts retained through SIM proposal, feedback, compact C4M cold reload and second step. Goal became `ACHIEVED_SIM` only after the second hosted transition. User's original model bytes unchanged.
- CI: must be independently checked after the code is committed. No claim of Android physical test.

## Known limitations

General world simulation, authenticated physical Android receipts, independent institutional provenance, rich multi-step causal deduction under uncertainty, full natural Russian understanding, true autonomous learning and learned novel reasoning operators are **not yet established**. Host assertions can be malicious or misconfigured: a callable mock is an interface test, not a physical measurement. The 4-owner constitution and pretraining gate remain in place.

C004 target: authenticated Android motor/sandbox receipt linkage and stronger independence accounting across teacher demonstrations and sensor events; follow frozen RED → repair → re-attack → native/full regression → `.c4m` cold → physical checkpoint. Keep broad-composition priority: do not turn this example into a one-off planning patch.