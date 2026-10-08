# C4 — единый рабочий журнал (append-only)

**Правило:** каждая запись идёт новой секцией в конец. Старые записи не переписываются и не удаляются. Каждая правка кода получает номер цикла, входной контрпример, изменённые реальные файлы, точную команду/результат тестов, отметку проверки на устройстве, результат cold reload и последний commit SHA. Противоречивые результаты указывать вместе, не выбирать удобный.

## Шаблон следующего цикла
```text
### C001 — <краткое имя> — START / BLOCKED / DONE
Дата/время:
Базовый HEAD:
Цель, пользовательское требование:
Исходные факты и актуальные файлы:
Конкретный негативный контрпример / ожидаемое поведение:
Изменения кода:
Какой существующий граф/память/рантайм использован (без копии):
Тесты: команды + число PASS/FAIL/SKIP + missing fixtures:
Экзамен: unknown/held-out + cold reload + causal trace:
Физический Android LIVE: НЕ ПРОВЕРЕНО / лог и наблюдение:
Сохранённые артефакты, хеши:
Git commit/checkpoint:
Остаточные риски:
Следующее первое действие (одна воспроизводимая команда):
```

### C000 — START → DONE — физическое открытие непрерывного журнала
Дата: 2026-10-08.
Базовый HEAD: `38c7354e20d937dfef1f75b2b6e7df6a9b9c373f`.
Запрос: пользователь согласился на ориентировочный многопроходный план разработки C4 с условием обязательного журнала на случай зависаний и лимита чата.
Сделано: записаны живой журнал, точка восстановления, матрица приёмки и неизменяемый начальный checkpoint в ту же экспериментальную ветку.
Изменения исполняемого C4: **нет**. `.c4m` не тронут. Чужая параллельная ветка/Android APK не тронуты.
Тесты в C000: не запускались; кода не меняли. Предыдущие G331 результаты представлены как историческое свидетельство и остаются непроверенными в этом цикле.
Итог: инфраструктура восстановления. Это **не** означает завершения этапа «человеческая когниция».
Физическая точка: `checkpoints/CP_C4_G331_C000_JOURNAL_BOOTSTRAP.md`, GitHub commit, содержащий эти четыре/пять файлов.
Следующее первое действие C001: снять точную карту путей событий `user_message → EVAL → COMMIT → DRIVE → MEDIATE → runtime_state / C4M` по фактическому G329/G331 коду, затем сформулировать и выполнить **один** held-out сквозной тест непрерывного диалога; только после получения RED делать минимальный ремонт.

### C001 — START
Commit `3f4cfe673eeac0cc71b2edd30b8dcc5db59f52ce`, до изменения исполняемых файлов. Frozen RED: операция CORRECT возвращает REJECTED.

### C001 — Temporal self-correction of a dialogue statement — DONE
Дата: 2026-10-08.
Базовый HEAD: `0051e696db82b55d0fccbfccb5bf9011189e21e5`; физический START: `3f4cfe673eeac0cc71b2edd30b8dcc5db59f52ce`.
Исполняемый commit: `a6aea791ed9c1896ca49ad3a2584bacb064bb39e`.
Цель: на **существующем C4Child/G329→G331** различать конфликт независимых SOURCE-свидетельств и явное исправление того же сообщения источником; отвечать на текущий и исторический запросы без WORLD-подмены и без потери памяти после compact C4M restart.
Замороженные RED: (1) `CORRECT` отклонялся, (2) cold reload терял историческую SOURCE-запись, (3) настоящий G329 10 781-фактный C4M отклонял отношение `COLOR`, потому что оно обучено как `entity`, в отличие от пустого `literal`-графа.
Изменения: старые `c4child/structured_cognition.py` и `c4child/checkpoint.py`; добавлен `tests/test_c001_temporal_dialogue.py`. **Новой памяти/весов/серверов нет.** `SOURCE_SUPERSEDED` сохраняется в hot-части прежнего `C4Graph`, версия C4M не менялась. Прямое указание старого `source_event_id` и исходного scope/scene/frames необходимо; другое событие корректировать нельзя.
Исполнение: `PYTHONPATH=. pytest -q tests/test_c001_temporal_dialogue.py tests/test_g331_real_organism.py` — **32 PASSED**. Полный `PYTHONPATH=. pytest -q tests` — **568 PASSED / 27 FAILED**. Все 27 FAIL являются `FileNotFoundError` для отсутствующих исторических G137/G151/G153/G207/G280/G302/G308/G309 контрольных моделей; никаких иных FAIL в этом запуске. Общий набор НЕ GREEN.
Настоящий исходный G329 C4M: хеш SHA256 `dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f`, **не перезаписывался**. `10781 → 10783` факта после двух сообщений, `10783` после холодной загрузки compact C4M. Исторический запрос: `teal`, текущий `amber` (в сцене `shapes-room`); пример не заложен в код. Графовые атрибуты и источник сохраняются.
Android: **НЕ ПРОВЕРЕНО на устройстве**. Новый исполняемый ZIP — 56 исходных модулей `c4child`, холодный импорт в отдельной папке, `C4LivingRuntime` и диалоговый smoke PASS. SHA256 `C4_G331_C001_NATIVE_RUNTIME.zip`: `0a7e6801cfcfe1494dee2dd1c5a70987a3df114697819f42d8302e789c676bbe`.
Артефакты в Library: `/C4_Candidates/G331_NATIVE_COGNITION/C001/` — native runtime, полный handoff, исходники, patch, trace и полные тестовые логи. Исходники и checkpoint в GitHub: `experimental_g331/C001_README.md`, `native_c4child/structured_cognition.py`, `native_c4child/checkpoint.py`, `tests/test_c001_temporal_dialogue.py`, `checkpoints/CP_C4_G331_C001_DONE.md`.
Нерешённые вопросы: полные три времени, самостоятельное понимание русского, нестандартные причинные операторы, реальный Android host-receipt. Нельзя заявлять, что один локальный ремонт создал человеческий диалог.
Следующее первое действие **C002**: зафиксировать unseen контрпример вложенных чужих высказываний с относительным временем события/сообщения/понимания; получить RED на истинном C4M, затем минимально править уже имеющийся `c4child`, делать re-attack, regression и cold reload. Перед работой — физический START.

