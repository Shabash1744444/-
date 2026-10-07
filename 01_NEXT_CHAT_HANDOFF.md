# NEXT CHAT HANDOFF — C4 G292 WEIGHTS + G289 RUNTIME

Weights:
child_g292_hierarchy_accelerated_concepts_green.c4m
1,952,929 bytes
SHA256 d5631373fbdf24f2bf7a8068ca768edc0a4e94765e5b43035c90c3712aa2d246

Runtime:
C4_RUNTIME_G289_MIXED_CHUNK_DEPENDENCY_GREEN_2026-10-07.zip
SHA256 8aedcf70f480ba821256d360d0c6139af915edcb477d4bdc969000b86c42a846

Combined:
C4_G289_RUNTIME_PLUS_G292_WEIGHTS_2026-10-07.zip
SHA256 6e6dc6b3ef89bc6c074285fcee23b63994b6d60e1c60a72cdb1b6a96ace8d89e

## G291
116 surfaces over four long explanatory chunks.
Direct source relations:
IS_A 68 / PROPERTY 12 / CAN 12 / CAUSES 24.
Held-out:
96/96 semantic inheritance, 24/24 causal CHAIN, 16/16 negatives UNKNOWN.
Direct member semantic leaks 0.
Cumulative and cold GREEN.

## G292
Purpose: test whether G291 hierarchy lowers next concept-learning cost.

16 new real instrument concepts.
60 surfaces.
44 known structural statements dedup.
16 new direct facts only, all concept -> leaf IS_A.
No new general semantic rules.

Each concept then inherits six controlled relations:
leaf PROPERTY/CAN,
mid PROPERTY/CAN,
root PROPERTY/USED_FOR.

Strict result:
96/96 after and cold.
Direct target semantic leaks 0.
Target WORD_FORM 0.
36/36 negative controls UNKNOWN.
Teacher questions 0.
Teacher words 0.
Learning leverage = 96 / 16 = 6.0.
Growth +3,423 bytes.

Full runtime regression 343/352; same nine historical missing-file failures only.

## Next
Keep testing declining direct lesson cost on genuinely new domains/concepts.
Increase passage diversity before expanding syntax.
Do not implement typo/prosody speculation into canonical runtime until isolated contrastive benchmarks exist.
