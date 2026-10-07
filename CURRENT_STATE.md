# CURRENT STATE

Date: 2026-10-07
Canonical GREEN weights generation: G274
Canonical runtime generation: G271

Current organism:
- child_g274_dense_semantic_core_green.c4m
- 1805052 bytes
- SHA256 6e566b67e54504fbdb9f2924bdba0ed330dce5ce525acb97234d5dd33676c20e

Canonical runtime:
- C4_RUNTIME_G271_MORPH_VERB_GUARD_GREEN_2026-10-07.zip
- 228891 bytes
- SHA256 5d7720e172017f0b32f2c0b92fcee3eb88e6a8be40580c454778eec6f6a76f31

Combined:
- C4_G271_RUNTIME_PLUS_G274_WEIGHTS_2026-10-07.zip
- 2036899 bytes
- SHA256 e23bcff6cb54746d5aeda27b6d0477452eff81f6c291046706c00bdc97bd06d3

Persistent binary recovery: personal Library /C4_Canonical/.

## G271 runtime safety
Counterexample: real verb surfaces could resolve to noun `сеть`.
Repair: productive transforms reconstructing lemma suffix `-ть` require explicit verb evidence.
Validation: 289/298 runtime suite; same 9 missing historical artifacts; G270 noun transfer stays 260/260.

## G272 verb transfer
- 84 target lemmas
- 0 target WORD_FORM
- 36 anchor WORD_FORM
- 128 direct facts
- 756/756 held-out
- transfer/direct 5.906
- marginal transfer/anchor 10.444
- +17060 bytes

## G273 adjective transfer
- 78 target lemmas
- 0 target WORD_FORM
- 16 anchor WORD_FORM
- 99 direct facts
- 780/780 held-out
- transfer/direct 7.879
- marginal transfer/anchor 15.750
- +13847 bytes

Homograph quarantine is normative:
`целый/целое`, `лёгкий/лёгкое`, `дорогой/дорога` are not force-merged.

## G274 Dense Semantic Core
- 92 semantic members
- 114 direct facts
- 472 novel derived truths
- IS_A 181 / PROPERTY 114 / CAN 105 / USED_FOR 72
- transfer/direct 4.140
- 10 decoys / 0 false transitions
- cold reload 472/472
- +17258 bytes

## Cumulative final state
- G270 nouns: 260/260
- G272 verbs: 756/756
- G273 adjectives: 780/780
- G274 semantic derivations: 472/472
- G271 verb guard: 10/10 restraint

G270 -> G274 weight growth: +48165 bytes.

## Curriculum law
Do not maximize facts.
Optimize:
direct lesson -> reusable structure -> unseen transfer -> restraint -> cold reload -> cumulative retention.

## Immediate next work
ActiveGaps / Teacher Cost:
- score gaps by downstream utility;
- ask only questions that unlock many blocked relations;
- create a fixed unseen-text benchmark;
- track teacher questions, teacher relations, correctly UNKNOWN, false inference and final competency.

Then begin GUIDED reading on small texts before broad book scaling.

## Scale prerequisite
Before aggressive 100-300MB growth:
disk-backed indexed graph + lazy loading + hot working set + incremental durable writes + checkpoint/export.
