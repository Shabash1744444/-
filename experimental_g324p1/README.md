# C4 G324-P1 — MATRYOSHKA / RECURSIVE CAUSAL CLOSURE

Date: 2026-10-08  
Status: **PHYSICAL EXPERIMENTAL CANDIDATE; NOT CANONICAL / NOT FULL GREEN**.  
Parent: G324-P0 isolated experiment (itself based on physically verified G322-P8). G309 remains canonical. G323-P9 is a separate candidate, not silently merged here.

## Hypothesis under test

Can an independently solved causal subgraph become a *typed interface* of a larger causal graph, recursively, without:
(a) losing combinatorial constraints; (b) creating independent evidence out of a child's own conclusions; (c) assigning COMMIT/DRIVE/MEDIATE authority to a read-only EVAL computation?

**Answer for finite structured problems: yes, subject to strict interface assumptions.** This is an explicit and narrower statement than "the four laws explain all cognition".

## One reusable mechanism

`runtime/c4child/recursive_closure.py`: project a child finite-domain constraint network onto shared public typed ports, preserving the candidate relation, **normalized soft marginal probabilities**, inherited evidence roots, and nesting depth. `glue()` joins such projections using the same generic `CausalConstraintClosure` engine. No reference to a single Russian phrase, one of the 54 cognitive phenomena, or a hand-authored intended conclusion is present in the compositional operator.

`runtime/c4child/causal_closure.py`: same P0 finite-domain engine, hardened with per-source contradictory root quarantine. Two mutually inconsistent statements from one evidence root are not treated as two independent supports, nor does choosing the maximum of them create an artificial preference. This new behavior applies to **read-only experimental EVAL**, **not** to the existing live epistemic COMMIT path.

## Conditional mathematical identity

For finite subgraphs F_i(X_i,Z_i), X_i the full exposed interface and Z_i hidden *private* variables, assume **(i)** distinct private variables across children; **(ii)** each cross-child shared variable is exposed at every boundary that uses it; **(iii)** source likelihood/evidence dependence is correctly factored (sources that share dependency roots are NOT independent); **(iv)** exact, budget-complete inference. Then:

    sum_{Z_1,...,Z_k} product_i F_i(X_i,Z_i)
       = product_i [sum_{Z_i} F_i(X_i,Z_i)]

up to overall normalization of posterior probability. This is a standard finite factorization identity, **not** a newly discovered universal law. Hence changing the grouping of children preserves the set of global external candidates and their conditional probability distribution, if those assumptions hold.

**Counterexamples and boundaries:**
- A shared variable hidden from a child interface makes the factorization **invalid**; the implementation rejects it with `HiddenSharedInterface`.
- Partial evaluation with budget exhaustion cannot be published as a complete relation; `IncompleteEvaluation`.
- Different child summaries sharing the same evidence root cannot have their probabilities multiplied as if independent; `SharedDependentRoot`.
- Exact duplicate child summaries are deduplicated to prevent certainty inflation by replay.
- A self-supporting cycle of constraints permits multiple fixed points; the presence of the cycle is NOT evidence that one unique external truth has been found.
- Potential calculations using untrusted or wrongly typed factor tables are only as reliable as their premises. The operator cannot certify that the world actually satisfies the supplied structural constraints.

## Four-law mapping — scope honestly bounded

- **EVAL:** `solve`, `project`, `glue` calculate candidate states and probabilities.
- **COMMIT:** no change of canonical world state is authorized by the operator; admission remains an external, separate guarded process.
- **DRIVE:** the operator does not choose whether to reason or act; host orchestration selects invocation, runtime DRIVE would need to own any autonomous invocation.
- **MEDIATE:** receipts/observations enter from independent channels, not from this computation. A nested model answer is NOT an external receipt.

The mapping is a **constitution-preserving design interpretation**, not proof of four-law universality. The operator itself is EVAL-only, so claiming it already realizes all four powers would be inaccurate.

## Tests (2026-10-08, local physical extraction)

| Suite | P0 baseline | P1 candidate |
|---|---:|---:|
| New P0 + P1 directed focused tests | 19 PASS | **42 PASS** |
| Full package pytest passing | 507 | **530** |
| Full package pytest failing | 27 | **27** |
| New failures relative to P0 | — | **0** |
| Randomized independent hidden-factor compositions | not tested | **256 fixed-seed cases passed** (within P1 focused test) |

The same 27 failing test identities are `FileNotFoundError` for historically referenced checkpoints/models not supplied in the distribution. **The full suite is not green.** The 256 randomized cases are toy finite CSPs compared to a direct exhaustive oracle, not 256 real perception/learning cases.

Directed tests cover: depth-9 nesting, associativity of candidate sets, posterior preservation, hidden private variable multiplicity, role/scope/time isolation, contradictory source roots, repeated self-/source replay, inconsistent cycles, incompleteness, invalid interfaces, and source dependence.

## What remains broken

1. The live G322 epistemic path can still elevate a false WORLD claim on the basis of three registered agreeing sources. **NOT FIXED** in this P1 experiment. Quarantining conflicts inside the read-only EVAL solver does not protect `EpistemicAdmission` unless it is safely integrated and real provenance validated.
2. There is no learned extraction of factor tables from sensory experience or language; the tests supply them.
3. No demonstration that all 54 empirical cognitive phenomena, their psychophysical exponents or their developmental processes arise from this framework.
4. `CausalLayer.solve` preserves probabilities for the experimental composed interface; direct use of the inner `.model.solve()` computes only feasible candidates, not the nested soft posterior. Clients must call the wrapper `solve()` for probabilities.
5. Exact enumeration can be exponential. Budget exhaustions must fail closed; production real-time perception needs approximate inference with explicit error bounds and preserved evidence dependencies.
6. Artificially naming EVAL/COMMIT/DRIVE/MEDIATE at every level is not evidence these roles uniquely emerge in evolution. Competing explanations include ordinary factor graphs and compositional dynamical systems.

## Next decisive test

Bring a **real, non-prestructured stream** of multi-modal events into a learned factor-generation path under the same typed-source contracts, then evaluate:
- transfer to unseen compositions;
- quantitative fit on held-out psychophysical/attention/memory phenomena, not 54 different XOR labels;
- negative controls, swapped frames and delayed external receipts;
- compare flat vs exact nested vs deliberately lossy approximate projections at equal time/memory budgets;
- full end-to-end false WORLD admission, including simulated sources, circular citations and collusion.

A real advancement would be *generalization and independent prediction from learned relations*, not just correctness of a solver fed the right relations.

## Scientific connections and caveat

- Compositional open dynamical systems and hierarchical interfaces: https://arxiv.org/abs/2206.03868
- Higher-order information and synergy: https://www.nature.com/articles/s44260-024-00011-1
- Distinguishing physical causation, statistical information and knowledge: https://link.springer.com/article/10.1007/s10441-025-09495-3
- Recursive structures of evolving intelligence (hypothesis, not established fact): https://doi.org/10.1016/j.biosystems.2025.105549

This work reuses established mathematical ideas; it does not establish intellectual novelty, discover physical laws, or demonstrate consciousness. The point is to test whether those ideas can serve as **one coherent implementation-independent organizational substrate** for C4.

**Persistence:** code, full test suite, result JSON, SHA256 and model in standalone zip; source and report saved on isolated GitHub branch, archive additionally uploaded to C4 candidates Library. Canonical state is unchanged.