# C4 G326-P0: start here

Status: isolated candidate, **not canonical**, not a verified G323 merge, not Android APK. The legacy world-state graph is preserved, and new learned weights are synthetic.

Run in folder after ZIP extraction (requires Python 3.11+):

```bash
python LIVE_SESSION.py --replay FROZEN_LIVE_PROMPTS.txt --out PRELIVE.jsonl --fail-on-unsafe
python LIVE_SESSION.py --out HUMAN_LIVE.jsonl --save-state HUMAN_AFTER.c4m
```

The second starts a text chat. Write `/exit` to finish; `HUMAN_LIVE.jsonl` contains input, output, parsed structure, source/frame IDs and graph fact count changes. `--save-state` saves a NEW model snapshot, never overwrites the input .c4m.

For tests (requires pytest):

```bash
cd runtime
python -m pytest -q tests/test_g326_perspective_integration.py
```

Full regression presently has 27 expected `FileNotFoundError` failures for earlier checkpoint fixtures not shipped here. See `CHECKPOINT_G326_P0.md` for blockers, honest test outcomes and hashes.

Read-only simulator learned dynamical process; do not use it as external WORLD evidence. For a live test, share `HUMAN_LIVE.jsonl`; don't treat generated responses as independently confirmed real-world facts.