# CLAUDE FRIDAY RUNTIME TASK — GIVE AFTER 20:00

Date prepared: 2026-10-07
Intended handoff: Friday evening after 20:00 local time

## Current canonical pair

Weights:
- child_g292_hierarchy_accelerated_concepts_green.c4m
- 1,952,929 bytes
- SHA256 d5631373fbdf24f2bf7a8068ca768edc0a4e94765e5b43035c90c3712aa2d246

Runtime:
- C4_RUNTIME_G294_RELATION_ALGEBRA_GREEN_2026-10-07.zip
- SHA256 3ce81d00f50a0cde28eef0d7e05bbe329f2665f41494a5a12fb9bd1b67998f32

Combined:
- C4_G294_RUNTIME_PLUS_G292_WEIGHTS_2026-10-07.zip
- SHA256 914873776a59e9e5f7ef75410e4191a357ff9825c5c05b558e49872a91af1e68

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
- reduce .c4db bloat when there is a principled architecture-level improvement;
- integer IDs/string interning/shared dictionaries/compression where safe;
- preserve provenance, corrections, conflicts and retraction;
- no optimization may erase epistemic distinctions.

3. Windows/desktop host readiness
- fast startup;
- durable local state;
- clean tool/action adapters;
- filesystem/process/app integration architecture;
- future screen/audio/video adapters;
- graceful crash recovery.

4. Streaming/realtime readiness
- do not block future voice/video streaming;
- incremental state updates;
- barge-in friendly event loop;
- async/evented execution only where semantics remain deterministic;
- make long work inspectable and interruptible.

5. Plugin/adapter boundary
- tools must be replaceable adapters, not hidden cognition;
- runtime should allow future camera/mic/screen/files/apps/browser/game interfaces;
- sensor/action adapters must not directly bypass epistemic admission.

6. Compatibility and migration
- exact current G292 weights must load;
- newer future weights from training chat must migrate without deleting USER_SAID / user-taught local experience;
- keep prior database backup;
- prefer schema migrations with explicit versions.

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

G294 relation boundaries:
- PART_OF <-> HAS_PART is a read-only inverse;
- BEFORE <-> AFTER is a read-only inverse;
- SYNONYM / ANTONYM / OPPOSITE are symmetric read-only;
- PART_OF is NOT transitive by default;
- HAS != HAS_PART;
- MEANS is not symmetric by default;
- ROLE is not inherited/symmetric by default;
- derived algebra never silently persists as direct evidence.

## Branch policy

Your work is a mutation/R&D branch.

DO:
- improve runtime;
- add tests;
- produce patches/diffs;
- benchmark memory/disk/latency;
- implement agent lifecycle;
- improve persistence/tool execution;
- package recovery artifacts;
- document every invariant and migration.

DO NOT:
- retrain or alter canonical G292 weights;
- import test/nonce vocabulary into weights;
- patch benchmark answers;
- weaken UNKNOWN/provenance/source distinctions;
- assume your branch automatically becomes canonical;
- replace C4 reasoning with an LLM agent hidden behind the API.

External LLM assistance is allowed as engineering/teacher tooling, not as hidden C4 cognition.

## Validation before handoff

At minimum:
1. exact canonical weights open;
2. memory mode if still supported;
3. SQLite/disk mode;
4. cumulative regression;
5. agent lifecycle tests;
6. crash/restart persistence;
7. migration from old weights/db;
8. user-taught state carry-forward;
9. no graph pollution from questions/actions;
10. benchmark latency/RAM/disk;
11. physical checkpoint + SHA256;
12. clear patch/diff against current canonical runtime.

Known historical missing-artifact failures should be reported separately and not confused with new regressions.

## Deliverables

- runtime ZIP;
- combined runtime + exact G292 weights package for smoke;
- checkpoint report;
- changelog;
- benchmark JSON;
- regression JSON;
- migration notes;
- exact hashes/sizes;
- patch/diff;
- README: what changed / what did not change / risks / next best work.

If you discover a counterexample to a current law or runtime assumption:
do not hide it.
Record it, build the smallest reproduction, and either repair it minimally or leave the candidate RED.

## Context

The training line is targeting approximately G1000 for broad trap-resistant human-like perception:
relation algebra -> dirty language -> discourse/deixis -> pragmatics/prosody -> source/conflict -> multimodal grounding -> long mixed material -> adversarial integration.

Runtime should prepare for those capabilities without prematurely hardcoding their answers.

Goal:
make C4 an extremely capable persistent local organism/agent runtime while keeping the cognitive architecture auditable and the organism independently trainable.
