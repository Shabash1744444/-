# RUNTIME CURRENT — G271 MORPHOLOGY VERB GUARD

Canonical runtime: G271.
Canonical weights: G274.

## Files
Runtime:
- C4_RUNTIME_G271_MORPH_VERB_GUARD_GREEN_2026-10-07.zip
- 228891 bytes
- SHA256 5d7720e172017f0b32f2c0b92fcee3eb88e6a8be40580c454778eec6f6a76f31

Weights:
- child_g274_dense_semantic_core_green.c4m
- SHA256 6e566b67e54504fbdb9f2924bdba0ed330dce5ce525acb97234d5dd33676c20e

Combined:
- C4_G271_RUNTIME_PLUS_G274_WEIGHTS_2026-10-07.zip
- SHA256 e23bcff6cb54746d5aeda27b6d0477452eff81f6c291046706c00bdc97bd06d3

## Base architecture
G271 keeps G269 kernel-floor/discourse behavior and changes only productive morphology safety.

G269 capabilities remain:
- read-only admitted-fact retrieval
- resolve-only question paths
- provenance receipts
- bounded answers / more / why
- exact math oracle
- dialogue history/contextual ellipsis
- USER/C4 perspective
- meta-language handling
- public-label firewall
- ASK awaiting-response gate

## G271 repair
A productive transformation reconstructing a lemma suffix ending in `-ть` may apply only when the candidate has explicit verb evidence:
- PREDICATE_RELATION, or
- IS_A -> глагол.

This prevents forms such as `сеет / сеют / сел` from resolving to noun `сеть`.

## Validation
- full runtime suite: 289/298 PASS
- only 9 known missing historical artifact FileNotFoundErrors
- focused morphology tests: 7/7
- G270 noun compatibility: 260/260
- final G274 cumulative morphology remains GREEN
