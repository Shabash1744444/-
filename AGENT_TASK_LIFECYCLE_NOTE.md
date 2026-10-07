# C4 FUTURE AGENT NOTE — TASK MEMORY VS TASK EXECUTION

Status: FUTURE AGENT CURRICULUM / ARCHITECTURE QUESTION

Remembering a task is not sufficient for acting as an agent.

Potential minimal first-class structures:
- TASK: durable obligation/assignment;
- GOAL: desired state/completion condition;
- TRIGGER: when it becomes actionable;
- STATUS: OPEN / WAITING / RUNNING / BLOCKED / DONE / CANCELLED;
- PLAN / dependency graph;
- ACTION_REQUEST;
- RECEIPT / environment response;
- VERIFIED_OUTCOME;
- NEXT_CHECK / continuation condition.

Candidate lifecycle:
TASK -> trigger -> goal -> plan -> action request -> receipt -> verify -> status -> continue/finish.

Important:
TASK MEMORY != TASK SCHEDULING
TASK SCHEDULING != ACTION
ACTION_REQUEST != VERIFIED OUTCOME
RECEIPT != CAUSAL PROOF

Prefer first-class persistent structures inside C4's own typed graph/state rather than a second independent "memory brain" when possible. Singularity ideas may inform invariants/requirements but should not be copied as architecture by default.

Do not implement during current developmental pretraining. Validate later as a separate AGENT curriculum track.
