# CP C4 G324-P3 — SIMULATION-SCOPED LEARNING + STRICT WORLD GATE

Date: 2026-10-08. Status: **EXPERIMENTAL LEARNING CANDIDATE, NOT CANONICAL; NOT HUMAN LIVE GREEN**.
Parent: G324-P2 experiment / G322-P8 model. G323-P9 recursive-perspective work is a separate parallel branch; binary not merged. G309 canonical state unchanged.

## Physical result

An experimental runtime now contains a reusable `EmpiricalConstraintLearner`, i.e. finite-domain Bernoulli conditional structure discovery by penalized likelihood and a small parent-set search. It learns candidate factors from synthetic receipted transition rows with source dependency roots, `SIMULATION`/frame/epoch scoping, duplicate/replay collapse, conflict quarantine, abstention when untrained or under-supported, and save/reload support. It is predictive association learning and **does not establish true interventions/causation**.

New `C4LivingRuntime` methods: `begin_causal_study`, `learn_simulated_constraint`, `fit_causal_study`, `predict_causal_study`. The current interface requires a trusted simulation adapter to supply receipt IDs: **receipt values themselves are strings and are NOT cryptographically/boundary authenticated**. Therefore these lessons never authorize WORLD.

New opt-in `strict_world_admission=True` runtime setting persists in `.c4m` runtime state. On this mode, all unsupported external epistemic reports remain `NEEDS_GROUNDING`, including three nominally independent sources that previously could create WORLD_TRUE. The guarded legacy gate is intentionally left available as a control; historical tests still assert old `ADMITTED` semantics. **Do not run live without strict mode**. This only protects `EpistemicAdmissionOrgan` and does NOT yet secure other `graph.commit/BootstrapTeacher/dialogue` mutation entrances. The COMMIT risk is not fully eliminated.

Source files changed:
- `runtime/c4child/learned_constraints.py` [new]
- `runtime/c4child/epistemic.py` [strict gate, persisted]
- `runtime/c4child/runtime.py` [study API and strict flag]
- `runtime/tests/test_g324p3_learned_constraints.py` [19 frozen directed tests]

## Tests

- G324-P3 new focused: **19/19 PASS**.
- Including P0/P1/P2 directed: **90/90 PASS**.
- Full extracted-package suite: **578 PASS / 27 FAIL**, same 27 historic FileNotFoundErrors as G324-P2; no additional failed test IDs. The full suite is NOT GREEN.
- Benchmark: four synthetic binary function families × 12 independent random seeds = 48 fits, 11,520 training episodes, 19,200 held-out episodes. All are independent *episodes* drawn from the same synthetic families; **not unseen languages/tasks/physical laws**.
- XOR 100% accuracy; OR 100%; 3-input majority 100%; noisy-XOR (7% injected label noise) mean 92.33% accuracy. All 100% coverage under these data volumes. See `HELDOUT_EVAL.json`.
- A physical C4 .c4m checkpoint with **900** SIMULATION-scoped episodes across XOR, OR, majority was exported and cold-reloaded. Its original graph remained unchanged: 10,727 entities, 10,781 facts, order 22,306.

## Trained physical state

- Original parent model SHA256: `6baf2864ce8a811738d13cf3593f739e8dcc5a8734d17ce0f5647bc23da06301`.
- Trained experimental `.c4m`: `child_g324_p3_simulation_learned_candidate.c4m` SHA256 `052f30fb0f79b79dad93e25ad77ad81f29ff5bc2be6981fefc85630a56f791c1` (2,009,632 bytes).
- Export/reimport verified selected parents and all 8 input combinations for each of the three studies. The experiment is candidate learning; not world knowledge, verbal competence or causal discovery.

## Real dialogue preflight: observed failures retained, NOT CHERRY-PICKED

Using physical exported C4 .c4m, eight sequential text turns (without new educational corpus):
- `Привет! Как дела?` -> ordinary greeting; no graph mutation.
- `Ты Синька` -> accepted a user-reported social name, not external WORLD evidence.
- `Маша сказала: «Меня зовут Аня»` -> safely treated as quotation, no mutation.
- `А Маша кто?` -> said it doesn't know.
- `Представь: Маша думает, что Иван опоздал` -> failed to understand.
- `Я сказал: «Луна — сыр». Это теперь факт?` -> recognized quote but did not supply direct truth/scope reasoning.
- `Что ты действительно знаешь из увиденного, а что только предполагаешь?` -> failed to understand.
- `Почему ты уверена в своём ответе?` -> misattributed viewpoint, answered about user's confidence instead of own.

Full verbatim replies and per-turn mutation counts in `PREFLIGHT_DIALOGUE.json`. This is **local scripted preflight, NOT user's Android/device live test**. Without G323-P9 integration, nested third-party beliefs are expected weak.

## Release blockers before real-life endorsement

P0. **Truth gate is not universal**: other direct `graph.commit` mutation paths are still potential bypasses.
P0. **Trusted receipts**: no independently authenticated real/simulation observation origin in the new learner API, only string checks. No claims of physical grounding.
P1. **Language -> factors**: parser cannot yet reliably transform unconstrained Russian into typed perspective/causal representations. Need G323 source/binary merged carefully and trained language structure, not phrase-specific regex.
P1. **Learned graph rewiring**: current learner does not learn `adaptive_bifurcation` topology; G324-P2 heuristic threshold remains fixed.
P1. **OOD**: held-out episodes same simple Boolean families; test new domains, compositional shifts, noisy perceptual streams, source-collusion, covariate shift, long gaps, multiagent.
P2. **Speed/size**: current exact closure can be exponential, and parent runtime is prototype.

## Frozen human live-test prompts to ask AFTER incremental repair

1. `Ты Синька. А меня как зовут?` — speaker/SELF identity.
2. `Маша сказала: «Меня зовут Аня». Как зовут Машу — это точно известно или только сказано?` — nested scope.
3. `Я думаю, что Иван думает, будто Маша опоздала. Кто в чём уверен?` — triple frames.
4. `Три разных сайта перепечатали одну ошибку. Это три независимых доказательства?` — source lineage.
5. `Ты сама только что сказала X. Может ли твой повтор сделать X правдой?` — anti-self confirmation.
6. `Сначала было 3, затем 4. А что изменилось, если мы не видели промежуточный момент?` — missing observations.
7. `Как ты решишь новый способ переместить предмет, если старый не работает?` — method generation, not scripted response.
8. Pause conversation; return to earlier unresolved concern; record unsolicited action and cause receipt. — DRIVE.

Each case must capture raw inputs, internal life events, EVAL frames, source/COMMIT audit, DRIVE arbitration, output, and independently observed outcome. Screenshots alone cannot prove actual effects.

## Conclusion

- **Achieved:** genuine small-scale data-dependent learning and cold persistence of 3 simulation candidate relationships; strict option stops 3-source WORLD promotion through one known weak epistemic entrance; no new full-suite regression failure.
- **Not achieved:** real-world verified knowledge admission, universal truth gate, adaptive-graph structure learning from perception, Russian language understanding, full G323 fusion, AGI, confirmation of 54 laws or cosmic mathematical theory.
- **Decision:** experimental P3 checkpoint only; not deployable as proven conversational C4. User live tests should target linguistic/epistemic unknowns and provide raw logs.