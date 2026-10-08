# CP C4 G323-P9 — Recursive Perspective / Presence Frames

Date: 2026-10-08
Status: **PHYSICAL GREEN CANDIDATE / NOT CANONICAL**.
Parent: G322-P8 candidate. Last canonical baseline: G309/G309.

## Physical code delta
- `runtime/c4child/perspective.py`: bounded recursive perspective recognizer, arbitrary-depth tree, nested quotes/reported speech/thoughts, witness vs actor.
- `runtime/c4child/semantic_spine.py`: `C4_SEMANTIC_SPINE_V0_3_RECURSIVE`, evidence-rooted non-authoritative frames, persistence and self-review candidates.
- `runtime/c4child/runtime.py`: event reception creates frames; EVAL proposes revisions to unsent public acts, DRIVE selects; published acts cannot be retrospectively rewritten.
- `runtime/tests/test_g323_recursive_perspective.py` and `runtime/tests/test_g323_cold_artifacts.py`: frozen cases.

Scope limitation: bounded Russian surface recognizer, not general natural language comprehension. No automatic irony/post-irony inference; the frame model can carry unresolved nested pragmatic interpretations.

Invariant: nested representation != independently verified world fact. SELF output/replay never creates independent evidence. Existing four-law constitution and graph state preserved.

## Tests
- New G323 frozen structural + cold tests: **17/17 PASS** from extracted combined ZIP.
- Full extracted-package test suite: **505 PASS / 27 FAIL**. The 27 are missing historical model fixture files; same failed-test identities as unchanged G322, tested in same environment.
- Original G322 in same environment: **488 PASS / 27 missing historical fixtures**. Therefore no new regression assertion failure was observed, but whole suite is NOT fully green.
- Cold c4m and SQLite round-trip verified. Graph: 10,727 entities / 10,781 facts / order 22,306; STRICT.

## Exact physical release (local session)
- `child_g323_p9_recursive_perspective_candidate.c4m` 2,001,406 bytes; SHA256 `db2da315543db6ee306a2a8a2eaefc4a9ca504bfa5eac3fe7b88deea9ac3338c`.
- `C4_RUNTIME_G323_P9_RECURSIVE_PERSPECTIVE_CANDIDATE_2026-10-08.zip` 357,788 bytes; SHA256 `ab36fb566937c1d620464a95617e71724f8d3e21bc5a9f9af31e5641aa3fda71`.
- `C4_G323_P9_RUNTIME_PLUS_STATE_CANDIDATE_2026-10-08.zip` 2,337,573 bytes; SHA256 `52574c7a6999d880855658e02b01cdefd5808ab2767bd9c0d1aaf9736064dc3b`.

Artifact files physically exist in the originating chat's sandbox. Do not assume binaries are available in a future chat until successfully copied to persistent Library; Library binary upload in current environment was unavailable. Verify exact hashes before using.

The release model was exported from G322 without injecting synthetic test dialogue. Retrained graph/world weights: none.

## Separate fifth law
See `C4_FIFTH_LAW_INTELLIGENCE_NON_CONSTITUTIONAL_2026-10-08.md` for Ruslan's new, **non-constitutional** target definition: intelligence solves nonstandard problems by nonstandard methods. This is a capability criterion, not a bypass of the four laws.

## Next
Retain G321 frozen replay and G314-G322 tests. Test live-derived nested-perspective edge cases (cross-event coreference, mixed quotes, irony) before promoting. G324 may model plans/expectations and time triggers when G323 scope is bounded and persisted.