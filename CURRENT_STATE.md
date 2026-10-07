# CURRENT STATE

Date: 2026-10-07
Canonical GREEN weights generation: G270
Canonical runtime generation: G269

Current organism:
- child_g270_fast_lemma_transfer_green.c4m
- 1756887 bytes
- SHA256 b081428bed0080f9982491247d98640009de4662d7f654c571946acd5e36fa1b

Canonical runtime:
- C4_RUNTIME_G269_KERNEL_FLOOR_DISCOURSE_GREEN_2026-10-07.zip
- SHA256 5541f67d56ec2cf0cd373cbff58801f0fa6d4445e333a229d34215813290475a

Combined:
- C4_G269_RUNTIME_PLUS_G270_WEIGHTS_2026-10-07.zip
- SHA256 2b62bcd06bd588324fd7aa3ebc5b1ddf7f7b6744089cdf961ae135ef8e457dde

Persistent binary recovery: personal Library /C4_Canonical/.

## G270 — Fast Lemma Transfer — CURRENT WEIGHTS
Parent: G266 object permanence weights.
Runtime change: none.

Purpose:
prove that Russian lexical growth can increase usable language surfaces through reusable morphology instead of storing every target form.

Training:
- 60 new noun lemmas
- five productive noun classes
- each target receives noun type + grammatical gender
- target WORD_FORM facts: 0
- anchor WORD_FORM facts: 38
- direct admitted facts: 158
- model growth: +19636 bytes

Held-out morphology:
- target-only baseline: 140/260
- after anchor families: 260/260
- wrong: 0
- unknown: 0
- productive suffix rules: 45 -> 56
- transfer/direct = 1.646
- marginal transfer/anchor = 3.158

Restraint:
- 19 unseen decoy lemmas
- 19/19 remained unresolved
- 0 false resolutions

Persistence:
- cold reload preserves 260/260

Dialogue surface check:
- о проекте -> проект
- о словаре -> словарь
- о ядре -> ядро

Regression:
- 288/297 PASS in 3.4 s
- only the same 9 missing G207/G137/G151/G153 historical artifacts
- 0 new semantic/runtime failures

## Runtime G269
G269 remains the canonical runtime:
- read-only admitted-fact retrieval
- resolve-only question paths
- provenance receipts
- bounded answers / more / why
- exact math oracle connection
- RussianDiscourseBridgeV1
- persisted dialogue history
- perspective/ellipsis/meta-language handling
- public-label firewall
- ASK awaiting-response gate
- questions do not create world entities/facts

## Current curriculum law
Do not optimize model size or raw corpus volume.

Primary direction:
direct lesson -> reusable structure -> unseen transfer -> near-miss restraint -> cold reload.

Every stage should reduce the cost of teaching the next stage.

## Immediate next work
Weights from G270:
1. regular verb morphology/conjugation transfer;
2. adjective agreement transfer;
3. dense semantic cells for high-utility core lemmas;
4. active gap utility / teacher-cost measurement;
5. fixed developmental benchmark at future size checkpoints.

Runtime remains G269 unless a reusable runtime counterexample requires repair.

## Scale constraint
Before aggressive 100-300MB growth:
disk-backed indexed graph + lazy loading + hot working set + incremental durable writes + checkpoint/export.

Do not solve scale by dropping provenance, UNKNOWN semantics, contradictions or source independence.

## Normative documents
- TRAINING_LAWS.md
- DEVELOPMENTAL_TRAINING_METHODOLOGY.md
- LEXICAL_GRAPH_SCALE_TARGETS.md
- RUSSIAN_CURRICULUM_BOOK_ROADMAP.md
- WEEK_ROADMAP_RUNTIME_WEIGHTS.md
- RUNTIME_ARCHITECTURE_PRINCIPLES.md
- MEMORY_CONSOLIDATION_COMPRESSION.md
