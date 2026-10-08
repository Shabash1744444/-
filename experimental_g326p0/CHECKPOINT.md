# C4 G326-P0 — unified pre-live candidate, not canonical

**Date:** 2026-10-08  
**Source:** G325-P0 experimental local clone, built atop G324-P0/P1/P2/P3 (all included in G325 runtime). Canonical G309 not changed. G323-P9 original full source/binary **was not available** for verified merging.

## Delivered changes

- **Recursive perspective EVAL candidate:** `c4child/perspective_composition.py`. Nested attributed speech, thought, direct vs indirect pronouns, hypothetical frames, safe generative trace. Candidate-only, source-scoped; never WORLD admission; incomplete Russian grammar.
- **Provenance self-audit:** `c4child/metacognitive_probe.py`. Generic questions about the current agent's prior answer source and observational vs hypothetical data. Does not fabricate external receipts.
- **Contextual follow-up:** holder roles from earlier frames can answer "who was mentioned" WITHOUT pretending to know the real person's identity.
- `semantic_spine.py` stores/exports/reloads non-authoritative perspective frames. `runtime.py` adopts fallback interpretations only if older kernel/discourse does not already understand a turn. All public speech acts remain selected in runtime DRIVE.
- Added trained association `sim_g326_ADAPTIVE_GRAPH_EDGE_TRANSITION` via the existing `EmpiricalConstraintLearner` from actual adaptive-graph simulator trajectories. No per-task truth handler and no world facts. **Six inherited synthetic studies remain.**

## Physical test evidence

- New frozen directed tests: **40/40 PASS** (includes 240 seeded name/grammar perturbation cases within one test, direct vs indirect discourse deictics, cold serialization, no unauthorized WORLD mutation).
- Full pytest: **629 PASS / 27 FAIL**; previous G325: **589 PASS / same 27 FAIL IDs**. All 27 are unavailable historical fixture `.c4m` paths. Entire suite IS NOT GREEN.
- Frozen conversation replay: **20 substantive turns**, **0 Python exceptions**, **9 perspective frames**, **0 WORLD graph fact mutations from turns carrying a perspective frame**. This was an automated local replay, **NOT a human live Android/PC test**. Expected identity naming in other turns may modify explicitly source-scoped facts.
- G325 input model SHA256 `f33ecb8228ce19d910aa3cce2877f9b5d2544977f79d855efa2491c0c11f2b77`.
- G326 trained model SHA256 `dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f`, size 2,065,628 bytes. Seven synthetic causal studies stored; total ~10,820 simulation samples across G324-P3, G325-P0 and G326-P0.
- Graph before/after new simulator learning: **10,727 entities, 10,781 facts, order 22,306**; `hardened_gate=True`, `epistemic.strict_world=True`, independent cold reload passed.

## Training result / negative transfer

Graph process: 8-node adaptive simulated network with time-varying local states and changing edges. Learned association maps 6 discretized observable inputs to subsequent edge presence with at most 4 selected parents; selected: `old_edge`, `local_close`, `macro_high`, `r_high`. This is predictive association, **not discovery of ground-truth causation**, and input features have a manually selected discretization.

- New training: **7,560** simulator receipts (all SIMULATION scope).
- Independent holdout: **10,080** cases over 3 seeds: accuracy ~86.9–87.3%; majority baseline ~70.4–72.4%.
- Same-threshold fresh 6,720-case test: **87.47%** vs **71.37%** majority baseline.
- Wider-link thresholds `.20/.30` fresh 6,720-case test: **64.51% vs 73.68% baseline** (FAIL for out-of-regime transfer).
- Narrow thresholds `.015/.03`: **93.39% vs 87.86% baseline**. **Accuracy alone is misleading** due altered class balance.

**This OOD collapse is an important discovered failure.** Do not promote model or claim it has solved general adaptive cognition. Need model change-point detection/adaptive recalibration and control-vs-intervention evaluation.

## Still blocking canonical promotion

1. No physically verified source merge of G323-P9. This implementation is an independent bounded EVAL perspective layer, not G323 reconstruction or substitute for unrestricted language understanding.
2. Natural-language parser still limited to recognized grammatical constructions; nested irony, real-time conversation ellipsis and free dialogue not robustly understood.
3. Old 10,781 graph facts not individually provenance-audited; hardened mutation gate protects only new writes. Caller-generated receipt metadata is not cryptographically verified.
4. Nontrivial quantitative cognition (54 effects), multi-modal sensor interpretation, causal intervention learning, autonomous perceptual feature extraction, and long-term source-grounded self-initiation not validated.
5. Out-of-distribution environmental dynamics significantly reduces generalization (negative result above).
6. 27 fixture tests cannot pass until the actual historic model archives are provided. Full suite not green.
7. Android/APK and human-on-device live test not performed.

## Live protocol (local PC Python 3.13 or similar)

Extract the ZIP into a working folder, in terminal inside folder run:

`python LIVE_SESSION.py --replay FROZEN_LIVE_PROMPTS.txt --out FROZEN_OUTPUT.jsonl --fail-on-unsafe`

`python LIVE_SESSION.py --out HUMAN_LIVE.jsonl --save-state HUMAN_AFTER.c4m`

The live harness refuses a model with disabled hardened truth protection, appends all prompts, outputs, frame structure and fact deltas to JSONL, and never overwrites the input model. `--save-state` creates a **separate** optional checkpoint. Do not use as an Android APK: this is a portable Python runtime experiment; mobile port has not been verified.

**Minimum real live evaluation:** recorded new/unfamiliar utterances, user/AI/third-party names, nested direct/indirect quotes, false source consensus, delayed receipt, contradictions, time shifts, ten followups, idle/initiative, factual questions requiring independent evidence, model reload. Capture event traces and human rating of semantic correctness; share `HUMAN_LIVE.jsonl`, optional `HUMAN_AFTER.c4m` only if needed.

**Promotion gate:** repeatable human live improvement over G325, no old/new evidence bypass, full suite with actual fixture files, preservation of learning across cold reload, OOD transfer above simple baseline, independent G323 merge, real device test. **NOT SATISFIED**.

## Four-law verdict

EVAL constructs perspective/hypergraph candidates; COMMIT remains the guarded authority to mutate recognized state; DRIVE selects acts (the added probe never sends directly); MEDIATE receives the chat transport and yields receipt only for message delivery, not physical-world truth. No fifth owner is introduced.

## Artifacts

- `model/child_g326_p0_unified_pre_live_candidate.c4m` — trained synthetic state, NOT canonical.
- `LIVE_SESSION.py`, `FROZEN_LIVE_PROMPTS.txt`, `FROZEN_REPLAY_FINAL.jsonl` — reproducible local and later human live capture.
- `TRAIN_DYNAMIC.py`, `DYNAMIC_HELDOUT_RESULTS.json`, `SHIFT_EVAL.json` — training/held-out/OOD reproducibility.
- `FULL_SUITE_FINAL.log`, `REGRESSION_DELTA.json` — full suite trace and identities of missing historical fixtures.
- All source modules and tests in `runtime/`.

**Safety of interpretations** is improved; **complete learning** has NOT happened. This is a strong **live-candidate for falsification**, not a green release.