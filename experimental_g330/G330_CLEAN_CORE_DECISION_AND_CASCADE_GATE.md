# G330 — решение о чистом когнитивном контуре и каскадный контракт

**Дата:** 2026-10-08. **Статус:** решение/проектный контракт, НЕ реализованный рантайм, НЕ канон, НЕ GREEN.
**Основание:** физически выгруженный G329 Android лайф `c4_chat_1791470574930.json`, предыдущий `c4_chat_1791469053232.json`; `experimental_g330/G329_REAL_DEVICE_CAUSAL_AUDIT.md`; `experimental_g330/tests/test_g330_real_device_red.py`; `FOUR_LAWS_CONSTITUTION.md`; `DEVELOPMENTAL_TRAINING_METHODOLOGY.md` и `RUNTIME_ARCHITECTURE_PRINCIPLES.md`. 

## Решение

**Пересобрать связку понимание события → рассуждение над событиями → арбитраж действия как отдельный C4 Clean Core.** 
НЕ перезаписывать канон и НЕ уничтожать G329. Физическая база G329 — 2,065,628 байт compact C4M; `graph_hot.json` содержит 10,727 entities, 10,781 facts; `runtime_state.json` содержит 7 causal_studies. Это накопленное содержание и история, не доказательство дееспособного общего семантического парсера. На этапе архитектурного тестирования использовать **новое пустое состояние**, сохраняя исходные .c4m и обученный корпус read-only как отдельный benchmark; после GREEN переносить только прошедшие реконструкцию и provenance-проверку данные.

Сохранить концептуальные **права владельцев**, графовую модель, provenance/lineage/source scopes, журналы, receipt-переходы, C4M и Android-мост как контракты; реализацию каждого механизма проверять и при необходимости заменять. Не наследовать автоматически старый `dialogue.say()` / `answer_batch()` / `dialogue_focus` как общую физику интеллекта. Редиректы по заранее заданным фразам и жёсткие fallback для вопросов — RED.

## Три независимо подтверждённых фальсификатора

G329 archive independent offline run: `3 failed in 0.23s`, reproduces already-committed RED tests on the packed 55-module runtime:
1. `Ира унесла большой камень к мосту.` + `Кто унес камень?`: returns generic refusal rather than evaluating the same-message scene.
2. `Сева поставил стакан на полку.` + `Где находится стакан в этом рассказе?`: same.
3. Prior **USER** utterance `Какие вопросы ты сама задавала?` retrieved as evidence of **C4's own ASK**. Source-role mismatch.

Это FAIL смысла и происхождения, не просто недостаток словаря. Кандидат может иметь маленький словарь, но если вход представлен уже как корректная структурированная сцена, обязан дать поддержанный вывод либо точное неведение.

## Универсальный новый путь — no answer-key

