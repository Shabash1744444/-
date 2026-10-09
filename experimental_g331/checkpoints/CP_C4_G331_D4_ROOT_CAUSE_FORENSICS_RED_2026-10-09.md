# C4 G331 — D4 ROOT CAUSE FORENSICS (2026-10-09)

**Status: RED; read-only forensic study. No C4 weights, source runtime, four-owner constitution or Android host changed.**

## Source pins
- Native P2C C4M: `36e9fb9c54691d1ba7a0625e88d65d85017d60d4e4a021d320ecbd8a064ee385`.
- Native D4 research C4M: `04495a5f558a0974d7084b4597529ccc897c71a2558de88cccf0f7e365188480`.
- Original D4 full evidence ZIP `a93d590dab58305deaaa5b1a82b67d05a9135dd0c768e46c7dead8765cde1468`; frozen challenge SHA `42385c3807e41fd38815e09ebba921e41bffd907c9f078c8da9ae0489916409d`.
- Teacher dataset SHA `e1cc242f71aa969dc1382059450b6f022ab4c7ff9f4b9f03b3ed76d711f9d4b2`.

## Direct causes verified on actual model code and frozen weights
1. **Teacher label collapse.** In 1880 synthetic training rows, 163 negated-attribution utterances, 36 negated inner propositions, 41 denials all receive one unscoped `POLARITY=не`; 51 reported speech acts (`говорит`) receive `BELIEF`; 67 proposals (`Пусть в сказке`) receive `NARRATOR`. This is not a valid semantic training target for ordinary Russian.
2. **Real output collisions.** In both cold-loaded P2C and D4 C4M, semantic projection of `Мира не думает, что куб синий` equals `Мира думает, что куб не синий`. `Мира говорит...` equals `Мира думает...` likewise. They are logically distinct; the typed role/intent/polarity projection loses operator scope even though the raw text/tags may still be available.
3. **Heldout failure decomposition.** For 100 frozen novel grammar cases, P2C correct 22, erroneous/missing/extra role 63, other rejection 15. D4 correct 27, erroneous role 70, other rejection 3. Primary measured failure is role composition, not merely lack of lexical labels.
4. **Replay comparison confounded.** D4 `negatives+300 OTHER` vs `negatives+180 OTHER+120 old-positive` changed 2 factors. Added independently preregistered equal-update comparator `negatives+180 OTHER+120 duplicate negatives`: seed 23 old-positive 61 vs replay 72 vs naive 113; seed 37 old-positive 76 vs replay 110 vs naive 62. Thus replay helps against count-matched reduced-OTHER controls in these 2 seeds, but not uniformly versus original naive. No stable continual-learning method proved.
5. **Architecture distinction.** Existing `structured_cognition._ctx` stores 1- and 2-level `BELIEF` perspective frames under STORY, showing a richer structural substrate than flat D2 roles. It does NOT prove learnable NL→frame composition, nor scoped NOT handling. Existing C4 four laws not implicated by this test.

## Tests and reproducibility
- First combined run: `18 passed / 4 expected failures / 1 file-path failure` (historical report path missing).
- Exact same suites re-run with explicit existing report path: **19 PASS / 4 strict XFAIL**, no unexpected failures. Four strict XFAIL are required distinction between negative scopes and SAY/BELIEVE for P2C+D4, not evidence of success.
- Existing D4 frozen bytes and models not changed; no new training output promoted. Full historical suite and live Android not run.
- Self-contained ZIP `C4_D4_ROOT_CAUSE_FORENSIC_2026-10-09.zip`, SHA256 `627b8696a6a777a17f026c2c3db6488e6ca3a6311e453bd232225cb7e3b4ce80`, ZIP test CRC OK, includes original D4 evidence ZIP and complete new scripts/reports/tests/logs.
- Saved in personal Library `/C4_Candidates/G331_NATIVE_COGNITION/D4_ROOT_CAUSE_FORENSICS_2026_10_09/` alongside readable README and JSON.

## Stop/go conclusion
**D4 remains RED.** This research shows concrete flaws in *teacher semantic labels*, *flat learned readout* and *training comparison*. It **does not** establish a global C4 architecture limit or LLM replacement ability.
Next allowable narrow task: construct an independent scoped semantic gold contract distinguishing `NOT(BELIEF(...))`, `BELIEF(NOT(...))`, `SAY`, `PROPOSE`, and nested `BELIEF` with preserved provenance; preregister unseen syntax and role reversals; train ONE generic native C4 operator on model COPY with code-identical zero-weight and label-shuffle controls; verify >multiple seeds, cold C4M and four-law safety. No hardcoded per-phrase semantics, no Qwen mass distillation and no broader development until this passes.

**User priority**: understand real bound of C4 before general architecture work.