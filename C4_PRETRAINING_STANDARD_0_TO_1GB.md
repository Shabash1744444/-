# C4 PRETRAINING STANDARD — FROM CLEAN SEED TO 1 GB

Status: NORMATIVE METHODOLOGY
Date: 2026-10-07

This document is the reproducible training contract for building a new C4 organism from a clean seed up to large persistent-state checkpoints such as 1 GB.

It is intentionally independent of any one chat or agent.
An agent receiving only:
- a compatible C4 runtime;
- a clean/approved starting organism;
- training/evaluation materials;
- this file and the normative laws;
should be able to continue training without reconstructing hidden assumptions from conversation history.

Read with:
- TRAINING_LAWS.md
- DEVELOPMENTAL_TRAINING_METHODOLOGY.md
- MEMORY_CONSOLIDATION_COMPRESSION.md
- RUNTIME_ARCHITECTURE_PRINCIPLES.md
- RUSSIAN_CURRICULUM_BOOK_ROADMAP.md

---

## 0. Objective

Do NOT optimize:
- file size;
- number of facts;
- number of books;
- generation number;
- teacher verbosity.

Optimize the declining cost of acquiring new capability.

Primary developmental objective:

TeacherCost(new domain) DOWN
while
HeldOutCapability(new domain) UP
and
FalseInference / contamination stay bounded.

Useful core metrics:

LearningLeverage = correct novel held-out transfer / direct lessons

TeacherBurden = teacher questions + teacher relations + teacher words

AutonomyRatio = successfully acquired structure without human semantic intervention / total successfully acquired structure

NoveltyCompression = 1 - new primitive structure / usable structure extracted from material

ErrorAmplification = wrong derived structures caused by one wrong admitted primitive

No metric is valid by itself. A larger transfer ratio with rising false inference is failure.

---

## 1. Non-negotiable laws

UNKNOWN != FALSE
QUESTION != ASSERTION
LEXICAL RETRIEVAL != TRUTH
SIMILARITY != IDENTITY
HOMOGRAPH != IDENTITY
ORTHOGRAPHIC SUFFIX != LEXICAL POS
RAW SURFACE != LEMMA FACT
TEST TOKEN != VOCABULARY KNOWLEDGE
SPEECH FORM != GRAPH FACT
BOOK != TRUTH
AUTHOR != NARRATOR
CHARACTER != AUTHOR
FICTIONAL WORLD FACT != EXTERNAL WORLD FACT
REPLAY != NEW EVIDENCE
DERIVED != OBSERVATION
PREDICTION != EVIDENCE
ACTION_REQUEST != VERIFIED_OUTCOME
SUMMARY != ORIGINAL EVIDENCE
SCHEMA != OBSERVATION
COMPRESSION != NEW TRUTH

Never weaken one of these laws merely to improve a benchmark.

---

## 2. Runtime / organism split

Runtime contains reusable learning physics and organs.

Examples:
- graph and provenance machinery;
- admission/retraction;
- morphology mechanism;
- discourse and teaching protocol;
- ActiveGaps;
- guided reader;
- persistence;
- safe query/answer planning;
- future sensory/action adapters;
- consolidation machinery.

Organism / weights contain acquired experience and knowledge.

Examples:
- lexical concepts;
- word families actually learned;
- semantic relations;
- source-linked world knowledge;
- book-derived structures;
- conversation-derived knowledge;
- multimodal associations;
- personal/episodic experience.

RUNTIME BUG != TRAINING GAP.
TRAINING GAP != RUNTIME BUG.

If the same failure occurs across many otherwise unrelated concepts and cannot be solved by adding reusable learned structure, investigate runtime.
If one domain lacks knowledge while the acquisition machinery works on held-out analogues, train weights.

Runtime changes and weight-training generations MUST be separately checkpointed.

---

## 3. Source classes

Every input source MUST be tagged before ingestion.

TRAINING:
may contribute admitted learned state.

TEACHER_ONLY:
may answer gaps or produce candidate abstractions, but raw content is not automatically treated as C4 experience.

EVALUATION_ONLY:
must never train the organism, teacher, curriculum selector or morphology anchors for the evaluated capability.

ARCHIVE_ONLY:
retained only for audit/reproducibility.

Each source record should include where possible:
- source_id;
- title/origin;
- version/date;
- rights/license;
- language/register;
- source class;
- authority scope;
- historical/current/fictional designation;
- checksum.

SOURCE FILE != AUTHORITY.
A dictionary definition or book statement remains a sourced claim, not universal truth.

---

## 4. Clean-seed protocol

Before beginning a new pretraining run:

