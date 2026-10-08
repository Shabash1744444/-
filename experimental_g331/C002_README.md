# C4 G331 C002 — native nested-temporal perspective correction

**Status: EXPERIMENTAL, not canonical and not AGI.** This is the same `c4child` organism and Android import interface as C001/G329: 56 Python modules. Load the existing backed-up `.c4m`; do not install C4 LIFE v1 or replace trained weights.

## What changed

- `c4child/structured_cognition.py` now validates `time` instead of silently discarding it. `REPORT`/`CORRECT` may have `utterance_day` and a typed `about` anchor (`UTTERANCE` offset or previously recorded `SOURCE_CONTENT` with `event_id`). `QUERY` may have `time: {"about_day": N}`.
- These are *speaker-claimed scene time coordinates* and never trusted clocks. The native `SemanticSpine` captures its own `external_order`, `wall_time`, and `known_turn`, separately from the claimed date. The event retains source/provenance and exact nested perspective. No second memory was created.
- The same `C4Graph` stores existing source claims. A query may filter source evidence by represented day without declaring it WORLD truth.
- Untrusted temporal anchors in another scope/scene/perspective, forged event IDs, malformed clocks and unrecognized JSON fields are rejected before any graph admission. Cross-time CORRECT may not overwrite a different historical event; a correction that omitted utterance time does **not** fabricate it.
- `governance/constitution_contract.json`, `tools/c4_stage_gate.py`, `tests/test_c002_foundational_gate.py`, `tests/test_c002_training_gate.py` are durable engineering requirements, not a claim of complete human cognition. Autonomous massive pretraining is still **blocked** until independently evidenced acceptance gates pass.

## Phone installation

1. Back up existing `.c4m`; stop C4 Nursery organism.
2. In **Система → Импорт runtime ZIP** load `C4_G331_C002_NATIVE_RUNTIME.zip`.
3. In **Организм** select your original `.c4m`; start C4.
4. In the chat send **one** `@c4 {...}` pseudo message per turn; trace + export native logs. Original Russian branch is preserved but does not learn unrestricted language from this update.
5. To revert install C001/G329 runtime ZIP and restore the backed-up `.c4m`.

## Example: nested reported future versus utterance day

```text
@c4 {"op":"REPORT","scope":"STORY","scene":"volume3","frames":[{"actor":"Nadia","mode":"BELIEF"},{"actor":"Anton","mode":"QUOTE"}],"fact":{"subject":"parcel","relation":"STATE","object":"sealed"},"time":{"utterance_day":18,"about":{"basis":"UTTERANCE","offset_days":2}}}
@c4 {"op":"QUERY","scope":"STORY","scene":"volume3","frames":[{"actor":"Nadia","mode":"BELIEF"},{"actor":"Anton","mode":"QUOTE"}],"fact":{"subject":"parcel","relation":"STATE","object":"?"},"time":{"about_day":20}}
@c4 {"op":"QUERY","scope":"STORY","scene":"volume3","frames":[{"actor":"Nadia","mode":"BELIEF"},{"actor":"Anton","mode":"QUOTE"}],"fact":{"subject":"parcel","relation":"STATE","object":"?"},"time":{"about_day":18}}
```

Expected: first query yields a **SOURCE_REPORTED** `sealed` only for story day 20; second query **UNKNOWN** at day 18. Query with different `frames` and no quotation frame returns UNKNOWN. No WORLD truth added.

**Important:** this test supplies semantic roles and synthetic scene-day values; it does not prove C4 can parse a Russian narrative. Actual Android device LIVE has not been performed.

## Reproduce tests

From unpacked **handoff source** with `PYTHONPATH=.` in `runtime`:

```bash
python -m pytest -q tests/test_c002_nested_time.py tests/test_c002_foundational_gate.py tests/test_c002_training_gate.py tests/test_c001_temporal_dialogue.py tests/test_g331_real_organism.py
python -m pytest -q tests
python tools/c4_stage_gate.py --request autonomous_pretrain
```

The last command must return **BLOCKED** (exit 2) at current maturity. C002 local results: `79 directed PASS`; broad `615 PASS / 27 FAIL`, all 27 missing historical fixture paths. Real original G329 C4M `10,781 → 10,783 → 10,783` facts through cold reload; same SHA of original binary. Detailed evidence in handoff ZIP.
