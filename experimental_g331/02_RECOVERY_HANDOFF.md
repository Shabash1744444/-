# CURRENT STATUS 2026-10-09: C003 DONE; C004 INTEGRATED / DEVICE PENDING (NOT DONE)
Native C4 C004 integration source and exact 56-module ZIP pinned at commit f4fc8e5bb210cf9c1c39899be81c0a1865460e7b; C4 GitHub Actions SUCCESS run 37845141293: 104 passed, 2 skipped, SHA+cmp verified, constitution gate PASS, autonomous_pretrain BLOCKED.
Companion Android app branch Shabash1744444/Emu experiments/c4-c004-native-host at commit 0ba500e28bb406a1a6fb391ae55f233fe1249f29, Android assembleDebug SUCCESS run 37844344905. Pair the APK from this run with C004_NATIVE_RUNTIME.zip, never G331 C003/old app. Native runtime SHA256 eefcd7c89706357aafc5c5bae59ce3522ccdf2619817858b48cff5f90426d641.
Previous G329 trained .c4m unchanged (10,781 facts after cold). Local C004 83 PASS; no fresh full old test sweep; Android physical end-to-end NOT ATTESTED.
C004 cannot be marked DONE until a real phone trace shows ACTION_REQUEST → Java SANDBOX before/action/after → private native_room_receipt → original C4 SIM learning/cold reload plus replay/session negative tests. Background actions are fail-closed.
Next: physical device experiment and log assessment; no C005 unless C004 duly closed or status escalated BLOCKED with explicit reason. Consult 01_WORK_JOURNAL.md last and checkpoints/CP_C4_G331_C004_INTEGRATED_DEVICE_PENDING.md. Do not create second brain/memory or remove four-owner/anti-cascade guards.

---
# CURRENT HANDOFF: C003 DONE → C004 NOT STARTED
Updated 2026-10-08. Read the BOTTOM of `01_WORK_JOURNAL.md` FIRST. The last DONE is C003. C003 source SHA update `272b2cd4e8c770b5670967621fc0be3f00a45379`, CI run `37836262293` SUCCESS (95 PASS 2 SKIP), journal commit `8ffa1cda93c6c34731d78df4ecabfeee8fc2270e`. The old 10,781-fact `.c4m` survived cold reload unchanged. C003 runtime ZIP in Library `/C4_Candidates/G331_NATIVE_COGNITION/C003/`. GitHub C003 test: `experimental_g331/tests/test_c003_causal_credit.py`. Local full 633 PASS / 27 historical fixtures missing.

C004 NOT STARTED. BEFORE any code change: physical START checkpoint, frozen RED for Android host delivery/execution/feedback and independent lineage. Work ONLY in existing c4child/Emu integration; do not duplicate graph, model or memory. Do not call SIM mock an Android observation. Retain constitutional stage-gate and run native regressions/cold and CI.

---

# CURRENT HANDOFF: C002 DONE → C003 NOT STARTED (2026-10-08)
Start from `01_WORK_JOURNAL.md` bottom C002 DONE. Native code `8c88ed01c9a9914e495b7f94f043b0d056edbe7f`. Frozen regression workflow `10525f834f77175f92aae8d1142c363ac42d9013` (GitHub Actions 37832089735; inspect latest status). C002 79 directed PASS, 615 broad PASS / 27 historical fixture failures, original C4M cold 10781→10783. Runtime ZIP physically pinned at `experimental_g331/assets/C4_G331_C002_NATIVE_RUNTIME.zip`, same C4 G329/G331 model and native c4child. `governance/constitution_contract.json` and `tools/c4_stage_gate.py`: unproven autonomous pretraining BLOCKED. Android LIVE not attested.
NEXT **C003**: before editing any source, write physical START checkpoint; freeze RED on independent-root learning, delayed verified SIM outcomes and multi-step causal transfer. Never rebuild second memory/weights. Export trace and cold C4M; journal every cycle. 

# C4 — NEXT CHAT / RECOVERY HANDOFF

## На 2026-10-08
**Current cycle:** C000 DONE, C001 NOT STARTED.
**Working ref:** `Shabash1744444/-` branch `experiments/c4-g331-native-cognition`.
**Known code baseline before journal:** `38c7354e20d937dfef1f75b2b6e7df6a9b9c373f`.
**Последний надёжный документ:** `experimental_g331/01_WORK_JOURNAL.md`, самая нижняя запись с DONE и физическим checkpoint.

## Для нового чата — буквально
«Это C4, не Singularity OS. Продолжи текущую реализацию в существующем `c4child`/G329→G331, не создавая второй памяти и отдельного рантайма. Открой `experimental_g331/00_READ_ME_FIRST.md`, `01_WORK_JOURNAL.md`, `02_RECOVERY_HANDOFF.md`, `03_ACCEPTANCE_MATRIX.md` на актуальном HEAD ветки; выясни последний DONE. Выполняй следующий шаг, пиши START-checkpoint до опасной операции и DONE только после проверок. Сохрани исходный `.c4m`. Мне нужно исполняемое ядро и трасса, а не очередное теоретическое описание».

## Если зависание/лимит посреди работы
1. Сверить HEAD, последний DONE и START в `01_WORK_JOURNAL.md` и `checkpoints/`.
2. Если есть START без DONE: считать цикл **прерванным**, искать реальные изменения commit-by-commit; не объявлять его завершённым, не стирать evidence.
3. Если изменения есть только в несохранённом рабочем контейнере — считать их потерянными; повторить только доказанно незафиксированную работу от физического checkpoint.
4. Никогда не перезаписывать `.c4m` пользователя / G309 canonical / чужую параллельную ветку; использовать независимый бэкап и экспериментальную ветку.
5. На каждом цикле писать checkpoint: базовый HEAD, изменённые файлы, контрпример, тесты, известные RED, фактический SHA, первое действие следующего цикла. Фиксировать BLOCKED с реальной причиной вместо обещания закончить позднее.

## Не подменять задачу
- `C4 LIFE v1` — неподходящий отдельный прототип; не интегрировать как вторую память.
- Псевдоязык — временный **способ ввода структурированной семантики**, а не упрощение когнитивного механизма.
- Исходный `c4child` должен сохранить существующие источники, граф, полученные знания, lineage, инициативу и native `.c4m`.
- 96 направленных PASS и широкий PASS G331 **не подтверждают** свободный русский диалог, комплексное мышление и реальную обучаемость. Android LIVE пока не подтверждён.
- Следующая цель — held-out сквозная когниция в продолжительном разговоре: агент сохраняет чужую перспективу и внешнее время, сам уточняет, обновляет гипотезы и учится на доказанных последствиях без написанных для этой ситуации готовых ответов.

## Шаг C001
Провести read-only аудит траектории событий и frozen held-out тестов на действующей версии G331; записать первый RED, затем исправление в **родном** `c4child`. По завершении — реальное выполнение тестов и холодная загрузка, новое сообщение в журнале и immutable checkpoint.


## NEWEST checkpoint 2026-10-08
C001 DONE. Code commit: a6aea791ed9c1896ca49ad3a2584bacb064bb39e. See 01_WORK_JOURNAL.md and C001_README.md. C002 NOT STARTED. Begin C002 with START checkpoint on native c4child; freeze nested perspective + relative time RED. Do not redo C001.
