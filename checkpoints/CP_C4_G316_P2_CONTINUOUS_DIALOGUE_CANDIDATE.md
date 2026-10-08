# C4 G316-P2 — CONTINUOUS DIALOGUE / LIFE-LINE CANDIDATE

Status: CANDIDATE / NOT CANONICAL
Date: 2026-10-08
Parent: G315-P1 scope-aware truth over exact G309 semantic state.

## Purpose
Move dialogue away from request/response physics and make it a view over one continuous life-line while reusing existing vocabulary through semantic context.

## Added
- `receive_user_event()` records an external event only; it does not parse, mutate the graph, or reply.
- `cognitive_step()` processes pending input later under DRIVE.
- `user_message()` remains a compatibility wrapper, not the cognitive law.
- one persistent `life_events` line contains external receive, cognition, interpretation, speech-act choice and public reply events;
- semantic context is read-only and changes AVAIL/VALUE for retrieval, never COMMIT authority;
- explicit user mentions outrank derived reply objects for later reference;
- pronoun resolution uses recent semantic/parser focus but does not create facts;
- known predicate/verb forms are excluded from nominal pronoun candidates;
- learned communication-action family supports generic topic proposals (`давай <action> про <topic>`) rather than one hardcoded sentence.

## Minimal language growth
Strict BootstrapTeacher with explicit `LANGUAGE_CONVENTION` basis added only:
- `поговорить IS_A глагол`;
- `поговорить WORD_FORM поговорим`;
- `поговорить WORD_FORM поговорили`;
- `поговорить USED_FOR общение`;
- one supporting language relation needed by the dialogue family.

These are knowledge/language relations, not WORLD observations.

## Exact state
- entities: 10,721;
- facts: 10,769;
- order: 22,288;
- model bytes: 1,993,412;
- model SHA256: `8849948f36908b45e7875fcae2910693390688d9bddd4c555bfe78bdffd4f825`.

## Validation
Focused P0/P1/P2/context suite: 29/29 PASS.
Full regression: 456/475 PASS.
19 failures are unchanged FileNotFoundError cases for unavailable historical model/fixture paths.
New semantic/runtime assertion failures: 0.

## Cold re-attack on exact G316 state
- constitutional mode survives reload: STRICT / C4_CONSTITUTION_V1;
- `Радиация -> излучение` remains available as knowledge;
- `поговорить / поговорим / поговорили` remain reusable language knowledge;
- `Что ты знаешь про радиацию?` -> `Радиация — излучение.`;
- `Давай поговорим про излучение` -> topic speech act;
- `О чем поговорим?` reuses current life-line topic;
- follow-up `А что с ней связано?` uses semantic context without graph mutation;
- `receive_user_event()` produces PENDING with no reply and no graph mutation;
- after cold save/reload the topic/context still resolves.

## Boundaries
CONTEXT != TRUTH.
RECENCY != REFERENCE IDENTITY.
MESSAGE_RECEIVED != COGNITIVE_PROCESS.
COGNITIVE_PROCESS != PUBLIC_REPLY.
SPEECH-ACT VALUE != DRIVE DECISION.

## Next
P3: bind a small amount of AUDIO/VISION/SYMBOL experience to the same semantic units and episodes while preserving modality separation and the constitutional gate.
