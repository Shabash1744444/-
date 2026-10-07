# C4 COGNITIVE TRACE RUNTIME TASK

Date: 2026-10-07
Consumer: C4 Nursery 0.64.2+
Status: runtime integration task

## Goal

Expose structured, read-only diagnostic traces of C4 decisions without creating a free-form internal monologue and without mutating cognition.

## Commands

### TRACE_CONFIG
Payload:
{
  "schema":"C4_COGNITIVE_TRACE_V1",
  "mode":"OFF|EVENTS|DECISIONS|DEEP",
  "scope":"CONTINUOUS|NEXT_INTERACTION",
  "structured":true,
  "freeFormMonologue":false,
  "include":["OWNERS","INFLUENCES","CANDIDATES","EVIDENCE_ROOTS","PROVENANCE","GRAPH_DELTA","PUBLIC_EVENT_LINK"],
  "maxEvents":2500|10000
}

Runtime should return:
{
  "accepted":true,
  "mode":"...",
  "scope":"...",
  "traceId":"..."
}

Unsupported runtimes must return accepted=false / RUNTIME_CAPABILITY_UNAVAILABLE.

### TRACE_SNAPSHOT
Read-only diagnostic snapshot for the current active episode / life-line position.

## Output event

Runtime emits normal runtime events with type TRACE_EVENT.

Suggested payload:
{
  "schema":"C4_COGNITIVE_TRACE_V1",
  "traceId":"...",
  "episodeId":"...",
  "step":123,
  "wallTime":...,
  "owner":"EVAL|COMMIT|DRIVE|MEDIATE",
  "influence":"MASK|VALUE|AVAIL|TRIGGER|STATUS",
  "phase":"...",
  "operation":"...",
  "subject":"...",
  "candidateId":"...",
  "decision":"ADMIT|REJECT|DEFER|SELECT|SUPPRESS|REQUEST|VERIFY|...",
  "reasonCode":"...",
  "evidenceRoots":["..."],
  "provenance":[...],
  "graphDelta":{"added":[],"changed":[],"retracted":[]},
  "publicEventId":"..."
}

TRACE_STATUS / TRACE_BATCH are also allowed if useful.

## Required semantics

TRACE != EVIDENCE
TRACE != MEMORY
TRACE != TRAINING DATA
TRACE OBSERVATION MUST NOT MUTATE COGNITION

Trace hooks must sit beside existing gates, not become new owners.
No trace event may affect:
- EVAL result
- COMMIT authority
- DRIVE selection
- MEDIATE outcome validation
- graph admission/retraction
- initiative scheduling

## Four-law observability

For DECISIONS/DEEP, capture enough structure to reconstruct:
input/event
-> candidate(s)
-> owner decision
-> influence type
-> basis/evidence roots
-> graph delta or no-delta
-> selected public event/action

Do not generate natural-language rationales after the fact.
Prefer stable reason codes and exact IDs/relations.

## NEXT_INTERACTION scope

Arm trace before the next USER_MESSAGE.
Capture the complete resulting cognitive episode, including delayed TICK work causally attached to that episode.
Stop automatically after the episode closes or maxEvents is reached.
Emit TRACE_STATUS with state=COMPLETE.

## Persistence

Trace data is diagnostic and does not belong in .c4m learned state.
Nursery persists received TRACE_* events separately.

## Acceptance tests

1. TRACE_CONFIG OFF produces no TRACE_EVENT.
2. TRACE_CONFIG DECISIONS emits owner/influence/decision records.
3. TRACE does not alter response, graph hash, public events or checkpoint hash vs trace-off deterministic run.
4. NEXT_INTERACTION stops after one episode.
5. Evidence roots/provenance refer to existing runtime IDs.
6. Graph delta matches actual before/after graph mutation.
7. Unsupported trace is explicit, never fabricated.
