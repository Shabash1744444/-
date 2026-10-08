# C4 G327 — REAL ANDROID DUAL-STRESS AUDIT (2026-10-08)
Status: RED / LIVE INPUT. This is analysis of user-supplied live transcript, **not** synthetic automated test result.
Host: Shabash1744444/Emu (Android C4 Nursery); experimental core: G327. Distinguish runtime evidence and app UI evidence.

## Input condition
The user sent two lengthy sets of 28 natural-language stress questions, second with simplified vocabulary, and supplied one long C4 output corresponding to each. The answers are not verified via native trace; the app previously displayed C4 RUNNING, 5.6 MB transport trace, 0 B cognitive trace and RUNTIME UNSUPPORTED.

## Observations: first output
1. Retrieves general topics instead of solving questions: 'знание — информационный объект', 'думать — глагол', 'буква И — гласная буква'.
2. Echoes topical content and invites 'Скажи «подробнее»', rather than maintain explicit per-question focus.
3. Candidate teaching despite an exam-only context: 'Запомнила: изменение — когда состояние чего-либо становится другим.' Must inspect **actual** COMMIT graph delta and scope, not infer WORLD mutation from reply alone.
4. Incorrect extraction of event facts from a hypothetical temporal utterance: 'Приняла как твоё утверждение: Сегодня наступило — завтра.'
5. Useful distinction: quoted material is only example; USER_SAID is not verified physical-world fact; the output says no independent sensory evidence.

## Observations: second output
1. Repeats irrelevant lexical retrieval: 'буква И — гласная', 'буква В — согласная', 'думать — глагол', 'есть — действие'.
2. Dangerously lossy learning extraction: 'Запомнила: когда состояние чего-либо становится другим, растаял; стал водой.' A conceptual scenario became a broken relation.
3. Role and time collapse in simulation: 'Приняла как твоё утверждение: Вчера ты думала, что кошки может летать'; 'Сегодня увидела, что кошка не может летать'. In the question, these were *imagined events about C4*, not verified autobiographical episodes. Check scope of stored claims.
4. Source-following partially correct: 'Маша услышала — от Пети', 'Иван услышал — от Маши' remain source claims rather than confirmed WORLD observations.
5. Some answers do cite actual corpus identifiers (RU_DISCOURSE_TRANSFER, KARAMAZOV_BOOK3_CH9), showing provenance channel exists, but retrieval and task relevance are not assured.
6. Self-audit inconsistency: 'Мне нечего обосновывать: в прошлом ответе я не опиралась на свои знания' among many retrieved/cited knowledge statements. Could be local subevent history pointer failure; needs trace confirmation.
7. Negative outcome: cannot answer causal alternative explanations, instead 'Не знаю, почему так могло случиться' even when elementary reasoning over scenario would have been possible.

## Source inspection in GitHub: G327 mechanisms implicated

`experimental_g327/runtime/c4child/discourse_bridge.py`:
- `_Q_ACT`, `_Q_WHO`, `_Q_TRUTH`, etc. are *anchored surface regexes*. A recognized small form (e.g. 'Что думает Маша?') has specialized source-focused read-only handling; much of the 28-question long batch falls back to inherited lexical/context retrieval.
- `resolve_disposition` returns preformatted answers, not trained generalized semantic induction.
- The G326→G327 patch changes quote-aware punctuation segmentation in `runtime.py`, not general episodic dialogue understanding or comprehensive sentence semantic parsing.
- The last checkpoint explicitly acknowledges `dialogue.py`/Russian morphology still inherited, new complex pragmatic/temporal forms limited, and **no new training in G327**.
- Android `Emu/app/src/main/python/c4_mobile_bridge.py` supports TRACE_CONFIG and TRACE_SNAPSHOT via optional feature detection. G327 does not implement full native cognitive trace API, so UNSUPPORTED is accurate; transport log is not a cognitive ledger.

## Preliminary four-owner interpretation
EVAL: FAIL in whole-scenario frame construction, episodic segmentation and goal-relevant hypothesis evaluation; same surface terms drive unrelated answers.
COMMIT: PARTIAL containment, source-vs-WORLD distinction in some responses; **RED FLAG**: 'Запомнила' for assertions/exam examples, scope/source and future graph mutation unknown without the actual delta.
DRIVE: FAIL/INSUFFICIENT EVIDENCE for response selection/prioritization among 28 questions and whether open ASK items are preserved. Many topical auto-replies, weak 'none matches' capability.
MEDIATE: Android RUNNING and transport messages confirmed by UI; no model-native event-by-event TRACE yet. No claim of tested cognitive chain.

## Key falsifiable root-cause hypothesis
**Absence of a first-class episode / question / teaching / example / hypothesis transaction for each clause and of graph-grounded matching to open question intents** causes both irrelevant retrieval and accidental self-learning. A unified repair should handle:
1. `QUESTION`, `TEACHING`, `SIMULATION`, `QUOTE`, `CORRECTION`, `COMMAND`, and `UNKNOWN` as CANDIDATE interpretation types with probabilities/alternatives; no hard-coded recognition for specific object names.
2. Cross-clause and nested scope; retain text spans and sender/source roots.
3. Map any response to a specific open ASK via source/event references, without automatically choosing the last ASK; allow AMBIGUOUS/NONE.
4. EVAL candidate formation ≠ COMMIT: tests, stories, hypothetical samples, quoted instructions may not update WORLD/SELF_AUTOBIOGRAPHY without explicit legitimate evidence.
5. Read-only cognitive telemetry TRACE_CONFIG/SNAPSHOT + event-linked EVAL, COMMIT, DRIVE, MEDIATE; tracing should not mutate cognition.

## Required next instrumented reproduction
1. BACK UP the test organism as a separate C4M; do not promote or use its unchecked mutations as canonical training.
2. Export Android **«Выгрузить чат + logs»** and identify exact USER_MESSAGE boundaries (one bulk message vs several), REPLY/ASK events, elapsed time, runtime step and source event IDs.
3. Compare graph BEFORE and AFTER: new entities, facts, statuses, scopes, evidence roots; especially ‘сегодня наступило завтра’, fictional cat flying, and ‘изменение’ relation.
4. Test in separate *individual* turns:
   a. 'Величину можно измерить. Например, длину.'
   b. 'На какой из твоих вопросов я ответил?'
   c. 'Какие твои вопросы ещё открыты?'
   d. 'Я расскажу историю: Маша думает, что кошка летает.'
   e. 'Это факт мира, её мысль или просто пример?'
   f. 'На вопрос об излучении я пока не отвечаю.'
5. Repeat same prompts with same initial checkpoint and randomized word substitutions; compare responses and graph changes with any patch against G327.
6. Flag all cases where the app claims RUNNING but TRACE_CONFIG unsupported; do not reconstruct fake cognition from response text.

## Release decision
G327 APK live transport = physically observed RUNNING, but dialogue is **RED** for independent 28-question comprehension/learning isolation; do not canonize. A new generic event-centered reasoning/learning boundary and native diagnostic support are the next gates. Do not simply add 28 special handlers or memorize test answers. This report is a checkpoint of real observations, NOT implemented repair.
