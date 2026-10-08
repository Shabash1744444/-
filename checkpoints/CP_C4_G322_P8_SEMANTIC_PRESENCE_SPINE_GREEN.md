# C4 G322-P8 — SEMANTIC / PRESENCE SPINE GREEN CANDIDATE

Status: **GREEN CANDIDATE / NOT CANONICAL**
Date: 2026-10-08
Parent: G321-P7 LIVE REPLAY GREEN candidate.

## Purpose
Add a non-authoritative semantic/presence spine so C4 can represent one continuous event line:
who interacted, when, through which channel, what was literally received, which interpretations EVAL considered, what temporal/modal/quoted context applied, which operation DRIVE selected, and what status transition COMMIT/MEDIATE actually performed.

The spine is NOT a fifth law and has no authority to mutate truth.

## Four-law boundary
- EVAL may create arbitrary interpretation candidates.
- A spine interpretation may only request COMMIT eligibility; it cannot authorize COMMIT.
- DRIVE remains the sole action/publication arbiter.
- MEDIATE remains the boundary for external result/receipt.
- Existing constitutional gate remains the only truth mutation authority.

## New runtime structure
`C4_SEMANTIC_SPINE_V0_2`

Event envelope records:
- actor;
- channel;
- payload;
- internal causal step;
- external wall time;
- external order;
- event status.

Interpretation candidate records:
- source interpreter;
- speech act;
- SELF/OTHER subject role;
- relation/object;
- temporal scope;
- epistemic mode;
- quoted depth;
- confidence/status.

Presence snapshot is read-only and exposes:
- current internal step;
- external now;
- last external interaction event;
- elapsed real time since it;
- open/background inquiries;
- READY/BACKGROUND unsent public acts.

## Research counterexamples closed
1. Nested quoted retraction:
   `Проверим фразу: “Отзываю утверждение, что меня зовут Руслан”`
   -> QUOTED_SPEECH representation only; no state mutation.

2. Past name:
   `Раньше тебя звали Лира`
   -> PAST social interpretation; current NAME is not replaced.

3. Modal/hypothetical name:
   `Может, тебя зовут Север`
   -> POSSIBLE hypothesis; current NAME is not replaced.

4. Conflicting functional names:
   `Тебя зовут Лира и Север`
   -> ambiguity retained; no last-token / combined-string NAME commit.

5. Atomic deictic correction:
   `Не меня, а тебя`
   -> may rebind ONLY the value from one concrete prior source-owned NAME claim.
   The correction cannot invent a new name.
   The old binding is tombstoned and the corrected binding is linked by one audited transaction.

## Structural finite test
All 2048 combinations across:
- 4 source classes;
- quoted / unquoted;
- 4 temporal scopes;
- 4 epistemic modes;
- 8 speech-act classes;
- SELF / OTHER roles
were checked.

Only 24 structurally eligible combinations may even REQUEST COMMIT.
Eligibility is not COMMIT authority.
Quoted/question/hypothetical/non-current functional-name interpretations never request current-state COMMIT.

Result: 2048/2048 structural checks PASS.

## Exact G321 re-attack
On exact G321 state:
- nested quote safely represented;
- past and hypothetical names preserve current social state;
- multiple current names remain ambiguous;
- atomic `не меня, а тебя` transaction reuses the prior value and invents nothing;
- presence reports external elapsed time independently from internal step.

## Frozen G321 live replay under G322 runtime
Historical G321 bad-conversation replay remains:
`FINAL_FROZEN_REPLAY_GREEN`.

Preserved:
- process -> change HUMAN_TEACHING knowledge;
- WORLD remains UNKNOWN for human teaching;
- cat -> elephant remains UNKNOWN and source assertion retracts;
- USER/SELF social names remain correct in frozen replay;
- no smiley/opaque-tail entities;
- inquiry status survives cold reload.

## Persistence
Nonempty SemanticSpine survived c4m save/reopen:
- event envelopes persisted;
- interpretation candidates persisted;
- external elapsed-time presence remained computable;
- pending public acts remained visible;
- STRICT constitution persisted;
- semantic graph stayed 10,727 entities / 10,781 facts / order 22,306.

## Validation
Focused G310 + G314-G322 constitutional/dialogue/lifeline stack from extracted package:
**74/74 PASS**.

Full extracted-package suite:
**496 PASS / 19 FAIL**.
All 19 failures are FileNotFoundError for the same unavailable historical model/fixture paths.
New semantic/runtime assertion failures: **0**.

## Exact candidate state
Graph:
- entities: 10,727
- facts: 10,781
- order: 22,306
- constitutional mode: STRICT
- constitution: C4_CONSTITUTION_V1
- composition: 6 units / 5 links
- sensory concepts: 16

Model:
- `child_g322_p8_semantic_presence_spine_candidate.c4m`
- bytes: 2,001,382
- SHA256: `6baf2864ce8a811738d13cf3593f739e8dcc5a8734d17ce0f5647bc23da06301`

Runtime:
- `C4_RUNTIME_G322_P8_SEMANTIC_PRESENCE_SPINE_CANDIDATE_2026-10-08.zip`
- bytes: 352,437
- SHA256: `dd9e087c598b6c44472446a45eb02f9b51e9dcf389c927f9562499bae25cad8c`

Combined:
- `C4_G322_P8_RUNTIME_PLUS_STATE_CANDIDATE_2026-10-08.zip`
- bytes: 2,333,879
- SHA256: `be7308d40d7796b3f3818c63c73555202e0d23620b7022f056f282d688d59a3e`

## Important limitation
The spine now REPRESENTS temporal/modal/quoted/social structure, but natural-language extraction remains intentionally bounded. P8 proves that a correct structure cannot bypass the constitution; it does not prove broad free-form language understanding.

## Next
Before promoting beyond candidate:
1. bind plans/expectations and unresolved goals into the same presence line without creating chat locks;
2. add third-party reported speech / speaker attribution into the same spine;
3. use agent-development transcripts as episodic training with CLAIM / HYPOTHESIS / TEST / RESULT / CORRECTION scopes;
4. perform new Android live test from a clean copy and freeze every failure.