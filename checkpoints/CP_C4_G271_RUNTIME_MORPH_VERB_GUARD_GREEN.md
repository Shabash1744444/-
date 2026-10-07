# CP C4 G271 RUNTIME MORPH VERB GUARD GREEN

Date: 2026-10-07
Status: GREEN
Parent runtime: G269
Weights changed: NO
Compatibility weights: G270

## Counterexample
Learned verb suffix rules could map real Russian surfaces `сеет / сеют / сею / сел / села / сели` to the noun concept `сеть` because the old resolver guessed lexical POS from orthography.

## Minimal repair
Productive transforms whose reconstructed lemma suffix ends in `-ть` require explicit verb evidence:
- `PREDICATE_RELATION`, or
- `IS_A -> глагол`.

Exact admitted aliases remain authoritative.

## Validation
- G270 noun held-out remains 260/260.
- verb/noun collision controls: 10/10 restrained.
- focused morphology tests: 7/7 PASS.
- full runtime suite: 289/298 PASS.
- the 9 failures are unchanged missing historical G207/G137/G151/G153 artifacts.
- new semantic/runtime failures: 0.

## Artifact
- C4_RUNTIME_G271_MORPH_VERB_GUARD_GREEN_2026-10-07.zip
- 228891 bytes
- SHA256 5d7720e172017f0b32f2c0b92fcee3eb88e6a8be40580c454778eec6f6a76f31

Law: ORTHOGRAPHIC SUFFIX != LEXICAL POS.
