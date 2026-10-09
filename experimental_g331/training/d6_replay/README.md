# C4 D6: Episodic Replay, Recursion and Provenance — narrow proof, 2026-10-09

**FINAL STATUS: LIMITED POSITIVE (retrospective reinterpretation with a pre-existing improved language operator); NEGATIVE (mere repetition); NO-GO (general autonomous self-cognition/LLM).**

This is C4, not Singularity. Physical tests use the genuine pre-existing compact `.c4m` C4 graphs and native Python organs, without modifying the originals. This is NOT new training of C4's language model and not a new blind exam. Prereg protocol `PRE_REGISTERED_PROTOCOL.md` establishes these caveats. The second test is deliberately independent toy mathematics, not evidence of C4 natural-language competence.

## Case A — re-read prior raw experiences using newly acquired capacity

Old D3 source model `C4_D3_64_NESTED_LEARNED_CANDIDATE_NONCANONICAL.c4m`: actual strict compact C4Graph, 16,522 facts, frozen from previous D3. New D5 model `C4_D5_LEARNED_EDGE_RESEARCH_ONLY.c4m`: actual strict compact C4Graph, 16,731 facts, previously trained, no training this turn. SHA256s and cold counts are checked on original prior artifact; reloaded from bundled byte-identical copies.

Prior frozen D3 `reversed_role_order` 32 utterances were indexed as native `episodic_memory.index_event`, scope `SOURCE_SAID_ONLY`. These 32 are **synthetically generated old cases**, no novel blind test. Pre-replay old D3 positional `build_ast` gave **0/32 exact**. The SAME raw old event surfaces, passed to the NEW previously trained D5 tag+edge mechanism, gave **21/32** correctly reinterpreted full AST, i.e. **21 retrospectively corrected prior failures**. The interpretations were versioned in research-only ledger without editing original raw source or native graph. No teacher labels given to inference. Human-authored pre-existing D5 sample still **4/10**, and 1/6 unrelated phrases still yields spurious unadmitted candidate. No claim of solved free Russian speech.

**No-new-information control:** recompute exactly the SAME D5 decoder K=1,2,3,5,10,30,100 times with no new input, model change, or alternate hypothesis: **21/32 at every K.** C4 gains from a better representation and re-access to raw data, not from counting passes. Frozen historical model SHA256 and live graph len(facts)/len(audit) checked unchanged; no WORLD claim or altered source roots.

**Retrieval bottleneck:** native `episodic_memory.retrieve` on question mentioning only the story object, choosing top 2 of 32 past utterances, hits intended episode just **12/32** because subjects often repeat across events. An *oracle* using the whole original text to query hits **32/32** (upper bound, not a fair user-facing result). Hence genuine self-cognition needs learned event selection, not just a parser improvement; identical/ambiguous source events inherently cannot be uniquely addressed from a topic-only query.

## Case B — iterative graph pass microtest (NOT the C4 runtime)

Controlled graph math `iterative_graph_micro.py` on separately generated 60 training graphs and 200 novel DAG graphs. Only ONE scalar parameter learned from **one-hop** edge supervision via least squares. Given adjacency edges A (already observed, not inferred from words), recurrence:

  h^(0) = one_hot(source)
  h^(k+1) = clip(max(h^(k), w*(A^T h^(k))), 0, 1)

where learned w=1.0. Evaluate exactly nodes reachable within up to four hops, measured against independent graph reachability labels:

| passes | exact graphs/200 | precision | recall |
| 0 | 17 | 1.000 | .172 |
| 1 | 31 | 1.000 | .472 |
| 2 | 66 | 1.000 | .743 |
| 3 | 124 | 1.000 | .920 |
| 4 | **200** | 1.000 | 1.000 |
| 5 | 194 | .994 | 1.000 |
| 100 | **194** | .994 | 1.000 |

The formula itself is a **hand-provided generic graph propagation inductive bias**; no complex learned topology or Russian semantics here. This shows multi-hop iteration can solve reachability when a reusable propagation operator and valid edges already exist, and that excess passes can change the answer and harm correctness against a bounded query. It is NOT evidence of C4's emergent reasoning, AGI or that graph weights alone replace LLM. The use of simple least squares for w=1 is not a neural training methodology.

## Proposed C4 math, not implemented this turn

Immutable episode: E_i=(raw_surface,source_root,event_time,context_links); versioned interpretations H_i^(v) share dependency on E_i. A future learned proposed inner update:

  Z_(k+1) = F_theta(Z_k, E_i, Retrieve(G_t, Z_k), G_t, delta_t)

  score_theta(Z) = sum_{nodes} phi_theta + sum_{edges} psi_theta + scope/time/source compatibility - contradiction/unsupported penalties

DRIVE selects whether to replay event i and continuation budget k by expected improvement minus retrieval/compute risk/cost. EVAL only proposes interpretations, COMMIT must not mint a new evidence root from the replay, MEDIATE is needed for independent action receipts. **A repeated self-thought is not an independent factual observation.** Historical H_i remains viewable; only source-backed status may change. Fresh external observations may justify new beliefs, whereas re-evaluation of the same episode only justifies a new dependent interpretation.

Important impossibility: if old h=f(raw) discarded a distinction and the original raw episode is inaccessible, no postprocessing of h alone can reconstruct which distinct raw input produced it; extra iteration cannot invert an information-destroying map. Re-access to the original episode + improved learner is what works in Case A.

## Engineering verdict

- **YES** to testing native replay/reinterpretation as a future C4 cognitive process: possible and useful with improved downstream learner on some historical failures.
- **NO** to '100 loops automatically fixes D1/D3': it fails unchanged-detector controls and may worsen fixed-horizon reasoning.
- **STILL UNKNOWN** whether jointly learned grammar, variable binding, self-initiated replay policies and speech realization will solve broad language. Current C4 remains **NO-GO as standalone LLM replacement**.
- Next rigorous proof: independent new human-written raw episodes; freeze before training; one and same C4M across new training and delayed episodes, learned episodic retrieval/priority + general relational learner, compare information-matched single pass and iteration budgets, new source lineage, cold checkpoint, full original regression, real native `user_message` read-out. No artificial answers given at test time.

## Reproduce

From extracted ZIP containing `native_runtime/c4child`, `inputs/d3`, `inputs/d5`, run `python replay_native.py`, `python iterative_graph_micro.py`, `python -m pytest test_d6.py -q`. Requires Python 3.11+, NumPy, pytest; the native C4Graph portion uses only its existing Python environment. No external network, no API, no new weight training in Case A. `D6_RETROSPECTIVE_RESULTS.json` and `D6_VERSIONED_INTERPRETATION_LEDGER.json` are generated, no `.c4m` files are rewritten.