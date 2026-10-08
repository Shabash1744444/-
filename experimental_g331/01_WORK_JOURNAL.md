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


### C003 — Delayed grounded SIM transitions + bounded causal composition — DONE
Date: 2026-10-08.
Parent C002 HEAD: d844cd31d7a001665f967cbb69e4fd126c3224b5.
Physical START: commit 480ba9b79f54348c68c56fb504a0b968bfbdf079.
Frozen first RED: 5/5 failed on native C002 G331 (multi-step goal, no intermediate transition witness, failure handling, provenance root count, C4M cold). Original log saved in Library C003.
Repair: changed ONLY native existing `experimental_g331/native_c4child/structured_cognition.py`; no new brain, memory or model. Added GOAL.initial and bounded 6-step compositional search across relational before/action/after SIM examples; single-flight action proposal, host attested observed_action/before/after, required receipt_id and root_id for chained success, repeat-receipt and contradiction rejection; conservative teacher root treatment; deduplicated strategy feedback by host-declared original root per action; preserved SOURCE≠WORLD and G215 source trust firewall. Teacher demonstrations remain unverified, not independent factual proofs. Host root IDs are asserted by the host and not cryptographically authenticated.
Test methodology: original RED test refined in two places to accept safe NO_STRATEGY refusal and avoid direct private state mutation; raw initial RED log preserved. C003 new heldout 18/18 passed incl 12 generated three-step arbitrary symbol tasks. Directed native old+new 97 PASS. Available full suite 633 PASS / 27 historical missing fixture FileNotFoundError FAIL; NOT full green.
Real existing G329 C4M: original SHA256 dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f; original 10,781 facts, cold 10,781 facts; stage 1 -> OPEN, cold resume -> stage 2, confirmed SIM goal only after host-SIM receipt. Original baseline not overwritten. Android physical LIVE NOT TESTED.
Local runtime native ZIP 56 source Python files, SHA256 cc3fd869d9133fe9180a277d134c3c736d613c35d0e0306ee4202a0e9b430664; artifact and full handoff in Library `/C4_Candidates/G331_NATIVE_COGNITION/C003/`.
GitHub source repair commit 272b2cd4e8c770b5670967621fc0be3f00a45379, CI workflow commit c704f1d50143a0e563e6ec5fa6d615a8d123ccf5.
GitHub Actions run 37836262293: completed SUCCESS, byte-exact SHA256 of updated source confirmed, original runtime pinned SHA checked, 95 PASS/2 SKIP, constitution-only PASS, autonomous_pretrain correctly BLOCKED, 56 module CI runtime ZIP packaged as artifact 11574714954.
Risk explicitly open: mockable in-process Python host callback; real Android host receipt bridge and physical sensor provenance not yet connected. SIM planning is bounded deterministic hypothesis composition, not general cognitive reasoning or independently grounded world truth.
Next C004: NOT STARTED. Must begin with physical START checkpoint, freeze RED on Android native event/receipt linkage and source dependence, preserve original C4M/constitution, then reattack, full regression, cold load and CI; do not shorten architecture to templates or duplicate memory.


### C004 — Native Android host action linkage — START / RED (NOT DONE)
Date: 2026-10-09. Parent C003 DONE HEAD: `c953dcddcc26f2382945ca7da62a05294375bc3f`; physical START checkpoint: `checkpoints/CP_C4_G331_C004_START.md`.
Verified preceding C003: automated Actions SUCCESS run `37836471938`, earlier native local 97 directed PASS / 633 broad PASS, 27 historical missing fixtures; no Android physical evidence.
Frozen RED run against the unchanged physically extracted native C003 56-module ZIP. Scenario: SIM GOAL BALL LOCATION floor-left→held, DEMO TAKE, PLAN. The original C4 chose `TAKE` and stored `PROPOSED_NOT_EXECUTED`, but outbound was just `REPLY` instead of a host-dispatchable `ACTION_REQUEST`. `sim_action_receipt` without a host adapter correctly returned `SIM_HOST_NOT_BOUND` with no state promotion.
Command: `PYTHONPATH=<extracted C003 zip> python -m pytest -q experimental_g331/c004/frozen_red/test_c004_android_receipt_red.py`; result **1 FAIL, 1 PASS**. Test source SHA256 `f82c7a8c41ebfcd1081ac53136876180a7dae4b471cd1d78da2dc63e6f3ffa18`.
Additional cross-repo audit: existing `Shabash1744444/Emu` WebView supports `ACTION_REQUEST`→Java `executeRoomAction`, but its `c4_mobile_bridge.py` does not bind C003's `sim_action_receipt` host-owned adapter; WebView's `ACTION_RECEIPT` message is not a substitute for native independent evidence. Detailed contract and evidence: `c004/C004_BRIDGE_AUDIT.md`.
Changes in this segment: **only journal, checkpoint, frozen failing test, audit files**. No C4 core, Android app, or .c4m mutation. This is **not** C004 DONE. Next action: implement the host-owned Android private bridge + native C4 ACTION_REQUEST lifecycle atomically and re-run this RED, adversarial cases, all old regressions, C4M cold reload and physical Android live when possible. Preserve all constitutional and G215 cascade safety.

