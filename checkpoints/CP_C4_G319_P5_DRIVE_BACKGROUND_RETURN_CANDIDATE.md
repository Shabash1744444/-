# C4 G319-P5 — DRIVE BACKGROUND / RETURN CANDIDATE

Status: CANDIDATE / NOT CANONICAL
Date: 2026-10-08
Parent state: exact G317-P3, runtime parent G318-P4.

## Purpose
Remove the remaining FIFO assumption from unsent public acts.

## Added
- unsent speech/action candidates may be `READY`, `BACKGROUND`, or `PUBLISHED`;
- a sufficiently higher-VALUE new act can move a weaker READY act to BACKGROUND;
- BACKGROUND is preserved history/state, not deletion or failure;
- DRIVE selects among READY acts by VALUE rather than arrival order;
- BACKGROUND acts never auto-leak merely because foreground became empty;
- DRIVE may explicitly reconsider a context-relevant BACKGROUND act and return it to READY;
- low-value context-free leftovers remain backgrounded;
- each action candidate stores the semantic context present when it was formed.

## Laws
ARRIVAL ORDER != ACTION ORDER.
BACKGROUND != FORGOTTEN.
VALUE != EXECUTION.
RELEVANCE != TRUTH.
STATUS CHANGE != SEMANTIC COMMIT.
DRIVE remains the sole arbiter of publication.

## Cold re-attack
Exact G317 state:
- context-linked act `Вернусь к теме радиации.` value 0.60 -> BACKGROUND;
- later `Радиация — излучение.` value 0.86 -> READY;
- save/restart preserved both statuses;
- foreground answer published first;
- next step with background return disabled produced no output;
- explicit DRIVE background reconsideration returned the old context-relevant act;
- semantic graph unchanged.

## Validation
Focused P4/P5 + lifeline/multimodal: 30/30 PASS in the focused successor set.
Full regression: 474/493 PASS.
19 failures are unchanged FileNotFoundError historical fixtures/models.
New semantic/runtime assertion failures: 0.

## State
Weights/state unchanged from G317-P3:
- bytes: 1998549;
- SHA256: `0c62250f7845df1a52ea080434ee6eba84771e8d6715611a0dad840ca6d83810`.

## Next
P6: hierarchical semantic composition over the continuous life-line: WORD/PHRASE/PROPOSITION/EVENT/EPISODE/STORY with typed PART_OF/REFERS_TO/ORDER links and no truth mutation from mere composition.