1. Record exact runtime SHA256.
2. Record exact seed-organism SHA256 and bytes.
3. Freeze evaluation sets for the next milestone.
4. Create a training-run ID.
5. Create:
   - run manifest;
   - source manifest;
   - metric ledger;
   - checkpoint journal;
   - exclusion/quarantine ledger.
6. Verify cold-open.
7. Run baseline regression.
8. Record entity/fact/evidence/relation counts.
9. Record baseline memory, latency and deployed footprint.
10. No curriculum ingestion until baseline is reproducible.

A run without a reproducible clean seed is invalid.

---

## 5. Unit of training

The preferred training unit is NOT a book and NOT a paragraph.

The unit is a transferable structural lesson.

Examples:
- one morphology transformation family;
- one taxonomy edge that unlocks many descendants;
- one semantic root relation;
- one discourse rule;
- one causal pattern;
- one contextual lexical definition;
- one sensory invariant.

A good lesson produces multiple correct future applications.
A bad lesson only creates another isolated stored fact.

Preferred cycle:

material
-> candidate structure
-> compare with existing graph
-> identify only genuine gaps
-> rank by expected downstream utility
-> teach minimal missing relation
-> re-evaluate
-> held-out transfer
-> near-miss restraint
-> cold reload
-> cumulative regression
-> checkpoint.

---

## 6. Anti-storage rule

Before adding a direct lesson, ask:

Can existing structure derive it?
Can one higher-level relation unlock several missing instances?
Can morphology/schema/semantic inheritance replace many explicit aliases?
Is this already known through another valid path?
Is the apparent gap actually a runtime defect?

Never store target answers merely to make an exam green.

Target paradigms should remain unstored when reusable morphology can derive them.
Repeated properties should move toward shared class/schema relations when epistemically valid.
Do not collapse legitimate exceptions.

A batch that grows bytes without increasing held-out ability or reducing teacher cost is suspect and must be reviewed before promotion.

---

## 7. Fast Curriculum order

Default developmental order for a fresh Russian-first organism:

### Stage A — Morphological substrate
Start with a small high-frequency lexical seed.
Learn productive noun/verb/adjective families.
Test unseen surfaces.
Do not import every inflection as an independent fact.

Promotion evidence:
- held-out forms;
- wrong forms;
- correct UNKNOWN;
- homograph restraint;
- cold reload.

### Stage B — Dense semantic core
Build high-utility taxonomies and reusable root relations.
Favor concepts with high expected downstream centrality.

Teach:
class structure,
common capabilities,
properties,
functions,
roles,
opposites/synonyms only with context boundaries.

### Stage C — Composition and discourse
Simple propositions -> negation -> roles -> reference -> ellipsis -> dialogue acts -> multi-sentence context.

Language competence must transfer to unseen vocabulary.

### Stage D — ActiveGaps
Rank unknowns by estimated downstream unlock / teacher cost.
Ask ONE useful question at a time.
Re-rank after each answer.

### Stage E — Guided reading
Use short ordinary text.
Only supported deterministic/corroborated parses may become candidate lessons.
Unsupported sentences are skipped or become gaps.
External text must not inherit stale live-dialogue context.

### Stage F — Contextual lexical learning
Unknown inflected surface -> raw-form gap -> ask dictionary form + meaning.
Never guess and assert a lemma.
After teacher response, existing morphology must explain the original surface before the gap is considered closed.

### Stage G — Books / explanatory corpora
Books become generators of:
- new concepts;
- new relations;
- new linguistic structures;
- discourse;
- ambiguity;
- source identity;
- counterexamples.

Known material is skipped or used only as validation/repetition evidence when permitted.
Do not dump all sentences into graph memory.

### Stage H — Multimodal grounding
RAW SIGNAL != TEACHER LABEL.
Derived features, teacher descriptions and autonomous sensor competence remain distinct.

### Stage I — Consolidation
Repeated episodes -> schema + residual exceptions + provenance.
Regression before and after consolidation.

### Stage J — Agent/embodiment curriculum
SEPARATE TRACK.
Do not mix action competence into lexical pretraining metrics.

Agent curriculum should later cover:
goal selection, tool affordances, planning, action/receipt distinction, retry/rollback, environment models, permissions, self-initiated tasks and long-horizon continuity.

---

## 8. Mandatory batch protocol

Every canonical batch MUST record:

### Before training
- exact parent runtime + weights hashes;
- exact source manifest;
- held-out targets frozen before lessons;
- expected capability;
- direct-lesson budget;
- stop conditions.

