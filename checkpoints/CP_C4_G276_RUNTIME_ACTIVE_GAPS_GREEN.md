# CP C4 G276 RUNTIME ACTIVE GAPS GREEN

Date: 2026-10-07
Status: GREEN
Parent runtime: G275
Weights changed: NO

## Goal
Reduce Teacher Cost by asking the gap with the highest expected downstream learning value instead of the first gap encountered.

## Runtime change
Learning agenda now ranks approximate expected learning utility per unit teacher effort.
- unique cause_ids represent independent downstream needs blocked by a gap;
- LearningTarget exposes expected_unlocks and estimated_teacher_cost;
- DEFINITION gaps participate in ranked TEACHER agenda;
- HUMAN mode preserves the old one-question/FIFO definition dialogue contract.

Ranking changes what C4 asks next. It does not change graph truth.

## Counterexample
Before G276, definition gaps were excluded from ranked agenda and could be asked FIFO even when another definition blocked much more downstream work.

## Teacher Cost benchmark
Disposable controlled benchmark, not saved into canonical weights:
- 12 held-out classification targets;
- low-value-first FIFO: 4 teacher answers to reach 75% competency;
- ActiveGaps: 2 teacher answers to reach 75%.

Teacher question burden at that threshold: -50%.

## Regression
Clean-unzip full suite:
- 321/330 PASS
- 9 unchanged FileNotFoundError cases for missing historical G207/G137/G151/G153 artifacts
- 0 new assertion/semantic/runtime failures

## Artifact
- C4_RUNTIME_G276_ACTIVE_GAPS_GREEN_2026-10-07.zip
- 281120 bytes
- SHA256 6a8e174e0d3e79bd90c04d66e55964b9c22feb16f5eb9d83f0724278506d2a17

## Boundary
G276 is the question-selection layer for GUIDED learning. Arbitrary raw long-text parsing is not yet claimed.
