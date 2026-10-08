# G323 исходники: подтверждённая недоступность и безопасное продолжение

**Дата:** 2026-10-08. **Статус:** коррекция handoff после сообщения следующего чата, НЕ кодовый патч и НЕ получение бинарного пакета.

## Что проверено на GitHub

- В `Shabash1744444/-` поиск веток по `g323` не нашёл соответствующей ветки.
- В `experiments/c4-g330-device-red-cascade` путь `experimental_g323/` не существует.
- `checkpoints/CP_C4_G323_P9_RECURSIVE_PERSPECTIVE_GREEN.md` **существует**. В нём указан исполняемый код, который когда-то был в физическом sandbox: `runtime/c4child/perspective.py`, `runtime/c4child/semantic_spine.py`, `runtime/c4child/runtime.py`, два тестовых файла. Документ указывает, что архив сохранился в sandbox исходного диалога, но не подтверждает загрузку бинарников в постоянное GitHub/Library.
- `experimental_g327/README_FIRST.md` уже содержит прямое предупреждение: `No binary/source merge of G323-P9: only its checkpoint could be located, not the exact complete source artifact.`
- `experimental_g327/runtime/c4child/` на GitHub содержит **только** `discourse_bridge.py`, а не полный пакет.
- `experimental_g329/runtime/c4child/` на GitHub содержит **только** `episodic_memory.py` и `inquiry_link.py` (плюс отдельные tests и G328→G329 diff). Не путать этот видимый фрагмент с полным 55-модульным Android runtime ZIP.
- G329 `CHECKPOINT_G329_P0.md` документирует извлечение 55 модулей из runtime ZIP и cold smoke; это не означает, что ZIP сейчас существует в GitHub. Доступность ZIP надо отдельно физически проверить, не гадать по хешу.
- Другие ветки G324–G326 содержат отдельные патчи/файлы; они НЕ дают основание объявить полный G323 доступным.

## Коррекция задания для следующего чата

**Не стопориться на поиске G323, который уже обнаружено что отсутствует.** Не воссоздавать `perspective.py` по рассказам, называя это точным G323; не менять canon и G329.

Безопасные варианты работы:

A. Если у пользователя доступен исходный G323 combined ZIP в старой беседе или личной Library, физически скачать, сверить SHA256 `52574c7a6999d880855658e02b01cdefd5808ab2767bd9c0d1aaf9736064dc3b`, извлечь полный пакет **и тогда** диффовать. SHA указан в `checkpoints/CP_C4_G323_P9_RECURSIVE_PERSPECTIVE_GREEN.md`.

B. Если G323 ZIP недоступен, **начать M1–M2 как экспериментальные Python-модули с независимым типизированным API**, используя `C4_FOUR_LAWS_MATHEMATICAL_SKELETON_V01_2026-10-08.md` и имеющийся G327/G329 код/тесты как контракты. Не заявлять «переиспользовали G323»; документировать, что реконструкция имеет другой source lineage. Позднее G323 может служить независимым comparator.

C. Если доступен полный **G329 Android runtime ZIP**, предпочтительнее сначала распаковать и использовать 55 модулей как тестируемую исследовательскую базу для adaptor integration. Нельзя признать пакет физически доступным только по GitHub markdown.

## Точное исполняемое задание M1-M2 без G323

1. Новый отдельный namespace `c4core/`: immutable `Event`, `Frame`, `Claim`, `Scope`, `Receipt`; source root IDs, clocks, source events, causal parents.
2. Единый COMMIT interface для признанного состояния; EVAL hypotheses nonauthoritative; DRIVE selection authorization; MEDIATE receipt transitions.
3. **Проверяемые API:** `receive_event`, `evaluate`, `propose_commit`, `arbitrate`, `execute_boundary`, `take_cognitive_step`, `save`, `cold_load` + read-only `trace`. Реализация может быть проще production, но ни одна функция не должна возвращать декоративный успех.
4. Frozen Gate A structured cases + property tests on unseen names/scopes; cascade journaling and scope truth separation; track violations, not phrase-only expected outputs.
5. Тесты, SHA, физический checkpoint, исходные файлы и результат прямого `pytest` в экспериментальную ветку; не canon.
6. Далее сравнить с доступными G327/G329 fixtures, не ломать старый граф и не тренировать ещё массу сведений.

## Важная открытая неопределённость

Отсутствие `experimental_g323/` на указанной ветке **не доказывает**, что G323 никогда не существовал или не лежит в других доступных пользователю файловых пространствах. Есть проверенный checkpoint, но в проверенном GitHub-пути исходников нет.

**Итог:** Новый чат прав, что не стал выдавать недоступный G323 за прочитанный source. Однако само исследование не блокируется этим отсутствием; M1–M2 могут и должны быть реализованы с явной оговоркой, что G323 merge ожидает его исходный ZIP.
