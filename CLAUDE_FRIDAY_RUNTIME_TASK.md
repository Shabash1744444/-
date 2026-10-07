# CLAUDE FRIDAY RUNTIME TASK — GIVE AFTER 20:00

Date prepared: 2026-10-07
Intended handoff: Friday evening after 20:00 local time

## Current canonical pair

Weights:
- child_g301_relation_language_bridge_green.c4m
- 1,972,611 bytes
- SHA256 a37a7a1eebb3e38df29f4f29535b74b8d3ce2159d0e2ecb5b0d27f7c06721708

Runtime:
- C4_RUNTIME_G300_OPEN_RELATION_QUERY_GREEN_2026-10-07.zip
- SHA256 00d7be0378a0eb18b93c4e356dc9a7d28d9e1adc592ec9c16256cea8f069b27e

Combined:
- C4_G300_RUNTIME_PLUS_G301_WEIGHTS_2026-10-07.zip
- SHA256 cad9df74322bc94a8b9f5e4a5fb68416636889fa93ab3d63dd01fec86cb26a10

## Mission

Build the best possible C4 runtime/body around the current organism without silently changing C4 cognitive laws or contaminating weights.

Work autonomously for as long as useful within tool/usage limits.
Prefer durable, reusable infrastructure over cosmetic features.

The main training chat continues to evolve the organism separately.
A separate mobile-app branch continues APK/UI/runtime-shell work.
Your branch may focus aggressively on runtime engineering and agent execution.

## Highest-value areas

1. Agent task execution inside chat
- persistent TASK / GOAL / STATUS / TRIGGER / PLAN structures;
- long-running task lifecycle across turns/restarts;
- ACTION_REQUEST != VERIFIED_OUTCOME;
- environment/tool receipts;
- blocked/waiting/done/cancelled states;
- retries and resumability;
- user can say "remember this task and do it" and the runtime can preserve and progress it.

2. Runtime/storage scale
- keep SQLite/disk-backed graph fast;
- reduce .c4db bloat only through principled architecture-level improvement;
- integer IDs/string interning/shared dictionaries/compression where safe;
- preserve provenance, corrections, conflicts and retraction.

3. Windows/desktop host readiness
- fast startup, durable local state, clean tool/action adapters;
- filesystem/process/app integration architecture;
- future screen/audio/video adapters;
- graceful crash recovery.

4. Streaming/realtime readiness
- do not block future voice/video streaming;
- incremental state updates;
- barge-in friendly event loop;
- make long work inspectable and interruptible.

5. Plugin/adapter boundary
- tools are replaceable adapters, not hidden cognition;
- sensor/action adapters cannot bypass epistemic admission.

6. Compatibility and migration
- exact current G301 weights must load;
- future weights from training chat migrate without deleting USER_SAID/user-taught local experience;
- keep prior DB backup and explicit schema migrations.

## Canonical laws that MUST survive

UNKNOWN != FALSE
QUESTION != ASSERTION
DERIVED != OBSERVATION
PREDICTION != EVIDENCE
ACTION_REQUEST != VERIFIED_OUTCOME
RECEIPT != CAUSAL PROOF
SIMILARITY != IDENTITY
CANONICAL != VERIFIED AUTHORITY
SOURCE/ADDRESS != EVIDENCE
SUMMARY != ORIGINAL EVIDENCE
COMPRESSION != NEW TRUTH
RAW SIGNAL != TEACHER LABEL

Current relation/runtime boundaries:
- PART_OF <-> HAS_PART read-only inverse;
- BEFORE <-> AFTER inverse and bounded strict temporal transitivity;
- temporal cycle -> CONFLICT;
- ORDER != CAUSE;
- SYNONYM / ANTONYM / OPPOSITE symmetric read-only;
- PART_OF not transitive by default;
- HAS != HAS_PART;
- MEANS not symmetric by default;
- ROLE not inherited/symmetric by default;
- derived algebra never persists as direct evidence;
- EVIDENCE HISTORY != CURRENT SOURCE STANCE;
- RETRACTION != RESURRECTION OF OLD STANCE;
- derived state must invalidate when support disappears.

## Branch policy

Your work is a mutation/R&D branch.

DO:
improve runtime; add tests; benchmark; implement agent lifecycle; improve persistence/tool execution; package recovery artifacts; document invariants/migrations.

DO NOT:
retrain/alter canonical G301 weights; import nonce/test vocabulary; patch benchmark answers; weaken UNKNOWN/provenance/source distinctions; assume auto-canonical promotion; replace C4 reasoning with hidden LLM cognition.

## Validation before handoff

At minimum:
1. exact canonical G301 weights open;
2. memory mode if supported;
3. SQLite/disk mode;
4. cumulative regression;
5. agent lifecycle tests;
6. crash/restart persistence;
7. migration;
8. user-taught carry-forward;
9. no graph pollution from questions/actions;
10. latency/RAM/disk benchmark;
11. physical checkpoint + hashes;
12. patch/diff against current canonical runtime.

Known historical missing-artifact failures must be separated from new regressions.

## Deliverables

Runtime ZIP; combined runtime+exact G297 weights smoke package; checkpoint; changelog; benchmark/regression JSON; migration notes; hashes/sizes; patch/diff; README with changed/not-changed/risks/next.

If a counterexample appears, preserve it and repair minimally or leave RED.

## Context

Training target is approximately G1000 for broad trap-resistant human-like perception:
relation algebra -> dirty language -> discourse/deixis -> pragmatics/prosody -> source/conflict -> multimodal grounding -> long mixed material -> adversarial integration.

Runtime should prepare for these abilities without hardcoding training answers.

Goal:
make C4 an extremely capable persistent local organism/agent runtime while keeping cognition auditable and the organism independently trainable.
