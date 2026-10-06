# CURRENT STATE

Date: 2026-10-07
Canonical GREEN weights generation: G266
Canonical runtime generation: G268
Current organism: child_g266_object_permanence_green.c4m
Weights size: 1737251 bytes
Weights SHA256: 1fbbf2c26c8253dab51c5e7555bbb0656a36ca0de98a7874a5589556017b3ea6

## Runtime G268 — Surface / Verbalizer Repair — CURRENT
Runtime artifact:
- C4_RUNTIME_G268_SURFACE_VERBALIZER_GREEN_2026-10-07.zip
- SHA256 db02d7f9c4da15cfbcc38ef4a3110e696e611eaaef90e3612effa84761cf60bb

Combined runtime + weights:
- C4_G268_RUNTIME_PLUS_G266_WEIGHTS_2026-10-07.zip
- SHA256 ad93604fb662da091e696a31e7f66cf7794ea51a6fd71efaa32892cea69dc1aa

Weights changed by G267: NO.

### Counterexample
Android app repeatedly showed:
`Я пока не понимаю эту фразу. Попробуй сказать проще или научи меня.`
for distinct user inputs such as short contextual replies and meta-language questions.

The exact fallback string was found in `c4child/dialogue.py`, proving a runtime language bottleneck rather than an APK-only UI string.

### Root cause
`RussianChildLanguageV0` is a bounded exact/compositional parser. When all semantic parsers return UNKNOWN, `dialogue.say()` collapses to one hard-coded fallback before rich G266 knowledge gets a chance to participate in ordinary dialogue.

### Minimal repair
Added `RussianDiscourseBridgeV1` above the exact parser:
- exact existing semantic parser still wins when it understands the utterance;
- compact dialogue history (16 turns);
- short adjacency-pair answers: yes/no/continue/stop;
- contextual elliptical teaching offers such as `Научу`;
- meta-language/meta-capability questions;
- unknown-language vs unknown-world-knowledge separation;
- partial grounding report instead of opaque fallback;
- dialogue history persists in runtime state;
- after runtime emits ASK, further autonomous ASK events wait for a user/teacher response;
- direct teacher events/rule examples clear the wait gate.

Hard boundary:
DISCOURSE CONTEXT != WORLD EVIDENCE.
The bridge itself does not commit world facts.

### G267 validation
New adversarial dialogue tests: 7/7 PASS.
Full source suite: 261 PASS / 9 FAIL.
All 9 failures are unchanged FileNotFoundError cases for missing historical G207/G137/G151/G153 artifacts.
No new semantic/runtime assertion failure.

Real G266 re-attack:
- `Какие фразы ты знаешь?` -> meta-language response, not legacy fallback.
- `Научу` -> OFFER_TEACH discourse act.
- after C4 ASK `Можешь объяснить?`, `Научу` -> `Хорошо. Я слушаю.`
- one ASK followed by 10 ticks without user input -> 0 extra ASK events.
- context/wait state survive runtime_state save/load.

## Weight lineage G263-G266
G263:
- OmniCaption abstraction pass 3
- 117/117, cold 14/14
- 1602113 bytes
- SHA256 8267844a7169641ea52382cc122c08a223e2eaf7f7f53ad4eec2853a30dd5b7c

G264:
- Russian sensory-reasoning transfer
- 84/84, cold 14/14
- 1619770 bytes
- SHA256 aef1f49725358a46915955affe0e4c5ac58ad6055a735e576990fb818e072b3a

G265:
- 108 synthetic raw PNGs, 72 train / 36 held-out
- 748/748, cold 10/10
- 1707998 bytes
- SHA256 6e62f3839ea41a13a9f420f0e579f549d3b1c95a766d93de01c076ea19a0d8de

G266:
- 18 object-permanence sequences / 162 frames
- 220/220, cold 9/9
- 1737251 bytes
- SHA256 1fbbf2c26c8253dab51c5e7555bbb0656a36ca0de98a7874a5589556017b3ea6

## Current policy
Russian remains active language-learning channel.
English OmniCaption lexical/syntactic form remains quarantined.
No runtime patch is allowed to rewrite epistemic/causal laws merely to improve chat UX.

## Normative loop
counterexample -> minimal repair -> re-attack -> regression -> physical checkpoint -> next

## Next
Use G267 runtime with exact G266 weights.
Do NOT train around the old fallback screenshots.
Next language work should test whether richer free Russian dialogue can reach existing knowledge through the new bridge before adding more language facts.


## G268 Android screenshot re-attack
Observed failures:
- `Привет` fell into unresolved-language output.
- `Я не понимаю тебя` leaked internal SELF grounding.
- initiative exposed opaque graph labels like `g223 ... node A/B`.

Minimal runtime repair:
- basic social/discourse acts;
- user-vs-C4 perspective for misunderstanding reports;
- pronoun/internal-ID filtering in read-only mention grounding;
- human-facing public-label firewall for initiative;
- unrenderable internal gaps stay internal and cannot monopolize ASK output.

Validation:
- G267+G268 dialogue tests: 14/14 PASS;
- full suite: 268 PASS / 9 unchanged missing-historical-artifact FAIL;
- real G266 re-attack: all three screenshot classes fixed;
- weights unchanged: still G266.
