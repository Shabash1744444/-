# C4 COMPLETE SKELETON — ИНТЕГРАЦИОННАЯ СПЕЦИФИКАЦИЯ v0.1
**Дата:** 2026-10-08. **Статус:** архитектура для эксперимента / НЕ исполняемое ядро / НЕ доказанная полнота AGI.
**Первичные источники:** `FOUR_LAWS_CONSTITUTION.md`; `C4_FOUR_LAWS_MATHEMATICAL_SKELETON_V01_2026-10-08.md`; `C4_COGNITIVE_LAWS_FOUR_OWNER_ATLAS_2026-10-08.md`; `C4_CAUSAL_INTERSECTION_HYPERGRAPH_54_V01_2026-10-08.md`; `C4_NEXT_CHAT_HANDOFF_G322_TO_G323_2026-10-08.md`; `01_USER_VERBATIM.md` / `03_EVIDENCE_ERRORS_AND_DECISIONS.md`.
Цель: вместо patchwork-обработчиков — **один исполняемый мир состояний**, способный принимать новые органы без нарушения закона. Спецификация должна быть полной по *местам механизмов* и *контрактам*, не по заранее выученным знаниям и не по всем возможным algorithms.

## 0. Неизменяемая конституция (4 владельца, не 4 последовательные стадии)

**EVAL:** построение конкурирующих интерпретаций/прогнозов/доказательных путей; `THOUGHT != TRUTH`. Не признаёт WORLD сам.
**COMMIT:** единственный gate признанного состояния с basis, scope, source lineage и versioned audit. Внешний чужой/симулированный рассказ допускается как факт *получения соответствующего сообщения*, не факт внешнего мира.
**DRIVE:** единственный арбитр **собственного продолжения**, включая THINK, ASK, ANSWER, WAIT, ACT, EXPLORE, REVIEW, NO_OP, REVISE. Ни входящее сообщение, ни pending ASK не могут сами выбрать действие.
**MEDIATE:** frontière execution, request/attempt/receipt/verified outcome, отдельно от самой команды; `SENT != RECEIVED != UNDERSTOOD != VERIFIED EFFECT`.

Влияния **MASK / VALUE / AVAIL / TRIGGER / STATUS**: разрешённые 4×4×5=80 **классов meta-causal подписей**, НЕ смысловые рёбра, НЕ функции, НЕ право третьего состояния. Реализация обязана логировать тип каждого перехода, не писать 80 special cases.

## 1. Общее состояние и единая жизненная линия

```text
S = (L, Q, K, G, O, A, R, C, M, T, P, B)
L: append-only life-line событий и связанных receipts; stable IDs
Q: конкурирующие гипотезы EVAL, с оценками и зависимостями
K: принятые scoped statements и их статусы; НЕ плоское truth()
G: typed semantic graph + compositional frames + procedural schemas
O: open/background/resolved/superseded questions, goals, interests
A: action proposals, decisions, pending/attempted outputs
R: transport/sensor/action receipts, verified outcomes, error states
C: contexts (speaker/recipient/witness, conversation, story, sensor, virtual world)
M: memory tiers + source-linked episodic/semantic/procedural/self/other/sensory indexes
T: monotonic step + wall time + claimed event time + partial causal order + planned deadlines
P: policies/admission criteria/learning operator versions (not learned truth)
B: resource budgets, priorities and limits
```

Ни один орган не получает writable ссылку на K/G; единственный интерфейс изменения признанного факта — **COMMIT transaction**. Эфемерные Q/C/L записи не равны принятию истины.

### Event envelope и source-lineage

```text
Event(id, origin_actor_id, addressed_to_ids, source_channel,
      payload_ref, received_at, event_time_claim, logical_step,
      causal_parent_ids, content_scope, source_root_ids, receipt_id,
      integrity_status, interpretation_status)
```

Два разных события могут иметь один evidence_root; пересказ не повышает независимость. `timestamp(received) != claimed_event_time`. Любое сообщение от Android, микрофона, камеры, игры, инструмента, синтетического мира или внутреннего цикла проходит через тот же envelope и меняет собственный канал/receipt.

## 2. Общая структура значения — рекурсивные представления

```text
Meaning ::= ATOM(type, ref)
          | FRAME(holder, speaker, recipient, actor, witness,
                  act, mode, scope, event_time, source_event,
                  target: Meaning)
          | COMPOSE(relation, [Meaning...], bindings, scope)

MeaningRef: id + type + provenance + temporal constraints
```

Типовые роли не подменяются фразой "последний говорящий".
`я/ты/он/она/они/этот` разрешаются **относительно вложенного FRAME**, в котором находится указатель. Система не обязана сразу найти одного holder: неоднозначность = несколько Q-кандидатов, нет самовольного COMMIT.
Модальности: direct_report, reported_speech, belief, doubt, plan, prediction, quote, fiction, satire/irony-candidate, hypothetical, replay, observation, remembered-event. **Это обучаемые режимы содержания, не новые конституционные владельцы.**
Рекурсивно представимы ирония на иронию, «репрезентация репрезентации», чужой рассказ о своих мыслях, свидетельство без участия. Глубина вычисления ограничена бюджетом B, не произвольным фиксированным числом 2–3.

**Самотождественность:** стабильный `SELF` как субъект внутренних решений; человеческое имя «Синька» — source-scoped социальный атрибут SELF с provenance, а не магически истинный текст. `USER`, `OTHER`, `NARRATOR`, `WITNESS`, `FICTIONAL_CHARACTER`, `SIMULATED_AGENT` изначально разные позиции.

