# C4 SKELETON — ГЕЙТЫ ИНТЕГРАЦИИ, АТАКИ И ПЛАН СОЗДАНИЯ
Дата: 2026-10-08. Из `04_C4_COMPLETE_SKELETON_SPEC.md`. НЕ достигнутый GREEN.

## 0. Критическая разница с предыдущей разработкой

НЕ вводить в эксплуатацию весь каталог "15 органов", заполненный пустыми заглушками. Должен сначала существовать **минимальный исполняемый когнитивный контур**, который структурно работает на всех четырёх законах. Механизмы могут быть простыми, но не фиктивными; каждый должен иметь реальные inputs/outputs, явную проверку нарушения прав и детерминированный replay.

### Пакеты (предлагаемые границы)

```text
c4core/types.py          — immutable Event/Frame/Claim/Proposal/Action/Receipt
c4core/lifeline.py       — events, causal_order, three clocks, replay
c4core/contexts.py       — nested holder/speaker/recipient/witness scopes
c4core/constitution.py   — EVAL/COMMIT/DRIVE/MEDIATE authorization
c4core/influences.py     — MASK/VALUE/AVAIL/TRIGGER/STATUS typed graph
c4core/store.py          — journal, scoped truth graph, migration, cold reload
c4core/eval.py           — candidate generation, structural scene query, reflection
c4core/drive.py          — selection with explainable reasons, action budgets
c4core/mediate.py        — boundary, transport, fake/real receipts
c4core/learning.py       — evidence-bound abstraction, transfer and correction
c4core/memory.py         — episodic/semantic/procedural/self/other retrieval
c4core/language_ru.py    — RU mapping into general frame, NOT canonical truth door
c4core/perception.py     — audio/video/virtual world event normalization
c4core/trace.py          — observational events, no cognitive mutation
c4core/runtime.py        — event loop/clock adapter, never ad hoc graph.commit
tests/...                — invariants, property and differential live replay
```

Наличие названий файлов не означает, что файлы уже написаны. Не реплицировать историческое дерево по этому списку вслепую: сверить G314–G323 существующие сильные реализации.

## 1. Test Gate A — СТРУКТУРНОЕ мышление БЕЗ русского

Формы событий подаются напрямую как типизированные объекты. Генерировать новые имена/объекты/порядки/временные интервалы:
- `story(Nina put Cube into Box)` ⇒ answer LOCATION(Cube)=Box **in STORY**, WORLD still UNKNOWN.
- `Nina says Dima saw Cube` ⇒ `said` is committed as text; Dima seeing is separate claim not observed.
- `Masha believes late(Ivan); story asserts on_time(Ivan)` ⇒ query perspective(Masha)=late; STORY fact=on_time; external WORLD unknown.
- `Ivan says Masha says Petya believes ...` depth 1/2/4/8 => correct owners, quote scopes; resource exhaustion => honest DEFER, not actor swap.
- source A ⇒ user B ⇒ C paraphrase; independent evidence roots unchanged after 1/10/100 repetitions.
- `SELF produced public answer` + `SELF re-read it 100 times` never increases independent roots.
- TIME: yesterday's plan for today + present clock advancement ≠ verified accomplished action; temporal order/causal order distinct.
- Current open C4 ASK + unrelated user message ≠ answered ASK, unrelated message can change topic; older relevant answer later may be evaluated without latest-ask monopoly.
- Contradictory statements, uncertainty and retraction: no false WORLD admission, old evidence remains historically attributable.
- ACTION: DRIVE authorized SEND, MEDIATE records SENT, but no RECEIVED⇒ no false success; verified receipt changes only correct scope.
- C4 may rerun EVAL on previous Q, revise Q and even revise unsent answer, with no new evidence roots.
- Source event actor == USER cannot be returned as `C4-origin ASK`. Empty C4 ASK ledger ⇒ honest no-ASK, not the user's exam prompt.

**Gate A pass:** generated property-based cases with typed origin/scope/IDs plus exact owner ledger. No output-string shortcuts. Check result+graph+log+post-restart.

## 2. Gate B — НАСТОЯЩЕЕ освоение языкового интерфейса

- Russian morphology, word order, pronoun changes, multiple speakers, nested direct/indirect speech: parse to same frames as Gate A, if understood.
- Multiple statements + questions in **ONE incoming message**, before any current user answer, must operate on shared scene state. User may speak 14 episodes with narratives and questions.
- New unseen names and entities; lemma variations; swapped recipient/speaker; oblique cases and negations. No hardcoded "Нина", "коробка", "камень", "стакан", "кубик", "Маша", "Синька".
- `Отлично, ты молодец` / `Молодец` / `Не за что` and typo variation should not trigger unrelated `буква Ю` knowledge; evaluate social-act handling separately from lexical facts.
- `Рысь` when not known => precise request about intended meaning rather than fake WORLD claim. Unknown surface forms may remain lexical candidates.
- User exam question "ты помнишь, какой вопрос ты задала?" retrieves only C4 ASK, NEVER USER-authored question that mentions C4.
- Nested irony, irony inside reported irony: store alternative pragmatic interpretation; do not automatically make narrator's sarcastic sentence narrator's literal worldview.
- Same ability on fresh syntax/context after teaching => acquired structure, not repetition of example.
- ASR/voice/audio/sensors as separate upstream adapters with timing, source and ambiguity.

**Gate B pass:** semantic frame F1 on train + held-out F2 with no name/phrase leakage; correct restraint on near-miss, F2 persists after cold restart.

