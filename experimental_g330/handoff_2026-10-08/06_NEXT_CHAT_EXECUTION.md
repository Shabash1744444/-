> **G323 source blocker (verified 2026-10-08):** See [07_G323_SOURCE_BLOCKER_AND_RECOVERY.md](07_G323_SOURCE_BLOCKER_AND_RECOVERY.md). Full G323 sources NOT present under checked repo path; do not require them to implement experimental M1–M2. Do not claim missing sources are merged.

# ПЕРЕДАЧА СЛЕДУЮЩЕМУ ЧАТУ — C4, 2026-10-08
## Зачем читать
Пользователь попросил сохранить его идеи и доступную беседу на GitHub и собрать скелет когнитивной системы, прежде чем чат закончится. Эта задача находится в **том же самом чате**, не выдумывай «другой чат». C4 ≠ Singularity OS.

**Репозиторий:** `Shabash1744444/-`
**Ветка:** `experiments/c4-g330-device-red-cascade`
**Папка:** `experimental_g330/handoff_2026-10-08/`

## В обязательном порядке прочитать

1. `01_USER_VERBATIM.md` — дословные авторские сообщения, не корректировать орфографию и не вытеснять авторский голос.
2. `02_CHAT_DECISION_TIMELINE.md` — хронология, разногласия, ошибки ассистента, что было предложено.
3. `03_EVIDENCE_ERRORS_AND_DECISIONS.md` — почему старая система не выполняла замысел, доказательства и честные границы вывода.
4. `04_C4_COMPLETE_SKELETON_SPEC.md` — проект единого типизированного C4 core: 4 закона, 80 meta signatures, SELF/OTHER, perspectives, three clocks, provenance, thought/action cycles, all organs.
5. `05_ACCEPTANCE_AND_BUILD_PLAN.md` — M0–M8, property/integration tests и следующий практический шаг.

Далее обязательно читать в корне:
- `FOUR_LAWS_CONSTITUTION.md`, `TRAINING_LAWS.md`.
- `C4_FOUR_LAWS_MATHEMATICAL_SKELETON_V01_2026-10-08.md`.
- `C4_FIFTH_LAW_INTELLIGENCE_NON_CONSTITUTIONAL_2026-10-08.md`.
- `FOUR_LAWS_TRAINING_AUDIT_G222_G310_2026-10-08.md`.
- `C4_NEXT_CHAT_HANDOFF_G322_TO_G323_2026-10-08.md`, `00_READ_ME_FIRST.md`, `01_NEXT_CHAT_HANDOFF.md`.
- `RUNTIME_ARCHITECTURE_PRINCIPLES.md`, `DEVELOPMENTAL_TRAINING_METHODOLOGY.md`.
- `experimental_g330/G329_REAL_DEVICE_CAUSAL_AUDIT.md`.
- `experimental_g330/tests/test_g330_real_device_red.py`.
- `experimental_g330/RED_TEST_G329.log`.
- `experimental_g330/G330_CLEAN_CORE_DECISION_AND_CASCADE_GATE.md`.

## Незакрытые противоречия (НЕ сглаживать)

- Пользователь спрашивал и «можно ли отремонтировать существующую C4?», и «если начать с 0, можем ли сразу заложить все механизмы?». **Не решать молча, что всё переписывается:** смысл пакета — один интеграционный скелет; использовать ранее доказанные механизмы при прохождении контрактов. Сперва M0 diff.
- После G323-P9 есть полезный recursive/presence GREEN candidate, но не canonical. G329 Android показывает real failures с organism G327/G329-sha и новым G329 runtime; надо явно разделять ветки, не переименовать одну в другую.
- Были сотни PASS, но реальные RED на local scene и attribution. Не объявлять «универсальную семантику» по lexical fallback или регрессии.
- "Заранее все механизмы" означает полные **контракты и места для обучения**, а не гарантированную реализацию всех когнитивных алгоритмов или неограниченный AGI.
- Прямой `graph.commit` из диалога/учителя недопустим; но если в G314–G323 он уже закрыт, не вводить второй gate. Сначала исследовать код конкретной ветки.
- Не рассказывать пользователю, будто создан ZIP, APK, обученный .c4m или M1+M2, если в репозитории существуют только Markdown-файлы.
- Не предполагать, что новый chat имеет физически доступный файл `c4_chat_1791470574930.json` без проверки; сохраняются только отчёты по нему и указание на вложение в исходной беседе.

## Следующее практическое действие, без повторного философского круга

1. Найти конкретные source paths G323 и G329 и проанализировать дифф контрактов representation/commit/drive/mediate.
2. Реализовать минимально исполняемый **typed Event → Frame → EVAL hypotheses → single COMMIT gate → DRIVE decision → MEDIATE receipt** со snapshot/replay и автономными TICK; начать без русского.
3. Написать property-based tests с генерацией новых участников/историй/времён/scope, в т.ч. C4 own ASK != USER quote.
4. Подключить существующий русский язык и обучающий organ через интерфейсы, не подгонять ответы под frozen tests.
5. Сравнить G329, G323 и clean integration candidate на holdout и реальном Android. После **GREEN** и cold reload выпускать артефакты со строгими SHA.

Отвечать пользователю на «Продолжай» конкретными коммитами, тестами, статусом M*, а не описанием ещё одного большого плана.

## Как интерпретировать «с рассуждениями»

Публичные, проверяемые основания решения находятся в файле 03. Это **не** скрытая chain-of-thought и не автоматический API-экспорт полной переписки. Скрытый ход не воспроизводить; сохранять source-grounded инженерную аргументацию, ошибки и альтернативы.

## Итоговая позиция

Сохранить C4 как проект, его законы, наработки и источник истории. Пересобрать **обязательный общий причинный интерфейс**, не только словесные ответы. Сначала безопасный минимальный работающий механизм с реальными проверками, затем когнитивные органы, обучение, сенсорику и реальную автономию. Цель — устойчивое самообучение без самозаражения, а не рост числа фактов или эффектный чат.