### During training
- attempted inputs;
- parsed/supported/skipped;
- admitted/rejected/deduped;
- new gaps;
- questions asked;
- teacher words;
- teacher relations;
- direct lessons;
- quarantined ambiguous items;
- runtime defects discovered.

### After training
- exact held-out score;
- correct UNKNOWN;
- false inference;
- near-miss restraint;
- cold reload;
- previous-generation cumulative regression;
- bytes added;
- live RAM/index footprint when relevant;
- latency changes;
- exact artifact SHA256.

No physical checkpoint -> generation does not exist.

---

## 9. Held-out discipline

Held-out items must be selected BEFORE their answers are taught.

Disallowed:
- train on an answer and later call a paraphrase held-out;
- tune morphology anchors on the exact target surfaces;
- repair a failed target with a one-off alias and count it as transfer;
- allow EVALUATION_ONLY material into teacher context;
- count already-TRUE relations as novel transfer.

Strict novelty is preferred:
relation was not TRUE on the exact parent organism,
became TRUE after the batch,
remains TRUE after cold reload.

For language, also include adversarial near-misses and homographs.

---

## 10. Teacher-cost protocol

Track at least:
- questions;
- semantic relations supplied;
- teacher words/tokens-equivalent;
- turns;
- unresolved questions;
- low-value questions asked before competency.

Competency threshold must be predefined.

For comparable unseen domains, plot:
TeacherCost vs organism size/development stage.

A more developed C4 should need less teaching for structurally similar new domains.

If Teacher Cost does not fall over developmental checkpoints, inspect:
- curriculum density;
- missing reusable schemas;
- poor gap ranking;
- parser bottlenecks;
- over-storage;
- retrieval degradation.

---

## 11. Scale gates: 0 -> 1 GB

Byte milestones are engineering gates, not intelligence targets.

### Gate 0: seed -> ~2 MB
Purpose:
prove core learning physics.

Require:
- reproducible persistence;
- provenance;
- UNKNOWN restraint;
- transfer on morphology/semantics;
- no question-created facts.

### Gate 1: ~2 -> 5 MB
Purpose:
dense core language + semantic reuse.

Require:
- teacher-cost measurement;
- active gaps;
- cumulative retention;
- ordinary short-text guided learning.

### Gate 2: 5 -> 10 MB
Purpose:
broader lexical/semantic families and mixed passages.

Require:
- strict novelty accounting;
- source manifests;
- first consolidation experiments;
- latency/index monitoring.

### Gate 3: 10 -> 30 MB
Purpose:
multi-domain guided reading.

Require:
- stable query quality;
- robust homograph/polysemy quarantine;
- source-aware book/article ingestion;
- teacher burden declining on repeated benchmark families.

### Gate 4: 30 -> 100 MB
Purpose:
broad curriculum.

Before promotion:
- storage architecture must no longer require naive full Python-object loading;
- disk/index/hot-set design must be tested;
- consolidation must preserve provenance/retraction.

### Gate 5: 100 -> 300 MB
Purpose:
large persistent learner.

Require:
- disk-backed/lazy graph;
- incremental durable writes;
- checkpoint recovery;
- memory tiers;
- no full-file autosave bottleneck;
- long-run contamination/retraction tests.

### Gate 6: 300 MB -> 1 GB
Purpose:
large-scale developmental pretraining, NOT raw accumulation.

Require:
- stable sublinear retained growth for repetitive material;
- multi-domain held-out transfer;
- repeated teacher-cost benchmarks;
- source/provenance audit;
- consolidation/reconstruction audits;
- long-horizon persistence tests;
- storage/index/latency budget suitable for target hardware.

At 1 GB, success means capability density and learning efficiency improved. A 1 GB graph with 1 GB of isolated facts is failure.

---

## 12. Corpus ingestion standard

For each book/document:

source registration
-> rights/license check
-> chunking
-> safe linguistic parse
-> candidate structures
-> dedup against graph
-> detect unknown lexical surfaces
-> detect semantic gaps
-> utility rank
-> teacher/clarification loop
-> admit supported structure with provenance
-> generate held-out combinations
-> restraint test
-> periodic checkpoint.

Do not ingest a whole book in one transaction.

Recommended chunk promotion:
small clean chunk
-> checkpoint
-> larger chapter batch
-> checkpoint
-> work-level consolidation.

If parser confidence/support is insufficient:
SKIP or GAP.
Never “best guess” into world truth.

---

## 13. Books and fiction

Every text-world relation must preserve source/world scope.

For fiction:
- narrator statements belong to fictional/discourse scope;
- character claims are character claims;
- fictional events are not external-world observations;
- author identity is not narrator identity.

