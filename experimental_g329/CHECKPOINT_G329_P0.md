# G329-P0 — STRUCTURAL INQUIRY LINK + CAUSAL CASCADE AUDIT

Date: 2026-10-08. Status: **PRE-LIVE RESEARCH CANDIDATE, NOT CANONICAL**.
Parent: G328-P0; weights unchanged from G326/G327/G328. C4 core `Shabash1744444/-`; Android host `Shabash1744444/Emu`. Four owners not modified. Five influence classes unchanged.

## Required methodology (from C4 and Singularity)

`research -> structural causal synthesis -> frozen counterexample -> minimal general repair -> re-attack -> full regression -> cross-domain cascade -> cold reload -> physical checkpoint -> live`. No lexical answer-keys, benchmark phrases, imitation of hidden reasoning or prompt-only fixes. Inspect `INPUT -> EVAL candidate -> COMMIT/admission+scope -> DRIVE arbitration -> MEDIATE/actual boundary -> state delta -> future cognition` and preserve IDs.

## Architectural changes

1. `episodic_memory.py`: quote-aware direct questions, query transactions for multiple directly addressed questions rather than arbitrary threshold >=3, C4 ASK-memory queries over actual source IDs, calibrated lexical retrieval and C4 own REPLY history. A memory of a user test-question is *not* an observation of the hypothetical story.
2. `inquiry_link.py`: EVAL-only alignment among **all** open questions; returns candidate IDs or AMBIGUOUS/NO_MATCH/NOT_ANSWER. Attach `answer_candidates` to the selected inquiry as `UNVERIFIED` with external source event ID; don't set RESOLVED or WORLD truth. No latest-question privilege. Topic-independent.
3. `runtime.py`: read-only origin-aware indexing of actual C4 asks/replies; explicit `EVAL_INQUIRY_LINK`; legacy pending_ask single-focus protection with release only for a uniquely contextualized anaphoric exchange. A trial strict mask initially broke six historical teaching tests, so repair broadened only on *causal resolution of competing focus*, NOT fixed words or names. Old `dialogue.py` natural teaching remains operational.
4. `CASCADE_OUTCOME` row on each processing pass includes actual fact/entitiy delta IDs, graph order, inquiry changes, and public event/transaction refs. Native trace API from G328 remains supported, opt-in and observational.

## Falsification work

- Negative #1: G328 returned NO_EVIDENCE to real C4's 3 old asks; G329 lists the spoken text and OPEN status after same .c4m initialization.
- Negative #2: one old query-exam cache was treated as story testimony. G328 had partial protection; G329 preserves QUESTION vs C4_ASK vs C4_REPLY vs USER_MESSAGE.
- Negative #3: old G328 could bypass 3-question batch for two direct questions. G329 treats 2+ direct asks as a non-teaching compound; nested questions inside quotes do not become user direct questions.
- Negative #4: naive pending-ask masking damaged 6 existing tests (`test_g270_store`, `test_g275_live_teaching`, `test_g310_four_laws_dialogue_lifeline`). After source-level diagnosis of anaphoric links and already answered older inquiries, targeted rerun recovered 26/26, final whole suite restored all six.
- Negative #5: `Какие твои вопросы ещё без ответа?` without 'помнишь' initially bypassed typed inquiry retrieval. Fixed via typed ASK intent and passed clean cold ZIP smoke.

## Metrics and validation

- 61/61 directed checks PASS across G328+G329 suites, including never-seen Russian nouns and real graph link invariants.
- Full pytest: **715 PASS / 27 FAIL**; all 27 `FileNotFoundError` from absent historical checkpoint fixtures (not assertion regression). Previously G328: **667 PASS / 27 FAIL**.
- Exactly same clean trained organism bytes as G328: 2,065,628; SHA256 `dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f`.
- Cold Android import simulation: 55 Python modules extracted, model opened via `load_c4m_compact`, 7 studies preserved, native `TRACE_CONFIG` succeeded, 10 TRACE events, 3 C4 asks and a source-linked earlier answer candidate survived save/restart. This is **not hardware execution**.
- G328/G329 same 11 dialogue turns real trained model: G329 recovered real 3 C4 ASK events vs G328 unknown. Normal teaching one source asserted fact adds +1 fact/+1 entity in **both**; no extra graph mutation from the inquiry/memory prompts. Some complex Russian history remains not understood; no claim of comprehensive semantic model.

## No-hardcode classification

Runtime still has ordinary bootstrap Russian lexical/grammar patterns (a known limitation), but these updates introduce **no fixed names, no correct-answer table, no banned phrases or impossible-to-learn topic walls**. Multi-episode grouping and ASK event types are generic causal structure. Source-backed quotation and conservative uncertainty are not artificial answer constraints. Check composition effects on normal teaching explicitly.

## Known limitations / next gate

- Source memory and lexical matching do **not** equal broad semantic understanding. Free text may still fail and needs a future general structural learner.
- Multiple direct questions are processed read-only with bounded public response; true dynamic chunk streaming is not yet complete.
- `ANSWER_CANDIDATE` does NOT close the knowledge gap or prove independent correctness; lawful source-aware transfer tests and authenticated receipt still missing.
- Open/inactive question budgets remain future DRIVE utility optimization, not a semantic law.
- Training seven causal studies stays simulated; threshold-shift transfer still bad. Do not mistake read-only restraint for positive reasoning.
- Tests do not include actual phone ARM64 runtime, network, microphone/camera, 3D physical receipts or human-private corpus review.

**Next device gate**: install separate G329 runtime ZIP and unchanged clean `.c4m` through existing Emu APK, run the frozen short multi-turn test individually (not 28 questions at once), enable DEEP/NEXT_INTERACTION, verify trace status and saved-state continuity, export C4 Nursery chat+logs and compare graph and inquiry event IDs. Do NOT canonize until physical run, actual logs, and unchanged regressions.