### C004 — Android host SIM action/receipt integration — INTEGRATED / DEVICE PENDING (NOT DONE)
Date 2026-10-09. START checkpoint `29722916a5ff9c5ce5db450d7c2c9f9afa2271a3`, frozen 1 FAIL / 1 PASS. Previous full DONE C003. Native code/C004 pinned runtime committed as `f4fc8e5bb210cf9c1c39899be81c0a1865460e7b`.
Changes to existing `c4child`: `runtime.py` and `structured_cognition.py`; original graph and C4M unchanged. SIM-home PLAN now emits a typed host `ACTION_REQUEST` with exact action/subject/requestID while status is unexecuted. Native Java host dispatch in `Shabash1744444/Emu`, experimental branch `experiments/c4-c004-native-host` commits `0cbed7eff269c0941da249084290895b76c99f9c`, `0ba500e28bb406a1a6fb391ae55f233fe1249f29`. Java directly performs sandbox operation and calls private Python bridge; JS `ACTION_RECEIPT` cannot earn C4 cognitive SIM credit.
Locally reproduced: C001–C004 combined 83 PASS; original G329 real C4M SHA256 `dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f`, 10,781 facts unchanged after SIM host callback and cold `.c4m`, original source not overwritten. Native app GitHub Actions `37844344905` SUCCESS (debug APK compiled). On C4 branch updated CI run `37845141293` requested; final status must be checked before claiming success.
Artifact pinned: `experimental_g331/assets/C4_G331_C004_NATIVE_RUNTIME.zip`, SHA256 `eefcd7c89706357aafc5c5bae59ce3522ccdf2619817858b48cff5f90426d641`, exactly 56 Python files. Library: `/C4_Candidates/G331_NATIVE_COGNITION/C004/`.
IMPORTANT: **C004 not DONE** until actual Android device test with paired APK+runtime and genuine trace of execution→host feedback→cognitive update→cold reload. No fresh 633-test full sweep in C004; earlier 27 historical missing fixture errors remain unresolved. Background host actions fail closed instead of executing through JS. Do not turn those into fake success or a claim of AGI.
Next first action: check C4 CI status; on real device run frozen authorized SIM room action, replay + stale session attacks, export native logs; close C004 only with proof. Keep constitution and mass-autonomous-pretrain BLOCKED; C005 NOT STARTED.

### C004-R1/R2 — native action trust + planned destination — CODE GREEN / DEVICE PENDING
Date: 2026-10-09. C004 START/RED from prior checkpoint; previous full DONE C003.
Frozen R1 RED: public WebView Java executeRoomAction accepted the same caller-chosen `trial:*` namespace as host-issued cognitive actions, allowing replay-key preemption. Added private `executeRoomActionTrusted`, trimmed-prefix rejection on JS API and an Android Actions regression check. Latest R1+R2 Android Java branch: `Shabash1744444/Emu`, `experiments/c4-c004-native-host` commit `a528129a8ed7b6a675ee49d9f8c0ecaf0cfd6952`. CI run 37851562352 SUCCESS; APK build passed.
Frozen R2 RED: typed `PLACE BALL held→basket` planned by C4 emitted ACTION_REQUEST without target; Java would choose its unrelated default floor-right. Original `c4child/structured_cognition.py` now carries the target for PLACE/RELEASE, rejects unsupported native room zones from the actuator request; private Java dispatcher validates and forwards the exact target. Previous source code, actual C4Graph and old .c4m retained.
R2 new test: 10 PASS local; real 10,781-fact G329 model original SHA dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f, unchanged across PLAN, witnessed host-style SIM outcome, save/cold reload, 10,781 facts throughout; goal ACHIEVED_SIM only after receipt.
Pinned 56-module runtime SHA256 `7bd314029d4b927eb00e847ec52d2d3d45ffba06b7f30bba094a06af6be47f76`, tested source SHA `e61f417c78a594db6d49262e9a876771795e4f1b98872fb893f8898657bbef13`, C4 GitHub commit `3aa7a3c798fb052f028ba51a21b495bd5f00d2f4`. C4 CI run 37851791773 SUCCESS: 114 PASS / 2 SKIP, constitution PASS and autonomous_pretrain BLOCKED.
Full C004 **NOT DONE**: no physical Android action→receipt→credit→cold trace. No new full-suite 27 historical fixture retest; these remain previously unavailable. Latest physical checkpoint `checkpoints/CP_C4_G331_C004_R1_R2_CODE_GREEN_DEVICE_PENDING.md`. Phone protocol `c004/C004_R2_PHONE_LIVE_PROTOCOL.txt`. Runtime ZIP in Library `/C4_Candidates/G331_NATIVE_COGNITION/C004_R2/`.
NEXT: paired APK+runtime physical phone test; check before/action/after, private result, replay/session, save+reload. Do not start C005 or declare C004 DONE on CI alone.
