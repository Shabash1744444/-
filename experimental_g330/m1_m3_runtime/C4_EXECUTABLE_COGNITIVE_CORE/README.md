# C4 Experimental Executable Skeleton M1–M3 (2026-10-08)

**Actual Python code, not a design-only document.** Experimental, separate from canonical C4; does not modify G309, G323, G329, C4M or Android. No dependency on OpenAI/LLM/cloud.

## Run

Python 3.11+:

```bash
python demo.py
python -m pytest -q tests
```

## Implemented and verified by tests

- Dataclass-typed append-only life-line and separate receive/event-time/causal-parent order.
- Recursive holder perspectives: arbitrary nested thought/quote/belief structures via typed `Perspective` and `Proposition`.
- EVAL-only hypotheses and scoped queries; learning-scoped SOURCE/STORY/SIM answers cannot be interpreted as verified WORLD.
- COMMIT-only recognized claim mutations with source roots; dependent relay copy keeps roots; explicit audited retraction.
- DRIVE selects actions among candidates and autonomously ASK/THINKs in `tick()`; no global pending question lock.
- MEDIATE requires drive authorization and tracks `SENT` vs `DELIVERED` (demo does *not* possess real physical-world receipt generation).
- Basic relational induction: two independent unary *demonstrations* induce read-only provisional inference; per-entity counterexample blocks overgeneralization. Not a general learning theory.
- Source-role memory: USER question about C4's asks is never indexed as C4 ASK.
- Deterministic read-only trace OFF/ON and cold JSON snapshot with SHA256 integrity + atomic rename.

## Known gaps (not cosmetic)

- Input to core is **structured**, not a free-form Russian conversation. A language organ that learns words, grammar, temporal discourse, intentions, irony, etc., remains future work.
- This M1–M3 implements a small learning operator, *not* broad self-training, continual gradient updates, open-ended common-sense inference or AGI.
- No real Android/PC transport, screen/audio/video, sensor receipts, GPU training, or full old C4M migration.
- In-process Python code with direct object access is not a security sandbox. External sensors/tools need trusted adapters and an explicit boundary protocol.
- Rules are very narrow unary structural patterns. They don't infer universal physics; synthetic examples are not independent physical evidence.

## Status

Requires test output + source/ZIP SHA and GitHub commit to be counted as a built experimental candidate. No pretense that an architectural skeleton alone proves general intelligence.

## Interactive JSONL runtime

```bash
python -m c4core.cli --state ./my_brain.c4j < example_session.jsonl
```

Each line is an independent typed event; output contains structured status, scoped evidence roots and action receipts. `--state` reloads from disk at start and atomically persists after each successful command. Run interactively by starting without the input redirection and entering one JSON command per line.

**Real-world observations:** `C4.sense(sensor_id, callback)` is a mockable adapter boundary. The caller is responsible for independently validating its sensor callback; the core itself cannot authenticate physical observations. Human/fiction assertions passed with `scope=WORLD` are downgraded to sourced claims.
