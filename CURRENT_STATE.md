# CURRENT STATE

Date: 2026-10-07
Canonical GREEN weights generation: G266
Canonical runtime generation: G269
Current organism: child_g266_object_permanence_green.c4m
Weights size: 1737251 bytes
Weights SHA256: 1fbbf2c26c8253dab51c5e7555bbb0656a36ca0de98a7874a5589556017b3ea6

## Runtime G269 — Kernel Floor + Discourse / Initiative Bridge — CURRENT
Runtime artifact:
- C4_RUNTIME_G269_KERNEL_FLOOR_DISCOURSE_GREEN_2026-10-07.zip
- SHA256 5541f67d56ec2cf0cd373cbff58801f0fa6d4445e333a229d34215813290475a

Combined runtime + weights:
- C4_G269_RUNTIME_PLUS_G266_WEIGHTS_2026-10-07.zip
- SHA256 f205f0230b3038a2f5bfee2b8c7d05fab5bdffa01c2b31ac7941e80800d888d1

Weights changed by G269: NO.

## Base: user-supplied Claude G267 Kernel Floor
Independent audit of the uploaded runtime confirmed its main claims:
- 274/283 test suite PASS on rerun;
- all 9 failures are the known missing historical G207/G137/G151/G153 files;
- questions do not create graph entities/facts;
- read-only lexical retrieval reaches admitted kernel facts;
- provenance receipts and bounded answers work;
- exact math oracle is reachable from ordinary Russian;
- graph/admission/reasoner/epistemics/bootstrap/checkpoint physics were not modified.

The base is materially stronger than previous G268 for ordinary knowledge access.

## Remaining counterexamples found during independent re-attack
On exact G266 weights, Claude G267 still produced:
- `Я не понимаю тебя` -> unrelated lexical facts about C4 layers;
- `Какие фразы ты знаешь?` -> facts containing the word "фраза", not a language-capability answer;
- `Научу` -> unresolved fallback;
- autonomous ticks exposed opaque `g223 world ... node A/B` identifiers;
- one different internal gap could emit a new ASK on every tick, so 30 ticks produced 30 opaque ASK events.

These are runtime/discourse/verbalization failures, not weight failures.

## G269 minimal merge
G269 keeps Claude G267 Kernel Floor and adds only the independently proven G267/G268 discourse repairs:
- `RussianDiscourseBridgeV1` for explicit social/meta/context acts;
- persisted compact dialogue history;
- short adjacency-pair answers;
- contextual ellipsis such as `Научу` after C4 ASK;
- correct USER/C4 perspective for `Я не понимаю тебя`;
- meta-language/meta-capability questions;
- public-label firewall for initiative;
- opaque graph identifiers stay internal;
- awaiting-response gate: after ASK, ticks cannot emit another ASK until a user/teacher event arrives;
- teacher events and rule-study examples clear the wait gate;
- unclassified language falls through to Claude's stronger read-only retrieval rather than being swallowed by the discourse bridge;
- Claude's resolve-only `surface:` gap logic is preserved, so questions still do not create entities.

Hard boundaries:
DISCOURSE CONTEXT != WORLD EVIDENCE.
LEXICAL RETRIEVAL != PROPOSITION TRUTH.
SIMILARITY != IDENTITY.
ASK WAIT STATE != GAP RESOLUTION.
The merge does not change G266 weights or core epistemic/causal laws.

## Validation
Combined suite: 288/297 PASS in 4.8 s.
All 9 failures are unchanged FileNotFoundError cases for missing historical G207/G137/G151/G153 artifacts.
Focused overlap/adversarial suite: 41/41 PASS.

Real G266 re-attack:
- `Привет` -> `Привет.`
- `Я не понимаю тебя` -> USER-perspective dialogue repair, no SELF leak
- `Какие фразы ты знаешь?` -> meta-language capability response
- runtime ASK -> `Научу` -> `Хорошо. Я слушаю.`
- `Мяч закрыли коробкой. Он исчез?` -> object-permanence knowledge reached through kernel floor
- `Почему идёт дождь?` -> 0 new entities / 0 new facts
- 30 ticks while awaiting a response -> 0 additional ASK events

## Weight lineage
Canonical weights remain G266:
- child_g266_object_permanence_green.c4m
- 1737251 bytes
- SHA256 1fbbf2c26c8253dab51c5e7555bbb0656a36ca0de98a7874a5589556017b3ea6

