# CP C4 G280 GUIDED EVERYDAY CORE GREEN

Date: 2026-10-07
Status: GREEN
Parent weights: G279
Runtime: G278

## Goal
Scale the already-safe guided-reading path to a larger everyday semantic block without inflating transfer using relations that were already true in G279.

## Curriculum
- 109 everyday concepts.
- 118 ordinary Russian text surfaces.
- parsed 118/118; skipped 0.
- eight reusable semantic classes.
- class membership and shared purpose came from EXTERNAL_CORPUS prose.
- eight missing class->parent links were deliberately left for ActiveGaps.

## Teacher burden
Questions were ordered by expected unlock:
24 -> 15 -> 14 -> 14 -> 12 -> 12 -> 10 -> 8.

Teacher cost:
- 8 questions
- 8 relations
- 24 words in minimal answer surfaces

## Strict held-out novelty
Target set: 338 relations.
- true before teacher: 124/338
- true after: 338/338
- cold: 338/338

A transfer counts only when that exact relation was NOT TRUE on exact G279 before training, became TRUE in G280, and remained TRUE after cold reload.

- strict novel transitions: 327
- direct new lessons: 126
- transfer/direct: 2.595

## Artifact
- child_g280_guided_everyday_core_green.c4m
- 1,846,970 bytes
- growth vs G279: +20,757 bytes
- SHA256 8cae07434b776d9a101bb7390bfee930a0ca845d790dca9945e3544502006f8a

Weight release:
- C4_G280_GUIDED_EVERYDAY_CORE_GREEN_2026-10-07.zip
- SHA256 c09e4868e894b67f39e3b679f38eea1987181292357ee225775337a47fdf1ced

Combined with exact G278 runtime:
- C4_G278_RUNTIME_PLUS_G280_WEIGHTS_2026-10-07.zip
- SHA256 7a57a75082c7e294aefe2b99a610a7286449b3a0a572618654c4beaca3e562ab

## Cumulative
- G270 nouns 260/260
- G272 verbs 756/756
- G273 adjectives 780/780
- G274 semantics 472/472
- G277 measurement 78/78
- G279 prose 184/184
- G280 strict novel 327/327
- verb/noun restraint preserved
- homograph boundaries preserved
- unsupported reader probe: 0 entity / 0 fact growth
- rejected external test token absent

## Next
Quality-first lexical hypotheses for unknown inflected terms inside action/predicate clauses. A hypothesis may create a question but never a graph fact. Ambiguous and irregular forms must remain unresolved.
