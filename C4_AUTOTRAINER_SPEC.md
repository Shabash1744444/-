# C4 AUTOTRAINER — FUTURE ORCHESTRATOR SPEC

Status: DESIGN SPECIFICATION. NOT YET CANONICAL RUNTIME.
Date: 2026-10-07

Purpose:
build a reproducible training application that accepts books/corpora/material and drives C4 through the normative pretraining loop without turning an external LLM into hidden cognition.

AutoTrainer is an orchestration layer around C4.
It is NOT C4's mind and must not silently inject unsupported world truth.

## Desired user flow

Input:
- starting runtime;
- starting .c4m;
- folder/files/books/corpus;
- source class + provenance/license metadata;
- target curriculum profile;
- optional teacher provider;
- evaluation pack.

Output:
- next GREEN .c4m generations;
- metrics;
- checkpoints;
- source/provenance ledger;
- quarantine ledger;
- rejected/skipped material;
- combined recovery packages;
- resumable run state.

## Pipeline

1. SOURCE REGISTRY
Register files, hashes, rights, language, authority/scope and TRAINING/TEACHER_ONLY/EVALUATION_ONLY status.

2. CHUNKER
Produce deterministic passage/chapter units with stable IDs.
No semantic admission here.

3. SAFE READER
Pass text through current canonical guided reader.
Output:
- admitted supported structures;
- skipped sentences;
- raw lexical gaps;
- semantic gaps;
- ambiguities.

4. DEDUP / BASELINE
Compare proposed capability targets against exact parent organism.
Already-TRUE targets may be retained for corroboration where appropriate but do not count as novel transfer.

5. GAP SCHEDULER
Rank:
expected downstream unlock / estimated teacher cost.
Ask one high-value question at a time.

6. TEACHER ADAPTER
Possible teacher:
- human;
- trusted curated dictionary/corpus;
- external LLM in TEACHER_ONLY role.

All teacher answers receive explicit provenance.
LLM answer confidence is not authority.
Teacher may propose; C4 admission laws decide.

7. LESSON EXECUTOR
Apply minimal structural answer.
Re-evaluate gaps immediately.
Never dump a whole generated explanation as one opaque fact.

8. EXAM GENERATOR
Generate held-out combinations from known pieces.
Freeze exam before teaching answers.
Track:
memorized / inferred / correctly unknown / false inference.

9. RESTRAINT SUITE
Homographs, irregular forms, unsupported syntax, source conflicts, negative controls.

10. COLD RELOAD
Persist and reopen exact candidate.

11. CUMULATIVE REGRESSION
Run all protected prior capabilities.

12. CONSOLIDATOR
Optional only when normative consolidation gate triggers.
Must produce before/after audit.

13. CHECKPOINT MANAGER
On GREEN:
hash, package, metrics, checkpoint, manifest, handoff.
On RED:
discard candidate weights or retain as EXPERIMENTAL only; resume canonical from parent.

## Data model for a run

run_id
parent_runtime_sha
parent_weights_sha
source_manifest
eval_manifest
curriculum_stage
random_seed
teacher_provider
teacher_source_id
direct_lessons
questions
teacher_words
teacher_relations
admitted
rejected
skipped
quarantined
heldout_before
heldout_after
false_inference
correct_unknown
bytes_before
bytes_after
latency_before_after
cold_reload
cumulative_results
artifact_hashes

## Required modes

BOOTSTRAP
high teacher involvement; builds reusable substrate.

GUIDED
C4 reads supported material, ranks gaps and asks targeted questions.

AUTONOMOUS
future mode only after contamination/retraction benchmarks prove safe.
C4 selects material/hypotheses but source and admission laws remain active.

## Proposed CLI

c4train init --runtime <zip> --weights <c4m> --run <dir>

c4train add-source <path> --class TRAINING --source-id <id> --license <tag>

c4train ingest --profile russian_guided --max-chunks 100

c4train answer-gaps --teacher human
or
c4train answer-gaps --teacher <teacher-adapter>

c4train exam

c4train consolidate --dry-run

c4train checkpoint --promote-if-green

c4train status

c4train resume

## UI idea

