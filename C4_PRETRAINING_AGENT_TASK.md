# C4 PRETRAINING AGENT TASK

Use this file as the ready-to-run assignment for an autonomous training agent.

## Mission

Develop a C4 organism from the exact supplied physical GREEN checkpoint toward the requested scale/capability milestone while maximizing reusable capability and minimizing teacher cost.

DO NOT optimize for bytes, generation count, books consumed or raw fact count.

Primary objective:

more reusable structure
-> less teacher work for the next domain
-> more held-out transfer
-> stable restraint/provenance
-> less redundant storage.

## Mandatory reading before any mutation

1. 00_READ_ME_FIRST.md
2. CURRENT_STATE.md
3. 01_NEXT_CHAT_HANDOFF.md
4. C4_PRETRAINING_STANDARD_0_TO_1GB.md
5. TRAINING_LAWS.md
6. DEVELOPMENTAL_TRAINING_METHODOLOGY.md
7. MEMORY_CONSOLIDATION_COMPRESSION.md
8. RUNTIME_ARCHITECTURE_PRINCIPLES.md
9. C4_AUTOTRAINER_SPEC.md
10. latest physical checkpoint + metrics + quarantine ledger.

Repository state and physical artifact hashes outrank chat/model memory.

## Startup contract

Before training:
- verify runtime SHA256;
- verify weights SHA256;
- cold-open exact weights;
- run current regression/smoke suite;
- create run_id;
- create source manifest;
- create quarantine ledger;
- generate AND VALIDATE candidate held-out set;
- freeze valid held-out before teaching;
- record baseline bytes/entities/facts/evidence/latency where available.

Do not start if parent artifact cannot be reproduced exactly.

## Training loop

For one bounded curriculum block:

material
-> safe parse
-> dedup against current organism
-> genuine gaps only
-> RUN-LOCAL queue
-> choose ONE highest-value gap
-> ONE teacher answer
-> re-evaluate
-> rerank
-> continue until predefined competency/stop condition
-> held-out
-> restraint
-> cold reload
-> cumulative prior-skill regression
-> full runtime regression
-> physical checkpoint if GREEN.

GLOBAL GAP MEMORY != RUN-LOCAL TRAINING QUEUE.

## Never do

- do not guess lemma and commit it as fact;
- do not teach a target-specific alias merely to fix held-out;
- do not let questions create facts;
- do not count already-TRUE relations as novel transfer;
- do not accept automatically generated held-out as ground truth without validation;
- do not bulk dump book text;
- do not flatten source/narrator/fiction boundaries;
- do not weaken epistemic laws to pass an exam;
- do not continue canonical lineage from RED/EXPERIMENTAL state;
- do not reconstruct lost work from memory.

## Runtime vs training decision

If a reusable capability fails across unrelated domains, classify/investigate a runtime defect.

If acquisition machinery works but a domain lacks actual knowledge, train persistent state.

RUNTIME BUG != WEIGHT GAP.
WEIGHT GAP != RUNTIME BUG.

Runtime changes require their own generation/checkpoint/regression before weight training continues.

## Metrics required for every batch

- parent hashes;
- source IDs/classes;
- attempted/parsed/skipped material;
- direct lessons;
- questions;
- teacher words;
- teacher relations;
- held-out before/after;
- strict-new transfer;
- correct UNKNOWN;
- false inference;
- quarantine count;
- direct target leaks;
- cold reload;
- cumulative regression;
- bytes before/after;
- latency/memory where scale-relevant;
- artifact SHA256.

Report morphology, semantic, causal, discourse and agent metrics separately. Do not create a meaningless combined ratio across heterogeneous abilities.

## RED protocol

On any real RED:
1. stop promotion;
2. preserve counterexample;
3. identify R/E/M/I/T failure class;
4. discard dirty candidate or mark EXPERIMENTAL;
5. repair reusable cause only;
6. restart training from last physical GREEN when the candidate was contaminated;
7. re-run exact counterexample + full regression.

Quality outranks progress.

## GREEN promotion

A generation exists only after:
- held-out GREEN;
- restraint GREEN;
- cold reload GREEN;
- previous cumulative GREEN;
- full runtime regression unchanged except documented historical missing files;
- physical artifact written;
- SHA256 + bytes recorded;
- checkpoint written;
- Library/canonical storage updated;
- CURRENT_STATE/HANDOFF/MANIFEST/JOURNAL updated.

## Scale mission

Use the gates in C4_PRETRAINING_STANDARD_0_TO_1GB.md.

Do not interpret “train to 1 GB” as “make a 1 GB file.”

At each gate ask:
Has the next domain become cheaper to learn?

If not, stop growth and improve structure/curriculum/runtime/consolidation first.

## Agent capability

Agent/embodiment training is a separate curriculum profile.
Do not mix its scores into lexical/book pretraining.

Future agent loop:
perception -> goal -> plan -> action request -> environment receipt -> verified outcome -> correction -> reusable skill schema.

ACTION_REQUEST != VERIFIED OUTCOME.

## Deliverable at interruption

If execution must stop:
- never claim unfinished candidate as canonical;
- leave exact latest GREEN hashes;
- current run status;
- RED counterexamples;
- next action;
- all generated files physically written.

The next agent must be able to resume without this agent's hidden memory.
