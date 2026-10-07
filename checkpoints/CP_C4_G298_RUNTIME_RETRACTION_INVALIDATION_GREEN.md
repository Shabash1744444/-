# CP C4 G298 RUNTIME RETRACTION INVALIDATION GREEN

Parent runtime G296.
Canonical weights validated: exact G297.

Counterexample:
A source could assert a FUNCTIONAL value, later negate that same value, yet source-conflict reconstruction still treated the source as currently supporting it.

Repair:
functional source stance is reconstructed in evidence order.
Later POS selects/revises.
Later NEG of selected value retracts.
NEG of another value preserves current positive.
Retraction never resurrects an older superseded value.
Evidence history remains intact.

Derived invalidation:
PART_OF/HAS_PART inverse disappears after support removal.
OPPOSITE symmetry disappears after support removal.
Temporal chain disappears after bridge removal.

Focused G294-G298 32/32.
Full memory 380/389.
SQLite 380 pass + same nine historical missing-artifact failures.
Streaming SQLite 5/5.

Exact G297 on G298:
memory 32/32 derived + 26/26 restraint, direct leaks 0.
SQLite 32/32 derived + 26/26 restraint, direct leaks 0.
Cumulative G270-G292 GREEN.

Runtime SHA256 7ff72ff492ef247c18fe9d44a6927ca06434945c4c7254781930ce960221897f.
