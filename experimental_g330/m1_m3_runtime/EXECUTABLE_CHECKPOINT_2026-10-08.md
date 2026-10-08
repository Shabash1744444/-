## STATUS UPDATE — CODE IS REAL, LIBRARY ZIP IS COMPLETE

The full tested source was saved in a ZIP to ChatGPT Library at `/C4_Code/C4_EXECUTABLE_COGNITIVE_CORE_M1_M3_2026-10-08.zip`. ZIP validation verified 11 entries, CLI included, SHA256 `4578bdd764e174e2c8b8a963cf864fea6df06b54e0c658caeee74fa1d26bb1d1`.

**GitHub sync status:** the paths `C4_EXECUTABLE_COGNITIVE_CORE/c4core/kernel.py`, `c4core/__init__.py`, `tests/test_kernel.py`, `demo.py`, README, example JSONL and test logs were physically committed and read back. **The `c4core/cli.py` GitHub file upload was blocked**; it is present in the complete saved Library ZIP. As a result the GitHub-only checkout is NOT claimed fully executable/tested as-is. Execute the ZIP, not an incomplete GitHub-only checkout. Do not infer the other file's contents as full from manifest alone.

---

# C4 M1–M3 — ACTUAL PYTHON EXECUTABLE CHECKPOINT (2026-10-08)

**STATUS:** EXPERIMENTAL PYTHON CODE EXECUTED; **28/28 local pytest checks PASS**; runnable demonstration and JSONL command loop checked. **NOT** AGI, not production C4, no G309/G329 model migration, no Android integration.

## Physical saved artifact (persistent ChatGPT Library)

Full source ZIP physically uploaded and confirmed:
- Library: `/C4_Code/C4_EXECUTABLE_COGNITIVE_CORE_M1_M3_2026-10-08.zip`
- Library stable ID: `libfile_39c1c949e28c819186013e7c9b87e544`
- ZIP bytes: `21,339`
- ZIP SHA256: `4578bdd764e174e2c8b8a963cf864fea6df06b54e0c658caeee74fa1d26bb1d1`
- The ZIP includes **actual source** `c4core/kernel.py`, `c4core/cli.py`, `c4core/__init__.py`, `tests/test_kernel.py`, `demo.py`, `example_session.jsonl`, `README.md`, `C4_STATE_EXAMPLE.c4j`, `TEST_RESULTS.txt`, `DEMO_OUTPUT.txt`, `SHA256SUMS.txt`.

This markdown is a GitHub **checkpoint/pointer**. The actual source ZIP lives in persistent Library, **not** yet GitHub blobs. Never confuse those; to edit/push code, materialize that ZIP using the Library file ID. Do not invent source URLs under this repo. The user also received a sandbox link to the generated ZIP in the originating conversation.

## Tested executable behaviors

- `Event` append-only in-memory event ledger (parent causal edges; received vs claimed time).
- Recursive `Perspective` (actor/holder, multiple BELIEF/QUOTE/etc. nesting) over `Proposition`, scoped scene queries.
- EVAL builds candidates; does not automatically change recognized truth.
- COMMIT admits sourced narrative/simulator claims, downgrades unsupported WORLD assertion, checks original roots, deduplicates dependent replays, handles audited retraction.
- DRIVE chooses among competing `ASK|THINK|WAIT|ANSWER|SENSE|...` actions; tick may initiate question independent of user.
- MEDIATE enforces DRIVE authorization, keeps `SENT` separate from `DELIVERED`, plus a mockable sensor `sense()` that requires an adapter callback and returns an explicit receipt. This does **not** authenticate real physical sensors.
- Read-only typed query with provenance and scope. Unsupported = UNKNOWN, not fabricated world fact.
- Limited unary relational `learn_example` induction: two distinct rooted demonstrations → tentative read-only inference for unseen entity, local negative example suppresses that inference, no WORLD truth escalation.
- Prevents external caller injecting `C4 ASK` directly and falsely populating C4's own-question memory.
- Deterministic trace OFF/DEEP cognition, SHA256 JSON checkpoint with atomic write/restore.
- Interactive JSONL CLI persists after commands: `python -m c4core.cli --state my_brain.c4j < example_session.jsonl`.

## Tests

Actual recorded local test run:

```text
............................       [100%]
28 passed in 0.05s
```

Additional demo output verified:
```text
Что думает Маша? -> SUPPORTED ... receipt: SENT
Что произошло по рассказу? -> SUPPORTED ... receipt: SENT
Это доказательство во внешнем мире? -> UNKNOWN () receipt: SENT
Автономный цикл -> SENT собственные вопросы: ('Что такое температура?',)
Следующий цикл -> INTERNAL
Новый предмет по двум демонстрациям -> INFERRED
Факт в реальном мире? -> UNKNOWN
Cold restore: True ; events: 12 ; claims: 4
Owners: ['COMMIT', 'DRIVE', 'EVAL', 'MEDIATE'] ; trace records: 44
```

## Restrictions that must stay explicit

This is the **structured cognitive skeleton**, **NOT** a trained Russian conversational model. Input is currently structured Python or JSON, not general free-text language. Learner only covers simple unary relational induction; not open-ended autonomous training. The legacy C4M, trained corpus, live GUI, Android video/audio and full empirical G329 RED turn replay are not integrated. 28 unit/integration tests are NOT proof of intelligence.

New chat should materialize the exact Library ZIP, verify its SHA256, unpack, run `python -m pytest -q tests`, inspect the code and extend the executable skeleton rather than writing another paper. Preserve existing old weight archives separately.

## Immediate next technical work

1. Replace public mutable in-process interfaces with stronger validated transactions and immutable snapshot manifests.
2. Language-to-frame Russian parser/learner for current-event scenes; benchmark C4 G329 RED on unseen names.
3. Integration of existing C4 learned vocabulary/graph as source-scoped migration, never blindly WORLD.
4. Add multi-place causal inference, event-time belief revisions, predictive action loops, regularity induction with independent source roots.
5. Real sensor/PC/Android boundary and 100-day simulated lifecycle tests.

**Code artifact exists and was tested; repository currently contains the checkpoint while bytes reside in verified Library.**
