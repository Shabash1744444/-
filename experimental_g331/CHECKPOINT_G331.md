# G331 — Native C4 integration checkpoint (experimental)

Date 2026-10-08. Parent: G329 C4Child Android runtime (55 Python files, genuine C4M model). Branch isolated from G330 and canonical G309. Commit pending at packaging time.

## Objective
Correct earlier assistant error that created a second, incompatible C4 LIFE V1 model with second memory. **Never use c4life for Android**. Extend the original `c4child.runtime.C4LivingRuntime` with typed symbolic cognition as an input path, not a replacement engine.

## Code delta
- modified `c4child/runtime.py` + added `c4child/structured_cognition.py`.
- No rewriting `c4child/graph.py`, `dialogue.py`, `checkpoint.py`, learned C4M facts, word models, sensory organs or Android Java code.
- `user_message('@c4 {...}')` -> same receive / semantic_spine / cognitive_step / graph / life_events / outbox; legacy Russian route untouched.
- Durable state is `runtime_state.cognitive_g331`, stored by existing save_c4m_compact. Procedural goals/examples/actions, not duplicate semantic/episodic memory.
- Strict source-only admission for structured user REPORT; source-based G215 conflict without trust downgrade; perspective / scene isolation; social dialogue event linking; exploratory goal-action hypotheses with no fake execution, optional host-bound SIM receipt for learning from results.

## Tests
- New 23/23, prior directed 73/73, broad 559 PASS 27 missing-fixture fails.
- Real G329 C4M 10,781 facts successfully loaded, saved and reloaded with new component state.
- No new model weights: use existing backed up C4M.

## Hard limitations
- SIM host feedback tested in Python, not Android room actuator; no observed real-world reward channel. Initial `PLAN` remains a proposal.
- No generalized Russian or multimodal language-to-event understanding; pseudo JSON input explicitly supplies intent.
- Schema-level procedural generalization here is elementary; full G324–G329 causal closure and open-ended cognition not subsumed by this new organ.
- Python in-process private object access remains unisolated, old constitutional route can be LEGACY; this specific typed protocol uses STRICT gate and source-only entry.
- Lack of immutable full audit beyond existing bounded episode/trace windows.

## Next steps for G332
Bind physical sandbox events to an authenticated Android simulator receipt and correlate action IDs with actually performed motor actions. Test held-out multi-step problem solving and human language-to-typed-event learning, then tackle unanticipated red cases; do not advertise it as AGI.
