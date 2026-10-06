# EXTERNAL AUDIT — CLAUDE G268 ACQUAINTANCE (2026-10-07)

Status: useful external runtime candidate / evidence source.
NOT canonical by itself.
Canonical at time of import: G266 weights + G269 runtime.

Source artifacts supplied by Ruslan:
- C4_RUNTIME_G268_ACQUAINTANCE_2026-10-07.zip
- README_G268.md
- SHA256 sidecar

## Verified report facts from supplied README
Model remained G266.

Changes addressed:
- topic retrieval on misunderstood assertions;
- acquaintance social act;
- postfix forms of "запомни";
- USER/SELF role/deixis verbalization;
- reverse creator queries;
- multi-sentence transport cleanup;
- "Ты меня помнишь?";
- lower-memory lexical index.

Reported regression:
G266 254/263
Claude G267 274/283
Claude G268 282/291
Same 9 historical FileNotFoundError failures.
G268-specific tests 8/8.

Reported performance:
- G266 model load ~0.37 s on laptop;
- first topical query/index build ~0.6 s;
- later replies ~2 ms.

## Scale measurements
G266:
- .c4m archive ~1.7 MB
- graph_hot.json ~11 MB
- 9,173 facts
- live Python graph/state ~43 MB
- lexical index ~6 MB after optimization
- neural h3_templates.json: 112 bytes

Linear x59 extrapolation for ~100MB archive:
- graph_hot.json ~650 MB
- ~540k facts
- live Python graph/state ~2.5 GB
- lexical index ~0.4 GB
- ~20 s laptop load, expected worse on phone

Conclusion:
current JSON-entirely-in-RAM representation is not suitable for 100MB+ mobile C4.
Disk-backed indexed/lazy graph becomes a runtime prerequisite.

These are linear prototype measurements, not guaranteed final scaling laws.

## Critical conceptual finding
In current C4, the useful learned mass is overwhelmingly persistent facts/graph state, not a conventional neural parameter tensor.

Therefore:
"weights" is convenient project terminology but must not mislead architecture decisions.

New factual/lexical knowledge grows persistent state.
New sentence constructions do NOT automatically emerge merely by adding facts; language-organ/runtime capability must also improve.

## Remaining limitations reported
- morphology generation remains weak;
- word formation/lemma families are not fully connected;
- role conjunction bug;
- USER identity and concept Ruslan stay separate unless explicitly represented;
- language understanding remains code patterns + learned lexical relations.

## Merge policy
Do not overwrite G269 blindly.
When importing Claude G268 improvements:
1. diff against G269;
2. preserve G269 discourse/perspective/initiative protections;
3. add only non-overlapping improvements;
4. run combined suite;
5. re-attack live phone counterexamples;
6. promote as a new runtime generation only if GREEN.
