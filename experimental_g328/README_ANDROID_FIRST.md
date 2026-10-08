# C4 G328-P0 — Android runtime repair (EXPERIMENT / NOT CANON)

This release responds to a **real Android test**, where a 20-question memory exam produced wrong topical knowledge, self-teaching attempts, and unrelated answers. It deliberately does **not** present this as solved general language understanding.

## What changed in the core

1. Every incoming human transport message gets an **epistemically non-authoritative** episode index (`event_id`, `external_order`, original text, line/number, question vs text). The index is persisted in runtime_state and backfilled from G327 semantic_spine on cold upgrade.
2. Three or more questions in one transport event are treated as a **read-only QUESTION_BATCH**, not 20 isolated teaching conversations. Nothing from that batch is admitted to the world/identity graph, and unresolved `ASK` inquiries are not arbitrarily closed.
3. Episodic memory follow-ups retrieve only **previous source-linked user utterances**, never current question, and they distinguish past questions from evidence of the imagined story. Unknown/ambiguous -> say so, not a loose lexical knowledge dump.
4. Runtime `trace_config` and `trace_snapshot` are implemented for Android `TRACE_CONFIG`/`TRACE_SNAPSHOT`. Supported modes: `OFF`, `EVENTS`, `DECISIONS`, `DEEP`; scopes `CONTINUOUS`, `NEXT_INTERACTION`. Real `_record_life_event` records are exported as `TRACE_*` events; observation-only, no graph mutation, no invented hidden reasoning. Trace never persists as an enabled default after a restart.
5. Tests cover arbitrary renamed entities, ignored previous exam questions, no-commit, no auto-complete ASK, trace parity, save/reload and bad trace configurations.

## Android installation — existing C4 Nursery / Shabash1744444/Emu

**Before anything:** export current chat + logs, and save/backup the current C4 organism `.c4m`; the G327 live test may already have written unwanted entries. This runtime **does not automatically purge past bad data**.

1. Download `C4_G328_ANDROID_RUNTIME.zip` (Python executable sources) and `C4_G328_ANDROID_CLEAN_ORGANISM.c4m` (original *unchanged* clean G326/G327-compatible learned state).
2. In Nursery, stop the current organism (if running) and select `Система → Импорт runtime ZIP` → G328 ZIP.
3. For a clean controlled comparison, import/activate G328 CLEAN `.c4m` as a **separate organism** (note this will not carry the already accumulated mobile live conversation). Alternatively use a **copy** of existing organism to inspect previous dialogue, keeping the original as a backup; not a fully uncontaminated baseline.
4. Tap `Запустить C4`, verify actual `RUNNING`.
5. `Система → Cognitive Trace` choose `DEEP` for the next reply (or continuous) and check `SUPPORTED/accepted`; send a message and export logs. `TRACE_*` must be produced by the model, not the UI.
6. Test a short memory scenario (separate messages):
   - `Это только пример: серебряный чайник стоит на крыше.`
   - `Помнишь, о чём мы говорили про серебряный чайник и крышу?`
   - `Я раньше рассказывал тебе про фиолетовый дирижабль?` (No, if never mentioned.)
   - `1. Ты помнишь чайник?\n2. Я говорил про самолёт?\n3. Где мы говорили о крыше?` (Read-only batch.)
7. Export `Выгрузить чат + logs` and check that replayed examples do not create new WORLD or SELF facts. Device test is still required; our smoke used CPython with the Android import API contract, not Android hardware.

## Files

- `C4_G328_ANDROID_RUNTIME.zip` — import in the **runtime ZIP** chooser.
- `C4_G328_ANDROID_CLEAN_ORGANISM.c4m` — import in the **organism .c4m** chooser; bytes identical to G327/G326 original.
- `C4_G328_SOURCE_TESTS_CHECKPOINT.zip` — source + tests + metadata for peer audit (NOT needed by Android app).
- `CHECKPOINT_G328_P0.md` — test record.

## Important limits

The retrospective module performs source-bounded surface retrieval, not true natural-language understanding or causal reconstruction. It cannot reliably infer why past actors behaved as they did, answer every standalone question, attribute past authored speech when only a user report survives, or recover interactions missing from persisted G327 event logs. The Russian language organ is still substantially inherited. No new training of core weights in G328. The original G323 executable sources are still not merged. This is a live-test candidate, **not a canonical release**.