# C4 G325-P0 — Hardened Common Truth Gate + Simulation-Scope Structural Learning

**Date:** 2026-10-08  
**Status:** PHYSICAL EXPERIMENTAL CANDIDATE, NOT CANONICAL, NOT G323-MERGED, NOT HUMAN LIVE GREEN.  
**Parent:** G324-P3 experimental model (G322 graph ancestry); last canonical G309.  
**Research hypothesis:** a single generic causal/learning substrate and one common graph mutation boundary can avoid many independent verbal patches while keeping source assertion, internal hypothesis and WORLD fact distinct.

## Physical changes

- `runtime/c4child/graph.py`: opt-in `hardened_gate` intercepts ALL public graph `commit`, `replace_relation`, `forget` entrances, after resolving original structural context and before any canonical mutation. External claims (USER_SAID, CORPUS, OBS, RECEIPT, etc.), including forged caller-supplied constitutional_basis and verified=True, become `SOURCE_ASSERTED` rather than WORLD facts. Unauthorized forgetting is blocked. Scoped identity naming and explicit language-convention relations retain dedicated social/linguistic scopes. Guard persists in graph checkpoint.
- `runtime/c4child/runtime.py`: opt-in `hardened_truth_gate` constructor plus `enable_hardened_truth()`, persisted runtime state and restored on cold reload. `EpistemicAdmission.strict_world` enforced in the same mode. Adds optional `max_parents` to generic `begin_causal_study` (default unchanged).
- `runtime/tests/test_g325p0_universal_truth_gate.py`: 11 adversarial source/COMMIT/bootstrap/dialogue/forget/reload/social-scope/control tests.
- `train_p4.py`: replayable **synthetic** context-switch, lagged-state and four-way-composition studies using the same P3 generic learner, no lexical hardcoding and no new world facts.
- `live_preflight.py` and `PREFLIGHT_DIALOGUE.json`: eight local dialog turns, including retained failures (no hand-tuned responses).

## Tests and measured results

- New guard: **11/11 PASS**.
- All P0/P1/P2/P3/P4 directed: **101/101 PASS**.
- Full existing + new: **589 PASS / 27 FAIL**. All 27 failing IDs identical to parent G324-P3; these require missing historical checkpoint/model fixtures. **The full suite is NOT green.**
- One initial P4 attempt introduced 6 SQLite failures (`hardened_gate` not defined in SQLiteGraph); fixed by using defensive option lookup and retested SQLite + guard: 20/20 PASS.
- One initial four-parent synthetic task failed because the public study API defaulted to 3 parents. Repaired generically with optional max_parents=4 and kept legacy default. No function-specific learner code inserted.
- Added **2,360 SIMULATION episodes** to 900 inherited P3 synthetic episodes, for 3,260 synthetic episodes total in recorded learned studies. Synthetically tested 3 held-out study families × 2 test splits × 400 examples = **2,400 held-out synthetic predictions**. See TRAINED_P4_RESULTS.json; full coverage and 100% accuracy on these limited deterministic binary functions, **not a measure of natural-language competence or real-world intelligence**.
- Original graph counts unchanged after training: 10,727 entities / 10,781 fact records / order 22,306.
- Parent P3 SHA256: `052f30fb0f79b79dad93e25ad77ad81f29ff5bc2be6981fefc85630a56f791c1`.
- G325 trained model SHA256: `f33ecb8228ce19d910aa3cce2877f9b5d2544977f79d855efa2491c0c11f2b77`; bytes `2030190`.
- Export then C4LivingRuntime.open() verified: graph hardened_gate and epistemic strict mode true, 3 new fitted studies restored and all 16 bit patterns per task reproduced.

## Known FAIL / blockers before canonical promotion

1. Actual language input parser still does not understand `Представь: Маша думает, что Иван опоздал`, and misattributes `Почему ты уверена в своём ответе?` to user perspective. Verbatim failures preserved. NO keyword-specific fixes were invented.
2. G323-P9 recursive perspective candidate exists by GitHub documentation, but original complete binary/source patch was not physically available in this working directory. This is **NOT a G323 integration**.
3. The new external gate fails CLOSED: ordinary teacher/corpus assertions remain SOURCE_ASSERTED and cannot become verified WORLD just by saying `запомни`. Proper scope-aware learned memory admission and trusted MEDIATE receipts remain necessary. This can reduce accessible knowledge in a new session; user-live quality is not proven improved.
4. Runtime cannot cryptographically validate or independently attest receipts. Caller-controlled origin/authority is still input metadata; system-level internal code could fabricate credentials. Candidate does not solve security against malicious code inside the process.
5. Existing inherited graph has historical admitted claims. The guard protects **new writes** and does not reassess 10,781 existing facts. Canonical migration still requires provenance auditing.
6. Synthetic learner detects predictive associations, not interventions or causal necessity. It does not yet learn real language features, visual grounding, adaptive-topology changes or self-initiated goals.
7. Current path still runs on G322-based runtime, not complete G323. Android/APK compatibility NOT verified.

## Clear promotion decision

**DO NOT MAKE G325-P0 CANONICAL.** Keep G309 canonical and G323 documented as separate P9 candidate. Next priorities:
- obtain actual G323 sources/artifact and merge in isolated copy with cold full tests;
- create scope-aware feature extraction from unstructured input, without target-specific surface phrases;
- provide independently controlled MEDIATE receipts and secure COMMIT admission for verified observations;
- test human live frozen dialogue and source-collusion attacks, control versus candidate, no regression;
- package verified Android runtime compatibility before mobile release.

No fifth constitutional law introduced. No claim of self-organized AGI or proof of 54 scientific effects.