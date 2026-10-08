# С4 — предварительный архитектурный контрпримерный аудит Guard V2
Дата: 2026-10-08. Относится только к исполняемому Python M1–M3 и исследовательскому состоянию; НЕ канонический C4.

### Архитектурные RED и конкретные ремонты
- EVAL Candidate имел подменяемый `scene/scope` и мог быть самодельным => EVAL registration id + полное равенство контента, scope, roots и scene исходному event.
- У зависимого event можно было передать пустые roots => запрет любой цепи без source roots.
- Инициатива могла быть подделана через публичный `receive(...,_mediated=True)` => только MEDIATE создаёт C4-origin events; публичный ingest C4 запрещён.
- COMMIT retract принимал любой текст того же actor => тот же семантический slot+scope+scene либо явный CORRECTION с родителем.
- Правило, выученное в одной симуляции, ошибочно применялось к другой => training rule теперь индексируется scene и scope.
- Непроверенное обучение могло создавать WORLD правило => запрет WORLD демонстраций через обычный учительский канал.
- MEDIATE `delivered=True` считался подтверждением доставки => вход запрещён до отдельного receipt integration.
- Любой вызов `sense(id, callback)` мог синтезировать проверенное WORLD свидетельство => только host-bound trust adapter, привязанный при создании объекта.
- `receive_gap_answer` связывал с открытым вопросом произвольный текст => несопоставимый target остаётся OPEN; не создаём false candidate.
- Хронологический запрос `as_of` терял факт, ретрагированный позднее => claim historical retracted_at и временной фильтр.
- `respond()` мог выдать другой выбранный DRIVE акт как якобы выполненный ответ => DEFERRED при иной DRIVE селекции.
- Вложенный Perspective был без бюджета; trace неограниченно рос => finite recursion budget / bounded trace.
- Примитивные malformed types могли попадать в типизированные отношения => базовая проверка str на входе.

### Неустранимое контрактами этого прототипа
- Самообучение G329/новой C4 ещё не запущено; это не доказанный general reasoning.
- Любой Python-клиент, получивший прямую ссылку на `C4`, может мутировать private attrs. Нужен отдельный process/domain boundary перед пользовательскими plugin/organs.
- Подписанный сенсорный receipt/verified action effect отсутствует. `host trusted=True` — смоделированная возможность.
- Переходы статусов gap/procedural rule должны пройти полный COMMIT audit; сейчас просто локальная ограниченная исследовательская реализация.
- База индукции из двух демонстраций не проверяет независимость source lineage двух измерений и может выучить ошибочную корреляцию. Нужны dependency groups, holdout, falsification protocol, support decay and reversible schema admission.

### Правило следующей итерации
ПРИОРИТЕТЫ: собственная causal event clock (раздельно announced_at, observed_at, known_at), enforcement capability boundary, provenance-aware learning admissions; затем абстракция и русский language organ. Не заниматься тренировкой обширного корпуса, пока типовые атаки проходят без false positives и cold reload. Вся новая способность обязана проходить held-out transfer+counterexample+post-restart; старая регрессия не заменяет реального live теста.
