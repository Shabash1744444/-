# CP C4 G295 RUNTIME FUNCTIONAL SLOT CONFLICT GREEN

Parent runtime G294. Exact G292 weights.

Counterexample:
A FUNCTIONAL slot could contain source disagreement on alternate values while a specific yes/no query hid that disagreement.

Repair:
specific yes/no answers surface functional slot source conflict as context while preserving the canonical direct state.
No new fact or negation is created.

Focused 6/6.
Memory 366/375.
SQLite split: 366 pass.
All nine failures are unchanged historical missing-artifact FileNotFoundError cases.
