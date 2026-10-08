# C4 Guard V2 — физический исполняемый checkpoint
Дата 2026-10-08. Статус: **EXPERIMENTAL STRUCTURED COGNITIVE CORE / CI GREEN**, НЕ CANONICAL, НЕ AGI, НЕ Android APK.

## Что физически есть
- Source: `experimental_g330/m1_m3_runtime/C4_EXECUTABLE_COGNITIVE_CORE/c4core/kernel.py`, `cli.py`.
- Tests: `tests/test_kernel.py` (28 исходных случаев, сенсорный контракт явно ужесточён), `tests/test_adversarial_red.py` (15 новых контрпримеров).
- Ограничения и остаточные риски: `HARDENING_REPORT.md`.
- Контрольный Python ZIP, сохранённый в Library: `/C4_Code/GuardV2/C4_COGNITIVE_GUARD_V2_PYTHON_2026-10-08.zip`.
- ZIP SHA256: `186621afffd1119bd23a858cf156c083345cdb547fc82ab1c38e392ce997d61b`; ZIP 30,820 bytes. Включает Python, CI workflow, 43 tests, README, исходные RED evidence и C4J migration example.

## Проверки
- Original M1-M3: 7/7 наиболее ранних guard tests RED (до изменений).
- Hardened V2: 43/43 PASS локально Python 3.13; V1 C4J успешно загружен, сохранён как V2 и заново открыт с тем же snapshot hash.
- GitHub Actions workflow `C4 Cognitive Core Guard V2` запуск `37815700511`, branch `experiments/c4-g330-device-red-cascade`, commit `829bfb96b1eb450f31eca7a9b14ac1284055ac47`: **completed SUCCESS**, 43 PASS, generated demo and CLI, artifact `C4-GUARD-V2-TESTS`.
- [Actions run](https://github.com/Shabash1744444/-/actions/runs/37815700511).

## Архитектурные риски, которые НЕ вправе считать исправленными
1. Python attrs accessible to in-process organs -> no security/capability isolation (EVAL can still mutate internals if caller malicious). Следующий шаг: single-owner transactional state service/process.
2. Learning procedural rules still uses lightweight EVAL hypothesis storage rather than a robust evidence-root independent procedural COMMIT gate. Support of two independently received events does not prove independence of original sources.
3. Real-world receipts cannot be independently validated by this prototype. Bound host callback is explicit trust transfer, not proof of physical world.
4. No general Russian language learning, semantics, irony, spatial/causal open-ended planning, rich multimodality, Android execution, model weights, legacy C4M migration.
5. Gap-answer match relies on exact typed topic symbol, not deep semantic question-answer alignment. ANSWER_CANDIDATE never means verified answer.
6. Time query supports claimed event-time and retraction event-time but lacks bitemporal known-at vs happened-at logic and proper handling of missing timestamps.
7. Current trace is bounded tail, not chunked immutable audit archive. Cannot use trace itself as EVIDENCE.
8. No comparative independent real-dialogue re-attack yet.

## Телефонный рабочий процесс
В мобильном GitHub открыть **Actions → C4 Cognitive Core Guard V2**; автоматическая проверка запускается на коммитах в экспериментальной ветке (вызов вручную зависит от наличия workflow на default branch). Нажать запуск, открыть logs и artifacts. НЕ нужны Windows, ПК, локальный терминал.
Преобразование этого кода в APK требует отдельного Android bridge; не приписывать workflow запуск на телефоне.

## Следующий фундаментальный этап
Не обучать корпуса до **atomic owner-governed transitions** + provenance-aware learning + bitemporal history + held-out transfer under nested perspectives. Это исследовательская система, пока не устойчивый самообучающийся интеллект.
