# CP C4 G289 RUNTIME MIXED-CHUNK DEPENDENCY GREEN

Parent runtime: G286.

Counterexamples:
- relation sentences in the same chunk could be skipped before their explicit definitions were admitted;
- explicit "X имеет свойство Y" could be overwritten by generic HAVE parsing.

Repairs:
- one bounded deterministic retry after pass-1 admissions;
- explicit PROPERTY grammar has priority over generic "иметь".

Focused 4/4.
Full regression 343/352.
All 9 failures are unchanged historical missing artifacts.
Unknown causal endpoints still create 0 entities/facts.
