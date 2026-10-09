# D7 — Native C4 D5 alternative interpretation paths, read-only experimental comparison

Run `python multipath_native.py` and `python -m pytest test_d7.py -q` with the prior D6 self-contained directory present as specified at the top of the script. The master ZIP bundles those exact native input files so the script is reproducible when the ZIP is extracted with the intended layout; see `RUN_FROM_EXTRACTED_PACKAGE.md` for a fully relative launch recipe.

**Actual input:** pre-existing cold hydrated native D5 C4Graph from SHA `b7b2dd0f826bbc217f2a5499e53ba554a61c415817fe5d1f2c5313f2caa81036` and previous frozen 32 old D3 synthetics, 10 manually authored but previously used sentences, 6 OOD queries. No test labels at inference; same D5 graph weights. No modified .c4m created.

| K-best allowed | reversed32 exact | manual10 exact | OOD false candidate /6 |
|---:|---:|---:|---:|
| 1 |21|4|1|
| 2 |25|4|2|
| 4 |25|4|2|
| 8 |25|5|5|
| 16 |25|5|5|
| 32 |25|5|5|

**Critical falsification:** broader internal search helps recover 4 earlier syntactic cases and one manual sentence; but **false semantically typed positives explode**, even though no WORLD writes occur. K=1 recognizer abstains rather than hallucinating. K=32 gives an interpretation for 5 of 6 unrelated requests. `first structurally valid` is a research selection heuristic, not scientific confirmation of a lawful cognitive engine.

In a quick CPU run on the actual container, average parse time per previously frozen reversed utterance was approximately 0.8 ms at K=1 and 3.6 ms at K=32; these are local process measurements, not phone/target platform performance.

**No-GO:** recursive self-cognition, learning cross-level operations and independent language competence are NOT proven. Need trainable critic/uncertainty/semantic verifier, independent source/episode retrieval and DRIVE stop. Do not interpret score improvement as AGI or LLM replacement.

## D7 NEW frozen manual research challenge (not a true external blind)

Before first evaluation of these newly authored samples, `D7_FRESH_ADVERSARIAL_FROZEN.json` was saved with SHA256 `1e039d9bedf981a4478025d157b2b2d3407199d18c8d53713ea231a5d7213f98`; results generated once by the unchanged K-best algorithm. This test was designed by the same research assistant after inspecting C4 internals and thus does NOT count as independent human-written blind validation. It was not used for training or a tuning loop.

| K candidate paths | fully correct semantic AST /10 | spurious semantic candidate for unrelated question /10 |
|---:|---:|---:|
|1|1|1|
|2|2|1|
|4|2|4|
|8|3|7|
|16|4|8|
|32|4|9|

**Critical result:** broader introspective search increases both recalled signal and semantic false positives. A standalone first-valid-candidate search is fundamentally inadequate as a trustworthy admission mechanism; in particular an unsupported request should remain outside the learned belief parser. No output was factually COMMITTED, so the graph law was respected despite risky CANDIDATE proposals. No newly trained weights and no live standard user_message integrated. JSON `D7_FRESH_REATTACK_RESULTS.json` saves each individual result and negative case.