**Пример:** «Маша думает, что Иван опоздал, но Иван пришёл вовремя»:
- `NARRATIVE(e)`
- `FRAME(holder=Masha,mode=BELIEF,target=LATE(Ivan))`
- `FRAME(holder=NARRATOR,mode=STATED_STORY_FACT,target=ON_TIME(Ivan))`
Запрос о Маше отвечает о belief; запрос о состоянии истории — о story fact; WORLD остаётся UNKNOWN.

## 3. Время и непрерывное присутствие

Четыре независимых величины: `logical_step`, `received_at`, `claimed_event_at`, `causal_precedes`. Планируемое время действия `deadline / intended_at` — атрибут цели, НЕ наблюдение исхода. История диалога — поток, не набор отдельных независимых chat rooms. Смена внешнего дня может пересчитать статусы *плана и ожидания*, но не превращает «пойду» в «сделал».
C4 вправе тратить TICK на THINK/REFLECT/REMEMBER/RETURN без входа пользователя (DRIVE решает). `WAIT` — локальное решение, а не блокировка всего организма. Часы стенда, Android, симулятора и внутренний цикл имеют отдельные source clock adapters; receipt нужен для внешней точности.

## 4. Контракт когнитивного цикла (петля, не конвейер)

```text
receive(event) -> append L, notify DRIVE/TRIGGER
evaluate(context,event) -> Q proposals with roots, frames, alternatives
schedule(DRIVE) -> choose one of eligible acts, including internal THINK
if act requires claim transition:
    COMMIT.propose(delta,basis,scope) -> ADMIT|DEFER|REJECT|REVISE with audit
if act crosses boundary:
    MEDIATE.execute(auth_id, request) -> sent/attempted/receipt/outcome
ingest(confirmed receipts) -> new event -> evaluate/commit/drive ...
reflect(old candidate / own utterance) -> Q revised, NOT new independent roots
repeat while budget/time allow; may remain silent and return later
```

EVAL не обязан перед каждым COMMIT исполняться ровно один раз; разные кандидаты могут пересматриваться. DRIVE нельзя обойти вызовом `dialogue.say()` напрямую; совместимый `user_message()` может быть только UI adapter вызова receive+ticks+publish.

### Структура `Proposal`

`Proposal(id, candidate_frame, source_event_ids, root_ids, holder, scope, time, alternatives, confidence, required_ops, justification_refs)`. Confidence — оценка, не полномочие; root не создаётся из текста модели.

### Обязательный контур итогов
`TRACE` должен содержать вход, варианты, owner transitions, selected act, **точную graph before/after delta включая изменённые факты**, referenced public event/receipt, checkpointer. Trace mode OFF/DEEP никак не меняет поведение или веса.

## 5. Механизмы как органы на общем субстрате

1. **Event/Presence:** ingestion, event identity, stream batching, clock sync, causal parent graph, replay as history only.
2. **Semantic composer:** typed entities/relations/frames, scope, nested quote, modalities, variable binding, negation and quantifiers.
3. **Epistemic COMMIT:** gate, truth scoped by world/source/story/self/sim, evidence roots, contradiction, retraction, versioned audit.
4. **EVAL inferencer:** hypothesis generation, multi-step deduction, counterfactual, causal candidate, induction and model comparison; explicit budget.
5. **DRIVE policy:** initiative/curiosity/urgency/risk/cost, scheduling internal vs external acts, active questions and background ideas.
6. **MEDIATE bridge:** tool/OS/Android/robot/game adapters, permission/boundary, receipts and verification, no action hallucination.
7. **Language organ:** morphology, syntax, deixis, anaphora, social acts, figurative speech and pragmatics as learned mappings into frames (RU first).
8. **Memory manager:** episodic, semantic, procedural, self/other, perception; content-addressed evidence; graph query, hot/warm/cold, consolidation/forgetting without authority inflation.
9. **Learner:** lexical induction, abstraction, schemas from repeated observations, counterexamples, transfer, competency confidence, optional weights updates under versioned training transaction.
10. **World models:** spatial/physical/temporal/causal predictors scoped by environment, simulator vs physical world disjoint.
11. **Multimodal binding:** audio phonemes/sound, speech, image, video, game pose, haptics; sensory raw != class label.
12. **Self-review:** re-evaluate unsent/sent own beliefs/answers; revisions audit, previous answers not new sources.
13. **Metacognitive calibration:** recognize gap, contradictory scopes, task difficulty; report only supported uncertainty; trace-readable rather than invented private monologue.
14. **Storage/SDK:** append-only event journal, disk-backed graph/index, snapshot, atomic checkpoint, cold restore, migration, trace export.
15. **Research interface:** deterministic simulation, counterexample generation, property checks, differential runs, reproducibility and agent sandbox.

Все органы получают **разрешённые API и event refs**, а не права на произвольное изменение глобального графа.

## 6. Фундаментальные неизвестные, которые не скрывать

- Объём корпуса и размер .c4m не гарантируют смысловой перенос.
- Нет заранее доказанного универсального inductive learner / language parser / AGI из этих прав; выбор операторов EVAL/обучения — исследовательский.
- Конкретные алгоритмы внимания, веса, nearest-neighbor, gradient/local rules и compression остаются заменяемыми. Нельзя заранее гарантировать «все способности» только каталогом органов.
- Реальный Android и realtime sensor/action boundary отдельно проходят MEDIATE testing; offline Python GREEN этого не подтверждает.
- Авторский «пятый закон» про решение нестандартных задач проверяется **held-out novelty + самостоятельно изменённый метод + verified outcome**, не красивыми репликами.