## 3. Gate C — УЧЁБА, СОБСТВЕННОЕ ПОВЕДЕНИЕ, НЕЗАВИСИМОСТЬ

- New relational concept taught by source; store `SOURCE_ASSERTION`, transfer using learned schema to new arguments in proper scope.
- Several independent episodes permit candidate generalization; one counterexample changes its support/status via audited COMMIT, doesn't delete all independent retained knowledge.
- Near-miss: source says hypothetical animal flies; system does not assert real animals fly.
- User correction older message causes scoped revision; does not replace unrelated belief.
- Multi-turn dialogue: questions open/background, user silent, DRIVE may select alternative action, later resume topic.
- Speech -> attempted actuator -> simulator/OS receipt -> verified status; simulated result not physical-world proof.
- Sensor teacher label ≠ raw image/audio; held-out perceptual generalization.
- Runtime TRACE OFF and DEEP produce identical decisions / graph hashes / public actions / save bytes.
- Model update logged: old learner hash, training roots, data scope, new hash and rollback; no direct unlogged mutation.
- Memory consolidation preserves original evidence IDs, counterexamples and independent roots; access comparable after hot/cold spill.
- Crash/restart: live state (SELF names, actor frames, questions, provenance, pending actions) restores, no duplicate run-once effects.

**Gate C pass:** multi-day deterministic simulation + real Android/PC checks, no irreversible experiment without explicit permissions.

## 4. Gate D — УСТОЙЧИВОСТЬ И НЕСТАНДАРТНЫЕ ЗАДАЧИ

Авторский не-конституционный критерий интеллекта проверяется не обещаниями и не удачным текстом:
1. Task distribution скрыта от learner; измерена дистанция от известных решений.
2. C4 строит новый/комбинированный способ через EVAL, DRIVE выбирает пробу.
3. MEDIATE подтверждает outcome; ошибочный метод не записывается как успех.
4. Отделить exploration from exploitation, originality from random novelty.
5. При повторном предъявлении, перезапуске и новой задаче сохраняется acquired transfer.
6. Сопоставить против trivial algorithm, prompt table и иной моделью того же объёма при честно измеренных runtime/weights/working set.

Это **исследовательский тест**, не заранее доказанное качество C4.

## 5. Порядок реальной реализации (один шаг = физический checkpoint)

- **M0 — Freeze and diff:** hash canonical G309, отдельно собрать known G314–G323 и G329 artifacts. Новые файлы только в экспериментальной ветке. Сделать manifest: какой закон реально enforce какой commit path.
- **M1 — Typestate:** Event/Frame/Claim/Scope/Time/Receipt, log + persistence; 100% невозможности SOURCE → WORLD через конструктор без COMMIT.
- **M2 — Constitution enforcement:** single COMMIT guard, DRIVE authorization tokens, MEDIATE receipts, typed influences; property tests запрещённых обходов.
- **M3 — Structural episodic inferencer:** scene/query over generic typed graph; actors, nested quotes, time, open question status. Выполнить Gate A на unseen typed structures.
- **M4 — Initiative/self-reflection:** many TICK without USER event; active/background ask; learn from own error without self-evidence. Cold reload.
- **M5 — Russian language organ:** morph/syntax/pragmatics and trainable grammar-to-frame; Gate B на real held-out, no answer-key; teach one unseen construction at a time.
- **M6 — Learning protocols:** teacher/source/scenario/sensor channels, counterexample loop, abstraction operator; Gate C and near-miss.
- **M7 — Multimodal / tool adapters:** Android, game body, PC action, clocks, sound vision frame; MEDIATE receipt validation, streaming.
- **M8 — Consolidation and benchmark:** hot/cold compression, 100 virtual days game life, novelty/efficiency comparison.

После КАЖДОГО M: focused checks + ALL OLD regression + adversarial cases + cold reload + canonical untouched + SHA/runtime bytes + exact graph deltas + CLI/native trace + checkpoint doc. **Ни один PASS вместо реальной способности не засчитывать.**

## 6. Точки отказа, которые нельзя закрывать словом «неизвестно»

- Слишком консервативный COMMIT, блокирующий нормальное обучение, — FAIL POSITIVE TEACHING.
- `EVIDENCE_BOUNDED_RECALL` вместо реального ответа на локальный вопрос — FAIL SEMANTICS.
- Переспрашивание каждого незнакомого слова без переноса структуры — FAIL LEARNER.
- Рекурсия только до глубины, встречавшейся в training, — FAIL HOLD-OUT (если budget позволяет глубину).
- Возврат строки из базы без роли, времени, источника и текущего frame — FAIL ATTRIBUTION.
- Реактивная-only чат-обвязка, запрещающая THINK без нового пользователя, — FAIL INITIATIVE.
- Ошибка Android adapter, выдающая потерянные traces или неверный checkpoint, — FAIL END-TO-END.
- Отсутствующий historical checkpoint fixture — `INCOMPLETE`, а не полноценный `GREEN`.

## 7. Следующий исполняемый шаг для нового чата

Не писать новый длинный «план». Написать и сохранить **реальный M1+M2 минимальный Python пакет** в отдельной папке/ветке с полноценными pytest тестами Gate A (начальные случаи). Существующие органы G314–G323 сначала изучить: переносить их функционал через интерфейсы без silent rewrites. Не использовать авторские примеры как единственные тестовые строки; заменить именами/объектами, переставить порядок.

Прежде чем спрашивать пользователя о деталях, изучить этот пакет, вложения и точные исходники. Пользователь будет писать «продолжай»; отвечать фактическими коммитами и результатами, а не очередной теорией.
