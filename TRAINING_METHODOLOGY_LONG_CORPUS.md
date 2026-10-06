# C4 LONG-CORPUS TRAINING METHODOLOGY

This file is normative for the current training line.

## 1. Physical learning criterion
A prepared lesson is NOT learning.
A claim may be called learned only after:
- it is admitted through the organism's existing learning path;
- the saved .c4m physically contains the resulting state;
- held-out/paraphrase/transfer tests pass;
- cold reload passes;
- regression shows no new unacceptable breakage;
- bytes + SHA256 + checkpoint are recorded.

## 2. Source decomposition
For books and other long sources, never flatten source text into canonical truth.
Represent at minimum:
SOURCE -> SECTION -> CLAIM
and distinguish author, editor, translator/commentator when relevant.

A source can be useful while wrong.
A correction is a new sourced event, not retroactive alteration of the original source.

## 3. Expansion rather than copying
Do not copy a long book into the graph.
For each semantic chunk derive compact structured lessons:
- entities/concepts
- typed relations
- causal/temporal/spatial structure only where supported
- definitions and distinctions
- provenance
- uncertainty/status
- paraphrases
- language phenomena
- counterexamples
- transfer questions

Expansion is allowed because one passage can teach many relations, but do not manufacture factual claims absent from the source unless explicitly labeled TEACHER_REFERENCE/EXTERNAL_SYSTEM_FACT.

## 4. Combo language learning
World knowledge and language grow together.
Each suitable unit should carry 2-3 language mechanisms, e.g.:
WORLD: light from distant star carries information from an earlier state
LANGUAGE: "вглядываться в прошлое" is figurative; "новость ещё не дошла" is figurative; temporal reference
EPISTEMICS: present observation can concern a past state; observation time != event time
TRANSFER: novel paraphrases and literal/figurative traps.

SIMILARITY != IDENTITY.
SHARED WORD != IDENTICAL PROCESS.

## 5. RED policy
RED is evidence, not embarrassment.
Never promote RED.
Before runtime repair ask:
- Is relation type appropriate?
- Is this a functional/special relation?
- Did teacher violate existing admission contract?
- Is exam testing memorization instead of represented capability?
- Is requested capability outside current physics?

If capability is outside current physics, record boundary. Do not fake it.

## 6. Runtime changes
No runtime-law changes merely to absorb a curriculum.
A runtime change requires a general counterexample showing an architectural/implementation defect, followed by minimal repair and old+new regression.

## 7. Exams
Use unseen wording.
Separate:
- memorized/direct fact
- inferred/structural transfer
- restraint/UNKNOWN
- source attribution
- conflict handling
- figurative-language interpretation
- SELF/OTHER transfer traps

Cold reload is mandatory for GREEN promotion.

## 8. Growth metrics
Track:
- .c4m bytes
- new/dedup/rejected lessons
- direct facts
- positive transfer
- restraint
- contamination/correction behavior
- cold results
- regression
- runtime changes
- SHA256

Never optimize byte count itself. 1 MiB and 30 MB are milestones, not objectives.

## 9. Checkpoint discipline
Checkpoint before risky/long operations and after every GREEN generation.
Unsaved work is lost.
Every checkpoint must identify exact parent baseline and exact output artifact.

## 10. Current Bryson protocol
Read by semantic arc, not arbitrary byte count.
Current opening arcs:
A. how knowledge is produced/corrected
B. cosmic scale and models
C. light, distance and seeing the past
D. supernovae, hypothesis and prediction
E. measurement and scientific institutions
F. chemistry, obsolete concepts, independent discovery
G. editor corrections as live source-conflict training

Keep narrative richness in the teaching material while storing compact reusable semantics in the organism.
