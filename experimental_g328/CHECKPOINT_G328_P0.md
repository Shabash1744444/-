# CP G328-P0 — Real Android memory-failure repair / cognitive telemetry

Date: 2026-10-08. Status: EXPERIMENTAL, NOT CANONICAL. Parent: G327-P0 runtime on unchanged G326-trained C4M. Android host: Shabash1744444/Emu `main` 0.64.3-trace-ru. Source core separate repo: Shabash1744444/-.

## Original real-device failures from user transcript
- 20-question final memory exam on Android: C4 says `Запомнила: меня зовут Синька` despite exam-only context, gives irrelevant words (`мир`, `спрашивать`, `ответ`, Halley's salt method) instead of remembering conversation, treats fragments of test as assertions, cannot recount its participation.
- Earlier 28-question batches also produced `Запомнила: изменение ...`, `Запомнила: ... растаял; стал водой`, and unrelated lexical fragments (`буква И — гласная`, `думать — глагол`). This is source-vs-epistemic task binding failure, **not merely a small vocabulary**.
- Android shows `Cognitive Trace UNSUPPORTED` because G327 lacks `TRACE_CONFIG`/`TRACE_SNAPSHOT` methods expected by `Emu/app/src/main/python/c4_mobile_bridge.py`.

## Root-cause reading of source
- G327 `runtime.py` splits one transport event into tens of independent surfaces and calls `dialogue.say()` for each, even when they are questions about old events. This can induce irrelevant kernel retrieval and teaching state mutation.
- G327 `discourse_bridge.py` can answer limited anchored phrase patterns (`Что думает Маша?`) but not most long natural-memory questions; this isn't generalized episode graph inference.
- G327 native `trace` flag was only in PC harness, not runtime API.

## Repair included (not a universal natural-language cure)
- New `c4child/episodic_memory.py`: source-linked sentence/numbered-item segmentation and index; read-only cautious retrieval from *old* event text; past-question != past-story evidence; unknown => fail closed.
- Runtime hooks: index inbound external messages, isolate question-batch or retrospection as EVAL-only query (zero graph COMMIT), preserve unanswered inquiries, include index in persisted runtime_state and reconstruct from old G327 spine.
- Real `trace_config`/`trace_snapshot` and `TRACE_*` event delivery via actual `_record_life_event`. Instrumentation is structured/observational, not hidden unobserved thoughts. `NEXT_INTERACTION` deactivates as requested. Return is adapter-compatible using map passed from Android's `_typed_runtime_call`.
- Device host unchanged; G328 can be loaded into existing `Emu/main` via user ZIP import; no new APK required and no native device success claim made.

## Evaluations
- 13 new negative/positive regression tests for G328. Existing G327 tests remain green.
- Whole suite: 667 PASS / 27 FileNotFoundError missing old historical model fixtures, no new assertion failures relative to G327's 654 PASS / 27 fixture failures.
- Actual G326-trained / G327-compatible model controlled replay: before and after batch graph `facts=10781, entities=10727, order=22306`, delta `(0,0,0)`; 5 query episodes answered conservatively; true old text on lamp/button and Katya/Oleg found with provenance; unsupported claims not invented.
- Physical cold checkpoint saved/loaded, original learned causal studies remain unchanged; episode index round trips, `TRACE_*` events come only from observed live life_events; after one interaction tracing OFF. Android's actual `install_runtime`/`open_organism` Python contract tested via extraction, import, load, send, save/reopen.

## Security / method caveat
- Detecting a query batch by at least three questions is a protective candidate policy, not a universal symbolic grammar. All names/objects are open vocabulary: no answer-key special cases. Conceptual answers are deliberately held back when evidence isn't reliable.
- Old G327 graph may already be contaminated. G328 **does not sanitize** old graph claims. Export/backup first and use clean unchanged original G326/G327 weights for a fresh comparison; keep collected Android logs for diagnosis.
- Old outstanding ASK matching and single-turn answer generalization remain unresolved. Native sensor/action/bodies beyond runtime trace untested. No claim of full cognition, broader world training, G323 merge or canonical promotion.

## Next gate
- Real Android user confirms trace `SUPPORTED`, structured `TRACE_*` from model and separate transport log.
- Test multi-turn grounded memory, passage-retrieval distractors, open ASK none/ambiguous/earlier-question resolution, and compare graph ledger with previous live state.
- Build genuine event-centered EVAL→COMMIT→DRIVE→MEDIATE inference from reference scopes, not a new bank of hardcoded template answers.