### C002 — Nested perspective / relative narrated time / non-regression gate — DONE (local)
Date: 2026-10-08. BASE HEAD: `4ad2b5f922de70a77ef02deb959cdb3bf90a9e51`; pre-mutation physical START: `bbfae7b0e8307cc44c37adc5ea0c74e0e81dab59`.
Goal: stop C4 from treating reported event time as message time, and make the four laws/methodology/cascade constraints executable across future cycles. Native C4 G329/G331 only, no new memory or model.
Frozen RED first: tests/test_c002_nested_time.py on C001 yielded **6 FAIL / 1 PASS**. The structured input was accepting `time` but discarding it: day12/day13 collisions and wrong-time corrections; no source temporal metadata or anchor validation.
Minimal repair: existing c4child/structured_cognition.py; strict finite temporal input, relative `UTTERANCE` / `SOURCE_CONTENT` anchored to exact same contextual source claim, separate represented day vs speaker-declared utterance day vs native external-order/known-turn and wall-clock timestamp. Query at content day and as_of_turn; correction must refer to the same target time, missing utterance date remains UNKNOWN. EVAL does not invent world truth. Native C4Graph+SemanticSpine unchanged in shape except additive original event metadata.
Anti-cascade: hardened unknown-field rejection; 16 variant G215 conflict loops, 9 nested/context swaps, 8 spoofed metadata attempts, source-only and no false receipts, old C001 suite, cold reload. `governance/constitution_contract.json` + `tools/c4_stage_gate.py` guard 4 owners/5 influences and forbid unproven mass autonomous pretraining; intentional pretrain BLOCKED exit 2.
Results: 79 directed PASS. Full available 615 PASS / 27 FAIL, all 27 FileNotFoundError for unavailable historical model checkpoints. This is NOT full green. Real G329 C4M SHA256 `dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f`, 10,781 → 10,783 → cold 10,783 facts, nested/perspective scope verified, source day12 `cobalt` day13 `ivory`, WORLD promotions zero. Android LIVE NOT TESTED.
Install native 56-module runtime ZIP SHA256 `b9551694410aacbf798635d4d5bcb5485d8e2bc76a2e92e0233a960063b3fc4e`; handoff archive SHA256 `eda519d3772c04c0ca0889a6e49383ea838924e4b78d9e5d77329c0f52012008`.
Physical code commit `8c88ed01c9a9914e495b7f94f043b0d056edbe7f`, workflow/pinned-binary commit `10525f834f77175f92aae8d1142c363ac42d9013`. GitHub Actions run `37832089735` triggered and was in_progress when writing this entry; final status must be checked separately. None of this attests a phone run.
Checkpoints and ZIPs: `/C4_Candidates/G331_NATIVE_COGNITION/C002/` Library; original source on GitHub under experimental_g331/; no C4M overwrite.
Known open risks: claimed days are user-supplied symbols, not natural language timestamps; `known_turn` reflects external-reception order only; no independent Android result receipt; no general teacher/heldout open-ended operator training; legacy Russian parse has its own independent limitations.
NEXT C003 NOT STARTED: compare teacher-issued examples against actual SIM receipts with independently rooted lineage, multi-step causal transfer and adversarial counterexamples; freeze RED, modify native runtime, full regression and cold reload; save START checkpoint **before** modifications. Do not declare autonomy or human-level dialogue from PASS counts.
#### C002 — CI POSTCHECK (same cycle, immutable evidence)
Дата: 2026-10-08. Automatic pipeline was first RED: run 37832089735 failed due missing numpy dependency and corrupted UTF-8 text in GitHub blobs. Reproduced errors from job logs. Root cause of damaged text: base64 transfer encoding missed '/' character; restored source blobs with byte-exact git object hashes and amended CI to install numpy, `cmp` checked tested source against pinned 56-module ZIP.
Final corrected source/CI commit `4dd85f34625bbe0986795c81e7ec1d3a0603d49e`.
Confirmed successful GitHub Actions: https://github.com/Shabash1744444/-/actions/runs/37832745676 (run 37832745676), **77 PASS / 2 SKIP** on runner, plus verified constitutional gate PASS and autonomous_pretrain BLOCKED by design. The 2 skips concern absent local real-weight C4M fixture on CI; real G329 C4M was separately cold-tested in local environment. Runtime ZIP's SHA256 matched pinned manifest; installed archive source and GitHub Python file compared byte-for-byte. Other old full-suite 27 missing fixture FAIL still unresolved; no physical Android test. All new logs/checkpoints remain in Library and branch.
C002 now DONE with local test evidence and CI run evidence. Next C003 START checkpoint required before editing.
