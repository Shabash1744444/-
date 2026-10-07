# NEXT CHAT HANDOFF — C4 G279 WEIGHTS + G278 RUNTIME

## Exact weights
- child_g279_guided_prose_core_green.c4m
- 1826213 bytes
- SHA256 2e9aa26a12ee40210dd465335a3f48865e133728b6f99e95f3d2b821a7444d17

## Exact runtime
- C4_RUNTIME_G278_GUIDED_READING_GREEN_2026-10-07.zip
- 1082920 bytes
- SHA256 009e33fb61aa7d173c1e5489d60dd19f50c2fd4bfded2f0ef98e029cc2e558ef

## Combined
- C4_G278_RUNTIME_PLUS_G279_WEIGHTS_2026-10-07.zip
- 2893848 bytes
- SHA256 eb810e3e440efab882be904c2360f5b38e3352450e13ad64f8cf4603a2b10e13

Persistent recovery: /C4_Canonical/.

## G278
Conservative short-prose reader:
- supported deterministic sentences -> EXTERNAL_CORPUS;
- unsupported sentences skipped;
- repeated compound classes preserved;
- class-definition gaps feed ActiveGaps;
- external text isolated from live-dialogue pending state.

During red-team a stale open question caused unrelated prose to be interpreted as its answer. That was fixed before GREEN.

Regression: 328/337; same 9 missing historical files only.

## G279
63 ordinary Russian sentences.
58 members across 5 repeated classes.
5 ActiveGap teacher answers / 15 words.
Hierarchy: 0/126 -> 126/126.
Shared purpose inheritance: 58/58 before teacher.
184 novel derived / 68 direct = 2.706.
Cold reload GREEN.

Cumulative:
260/260 nouns; 756/756 verbs; 780/780 adjectives; 472/472 G274; 78/78 G277; 184/184 G279.

## Next
Quality first.
Do not guess lemmas from inflected unknown words.
Next reader work should address terms inside action/predicate clauses only if lexical normalization is ambiguity-safe.
In parallel, continue larger guided-text blocks using already safe constructions.
