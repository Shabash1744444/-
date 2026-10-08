# CHECKPOINT G327-P0 — Revised Source-Scoped Dialogue Runtime

**Date:** 2026-10-08. **Status:** PHYSICAL EXPERIMENT, NOT CANONICAL.
**Baseline:** G326-P0 pre-live candidate (which uses G322 line; G323 exact source not merged). Last formal canonical remains G309.

## Physical change vs baseline

- New runtime/c4child/discourse_bridge.py: source-scoped discourse query over persistent nested perspective frames; source roots and event IDs preserved; never WORLD verification.
- runtime/c4child/runtime.py: real input→EVAL→DRIVE reply integration; quote-aware segmentation; ALL detected nested/report/belief frames quarantined even when legacy parser recognizes inner content as a direct assertion; source graph query emits auditable life events.
- runtime/c4child/perspective_composition.py: interrogatives never become attributed speech (the fictitious speaker 'Кто' defect).
- runtime/c4child/semantic_spine.py: compatible version identification.
- LIVE_SESSION.py and START_WINDOWS.bat: Windows-friendly launch; --trace makes EVAL, DRIVE, other life events and transaction ledger visible. /status lists graph entities, facts and causal studies.
- New adversarial test_g327_runtime_disclosure.py and FROZEN_G327_PRELIVE.txt.

## Exact test evidence

- New G327 tests: 25/25 PASS.
- G325/G326 targeted + G327: 76/76 PASS (25 + 40 + 11).
- Full runtime test suite: **654 PASS / 27 FAIL**, 27 remaining FAIL all from missing historical fixture/model files (FileNotFoundError); whole suite is NOT green.
- Live-harness frozen replay from actual G326 model: **20 processed dialogue turns**, **0 exceptions**, **0 mutation of graph facts on recognized nested perspective events**, `--trace` records every turn.
- Saved snapshot reopened successfully with **10,727 graph entities / 10,781 graph facts / 7 learned causal studies**; prior reported belief retained and answered from saved event-frames.
- Default G327-named model weights are byte-identical to G326 weights: SHA256 **dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f**. **No new training** this iteration.
- The old G326 in comparative replay treated 'Кто думает...' as a new speaker called 'Кто' and answered source questions through generic unrelated factual retrieval; new G327 answers from the correct attributed source graph. The old G326 also added one graph fact after 'Маша думает, что Луна — сыр' while G327 kept the graph unchanged in this exact replay. This does not imply G326 installed the claim as verified WORLD truth.

## Falsification and remaining limitations

1. **NOT the actual G323-P9 source merge:** only G323 checkpoint was retrievable; do not claim restored code.
2. **Not full Russian language understanding**. `dialogue.py` and Russian morphology are largely inherited; novel complex syntax, pragmatics/irony, implicit pronouns, out-of-order speech and multimodal grounding remain limited. EVAL needs much better representation construction.
3. Experimental `discourse_bridge` only gives read-only attributed-source inference, not knowledge acquisition from arbitrary text, evidence verification, world ground-truth, or genuine semantic COMMIT updates.
4. Learning studies are synthetic and not trained from live utterances; graph-learning accuracy under threshold shift remains weak (G326 negative control 64.51% vs majority baseline 73.68%).
5. Universal truth/gate remains a research candidate; direct proof a real WORLD fact is true needs verified MEDIATE receipts, and source/receipt spoof attacks remain live-test priorities.
6. No mobile APK, GPU inference pipeline, real microphone/camera or physical game loop incorporated.
7. Graph scan for source follow-ups currently O(number of perspective frames); production indexing needed for larger conversations.

## Canonical safety

G309 canonical untouched, main GitHub branch untouched, input G326 unchanged. Never auto-promote or overwrite the source model. Any new save goes to a separately named .c4m.

## Run / reproduce

Windows: double-click `START_WINDOWS.bat` or `python LIVE_SESSION.py --trace --out HUMAN_LIVE_G327.jsonl --save-state HUMAN_AFTER_G327.c4m` in the extracted root.
Frozen live: `python LIVE_SESSION.py --replay FROZEN_G327_PRELIVE.txt --out REPLAY_G327.jsonl --trace --fail-on-unsafe`.
Tests: `cd runtime && python -m pytest -q tests/test_g327_runtime_disclosure.py tests/test_g326_perspective_integration.py tests/test_g325p0_universal_truth_gate.py`.

## Next live questions

- Send 30–100 natural multi-turn messages and attach HUMAN_LIVE_G327.jsonl to examine EVAL/DRIVE/COMMIT/MEDIATE causal traces.
- Attack chronology across events, ambiguous pronouns, nested reported quotes, speaker role changes, and false-source collusion.
- Compare real G323-P9 source once physically obtained before any merge.
- Train structural extraction from unsegmented natural utterances and test unknown grammar; do not add answer-key hardcodes.