## Current policy
Russian remains the active natural-language learning channel.
English OmniCaption lexical/syntactic form remains quarantined.
Do not train weights around runtime language failures.
No runtime patch may weaken epistemic/causal laws merely to improve chat UX.

## Normative loop
counterexample -> minimal repair -> re-attack -> regression -> physical checkpoint -> next

## Next
Use G269 runtime with exact G266 weights in Android.
Collect real dialogue counterexamples.
Next language improvements should address remaining lexical morphology / WORD_FORM retrieval and Russian surface generation, without turning the runtime into an external LLM.


## Development methodology now normative
New mandatory documents:
- DEVELOPMENTAL_TRAINING_METHODOLOGY.md
- LEXICAL_GRAPH_SCALE_TARGETS.md
- RUSSIAN_CURRICULUM_BOOK_ROADMAP.md
- WEEK_ROADMAP_RUNTIME_WEIGHTS.md

Key policy:
- runtime and weights are co-equal but have different roles;
- do not train around runtime defects;
- do not hardcode corpus facts into runtime;
- atomic live teaching is diagnostic until language acquisition is stronger;
- Russian-first;
- corpus growth must be measured by held-out transfer, not bytes.

## Lexical graph scale hypothesis
Practical broad-Russian reference: ~180k lemma nodes.
Non-uniform semantic target:
- 20k CORE * ~30 typed semantic edges = ~600k
- 60k COMMON * ~12 = ~720k
- 100k LONG TAIL * ~3 = ~300k
- semantic total ~1.62M edges

Rough morphology target:
- ~180k lemmas * ~8 useful form/feature links = ~1.44M

Combined engineering scale:
~3.06M typed lexical+morphological links.

This is NOT a proof or requirement for emergence. It is a measurable graph-density target.

Random-graph sanity check only:
for N=180k, N ln N / 2 is about 1.09M undirected edges.
Semantic graphs are typed/non-random; connectivity != intelligence.

Storage implication:
current C4 serialization heuristically costs around 120-130 B per admitted relation in recent growth.
At current storage ~3M links could exceed 350 MiB.
A compact interned-ID representation near 32 B/link would put ~3M links near 93 MiB.
Therefore the 100 MB target now has a concrete storage/graph hypothesis and may require serialization compaction without changing C4 physics.

## Russian curriculum policy
Before scaling novels aggressively:
1. morphology / WORD_FORM substrate;
2. dictionary/semantic relations;
3. controlled RU dialogue nursery;
4. simple compositional prose;
5. varied classical prose;
6. scientific/explanatory prose;
7. complex argument/philosophy;
8. speech/vision grounding.

Dal is useful as HISTORICAL_RU for semantic neighborhoods, idioms and old vocabulary, but must not become the sole or default modern-Russian teacher.

See RUSSIAN_CURRICULUM_BOOK_ROADMAP.md for the first 20 corpus/work sequence.

## Immediate next work
Runtime:
continue from G269 with WORD_FORM/morphology/new-word acquisition/compositional teaching/persistence.

Weights:
continue from G266 under the new curriculum, prioritizing dense core-Russian connections and transfer over raw book count.

A new chat MUST read the four normative methodology/roadmap documents before modifying runtime or weights.


## Runtime architecture is now normative
Mandatory:
- RUNTIME_ARCHITECTURE_PRINCIPLES.md
- EXTERNAL_AUDIT_CLAUDE_G268_ACQUAINTANCE.md

Key rule:
runtime = maximally universal capability substrate;
weights/persistent state = acquired content/experience.

Do not hide factual corpora in runtime.
Do not compensate for runtime limitations by memorizing special phrases into weights.

## Claude G268 acquaintance import
External candidate imported and archived as evidence, NOT canonical.
Canonical remains:
- G266 weights
- G269 runtime

Claude G268 adds useful acquaintance/deixis behavior and reports lexical-index reduction from ~27MB to ~6MB.
It also establishes an important scale warning:
current full-JSON/Python-object graph representation cannot scale naively to 100-300MB mobile weights.

Before promoting any Claude G268 code:
diff against G269 -> preserve discourse/perspective/initiative protections -> combined regression -> real-device re-attack -> new runtime generation only if GREEN.

## 100-300MB mobile prerequisite
Persistent-state growth must be accompanied by runtime storage engineering:
disk-backed indexed graph + lazy loading + hot working set + incremental durable writes + checkpoint/export.

Track total deployed footprint, not .c4m compressed bytes alone.
