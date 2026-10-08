# C4 CONSTITUTION DESIGN REVIEW — Alice discussion

Date: 2026-10-08
Status: design review; not a canonical generation.

## Core conclusion

The Alice discussion strongly supports the current C4 repair direction: one deterministic constitutional gate must stand in front of every canonical mutation.

However, several parts must be adapted to C4 rather than copied literally.

## Adopt

### Deterministic constitutional validator
A non-learned validator enforces EVAL / COMMIT / DRIVE / MEDIATE invariants.
LLM/teacher/parser may propose; none may directly mutate canonical truth.

### Proposal != evidence != commit
A semantic proposition can exist as a candidate/source assertion without becoming canonical truth.

### Action request != outcome
External effects require MEDIATE and a verified receipt/outcome path.

### Audit operation
AUDIT is a lawful TRIGGER that asks the system to re-check a subgraph against constitutional invariants.
AUDIT itself does not delete or rewrite facts.

### Change journal
Every mutation should retain:
- proposer/source;
- candidate proposition;
- EVAL result;
- COMMIT basis;
- owner that authorized the transition;
- influence type;
- source/provenance/lineage;
- previous status;
- new status;
- external receipt when applicable.

## Modify

### hypothesis / evidence / committed are not universal entity kinds
They are epistemic roles/statuses over semantic content.

The same proposition should preserve identity while moving through statuses such as:
CANDIDATE -> SOURCE_ASSERTED -> SUPPORTED -> ADMITTED(scope) -> CONTESTED -> RETRACTED/HISTORICAL.

Creating a different semantic entity for every epistemic status would fragment identity and make retraction/history harder.

### Evidence existence is not enough
COMMIT requires admissible basis, not merely an incoming node called evidence.

The validator must test at least:
- relevance to the proposition;
- provenance;
- source lineage/dependency;
- replay/derived status;
- reality scope;
- temporal compatibility;
- observation vs simulation vs source report;
- whether the target truth scope matches the evidence scope.

EVIDENCE LABEL != COMMIT AUTHORITY.

### Five influences are meta-causal, not the entire semantic vocabulary
MASK / VALUE / AVAIL / TRIGGER / STATUS define lawful influence between EVAL / COMMIT / DRIVE / MEDIATE.

They do NOT replace semantic relations such as:
IS_A, PART_OF, CAUSES, BEFORE, WORD_FORM, MEANS, ROLE, etc.

The 4×4×5 = 80 matrix is a matrix of control/causal influence signatures, not a replacement for world semantics.

### VALUE and actions
The constitutional restriction is:
VALUE must not bypass DRIVE to cause execution.

An action candidate/request may have a VALUE attached for representation, but VALUE alone cannot create or execute the action.

### Parsing input does not automatically create evidence
Text parsing should create a source assertion / observation candidate with provenance.
An LLM/parser output remains EVAL.
A verified sensor/receipt may become evidence only through the appropriate MEDIATE boundary.

### Abstraction is not the validator's job
Repeated examples may TRIGGER EVAL to propose an abstraction.
The validator only checks whether the proposed abstraction can be COMMITted.
The validator must not invent semantic abstractions merely because many examples exist.

## Reject as too narrow

### SELF defined only from action-request/receipt chains
Useful signal, but insufficient.

SELF must be a persistent causal/perspectival subgraph including:
- stable agent identity;
- event authorship/initiation;
- observation access;
- memory/history continuity;
- body/runtime ownership;
- capability boundaries;
- self-reports and externally verified self facts;
- action/receipt chains.

SELF != current action set.

OTHER is modeled with the same evidence discipline.
OTHER intention/interest remains hypothesis unless reported/observed sufficiently.

### User as final DRIVE arbiter
In dialogue there are multiple agents, each with its own DRIVE.
The user may provide goals, constraints, feedback or permissions.
External policy may MASK effects.
But the user's existence does not replace C4's internal DRIVE arbitration.

## Apparent counterexamples that do not require a fifth law

### Generation of a new option
Not a sixth influence.
Generation is an EVAL operation that creates a new candidate/hypothesis.
The five influence types describe how owners affect state/choice, not every internal computational operation.

### Communication gap
'I said X' != 'you received X' != 'you understood X'.

This is MEDIATE across multiple boundaries:
INTEND -> SEND_REQUEST -> DELIVERY_RECEIPT -> RECIPIENT_OBSERVATION -> RECIPIENT_EVAL.
Understanding by another agent cannot be committed by SELF without evidence/feedback.

### Permanent constitution
Do not store the four laws merely as ordinary mutable committed facts.

The executable constitution belongs in a versioned, hashed validator/kernel outside ordinary self-editable semantic truth.
Graph facts may describe the constitution, but cannot authorize changing it.

A constitutional change requires an explicit offline/new-version process, not ordinary runtime TRIGGER/COMMIT.

Therefore AXIOM does not need to become a sixth influence type.

## Recommended physical architecture

### Semantic layer
SemanticUnit / Proposition / Event / Episode / Story entities with ordinary semantic relations.

### Claim layer
Claim:
- proposition_id;
- claimant/source;
- source lineage;
- timestamp;
- scope;
- polarity;
- status.

### Evidence layer
Evidence:
- source;
- evidence type;
- dependency root;
- reality scope;
- timestamp;
- receipt/observation reference.

### Constitutional layer
ConstitutionalKernel:
- evaluate_transition();
- validate_commit();
- arbitrate_drive();
- validate_mediate();
- audit_subgraph().

Only this layer may authorize canonical status transitions.

### Action layer
ActionCandidate -> DRIVE decision -> ActionRequest -> MEDIATE execution -> Receipt -> ObservedOutcome.

### Query layer
truth(proposition, scope=...) must be scope-aware.
Examples:
WORLD,
LANGUAGE_CONVENTION,
SOURCE_ASSERTION,
SELF_REPORT,
NARRATIVE_WORLD,
SIMULATION,
OBSERVATION,
SYSTEM_FACT.

USER_SAID(X) may be TRUE in SOURCE_ASSERTION scope while remaining UNKNOWN in WORLD scope.

## Immediate implication for current G310

Current C4Graph.commit() itself creates ADMITTED/REVISED facts and graph.truth() treats all active facts uniformly.
BootstrapTeacher and Dialogue call graph.commit/replace directly.

Therefore the next repair remains:

P0. One universal constitutional mutation gate.
P1. Scope/status-aware claims before world truth.
P2. Route Dialogue, BootstrapTeacher and EpistemicAdmission through the same door.
P3. Preserve legacy checkpoints through migration/import mode only.
P4. Make truth queries scope-aware.
P5. Add AUDIT and a transition journal.
P6. Only then resume live teaching and large-scale training.
