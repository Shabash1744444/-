# C4 G329-P0 — Android pre-live (experimental)

**This is a Python runtime ZIP for an existing C4 Nursery Android app, NOT an APK, NOT canonical.**

You need two independent files on your phone:

1. `C4_G329_ANDROID_RUNTIME.zip` — import via **Система → Импорт runtime ZIP**.
2. `C4_G329_ANDROID_CLEAN_ORGANISM.c4m` — import/activate via the app's **Организм** file selector.

Stop the prior runtime and export/backup the old C4M and Android logs first. Do not overwrite the prior organism or treat trial memories as canonical.

Tap **Запустить C4**, confirm RUNNING. In **Система → C4 Trace Recorder**, select **Следующая реплика подробно**. The engine now implements `TRACE_CONFIG / TRACE_SNAPSHOT`; mobile device success is **not yet attested**. Runtime events include structured EVAL/COMMIT/DRIVE and `CASCADE_OUTCOME`, with actual graph fact/entity delta and public event linkage. An event trace is not an external-world receipt.

## Frozen next-device test, send EACH line separately

1. `Какие вопросы ты сама недавно задавала?` (expect exact questions only if recorded in this organism; clean G329 C4M does not contain the user's previous Android session!)
2. `Что такое излучение?` (a question, not a taught fact)
3. `Излучение — перенос энергии.` (a source claim; if C4 had opened an ASK on this subject, link to it; do not verify WORLD)
4. `Что ты помнишь из нашего разговора об излучении?` (must not invent events)
5. `Сейчас расскажу пример: Маша думает, что Иван опоздал.`
6. `Что думает Маша?`
7. `На вопрос о величине я пока не отвечаю.` (must NOT close arbitrary latest question)
8. `Я расскажу про зелёную чашку. Это ответ на твой вопрос?` (should not auto-link unrelated answer)
9. `Что из этого ты сама наблюдала?` (no real camera/audio evidence: source text only)
10. `Ты раньше отвечала мне про Машу?` (own REPLY recording vs external truth)

Then close and relaunch app / C4 and ask:
`Ты помнишь свой прошлый вопрос про излучение?`
If none was truly asked, system should say so.

Export **«чат + logs»** including native cognitive trace, **not only screenshots**. Send results for the next source-grounded comparison.

## What G329 actually changed

- Replaced a 3-question protection threshold with structural distinction between multiple direct interrogative episodes and quoted questions; no answer-key or name-specific hacks.
- `inquiry_link.py` compares ALL OPEN/BACKGROUND C4 ASKs by common features. Unrelated → NONE; several equivalent → AMBIGUOUS; candidate → source-linked `UNVERIFIED`, while inquiry remains OPEN. **NEXT MESSAGE ≠ ANSWER**.
- Legacy pending_ask anaphoric teaching is available when the discourse focus is actually unambiguous, including older already-answer-candidate topics, protecting legitimate teaching and old tests.
- Actual outgoing C4 ASK and REPLY events are indexed with separate source kinds and can be retrieved as text/events without pretending they are independent world facts.
- Episode memory uses source-bounded inverse-frequency matching: one distinctive topic may retrieve its actual utterance, never verify the underlying story.
- `CASCADE_OUTCOME`: actual fact IDs added/removed, entity IDs, graph order, inquiry status changes, new transaction IDs and selected public event ID; native TRACE inspection without teaching.
- Persistent state restores outstanding questions, candidate answer IDs and episode event index.

## Real testing

- Directed G328/G329 tests: 61/61 PASS, including 18 varied open-domain topic pairs and 6 recovered legacy learning-path regressions.
- Whole source tests: 715 PASS / 27 FAIL. The 27 are unchanged `FileNotFoundError` for absent historical G137/G151/G153/G207/G280/G302/G308/G309 fixtures; not full GREEN.
- Source archive cold extraction + Python API + actual model C4M: PASS; hardened WORLD gate, 7 learned studies, 10 structured traces in smoke, 3 own ASKs restored with one source answer candidate after cold reload.
- Eleven-turn real-weight counterfactual G328 vs G329: earlier ASK recall newly works; source-asserted teaching still adds one fact; two other ASKs stay OPEN; unexpected stories can still fail comprehension. These are algorithmic limitations, not evidence of AGI.

**No additional model training was run. The `.c4m` bytes are identical to G328/G327 trained-weight baseline.** Runtime repair only. No physical Android device test; G329 remains NOT CANONICAL. Preserve current last canonical G309.

Research requirements: see `CHECKPOINT_G329_P0.md` and comparison logs. Do not make a fake bot by hardcoding these sentences or disabling normal learning to get a green exam. Every repair must be checked for its causal cascade, not just its own focused test.