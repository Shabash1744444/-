# CP G268 RUNTIME SURFACE VERBALIZER GREEN

Date: 2026-10-07
Status: GREEN
Weights changed: NO
Canonical weights: G266

Runtime SHA256: db02d7f9c4da15cfbcc38ef4a3110e696e611eaaef90e3612effa84761cf60bb
Combined package SHA256: ad93604fb662da091e696a31e7f66cf7794ea51a6fd71efaa32892cea69dc1aa

Counterexamples from Android:
- greeting -> unresolved language;
- user misunderstanding -> SELF leakage;
- internal graph node names -> human-facing ASK.

Minimal repair only in surface/discourse/verbalization layer.

Tests:
- 14/14 dialogue adversarial PASS
- 268 PASS / 9 unchanged missing-artifact FAIL in full suite
- real G266 screenshot re-attack PASS