Literature is primarily useful for:
language, discourse, perspective, social reasoning, ambiguity, metaphor, narrative state and cultural concepts.

It is not an authority feed for external reality.

---

## 14. Quarantine ledgers

Maintain explicit ledgers for:
- homographs/polysemy;
- irregular morphology;
- unsupported syntax;
- disputed world claims;
- source-license uncertainty;
- runtime defects;
- counterexamples not yet repaired.

Quarantine is preferable to silent wrong admission.

An item leaves quarantine only through a reusable mechanism or explicit sense/source representation, not a target-specific benchmark hack.

---

## 15. Consolidation schedule

Do not use a fixed “every N MB” rule alone.

Trigger consolidation when:
- repeated structures accumulate;
- duplicate subgraphs rise;
- retrieval latency increases;
- direct-storage ratio rises;
- teacher cost stops falling;
- graph memory expands faster than new capability.

Before consolidation:
save exact baseline and benchmark set.

After consolidation:
cold reload;
held-out transfer;
retraction audit;
provenance audit;
exception audit;
size/RAM/latency report.

Compression ratio alone never justifies promotion.

---

## 16. Canonical promotion rule

GREEN only if:
1. objective defined before training;
2. direct lessons recorded;
3. held-out frozen;
4. transfer measured;
5. false inference measured;
6. cold reload passes;
7. previous cumulative skills pass;
8. full runtime regression passes;
9. artifact physically exists;
10. SHA256 and bytes recorded;
11. README/current-state/handoff/journal updated.

Otherwise status is RED or EXPERIMENTAL.

Never continue canonical lineage from an uncheckpointed candidate.

---

## 17. Standard generation artifacts

Recommended:
- child_gNNN_<name>_green.c4m
- C4_RUNTIME_GNNN_<name>_GREEN_<date>.zip
- C4_GNNN_<name>_GREEN_<date>.zip
- C4_G<runtime>_RUNTIME_PLUS_G<weights>_WEIGHTS_<date>.zip
- checkpoints/CP_C4_GNNN_<name>_GREEN.md
- metrics/GNNN_<name>_metrics.json
- curriculum/run_<id>_source_manifest.json
- curriculum/run_<id>_heldout.json
- curriculum/run_<id>_quarantine.md

Checkpoint must say whether generation is RUNTIME or WEIGHTS.

---

## 18. Agent handoff contract

An autonomous training agent must never infer “continue training” as “add more material blindly.”

At startup it must:
1. read README/current state/handoff;
2. verify artifact hashes;
3. run cold-open smoke;
4. read this standard + laws;
5. inspect latest metrics;
6. resume from latest physical GREEN only;
7. train one bounded curriculum block;
8. stop on RED;
9. physically checkpoint on GREEN;
10. update canonical docs.

If a run is interrupted before checkpoint, restart from last physical GREEN, not reconstructed memory.

---

## 19. Success condition

The developmental curve we want is:

more reusable structure
-> fewer teacher interventions
-> more correct unseen transfer
-> better restraint
-> less redundant storage
-> stable persistence/provenance
-> broader autonomous learning.

The final objective is not “a 1 GB model.”

It is a C4 for which the next domain is dramatically cheaper to learn than it was for the seed.


---

## 20. Run-local gap scope

A persistent organism may carry unresolved gaps from many older experiences.

A training run MUST NOT blindly drain the organism's entire global gap backlog.

Use two layers:
- GLOBAL GAP MEMORY: all unresolved needs retained by C4;
- RUN-LOCAL QUEUE: only gaps caused by the current bounded curriculum source, plus explicitly imported prerequisites.

Within a run-local queue:
1. rank by expected downstream unlock / teacher cost;
2. select exactly ONE gap;
3. obtain one answer;
4. re-evaluate;
5. rank again.

Do not emit several unanswered questions in one training scheduler step and count them as one teacher interaction.

Historical gaps remain in global memory and can be revisited by a separate maintenance curriculum.

Gap priority changes scheduling only. It does not change truth, evidence or epistemic status.


---

## 21. Evaluation-item validation

GENERATED HELD-OUT ITEM != VALID EVALUATION ITEM.

Held-out examples are frozen before teaching, but they must also be linguistically/semantically validated before the run uses them as ground truth.

Automatic morphology, paraphrase or exam generation can itself hallucinate invalid surfaces.

Required preflight:
1. generate candidate evaluation item;
2. validate against trusted linguistic rules/source or a separately audited reference;
3. quarantine uncertain/irregular items;
4. only then freeze the held-out set.

Never teach C4 an invalid form merely because the exam generator produced it.

