# C4 G327-P0 — revised dialogue runtime for G326 learned state

**State: ISOLATED EXPERIMENTAL candidate; not canonical; not Android APK; not G323 full source merge.**

## What has actually changed

- `runtime/c4child/discourse_bridge.py`: one read-only query mechanism over previously heard nested/source-scoped `perspective_frames`, speaker and root references. Handles who-thinks/who-said, what-said/thought, world-proof questions, event vs receipt time and own-answer source audit. Produces **EVAL proposals**, not new world facts.
- `runtime/c4child/runtime.py`: integrates this mechanism into the real `user_message` → EVAL → DRIVE → reply path; **all** recognized attributed statements are quarantined from legacy direct teaching, even when a legacy parser recognizes the embedded noun/copula. Quote-aware surface segmentation prevents a sentence inside a citation becoming an independent top-level claim.
- `runtime/c4child/perspective_composition.py`: questions about reported claims no longer create fictional quoted speakers (e.g. `Кто` from `Кто думает, что ...?`).
- `runtime/c4child/semantic_spine.py`: version bump with backwards-compatible persistence.
- `LIVE_SESSION.py`: `--trace` captures per-turn EVAL candidates, DRIVE/other life events, provenance identifiers, transactions and learned-study availability. `/status` provides read-only model diagnostics.
- `runtime/tests/test_g327_runtime_disclosure.py`: new adversarial frozen tests, no hard-coded personal-name answer tables.

## What has NOT changed or been proven

- Learned G326 `.c4m` weights **are byte-for-byte UNCHANGED**. C4 does not suddenly know all Russian grammar, biology or physics; no new general pretraining was performed.
- No binary/source merge of G323-P9: only its checkpoint could be located, not the exact complete source artifact. G327 repairs this independently and should be compared against G323 when available.
- The old `dialogue.py` has NOT been replaced wholesale. A read-only structured conversational layer is now consulted before its fallback, and nested statements are prevented from becoming direct world-teaching operations.
- Four constitutional owners remain EVAL/COMMIT/DRIVE/MEDIATE. The recorded external messages and real receipts have not become interchangeable.
- Not tested on Android APK, live audio/video, real-world grounding or full long-form natural-language understanding. Training simulation learned studies remain synthetic.
- Full pytest is **not fully green** because historical checkpoint fixtures absent from the distribution continue to fail; compare exact names to baseline.

## Windows first run

Double-click `START_WINDOWS.bat`, or open PowerShell in this folder:

```powershell
python LIVE_SESSION.py --trace --out HUMAN_LIVE_G327.jsonl --save-state HUMAN_AFTER_G327.c4m
```

Type `/exit` to stop, `/status` to inspect loaded graph/studies, `/save` for immediate separate checkpoint. `HUMAN_LIVE_G327.jsonl` is the diagnostic file to share for human live testing. It includes original user texts; inspect before sharing.

## Frozen independent replay

```powershell
python LIVE_SESSION.py --replay FROZEN_G327_PRELIVE.txt --trace --fail-on-unsafe --out REPLAY_G327.jsonl
```

`--fail-on-unsafe` catches exceptions and unexpected graph mutation on recognized nested statements. It does not guarantee every general WORLD claim is correct.

## Tests

```powershell
cd runtime
python -m pytest -q tests/test_g327_runtime_disclosure.py tests/test_g326_perspective_integration.py tests/test_g325p0_universal_truth_gate.py
python -m pytest -q tests
```

No `pip install` is needed for the CLI itself; tests require pytest. Python 3.11+ recommended.

## File layout

`model/` includes original G326 and an identical `child_g327_runtime_compatible_weights_UNCHANGED.c4m` for provenance, plus older study checkpoints. The default launcher opens the G327-named identical file, never overwrites it. Always save post-live state to a new `.c4m` file.