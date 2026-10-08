# C4 G331 C002 — DONE checkpoint, 2026-10-08

Status: EXPERIMENTAL / NOT CANONICAL / NOT AGI. Based on G331 C001 branch HEAD before START `4ad2b5f922de70a77ef02deb959cdb3bf90a9e51`.

Physical START checkpoint commit: `bbfae7b0e8307cc44c37adc5ea0c74e0e81dab59`.

**Problem and first RED:** `tests/test_c002_nested_time.py` was frozen before the source edit. Original G331/C001 parsed but silently ignored supplied relative time, causing 6 FAIL / 1 PASS (past/future context contamination; missing three-time event metadata; unscoped cross-time correction, forged temporal anchors). Raw RED log included.

**Code:** changed only original `c4child/structured_cognition.py`; original `C4LivingRuntime`, `C4Graph`, `SemanticSpine`, `checkpoint.py` remain. Expanded time assertion validation, exact context guard, source-root anchor in existing graph, native spine event metadata, as-of query preserved, correction non-inheritance of unknown utterance time, strict pseudo operation fields. No new base C4M model or alternate memory.

**Methodology retained as runnable control:** versioned `governance/constitution_contract.json`, `tools/c4_stage_gate.py`; extended tests on G215 non-self-confirmation, SOURCE != WORLD, REPLAY != OBS, ACTION != OUTCOME, lineage/scopes and cold reload. Independent pretraining gate **BLOCKED** until higher-order competence proved.

**Evidence:** directed `79/79 PASS`; full available `615 PASS / 27 FAIL` (only FileNotFoundError for unavailable older C4M test fixtures); no other collected failure. Real G329 `.c4m` (SHA `dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f`), facts `10781 → 10783 → 10783` after cold `.c4m`, source day12 `cobalt`, source day13 `ivory`; no cross-perspective leakage, no WORLD promotion. Real phone Android NOT TESTED. `C4_G331_C002_NATIVE_RUNTIME.zip` SHA `b9551694410aacbf798635d4d5bcb5485d8e2bc76a2e92e0233a960063b3fc4e`, 56 py, ZIP integrity PASS.

**Known limitations:** scene time is typed and user-declared; NOT objective date parsing. Known-at is external reception order, not fully independently measured epistemic admission latency. No general Russian discourse organ trained, no proven open-ended operator induction, no genuine host-confirmed Android receipts, no isolation against malicious Python plugins, no independent institutional source identity. All unfinished acceptance gates remain explicit.

**Next C003**: systematically test a multi-step causal transfer and teacher-induced procedural learning from *independent* roots, delayed outcomes and heldout unknown combinations; build no special answer templates, insist on real native graph/weights and authenticated simulation host. Freeze RED, preserve C4M, reattack regression and cold reload; START checkpoint before mutation. Resume from GitHub 01_WORK_JOURNAL.md.