G285 established this rule when an autogenerated invalid form глянецом was caught before promotion. The correct irregular form глянцем was not derivable; the lexeme was quarantined instead of benchmark-patched.


---

## 22. Relation-level and causal curriculum protocol

A relation curriculum must test structure, not merely fact recall.

For CAUSES record separately:
- direct causal lessons;
- derived causal chains;
- direct endpoint leaks;
- reverse-direction controls;
- cross-chain/cross-motif controls;
- local direct causes of convergence nodes;
- local direct effects of divergence nodes.

A derived causal endpoint is GREEN only when:
1. it was not a direct fact on the exact parent/candidate;
2. a valid bounded path exists;
3. the answer is CHAIN/derived rather than silently persisted;
4. cold reload preserves the path;
5. reverse and sibling relations remain UNKNOWN unless separately supported.

For branching/converging motifs verify explicitly:
SHARED EFFECT != CAUSAL RELATION BETWEEN CAUSES.
SHARED CAUSE != CAUSAL RELATION BETWEEN EFFECTS.

Causal graph reachability is not intervention semantics.
Do not claim do(X), counterfactual, conditional-causality or causal-effect magnitude from ordinary CAUSES paths unless a separate capability implements and passes those semantics.

When ingesting causal prose:
- source/provenance is mandatory;
- unknown causal endpoints must not be invented from syntax alone;
- qualify event labels with relevant context when an unqualified causal claim would be over-broad.


---

## 23. Intra-chunk dependency protocol

A real explanatory chunk may define a concept and then use it in a later relation inside the same chunk.

Safe reader policy:
1. pass 1 admits only already-supported deterministic structures;
2. after pass-1 admissions, previously skipped surfaces may be re-run through the SAME parser once;
3. no new heuristic grammar may appear in retry;
4. if still unsupported, SKIP/GAP;
5. retry must preserve source/provenance.

SECOND PASS != GUESSING.

Explicit bounded grammar should outrank broader learned predicates when the broader parser would erase relation type. Example established by G289:
"X имеет свойство Y" => PROPERTY, not generic HAS("свойство Y").


---

## 24. Atomic pragmatics and prosody curriculum

Natural-language pretraining must not collapse slang/profanity/nonstandard forms into one sentiment label.

Separate:
surface form,
lexical identity,
speech act,
affect valence,
arousal/intensity,
stance,
target/addressee,
prosody,
discourse context,
world context,
social register,
confidence/ambiguity.

Required boundaries:
SURFACE FORM != INTENT.
PROFANITY != NEGATIVE AFFECT.
PROSODY != EMOTION.
INTONATION != TRUTH.
SLANG != ERROR.
UNDERSTAND != EMIT.

Train minimal contrasts:
same words / different prosody;
different words / same pragmatic act;
same words / different context or target;
prosody removed -> uncertainty should increase when interpretation depended on it.

Detailed future curriculum:
PRAGMATICS_PROSODY_ATOMIC_CURRICULUM_NOTE.md


---

## 25. Developmental cost reduction must be measured directly

A core C4 claim is not merely that stored knowledge grows, but that reusable structure makes later learning cheaper.

Preferred experiment:
1. generation A creates reusable hierarchy/schema/rules;
2. freeze a new-concept evaluation pack;
3. generation B adds only minimal concept classifications/definitions;
4. count how many strict held-out relations become available without direct target storage;
5. compare teacher/direct lesson cost to the previous stage;
6. retain false-inference controls and cold reload.

G291 -> G292 is the first explicit hierarchy-depth example:
- G291 created reusable leaf/mid/root structure;
- G292 added 16 new concept->leaf IS_A lessons and no new general semantic rules;
- those 16 lessons yielded 96/96 strict inherited relations;
- leverage = 6.0;
- direct target semantic facts = 0;
- negative controls 36/36 UNKNOWN;
- teacher questions 0.

This is evidence of curriculum-local cost reduction, not by itself a claim of general intelligence or universal emergent learning.


---

## 26. Disk-backed canonical runtime proof

G293 establishes the first canonical disk-backed graph runtime proof before large-model scaling.

Requirements demonstrated:
- same cognition in memory and SQLite modes;
- full canonical regression parity;
- lazy/indexed graph access;
- per-turn durable transaction;
- checkpoint import/export without semantic state change;
- USER_SAID carry-forward when newer weights replace the base checkpoint.

Do not treat .c4db size as model intelligence or learned-state size.
.c4m remains the canonical exchange/checkpoint artifact; .c4db is an execution representation.

Known engineering debt:
SQLite currently expands compressed checkpoints substantially on disk. Numeric IDs, shared string dictionaries and later architectural compression remain future work.
