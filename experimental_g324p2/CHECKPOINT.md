# C4 G324-P2 — Bifurcation / Adaptive Graph / Reverse Recursion

**Date:** 2026-10-08  
**Status:** GREEN **ISOLATED EXPERIMENT**, NOT CANONICAL and NOT claim of AGI/consciousness.  
**Inherited from:** G324-P1 candidate (physically extracted), itself based on the G322-P8 runtime + graph. Canonical G309 unchanged. Model SHA256 unchanged: `6baf2864ce8a811738d13cf3593f739e8dcc5a8734d17ce0f5647bc23da06301`.

## Hypothesis under test

Organizational levels may arise in a recursive adaptive dynamical graph: **node state changes topology → topology changes collective dynamics → collective aggregates feed back to node dynamics → repeat**. This provides a minimal *dynamic* extension to static G324-P1 typed causal matryoshka. Test separately whether there are (a) bifurcations of state dynamics, (b) changes of graph connectivity, (c) feedback across scales. None is sufficient by itself to prove fractality, emergence of four laws or intelligence.

## Specific finite model

There are N nodes with states `0 ≤ x_i ≤ 1` and an undirected graph `G_t`.

* Local nonlinear map `f_i(x)=r_i*x_i*(1-x_i)` (already established logistic toy, **not** a discovered cognitive learning law).
* Neighbor pool `n_i` = average of `f_j` over adjacent nodes (self if isolated).
* Mesoscale `c_i` = average `f_j` over the current connected component of i.
* Macroscale `m` = average `f_j` over all nodes.
* Two-level feedback: `x_i(t+1)=(1-eps-beta-gamma)*f_i + eps*n_i+beta*c_i+gamma*m`.
* Coevolving edges use similarity-based hysteresis: if present, remove when distance `> link_off`; if absent, add when distance `≤ link_on`, with `link_on ≤ link_off`. **These thresholds are an explicit engineering prior**, not an emergent topology law.
* Simulated graph is finite, bounded, deterministic, never WORLD evidence, and never authorized to take real actions.

Counterfactual ablations: `top_down=False` removes beta/gamma influence; `rewire=False` freezes edges. These ablations use the same starting state.

## Tests and independent verification

* **29/29** G324-P2 new targeted pytest tests PASS. Includes 4 period-doubling settings, explicit chaotic-not-periodic restraint, Lyapunov sign, endogenous edges, nonlocal nested feedback, 2 orthogonal ablations, 64 seeded stochastic graph initializations *inside a test*, failure closure for invalid floats, graph invariants, determinism and immutable simulation scope.
* **42/42** retained G324-P0/P1 targeted tests PASS.
* **Full runtime regression 559 PASS / 27 FAIL**. All 27 are identical to parent P1: missing historical fixture `.c4m` paths. No new failing test identity; full suite **not all green**.
* Seeded sweep: **6 r settings × 3 feedback settings × 8 initial graphs = 144 deterministic simulations** of 420 updates each, 60,480 total iterations. Scripts and raw summary preserved.
* Model weights never retrained; state file SHA unchanged.

## Selected measured results (last 100 updates per run; mean 8 seeds)

| r | Zero feedback: graph-churn steps | Moderate feedback | Strong feedback |
|---:|---:|---:|---:|
| 2.90 | 0 | 0 | 0 |
| 3.20 | 0 | 0 | 0 |
| 3.50 | 0 | 0 | 0 |
| 3.56 | 8.5 | 0 | 0 |
| 3.65 | 92.625 | 0 | 0 |
| 3.80 | 99.5 | 90.875 | 0 |

This shows **parameter-dependent network reorganization** and suppression of topology changes by some feedback strengths *for this specific toy, seed distribution, and threshold settings*. It is NOT a universal theorem about C4, cognition, or graphs. Strong feedback can also erase useful variety; frozen topology might be a bad learner. No performance reward or transfer test yet.

Independent logistic-map control: `r=2.9,3.2,3.5,3.56` gives approximate attractive periods `1,2,4,8`. At `r=3.65,3.8`, no detected small period; estimated single-map Lyapunov exponent `0.25842,0.43574` respectively. This is classic textbook logistic behaviour, **not** proof of a period-doubling cascade in the graph's *connectivity*, a fractal graph, or cognitive bifurcation.

**Unexpected discovered invariant:** global-mean feedback can change every leaf on step 1 but preserve the global mean at step 1, because convex mixing to the mean is mean-preserving. At step 2 nonlinear local maps yield different macro means. An initially wrong test expected immediate aggregate divergence; it failed, and was corrected to test delayed effect rather than tampering with the model.

## Fault isolation / what is still missing

1. The model can only rewire using the **hand-designed** distance rule; it is not learning its own constraints.
2. Macro `mean` is a simple engineered order parameter; it is not a discovered abstraction. Connected components are a second engineered grouping level.
3. The rewiring threshold itself causes discontinuous changes; distinguishing a true dynamical network bifurcation from threshold crossing requires continuation analyses, order parameters and robustness to thresholds/size.
4. Period doubling of the *scalar logistic map* is well established in science and does not establish fractal scaling in the adaptive graph. Need measure period ratios or graph-specific fractal features before using that term literally.
5. No new perceptual ability, language capacity, 54 cognitive phenomenon reproduction, source admission repair, SELF/OTHER grounding, or actual causal governance gained.
6. The old G322 `moon_is_cheese` false WORLD admission remains unresolved and deliberately unmodified.
7. State dynamics is autonomous in SIMULATION, but not equivalent to a C4's DRIVE-selected real action.

## Next falsification gates (NOT implementation promises)

- Replace hard-coded similarity rewiring with learned and provenance-aware **candidate constraints**; compare equally budgeted fixed graph, random rewiring, pairwise factors and recursive macro-feedback ablations.
- Sweep graph size, resource/noise, hysteresis widths, component structure and initializations. Measure persistence, transfer, prediction quality, anti-self-reinforcement and failure recovery; require multi-seed confidence intervals before calling robustness.
- Test under delayed/out-of-order MEDIATE events; simulation must never propagate to WORLD.
- Explicitly test whether deeper-than-two-level recursion helps on held-out tasks, and whether circular self-feedback makes the system wrongly confident.
- Keep G324-P2 isolated, never promote without cold re-run and human live adversarial cases.

## Scientific comparators

- Gross & Blasius (2008), Adaptive coevolutionary networks, J R Soc Interface: https://pmc.ncbi.nlm.nih.gov/articles/PMC2405905/
- Gross et al. (2006), Epidemic Dynamics on an Adaptive Network, Phys Rev Lett: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.96.208701
- Feigenbaum period-doubling is existing nonlinear dynamics theory; the logistic map alone cannot establish novelty.

**Conclusion:** an adaptive multiscale feedback mechanism was implemented and falsifiably exercised. The experiment separates periodic node bifurcation, topology changes, and top-down recurrence; they can coexist and influence one another, but no universal unifying cognitive law has yet been inferred.