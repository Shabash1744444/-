# C4 RUSSIAN CURRICULUM + BOOK / CORPUS ROADMAP

Purpose: grow modern Russian, composition, vocabulary and cultural/world knowledge without losing provenance or mixing languages.

## Corpus classes
TRAINING: permitted for actual weight learning under compatible rights/license.
TEACHER-ONLY: abstractions/annotations allowed, not raw sensory experience.
EVALUATION-ONLY: never train; preserve as held-out exam.

Verify exact source/edition/license before bulk ingestion.

## Priority 0 — morphology and dictionary substrate
### OpenCorpora
Highest priority.
Use lemma<->form links, grammatical features and morphology.
Goal: лёд/льда/льдом and создать/создал/создала/создаёт become one lexical family.

### Russian Wiktionary (compatible dump)
High priority if exact dump/license is accepted.
Use meanings, forms, semantic relations, synonyms/antonyms, usage/register with source provenance.
Community definition != verified world fact.

### Vladimir Dal
Useful but HISTORICAL_RU, not the sole modern foundation.
Strengths: semantic neighborhoods, synonymy, idioms/proverbs, folk/historical vocabulary.
Risk: archaic register/meanings. Do not let Dal become C4's default modern voice.

### Ushakov
Useful twentieth-century lexical semantics if exact edition/source rights permit.

### Ozhegov/Shvedova
Conceptually valuable for modern normative definitions, but bulk ingest only with permission/compatible licensed source.

## Priority 1 — simple compositional Russian
Candidates subject to exact public-domain/source verification:
- L. Tolstoy: "Азбука" and simple stories
- K. Ushinsky: selected educational stories
- Russian folk tales from clean public-domain editions
- Krylov fables
- Pushkin fairy tales/prose

Focus:
simple propositions, pronouns, temporal order, cause/effect, object/property/action, basic dialogue, literal-vs-figurative.

## Priority 2 — modern everyday dialogue
Current major gap.
Need licensed/self-created corpus of:
questions/answers, requests, offers, refusal, correction, ellipsis, slang, short chat messages, register.

Create RU DIALOGUE NURSERY with controlled meanings:
"Да." "Нет." "Научу." "Ещё." "Почему?" "А она?" "Ты тут?" "Не понял." "Что именно?" "Давай потом." "Я про другое."

Test every construction on unseen vocabulary.

## Priority 3 — varied classical prose
Already active: Dostoevsky.

Add variety:
Chekhov — dialogue/subtext
Pushkin prose — concise narrative
Gogol — irony/narrator
Turgenev — description/narrative
Tolstoy — long discourse/perspective
Leskov — voice/register
Goncharov — social long-form narrative
Lermontov — first-person perspective
Bunin — dense description, exact rights/source verified
Saltykov-Shchedrin — satire after literal language is stronger

Author frequency must not become C4 preference/value.

## Priority 4 — poetry/song language
Only after literal/compositional base is stable.
Train metaphor, ellipsis, rhythm/repetition, polysemy, lyrical-I, symbolism, ambiguity.
Do not train genre preference.

## Priority 5 — explanatory/scientific Russian
Balance literature with clear exposition:
mathematics
physics
astronomy
biology/evolution
Earth/geography
computation
logic/scientific method

Current/open licensed sources preferred.
Old popular science gets HISTORICAL_SCIENCE provenance.
OUTDATED SOURCE != CURRENT FACT.

## Priority 6 — philosophy/argument
After stronger composition.
Train premise/conclusion, counterargument, normative vs empirical, rhetoric vs evidence, disagreement and ambiguity.
CHARACTER ARGUMENT != AUTHOR POSITION.
PHILOSOPHICAL FORCE != EMPIRICAL TRUTH.

## Priority 7 — phraseology/synonyms/collocations
High value if rights permit:
synonyms with context restrictions
antonyms
phraseological units
collocations
register/style
polysemy

SYNONYM != INTERCHANGEABLE IN ALL CONTEXTS.

## Priority 8 — Russian speech
Candidates already identified:
RuLibriSpeech
Common Voice RU
FLEURS ru_ru
Golos only under accepted license constraints

waveform -> low-level auditory structure -> speech pattern -> Russian word/form -> concept.
ASR OUTPUT != RAW HEARING.

## Priority 9 — visual nursery
Continue controlled raw images:
shape/color/size/location -> multi-object -> containment/support/contact -> occlusion/reappearance -> motion -> cause/effect.
Then real photos.
RAW IMAGE != TEACHER LABEL.

## First 20 corpus/work sequence
1 OpenCorpora morphology
2 compatible Russian Wiktionary dump
3 selected Dal semantic neighborhoods (HISTORICAL_RU)
4 Tolstoy "Азбука"/simple stories
5 Ushinsky simple stories
6 folk tales
7 Krylov fables
8 Pushkin prose
9 Chekhov stories
10 Lermontov prose
11 Gogol selected prose
12 Turgenev selected prose
13 Tolstoy selected narrative/dialogue
14 Dostoevsky continuation/second work after transfer tests
15 Leskov selected prose
16 Bunin selected stories if source rights are clear
17 RU math explanatory corpus
18 RU physics/astronomy corpus
19 RU biology/evolution corpus
20 RU DIALOGUE NURSERY / conversational corpus

Evaluate before scaling to 50/100 works.

## Ingestion unit
book/chapter/chunk
-> semantic decomposition
-> lexical/morphological enrichment
-> discourse
-> source/provenance
-> figurative/ambiguity
-> transfer example
-> adversarial near-miss
-> cold reload
-> checkpoint

## Metrics
For every batch record:
admitted/rejected/dedup
new lemmas/forms
semantic edge growth
held-out transfer
morphology/reference/ellipsis scores
dialogue continuity
UNKNOWN restraint
bytes added
latency
regression
source/license tag

## Stop conditions
Pause corpus growth if:
output gets more archaic/noisy
transfer stops improving
retrieval worsens with density
provenance collapses
unsupported confidence increases
latency rises without capability gain

Diagnose before adding more books.
