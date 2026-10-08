# C4 G329 — Android LIVE: failure-cascade audit from attached export

**Status:** CONFIRMED LIVE FAILURES / no new C4 core repair in this report / mobile host repair separately experimental. 8 October 2026.

## Exact source
User-provided export `c4_chat_1791469053232.json`, format `C4_NURSERY_TRAINING_BUNDLE_V3`. Keep this as a research artifact, not a training corpus. Source is a system observation, not proof of world facts.

## Export context
- `runtime.state = RUNNING`, `runtimeId = null`, `buildId = null`, session `c4-1791468678191`.
- Organism sha `dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f`, size 2,065,628, labelled `IMPORTED_UNVERIFIED`.
- 27 conversation events = 12 user + 12 C4 reply + 3 C4 ASK; three C4 questions: `излучение`, `величина`, `изменение`.
- `TRACE_CONFIG: DEEP CONTINUOUS`, accepted. 46 cognitive records: 28 `TRACE_EVENT`, 10 `TRACE_EVAL`, 5 `TRACE_DRIVE`, 3 `TRACE_COMMIT`.
- Actual 51,243,387-byte transport trace was **not exported**: `nativeTransportTrace = [{error: TRACE_TOO_LARGE}]`; export only contains cognitive lane subset.
- `ORGANISM_ERROR`: G329 *clean* `.c4m` import rejected due `DIGEST_COLLISION_SIZE_MISMATCH`. No successful G329 clean-organism `ORGANISM_CHANGED` event appears. Do not claim the new clean checkpoint was used.
- Trace contains G329-style `EVAL_SOURCE_EPISODES` / `CASCADE_OUTCOME` operations, so G329 *runtime path* was running. Same model sha alone cannot identify version.

## Causal reconstruction
| external_order | inbound | EVAL_SOURCE_EPISODES | COMMIT | DRIVE | output outcome |
|---|---|---|---|---|---|
| 10 | 14 numbered points; one user message, 1,055 chars | 14 episodes | COMMIT_NOOP / BLOCKED / EXAM_OR_TRANSCRIPT_QUERY_NOT_TEACHING | EVIDENCE_BOUNDED_RECALL | 10 detected questions, only 2 matched source references, 0 new facts/entities |
| 11 | 7 numbered points; one user message, 753 chars | 7 episodes | COMMIT_NOOP / BLOCKED | EVIDENCE_BOUNDED_RECALL | 6 detected questions, 4 references, 0 new facts/entities |
| 12 | 4 numbered points; one user message, 429 chars | 4 episodes | COMMIT_NOOP / BLOCKED | EVIDENCE_BOUNDED_RECALL | 3 detected questions, 6 references, 0 new facts/entities |

**Total:** 19 recognized question spans in the three current batches; 13 publicly generated general fallbacks of `Это отдельный вопрос...`. Number of source references is not number of correct answers. There are no substantive answers for ordinary same-message reasoning such as `кто положил кубик`, `где лежал`, `что думала Нина`.

## Confirmed wrong memory attribution
At item 24, the request is to recall C4's own ASK. C4 returns a USER-authored previous exam question: `Какие вопросы ты сама мне задавала ...`. This is not a C4 ASK. The export does contain three older actual C4 ASK, but they predate the re-opened session; this export does not prove those specific ASK were present in G329's restored internal inquiry ledger. Regardless, substituting user's question violates source-role identity.

## Positive containment / negative behavior
The three `CASCADE_OUTCOME` records each show `added_fact_ids=[]`, `removed_fact_ids=[]`, `added_entity_ids=[]`, `new_transaction_ids=[]`, `inquiry_changes=[]`, graph order stays 22355. This demonstrates no observed graph fact/entity mutation during these exact batch requests, but does not prove full memory isolation for other inputs. A normal isolated self-name teaching command at external_order 9 updated graph order 22354→22355 with no added/removed IDs, a telemetry blind spot for in-place changes. Do not report order-only change as verified added fact.

## Proven bug from source
In `runtime/c4child/episodic_memory.py` `answer_batch` processes a question ONLY via `answer_memory_query` when it matches `is_memory_query`; every other question is hardcoded to the same refusal line. In `runtime.py` `_process_user_message_now` routes **any multi-question input** to that function and short-circuits ordinary semantic understanding. This architecture is effectively a lexically controlled bot for compound input, contrary to project repair law.

## Independent Android defects
1. `MainActivity` uses original file SHA as key in `organisms/store` while Python checkpoint overwrites that same path in place. Same SHA filename can therefore hold mutated contents; import encounters `DIGEST_COLLISION_SIZE_MISMATCH`. Treat digest collision as misleading filename/content inconsistency, not crypto collision.
2. `readRuntimeTrace()` returns `TRACE_TOO_LARGE` for logs > 16 MiB. This export loses all 51.2 MB transport events. The cognitive lane is present but omits causal events before it was enabled.
3. Runtime emits `event_id` while UI uses `eventId`; exported chat event IDs are null, preventing an exact direct join between chat and cognitive tracing without a normalization bridge.

## Acceptance gate for next C4 core repair
- Mix narrative statements, current-episode questions and historical memory questions in *one* message. Candidate explanations must use local scene/event/source frames, not raw lexical answer retrieval or blanket refusal.
- Positive transfer to new names/objects and shuffled question order. Questions referring to C4 ASK must only retrieve *C4-origin* ASK, not USER-origin questions about C4.
- Questions/stories/roleplays cannot silently become WORLD or SELF observations; per-span epistemic status.
- Track all four owners, candidate source event/semantic frame, graph changes including changed-fact metadata, selected public event and post-restart state.
- Compare trace OFF/DEEP and run prior word teaching/regression. No hardcoded test answers or brute threshold masking.
- Android checkout of experiment branch must build and pass physical test before declaring fixed. No new live test until offline gates are green.