# C4 D7 — multi-route continuous cognition: candidate mathematics, not an implemented cognitive engine

**Scope:** incremental hypothesis in independently designed C4, separate from Singularity OS. The research objective is *persistent cognitive dynamics*, not merely a chatbot pass count.

## 1. State with different lifetimes

At physical time t let `S_t = (G_t, E_{≤t}, W_t, Θ_t)`:
- `G_t`: persistent provenance-bearing typed graph; existing C4Graph and four-owner admissibility rules unchanged.
- `E_{≤t}`: immutable raw source episodes (message, time, actor/source root, transcript) and receipts. The unmodified primary source remains retrievable for reconstruction.
- `W_t`: active, volatile working graph/hypothesis set, attention, unresolved questions, partial plans, current interpretation versions.
- `Θ_t`: learned weights for retrieval, graph-edge proposals, semantic/speech alignment and value of cognitive actions.

This does not require a second canonical brain: W is a *view/working set over the one G and E*, not an independent truth database. Historical interpretations H_i^v are derived from E_i and retain that source dependency.

## 2. Multi-path internal dynamics

At each internal cognition iteration k, in response to an external event or own previously generated candidate:

`r_k ~ π_η(r | W_t^k, G_t, E_{≤t}, uncertainty, cost)`

The route r may request token-level reanalysis, phrase-level syntax, an alternative learned relational graph, episode retrieval, actor/source re-grounding, temporal chains, competing interpretations or counterexample search. **These are trainable operation families, not hand-authored Russian phrase cases.**

`Z_k = Retrieve_θ(E_{≤t}, G_t, route=r_k, query=W_t^k)`

`W_t^{k+1} = Update_θ(W_t^k, Z_k, G_t, context_t, r_k)`

Some possible learned dynamics on active typed nodes:

`m_v^k = Σ_(u,r,v) α_θ(h_u^k, h_v^k, r, context) · W_r h_u^k`

`h_v^{k+1} = GRU_θ(h_v^k, m_v^k, Z_k)`

`P_θ(edge u→v, type r | W,E,G) = softmax(score_θ(u,v,r,W,E,G))`

Graph *edge topology* and nonlinear composition must be learnable; a chain-only constructor is insufficient (D3/D5). The `GRU` here is an optional local recurrence cell, not replacement of the source/state substrate with a monolithic RWKV/Transformer.

## 3. Joint hypothesis scoring and source invariants

`Score_θ(H) = s_word + s_phrase + s_operator + s_attachment + s_scope + s_time + s_context - penalties`.

Scores are **compatibility** measures, *not* factual truth or independent evidence. A hypothesis must maintain a dependency DAG back to each actual source episode. Iterating on H_i^(v) cannot create fresh root evidence: `root(H_i^(v+1)) ⊆ root(H_i^(v)) ∪ root(new_external_evidence)`. Repeated interpretations of the same E_i must not be counted as independent observations.

`EVAL` creates/ranks candidate hypotheses; `COMMIT` checks source/authority, preserves version history; `DRIVE` alone selects internal cognitive next step or public act; `MEDIATE` keeps host intents distinct from verified world results.

## 4. Stopping, interruption, uncertainty

`ΔU_k = Expected[reduction in semantic ambiguity OR genuinely new inference] - λ_compute·cost_k - λ_risk·false-positive-risk_k - λ_loop·stagnation_k`.

DRIVE may stop or switch route if ΔU non-positive, no new constraints, deadline/resource limit, or a more important external event arrived. **100 steps are not an objective.** Single candidate abstention must remain available even after 100 passes. Avoid confidence escalation caused solely by counting repeated internal hypotheses as new evidence.

## 5. D7 actual empirical evidence from unmodified C4 weights

- Native D5 16,731 cold fact graph SHA256 `b7b2dd0f826bbc217f2a5499e53ba554a61c415817fe5d1f2c5313f2caa81036`.
- Existing learned D3 token/scope weights and D5 edge-attachment weights: `K-best` alternative BIO/operator paths (dynamic programming) → real D5 learned graph-attachment scorer. First structurally valid interpretation used as an *exploratory* decision; no gold labels used at inference.
- Old heldout synthetic reversed 32: K=1 21/32; K≥2 25/32. Frozen manually composed Russian 10: K=1 4/10, K≥8 5/10. OOD six unrelated utterances wrongly receiving a structural CANDIDATE: K=1 1/6, K≥8 5/6.
- This is **not** a learning experiment and the selection mechanism is a heuristic used to isolate benefit/risk of multiple hypotheses. It is not the final C4 learning methodology. It does **not** imply end-to-end free dialogue or improve sentence generation.
- On a separate previously verified D6 controlled graph task, 4 graph hops required 4 recurrent iterations to solve 200/200, but 100 iterations overshot task scope and yielded 194/200. That graph was provided and only a scalar was learned; it does not attest general cognitive self-reasoning.

## 6. Next falsifiable test Claude should design

An *end-to-end* small C4 organism, on SAME native C4Graph and user_message pathway, comparing (A) one static tagger, (B) 100 repeats of same hypothesis, (C) K alternative hypotheses without retrieval, (D) learned memory-replay route selector, (E) trainable multiscale graph dynamics with stopping calibration, and (F) compute-matched non-recursive capacity control.

Preregister human-authored new grammatical families; test owner inversion, arbitrary embedding, negation scope, speaker/reference/time, recurrences to immutable original episodes, delayed self-initiation, OOD false positives, calibration, cold reload and complete prior regressions. Use multiple seeds with equal teacher/cost budgets, independent teacher roots versus real external outcomes, and non-language graph generalization. If there is no genuine held-out transfer and no public language generation, this remains a specialist cognitive/provenance module. No Qwen-Omni mass synthetic distillation until qualified.

## 7. Current decision

**Multiple hypothesis routes = promising additional compute process, empirically useful in an old C4 task but actively dangerous without confidence calibration.** Dynamic architecture is a design direction, NOT yet proven neural intelligence. Existing C4 memory and four laws are valuable; general language remains RED.

## 8. Independent-from-prior-generator research challenge (2026-10-09)

Fresh assistant-authored (not external human) Russian assertions/requests frozen *before first D7 evaluation*, source sha256 `1e039d9bedf981a4478025d157b2b2d3407199d18c8d53713ea231a5d7213f98`: correct full AST 1/10→4/10 from K=1→32, but spurious CANDIDATE 1/10→9/10 on structurally inappropriate utterances. This **falsifies the naive rule that additional alternative hypotheses should be admitted if a valid structure can be found**. All measurements are candidate-level, no WORLD commitment. D7 must be represented to Claude as two separate gates: hypothesis *coverage* and false-positive *precision/calibration*. Any learned revision/replay policy must optimize both simultaneously and verify against independent future authored examples.