# C4 LANGUAGE ISOLATION METHODOLOGY

Normative from G258 onward.

## 1. Current active language
Russian is the primary active natural-language learning channel.

This does not mean foreign languages are forbidden as source material.
It means foreign linguistic form must not silently contaminate Russian lexical, morphological or syntactic learning.

## 2. Core distinction
LANGUAGE FORM != SEMANTIC CONCEPT.

A concept may later have labels in multiple languages.
A label is not the concept itself.

Cross-language abstraction transfer may occur through semantic structure:
source form -> interpreted concept/relations -> target-language form

Do not use:
source foreign syntax -> direct Russian syntax copying.

## 3. Language identity
Each external text fragment should have a LANGUAGE_ID when reasonably known.
LANGUAGE_ID may be UNKNOWN.

Language identity says nothing about truth, authority or SELF ownership.

Proper names, brands, formulae, filenames and abbreviations may use Latin characters inside Russian discourse without changing the language of the whole utterance.

## 4. Russian layer
Learn Russian morphology from Russian examples.
Learn Russian syntax from Russian examples.
Learn Russian idioms and pragmatic constructions in Russian context.
Do not treat foreign sentences as Russian grammatical evidence.

## 5. Foreign source quarantine
Foreign text may be retained as:
SOURCE_TEXT + LANGUAGE_ID + PROVENANCE.

It may teach:
- abstract relations
- cross-modal structure
- source/event organization
- logic/causal patterns

It must not automatically teach:
- Russian lexical choice
- Russian word order
- Russian morphology
- Russian idiom

## 6. Translation
TRANSLATION != COPYING.
Translation is a sourced semantic mapping hypothesis.

Translation may change word order and grammar.
Literal translation may fail for idioms.
One source sentence may have multiple valid translations.
Translation does not create independent evidence for the source proposition.

## 7. Code switching
CODE SWITCHING is an intentional/contextual language alternation.
ACCIDENTAL MIXTURE != CODE SWITCHING.

Quoted foreign text != global language switch.
Unknown foreign fragment may remain UNKNOWN.

## 8. Sensory grounding
Raw image pixels are not inherently Russian/English.
Raw waveform is not inherently Russian/English before linguistic interpretation.

Connections:
image -> concept -> Russian word
waveform -> speech pattern -> Russian word
must be learned/evidenced.

Later:
same grounded concept -> English label
may be taught without changing Russian grammar.

## 9. SELF/source boundary
Source language != source identity.
Source first-person != C4 SELF.
Translated first-person preserves original speaker ownership.
Learning a human language != inheriting a human biography.

## 10. Current corpus policy
Dostoevsky = Russian linguistic corpus.
Russian speech datasets = Russian speech curriculum.
OmniCaption uploaded JSON = overwhelmingly English teacher-only multimodal annotation corpus.
MERA Multi = evaluation-only benchmark, not training.

## 11. Held-out tests
Hide filenames, labels and translations where they would leak answers.
Test Russian generation after foreign teacher exposure for language contamination.
Test unknown foreign fragments for restraint.
Test future bilingual mode separately and intentionally.

## 12. Development loop
counterexample -> minimal repair -> re-attack -> regression -> cold reload -> physical checkpoint -> next

RED never canonical.
Do not change runtime merely to make foreign material fit.
