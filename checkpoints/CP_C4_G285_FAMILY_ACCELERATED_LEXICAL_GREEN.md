# CP C4 G285 FAMILY-ACCELERATED LEXICAL GREEN

Canonical checkpoint source is mirrored in /C4_Canonical/CP_C4_G285_FAMILY_ACCELERATED_LEXICAL_GREEN.md.

Weights:
- child_g285_family_accelerated_lexical_green.c4m
- 1,898,738 bytes
- SHA256 634c07b755e727d15e98e56a5d3a82f757e44aea4b77320b0204834510a1872e

Result:
- 40 new context-discovered lexemes
- 40 teacher questions / 147 words
- 0 target WORD_FORM
- 60/60 unseen morphology, cold 60/60
- 27 lexemes in existing G284 families
- 108/108 strict direct-family-rule inherited relations
- 0 direct member copies
- 5/5 cross-family restraint
- full regression 335/344; only 9 known missing historical artifacts

RED caught before promotion:
invalid generated held-out form глянецом. Rebuilt clean without глянец.
 SEMANTIC FAMILY CONSOLIDATION GREEN

Date: 2026-10-07
Status: GREEN
Parent weights: G283
Runtime: G281

## Purpose
Factor already acquired G282/G283 concepts into reusable semantic families instead of continuing raw lexical accumulation.

## Standardized run
G284 is the first canonical batch executed under C4_PRETRAINING_STANDARD_0_TO_1GB.md.
Before lessons:
- source manifest was written;
- exact parent hashes recorded;
- 148 strict held-out member relations frozen;
- all 148 verified NOT TRUE on exact G283.

## Curriculum
37 existing concepts -> 6 reusable families:
- electrical quantity: 5 members
- optical parameter: 6
- geometric quantity: 10
- physical property: 6
- ecological parameter: 7
- spatial parameter: 3

Direct lessons:
- 37 member -> family relations
- 24 family-level shared rules
- 6 family -> root definitions
Total direct lessons: 67.

Teacher cost:
- 6 questions
- 24 teacher words

## Strict transfer
Shared family rules:
- PROPERTY measurable
- CAN change
- CAN be measured
- USED_FOR domain description

Held-out:
- before: 0/148
- after: 148/148
- cold reload: 148/148
- direct held-out copies on member concepts: 0

Transfer/direct = 148 / 67 = 2.209.

## Restraint
Cross-family negative controls: 6/6 restrained.
No contamination such as acidity inheriting electrical-system use or voltage inheriting environment use.

## Cumulative
G270 nouns 260/260
G272 verbs 756/756
G273 adjectives 780/780
G274 semantics 472/472
G277 measurement 78/78
G279 prose 184/184
G280 strict-new 327/327
G282 morphology 31/31
G283 morphology 52/52
G284 semantic families 148/148

Full runtime regression:
335/344 PASS.
All 9 failures are unchanged FileNotFoundError cases for missing historical G207/G137/G151/G153 artifacts.

## Artifact
child_g284_semantic_family_consolidation_green.c4m
1,885,002 bytes
SHA256 efcdf9c63116fc056bf3fc19deeda83e62b08f922fe4123136b5a733f8b3a95b
Growth vs G283: +8,642 bytes

Release:
C4_G284_SEMANTIC_FAMILY_CONSOLIDATION_GREEN_2026-10-07.zip
SHA256 650233c967e0c5f00b6002f0b6b7db6d716a370d1d8ffc5df64802f2efff7f17

Combined:
C4_G281_RUNTIME_PLUS_G284_WEIGHTS_2026-10-07.zip
SHA256 1c99dc714e8e38ee975fc9be28f48a5860825648f1c78561c4032819ce5d4219

## Methodology lesson
GLOBAL GAP MEMORY != RUN-LOCAL TRAINING QUEUE.

A bounded training run must answer exactly one scoped gap, re-evaluate, then rank again. Historical unresolved gaps stay in organism memory but do not automatically drain into the active curriculum.