0. **INGEST** event envelope: `event_id, origin actor, addressed_to, channel, received_time, claimed_event_time, causal_parents, raw_text, source/receipt`. Приём события не даёт внешнего доказательства его содержания.
1. **PARSE/EVAL**: атомизировать не только вопросы, но и утверждения, цитаты, желания, планы, социальные акты, ошибки/правки; выдать **альтернативные** типизированные `SCENE_FRAME` с `holder, speaker, listener, actor, patient, predicate, object, time, modality, source, scope`. Если слова неизвестны, оставить unknown lexical spans; не подменять случайным контекстным фактом.
2. **CURRENT EPISODE WORKSPACE**: сцены и вопросы в одном сообщении живут совместно. Истории могут служить допущениями **только в NARRATIVE/SIMULATION**. Новый вопрос имеет ссылки на локальную сцену и на внешние прошлые события отдельно.
3. **EVAL**: запрос строит цели извлечения (WHO/WHAT/WHERE/WHY/WHEN/SOURCE/PERSPECTIVE и т.д.) из типизированной структуры. Вывод в рамках сцены не требует признания WORLD-факта и не создаёт нового независимого evidence root. Неизвестное → адресное уточнение, а не blanket refusal.
4. **COMMIT**: transaction type явно `USER_UTTERANCE`, `NARRATIVE_ASSUMPTION`, `SOURCE_ASSERTION`, `SELF_REPORTED`, `SENSORY_RECEIPT`, `WORLD_ADMISSION`, `LEARNED_FORM`. Никакое цитирование, пересказ, экзамен или самоповтор не делает независимое свидетельство. Каждое разрешённое изменение имеет точные before/after IDs и basis.
5. **DRIVE**: только DRIVE выбирает `ANSWER | ASK | THINK | WAIT | SHIFT_TOPIC | NO_OP | ...` из кандидатов с критериями цели/уместности/ресурса/неопределённости. `UNKNOWN` не означает ни `ANSWER`, ни `FLOOR` автоматически. Не путать backchannel («Спасибо», «Не за что»), тему и обучение.
6. **MEDIATE**: речь/действие/попытка/receipt/result/verification различаются. Каждому публичному ответу сопоставимы использованные event/frame IDs. Ответные реплики индексируются как собственные REPLY, ASK как собственные ASK; чужой вопрос о C4 не является C4 ASK.
7. **REFLECT**: повторное EVAL на собственной версии решения без прироста независимых источников; поправка статуса только через COMMIT. Замыкать на следующем цикле, учитывая новое время, новую реплику и real receipt.
8. **TRACE**: регистрация события read-only; сравнить OFF vs DEEP (ответы, graph hash, DRIVE choices, inquiry statuses и checkpoint bytes). Полный причинный граф: `inbound → hypotheses → chosen frame(s) → basis IDs → COMMIT delta → DRIVE candidate set + selection → MEDIATE public event → subsequent memory/reload`.

Здесь четыре закона — **четыре полномочия, не четыре такта конвейера**. Все MASK/VALUE/AVAIL/TRIGGER/STATUS сохраняются общим словарём типизированного влияния; они НЕ 80 жёстких обработчиков и НЕ готовые ответы.

## Независимые проверки / критерий допуска к обучению

**Gate A — structured (без русского парсера):**
- Typed `said(Nina,Dima,location(cube,box))` в `NARRATIVE` ⇒ query WHERE returns box **as in story**, not WORLD truth; query WHO_SAW returns unknown.
- Nested quote and mistaken belief resolve against local holder/speaker, with SELF != OTHER.
- Plan at t0 != verified action at t1; clock time != dialogue order != story-time.
- N incoming copies of one source keep one evidence root.
- Old ASK vs new ASK vs USER question; no arbitrary last-ASK pointer; ambiguity preserved.
- EVAL→COMMIT→DRIVE→MEDIATE trace complete, graph hash and output same OFF/DEEP; successful cold restart.

**Gate B — language organ (Russian):**
- Same scenes via natural Russian text with unseen substitutions of people/objects, word order and inflection.
- Mixed statements+questions in ONE message as well as separate-turn stories; learned language patterns transfer to held-out expressions.
- Unknown words => scoped lexical candidate + context-dependent ASK, not fixed "запомни: ..." demand.
- Social acts, typos and non-question replies do not create wrong active focus or trigger unrelated retrieval.
- No hardcoding old RED strings, names, benchmark-specific semantic replacements or special-case output templates.

**Gate C — learning and cascades:**
- Existing positive one-word teaching and lawful source-claim admission still work; no blanket prevention.
- Same info received as hypothetical story must NOT enter WORLD/SELF. Later corrections re-evaluate with audit instead of deleting history.
- Normal C4 initiative and on-device checkpoint restore continue.
- Full old regression plus new randomized/held-out tests; frozen RED repro must turn GREEN **for semantic reasons** not absence of refusal substring.
- Android import failure `DIGEST_COLLISION_SIZE_MISMATCH` and large trace export limitation are **separate host bugs**; host version must be verified separately before device gate.

## Release decision

Keep `G329` benchmark frozen. Work only in `experiments/c4-g330-device-red-cascade` or child branch. No new human live exam until Gates A, B, C, full regression and clean cold import pass. Do not call this document a fix; new runtime and new baseline C4M do not exist until tests and hashes are physically produced.

**Promotion evidence:** updated source + frozen/new differential results + graph delta evidence + causal trace sample + cold C4M reopen + exact runtime ZIP SHA/bytes + Android device test + audit checkpoint. Canonical path unchanged until then.
