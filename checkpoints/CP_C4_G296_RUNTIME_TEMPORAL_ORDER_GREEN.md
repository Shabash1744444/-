# CP C4 G296 RUNTIME TEMPORAL ORDER GREEN

Parent runtime G295. Exact G292 weights.

BEFORE/AFTER form one strict directed order.
Positive paths compose transitively read-only.
Reverse proven order refutes read-only.
Temporal cycles -> CONFLICT.
Explicit NEG against positive temporal path -> CONFLICT.

Restraint:
shared predecessor does not order siblings.
temporal order does not imply CAUSES.
no derived temporal fact is persisted.

Focused G294-G296: 25/25.
Memory 373/382.
SQLite: 373 pass + same nine historical missing-artifact failures.
Streaming SQLite 5/5.
