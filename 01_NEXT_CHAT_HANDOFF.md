# NEXT CHAT HANDOFF — C4 G244

Read CURRENT_STATE.md, TRAINING_METHODOLOGY_LONG_CORPUS.md and LITERATURE_TRAINING_METHODOLOGY.md first.

## Exact canonical baseline
- child_g244_karamazov_empathy_green.c4m
- 1059897 bytes
- SHA256 123d2c2d4701bb8ee4b568efaf20ef06e24839bbcfeb6ea1d2400e7826208ebb
- canonical generation G244
- > 1 MiB milestone reached without padding

Never silently fall back to G240 or reconstruct G244 from prose.
Verify bytes and SHA before training.

Persistent recovery:
- personal Library folder /C4_Canonical/
- expected files: exact G244 model and G244 release ZIP
- conversation/project artifacts are secondary fallback

## Active source
User-supplied full FB2 ZIP of Dostoevsky, "The Brothers Karamazov".
The physical FB2 is ~3.37 MB and contains 171 section nodes.
The novel is ACTIVE and not yet semantically closed.

Do not bundle source text into training release unless explicitly needed.
Use source as corpus, preserve provenance, and store compact semantic/language structures.

## Current literary progress
G241: Author/Narrator/Character/Reader, modality, family/history, long syntax.
G242: social pragmatics, politeness, irony, gestures, hidden intent, rumor.
G243: confession/self-report, desire/action/value, consent/coercion, nested provenance, hypotheticals.
G244: empathy, child conflict, memory, repair, mediation, causal restraint.

G241-G244 total:
- 697 admitted
- 0 rejected
- runtime changes 0

## Core literary laws
AUTHOR != NARRATOR
NARRATOR != CHARACTER
CHARACTER != AUTHOR
READER IN TEXT != CURRENT USER automatically
FICTIONAL_WORLD_FACT != EXTERNAL_WORLD_FACT
SOURCE TEXT != TEACHER INTERPRETATION
UTTERANCE != BELIEF
LITERAL CONTENT != SPEAKER INTENT
SELF_REPORT != ACTION != DESIRE != VALUE != OBSERVER_INTERPRETATION
POLITE FORM != BENEVOLENT INTENT
APOLOGY != REPARATION
SILENCE != CONSENT
EMPATHY != MIND READING
REMEMBERED SPEECH != VERBATIM RECORD
GOOD INTENT != VERIFIED GOOD OUTCOME
CERTAINTY != ACCURACY
HYPOTHETICAL != HISTORY

## Layer protocol
For useful scenes/ideas, build typed layers:
TEXT / SOURCE / SPEAKER / ADDRESSEE / NARRATIVE / TEMPORAL / SOCIAL / PRAGMATIC / EMOTION / ACTION / PHILOSOPHICAL / EPISTEMIC / LINGUISTIC / SELF-WORLD.

Teacher-added interpretation must stay clearly attributed as teacher analysis and must never be retroactively made into Dostoevsky's literal claim.

## Development loop
counterexample -> minimal repair -> re-attack -> regression -> cold reload -> physical checkpoint -> next

RED is never canonical.
No runtime repair merely to make a lesson fit.
No byte padding.

## Latest regression
254/263 passed.
All 9 failures are unchanged missing historical artifact FileNotFoundErrors for G207/G137/G151/G153.
No new semantic/runtime assertion failure.

## Recommended next arc
Continue from Book V "Pro and contra":
- philosophical argument vs character belief
- empirical premise vs normative value vs conclusion
- freedom, suffering, responsibility, authority
- nested story "The Grand Inquisitor"
- poem/story told by one character inside another narrator: preserve provenance depth
- rhetoric != evidence
- emotional force != logical validity
- contradictions can be layer/time dependent

Checkpoint every meaningful GREEN sequence and update repo state/handoff after each substantial group.
