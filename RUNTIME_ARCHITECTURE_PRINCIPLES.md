# C4 RUNTIME ARCHITECTURE PRINCIPLES

Normative from 2026-10-07 onward.

## 1. Runtime is the universal capability substrate
Runtime should be maximally universal and capability-dense.

Rule of thumb:
IF a capability is required to acquire experience at all -> runtime / organ.
IF content can in principle be acquired from experience -> weights / persistent learned state.

Examples suitable for runtime:
- graph operations, admission, retraction, provenance;
- temporal logic and state transitions;
- UNKNOWN handling;
- source/SELF/OTHER/WORLD separation;
- language parsing/generation mechanisms;
- morphology/syntax/reference/ellipsis machinery;
- query planning and read-only retrieval;
- curiosity/gap prioritization;
- initiative arbitration and wait states;
- consolidation/compression/forgetting mechanisms;
- checkpoint/autosave;
- sensor/actuator interfaces and receipts;
- semantic operators and type system;
- storage/indexing infrastructure.

Examples that belong in learned state:
- Ruslan, Synka, Dostoevsky, Bryson;
- word meanings/usages and lexical relations learned from corpora;
- facts, stories, personal history, game lore;
- observed sensory associations;
- conversation-derived knowledge.

RUNTIME != HIDDEN KNOWLEDGE BASE.
Do not hardcode corpus facts to improve demos.

## 2. Full C4 system size must be measured honestly
C4 is not only the .c4m archive.

Report:
runtime code + persistent graph/state + indexes + live working memory.

The .c4m archive may be highly compressed relative to expanded in-memory graph.

## 3. Runtime / language-organ / weights split
Universal core:
- semantic graph physics;
- provenance/epistemic rules;
- generic discourse state;
- learning protocol.

Russian language organ:
- Russian morphology;
- agreement;
- declension/conjugation;
- syntax;
- reference/deixis;
- sentence planning and surface generation.

Learned state:
- concrete lemmas, senses, forms, collocations, idioms and corpus examples.

A language organ may be replaced/extended later without changing world knowledge.

## 4. Questions are read-only
QUESTION != ASSERTION.
Parsing/querying must never create graph entities/facts merely to ask about them.

Unknown surface forms may be stored as unresolved surface gaps, not admitted world entities.

## 5. Retrieval boundaries
LEXICAL MATCH != TRUTH.
TOPIC MATCH != PROPOSITION SUPPORT.
SIMILARITY != IDENTITY.

Read-only retrieval may expose relevant admitted knowledge, but yes/no truth must use relation semantics/reasoner, not word overlap.

## 6. Human-facing verbalization
Internal relation codes/IDs must not leak by default.

PUBLIC LABEL != INTERNAL ID.
OPAQUE GAP != HUMAN QUESTION.

Initiative must select a human-readable gap or remain silent.

## 7. Initiative
Many internal gaps may exist simultaneously.
External policy:
rank -> select one -> ask -> wait -> incorporate answer -> rerank.

ASK WAIT != GAP RESOLUTION.
A new unrelated internal gap does not bypass the wait gate.

## 8. New-word acquisition
Required runtime protocol:
unknown surface -> identify language -> ask/receive definition -> create lexical candidate -> bind meaning/source -> ask for/use example -> near-miss test -> admit -> WORD_FORM/relations update.

Do not force teacher to use developer syntax forever.

## 9. Persistence
Mobile runtime must support:
- incremental durable writes;
- explicit checkpoint/export;
- autosave after admitted learning;
- crash-safe journaling;
- versioned migration;
- cold reload verification.

RAM continuity is not sufficient evidence of persistent learning.

## 10. Mobile scale architecture
Current full-JSON/Python-object materialization is a prototype, not the 100-300MB architecture.

Before large weight growth:
- disk-backed graph store;
- indexed on-demand retrieval;
- hot working set/cache;
- immutable/shared dictionary tables where useful;
- compact integer IDs;
- string interning;
- shared provenance tables;
- incremental indexes;
- lazy loading;
- background-safe checkpointing.

SQLite is a plausible first implementation, not a sacred architectural choice.

## 11. Game scale
For many residents, separate:
shared runtime
+ optional shared world/language base
+ per-agent learned state/history.

Do not duplicate a whole runtime per NPC if process architecture can share it.

## 12. Promotion rule
Every runtime improvement:
counterexample -> minimal reusable repair -> focused tests -> full regression -> real-device re-attack -> artifact/SHA -> checkpoint.

Never promote because conversation merely sounds nicer.


## 13. Memory consolidation and compression is a core runtime ability
Compression is not postponed storage cleanup.
A lifelong learner requires active consolidation.

Runtime must support:
HOT/WARM/COLD/ARCHIVE memory tiers,
deduplication,
schema extraction,
common-subgraph factoring,
provenance-preserving compaction,
controlled forgetting,
and disk-resident cold memory.

Important invariants:
SUMMARY != ORIGINAL EVIDENCE.
SCHEMA != OBSERVATION.
COMPRESSION != NEW TRUTH.
DEPENDENT EVIDENCE must remain dependent after compaction.

Most persistent state may live on SSD/flash; only a locality-aware working set needs to be resident in RAM.

Read MEMORY_CONSOLIDATION_COMPRESSION.md before changing memory/storage architecture.