Simple desktop/mobile training console:
- source queue;
- current C4 question;
- teacher answer;
- gaps ranked by utility;
- capability/teacher-cost graphs;
- skipped/quarantine review;
- checkpoint button;
- source/provenance inspector.

Books can be dropped into an inbox, but ingestion must remain gated by safe parsing, rights metadata, held-out tests and checkpoint discipline.

## Safety boundary for external LLM teachers

EXTERNAL LLM != C4 COGNITION.

An LLM may:
- explain a gap;
- suggest lesson structure;
- generate adversarial exam candidates;
- propose source annotations.

It may not:
- directly mutate C4 graph outside admission APIs;
- mark its own statement as observation;
- fabricate independent source roots;
- see EVALUATION_ONLY answers during teaching;
- repair a failed held-out target with a hidden target-specific alias.

## Future agent curriculum

Agent capability should be a separate AutoTrainer profile rather than mixed into lexical/book pretraining.

Future profile may train:
perception -> goal -> plan -> action request -> environment receipt -> verified outcome -> correction -> skill schema.

Critical laws:
ACTION_REQUEST != VERIFIED OUTCOME.
RECEIPT != CAUSAL PROOF.
SIMULATION != OBSERVATION.

Agent competence should be benchmarked in sandbox environments with held-out tasks and long-horizon persistence.

## Implementation order

1. manifest + run ledger;
2. resumable checkpoint manager;
3. current G281/G283-style guided text ingestion;
4. gap/teacher queue;
5. held-out generator;
6. cumulative test runner;
7. metrics dashboard;
8. source-license/provenance UI;
9. consolidation runner;
10. only later autonomous material selection.

Do not build a giant GUI before the training loop is deterministic and resumable.


## Run-local scheduler requirement

AutoTrainer must distinguish:
- organism-global gap backlog;
- current-run gap queue.

Every ingested chunk attaches run/source cause IDs.
By default, answer-gaps operates only on gaps attributable to the active run or explicitly imported prerequisites.

Loop:
TOP scoped gap -> ONE question -> ONE answer -> refresh -> rerank.

Never drain several unanswered questions in one scheduler call.

Future commands:
- c4train gaps --scope current-run
- c4train gaps --scope global
- c4train import-gap <gap_id>
- c4train answer-next

This became a concrete requirement during standardized G284: unrelated historical gaps could compete with the current curriculum unless orchestration scoped the queue.


## Evaluation preflight

The EXAM GENERATOR must not be its own unquestioned oracle.

Pipeline:
candidate exam -> linguistic/semantic validator -> quarantine uncertain items -> freeze valid held-out -> train.

For morphology, generated forms need validation before they become expected answers.
For semantics, generated negative controls must be checked not to be secretly true through another legitimate sense or relation.

AutoTrainer should retain both:
- rejected-evaluation ledger;
- reason for rejection.

This requirement was promoted after G285 caught invalid autogenerated глянецом before canonicalization.


## Relation-level exam profile

AutoTrainer should provide a relation exam mode that distinguishes direct retrieval from structural inference.

For CAUSES:
- freeze direct source edges separately from non-adjacent endpoint tests;
- require derived endpoints to remain absent as direct facts;
- generate validated reverse/cross controls;
- for motifs, inspect direct-cause and direct-effect sets at convergence/divergence nodes;
- retain a provenance report for every direct edge;
- never label graph reachability as intervention/counterfactual competence.

Suggested report fields:
direct_relation_lessons
derived_relation_targets
derived_correct
direct_endpoint_leaks
reverse_controls_correct_unknown
cross_controls_correct_unknown
convergence_nodes_correct
divergence_nodes_correct
cold_relation_score
provenance_failures


## Mixed-chunk dependency pass

AutoTrainer safe-reader orchestration should support a bounded intra-chunk dependency retry:
pass 1 -> admit supported definitions/classes -> retry initially skipped surfaces once -> final skipped/gaps.

The retry uses the exact same deterministic parser and must not expand grammar or confidence.

Metrics:
pass1_parsed
retry_recovered
final_skipped
relation_type_counts
provenance_failures
cross_type_failures

This became required in G289/G290 when a single explanatory source mixed definitions, properties, functions and causal relations.
