# CP C4 G278 RUNTIME GUIDED READING GREEN

Date: 2026-10-07
Status: GREEN
Parent runtime: G276
Weights changed: NO

## Goal
Read short ordinary Russian prose conservatively without converting parser guesses or live-dialogue context into world facts.

## Added
- `GuidedReaderRU` + `C4LivingRuntime.guided_read()`;
- sentence-by-sentence EXTERNAL_CORPUS admission through existing deterministic language organs;
- corpus first pass preserves repeated / explicitly defined adjective+noun class phrases as compound concepts;
- unsupported prose is skipped, not guessed;
- repeated members of an undefined class aggregate cause IDs into one ActiveGap;
- pure POS typing does not count as a semantic definition for guided reading;
- external reading is isolated from open live-teaching state;
- structured teacher events clear resolved pending definition prompts.

## Red attacks
1. re-resolved surface gap lost `reason` -> fixed;
2. stale `pending_ask` could make unrelated external prose look like its answer -> reader parsing isolated + resolved prompts cleared.

## Validation
Focused: 7/7.
Full clean suite: 328/337.
Only 9 unchanged FileNotFoundError cases for G207/G137/G151/G153.
0 new semantic/runtime assertion failures.

## Boundaries
GUIDED READING != arbitrary language understanding.
UNSUPPORTED SENTENCE != FACT.
OPEN CHAT QUESTION != EXTERNAL TEXT CONTEXT.
