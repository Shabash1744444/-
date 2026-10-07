# NEXT CHAT HANDOFF — C4 G290 WEIGHTS + G289 RUNTIME

Weights:
child_g290_mixed_explanatory_prose_green.c4m
1,933,483 bytes
SHA256 57ac0bac91d16fd320df838c41e527038bf70e2ee1c8a18e3403c997e3670a8a

Runtime:
C4_RUNTIME_G289_MIXED_CHUNK_DEPENDENCY_GREEN_2026-10-07.zip
SHA256 8aedcf70f480ba821256d360d0c6139af915edcb477d4bdc969000b86c42a846

Combined:
C4_G289_RUNTIME_PLUS_G290_WEIGHTS_2026-10-07.zip
SHA256 73238df880d2334de65528287d8f7817c29a4aa610df056d6a4e4617f8973233

## G289
Counterexamples:
1. same-chunk CAUSES could be skipped before endpoint definitions from that same chunk were admitted;
2. explicit "X имеет свойство Y" was overwritten by generic predicate "иметь" -> HAS.

Repair:
- one bounded deterministic retry after pass-1 admissions;
- explicit PROPERTY grammar has priority.

Regression: 343/352; same 9 historical missing artifacts only.

## G290
One mixed explanatory source, 64 surfaces.
Direct:
- IS_A 44
- PROPERTY 4
- USED_FOR 4
- CAUSES 12

Held-out:
- semantic inheritance 48/48, cold 48/48
- causal chains 12/12, cold 12/12
- cross-type controls 12/12 UNKNOWN
- direct leaks 0
- EXTERNAL_CORPUS provenance retained.

All prior cumulative skills GREEN.

## Next
Increase explanatory passage length and dependency depth gradually.
Do not add broader syntax by guessing.
Prefer relation-rich passages over isolated vocabulary.
Future AGENT track remains separate; see AGENT_TASK_LIFECYCLE_NOTE.md.
