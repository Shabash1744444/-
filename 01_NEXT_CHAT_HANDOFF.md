# NEXT CHAT HANDOFF — C4 G283 WEIGHTS + G281 RUNTIME

Weights:
child_g283_contextual_quantities_green.c4m
1,876,360 bytes
SHA256 011fc6ce852ca169f4a2e3e66d9025c334fa10c904757b1f0c76ce7031fd141e

Runtime:
C4_RUNTIME_G281_LEXICAL_GAPS_GREEN_2026-10-07.zip
SHA256 eb1572c417c25eb7e6ef5a9d2b620b5692ada859ff5011931a561625aa18bc04

Combined:
C4_G281_RUNTIME_PLUS_G283_WEIGHTS_2026-10-07.zip
SHA256 64fba4cf398d157a2239fb5819244eb23cf2520c1f5157f003e2d66bc25c7bc3

G281 full regression: 335/344, only 9 known missing historical artifacts.

G283:
- 32 new context-discovered concepts
- 64 supported action sentences
- 32 lexical questions / 96 teacher words
- 0 guessed lemmas
- 0 target WORD_FORM
- 52/52 unseen forms, cold 52/52
- full cumulative GREEN

Do not fix irregular words by target-specific alias just to pass. Keep a separate irregular curriculum.

Next: continue contextual guided learning, then consolidate high-reuse semantic families and measure teacher cost per new lexeme/domain.
