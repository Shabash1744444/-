# C4 MEMORY CONSOLIDATION / COMPRESSION PRINCIPLES

Normative from 2026-10-07 onward.

## Goal
C4 must be able to live for a long time without persistent state growing linearly with every observation, sentence, frame or conversation turn.

RAW EXPERIENCE GROWTH != REQUIRED LONG-TERM STORAGE GROWTH.

Compression is cognitive consolidation, not merely file compression.

## Memory tiers
HOT:
current dialogue, active goals, nearby world state, unresolved gaps.

WARM:
recent episodes, recently used concepts, local social/world history.

COLD:
long-term semantic knowledge, summarized episodes, old provenance chains, inactive skills.

ARCHIVE:
rare raw evidence/receipts retained for audit or reconstruction.

Runtime may move information between tiers without changing epistemic meaning.

## Consolidation target
episode_1 + episode_2 + ... + episode_n
-> shared invariant/schema + exceptional residuals + provenance references.

Example:
100 observations of dropped unsupported objects falling
should not require 100 independent full semantic copies forever if a supported general relation plus retained exceptions/provenance can represent the useful structure.

But:
SUMMARY != ORIGINAL EVIDENCE.
SCHEMA != OBSERVATION.
COMPRESSION != NEW TRUTH.

## Never destroy epistemic boundaries
Compression must preserve:
- source identity/lineage where relevant;
- observation vs report vs inference;
- uncertainty/status;
- contradictions;
- retraction/correction history;
- exceptions;
- privacy/ownership;
- temporal ordering when causally relevant.

Two dependent reports must not become "two independent confirmations" during consolidation.

## Candidate compression operations
1. deduplicate exact/near-exact structural duplicates;
2. intern repeated strings/entities/relations;
3. morphology paradigms instead of storing every form independently where derivable;
4. common subgraph factoring;
5. repeated episode -> schema + residual exceptions;
6. old dialogue -> semantic memory + selected episodic anchors;
7. provenance DAG compaction without lineage loss;
8. inactive indexes rebuilt/on-demand rather than fully resident;
9. cold raw sensory traces compressed or archived after stable abstractions, subject to retention policy;
10. learned summaries with explicit DERIVED/SUMMARY provenance.

## Information-preservation test
Before deleting/replacing detail, ask whether the compressed form can still answer the queries that matter.

Compression candidate is acceptable only if held-out query/reconstruction tests remain within the allowed loss budget.

Important:
LOSSY COMPRESSION must be explicit.
LOSSLESS and LOSSY consolidation are distinct operations.

## Forgetting
Forgetting should be controlled by expected future utility, reconstructability and epistemic importance, not simply age.

Potential utility signals:
frequency
recency
goal relevance
dependency centrality
source uniqueness
exception value
causal importance
identity/history importance

Do not forget rare counterexamples merely because they are rare.

COUNTEREXAMPLE VALUE may exceed frequency.

## Emergence and compression
If richer behavior emerges from a dense graph, uncontrolled pruning may destroy it.

Therefore record graph/capability metrics before and after each consolidation experiment:
- held-out transfer
- path structure
- connected components
- relation-type coverage
- contradiction/retraction tests
- language tests
- initiative quality
- latency
- bytes/RAM

Compression ratio is NOT success if capability collapses.

## SSD-resident organism
Long-term C4 should be able to keep most persistent state on SSD/flash and only a hot working set in RAM.

Conceptual architecture:
SSD/DISK PERSISTENT GRAPH
-> indexes / mmap or DB pages
-> hot cache / working set
-> reasoning/dialogue operations
-> incremental durable commit

The organism can therefore be physically much larger than RAM while remaining responsive if locality and indexes are good.

Do not load the entire graph into Python objects at startup.

## Identity/continuity
Moving a memory from HOT to COLD or compressing it does not by itself erase technical continuity.

But:
COMPRESSED HISTORY != FULL EPISODIC REPLAY.

C4 must know whether it retains:
- exact record,
- summary,
- derived schema,
- or no recoverable detail.

## Long-life benchmark
Run simulated long-life tests:
1 day -> 10 days -> 100 days -> 1000 days equivalent.
Measure state growth and capability.

Desired curve:
experience volume grows much faster than persistent storage.

A useful target is sublinear retained-memory growth after recurring patterns stabilize, while genuinely novel information still increases state.

## Promotion rule
No compression mechanism becomes canonical until:
baseline -> compress -> cold reload -> regression -> held-out transfer -> provenance audit -> retraction audit -> size/RAM/latency report.

Never promote solely for saving bytes.
