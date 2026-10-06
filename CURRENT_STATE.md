# CURRENT STATE

Date: 2026-10-06
Canonical GREEN generation: G258
Current organism: child_g258_russian_language_firewall_green.c4m
Size: 1485478 bytes
SHA256: 97d91d65b98171f16d398e9939b69a20de1b183546dbd429115f5a85cbb302cd

## Normative methodology
Read:
- TRAINING_METHODOLOGY_LONG_CORPUS.md
- LITERATURE_TRAINING_METHODOLOGY.md
- SONG_AUDIO_TRAINING_METHODOLOGY.md
- SENSORY_TRAINING_METHODOLOGY.md
- ABSTRACTION_TRANSFER_METHODOLOGY.md
- SELF_WORLD_MULTIMODAL_METHODOLOGY.md
- LANGUAGE_ISOLATION_METHODOLOGY.md

Development loop:
counterexample -> minimal repair -> re-attack -> regression -> cold reload -> physical checkpoint -> next

RED is never promoted.
No runtime-law change merely to absorb curriculum.
No byte padding.

## Recent lineage
G256 SELF/WORLD multimodal: 1426007 bytes.
G257 OmniCaption external multimodal teacher: 1458745 bytes, SHA256 762e0991d4d92a898c12220a85e207bb2bf92513eaeddb52ac3bc8fd3f2ae213.

## G258 — RUSSIAN LANGUAGE FIREWALL — CURRENT GREEN
Parent: G257.
- 130/130 admitted
- 0 dedup
- 0 rejected
- cold 20/20
- 1485478 bytes
- SHA256 97d91d65b98171f16d398e9939b69a20de1b183546dbd429115f5a85cbb302cd
- runtime changes 0

Purpose:
Keep Russian as the active natural-language learning channel while allowing foreign corpora to contribute abstract semantic structure without contaminating Russian lexicon/syntax.

Core:
LANGUAGE FORM != SEMANTIC CONCEPT.
LANGUAGE_ID is a property of message form, not truth.
LANG_RU is current active language-learning context.
LANG_EN remains an external/source context unless a future bilingual curriculum explicitly activates it.
Cross-language transfer must pass through semantic abstractions rather than mechanical word/syntax mixing.

Russian layer:
- Russian morphology is learned from Russian forms.
- Russian syntax is not copied from English word order.
- Russian idioms are not literal calques by default.
- Russian pronoun/reference mechanisms remain language-contextual.
- foreign sentences are not examples of Russian grammar.

English source quarantine:
- English quotation remains SOURCE_TEXT LANG_EN.
- English teacher text can teach an abstract relation without teaching Russian wording.
- English vocabulary/syntax from OmniCaption is not counted as Russian language training.
- foreign unknown fragments remain UNKNOWN rather than guessed.

Translation/code-switching:
TRANSLATION != COPYING.
TRANSLITERATION != TRANSLATION.
Accidental language mixture != intentional code-switching.
Code-switching and bilingual competence are future separately tested capabilities.

SELF/source:
source language != owner of experience.
source first-person != C4 autobiography.
language/source/content/SELF are separate dimensions.

Sensory language grounding:
raw waveform is not Russian or English before speech interpretation.
sound -> Russian word must be learned.
image -> Russian word must be learned.
one grounded concept may later acquire labels in several languages while preserving separate language rules.

## OmniCaption language audit
Uploaded OmniCaption remains a teacher-only corpus.
Measured across collected annotation text:
- Latin letters: ~15,964,104
- Cyrillic letters: 155
- Cyrillic detected in only 11 of 92,823 collected text fields
Therefore this uploaded corpus is overwhelmingly English.
Its abstract multimodal relations may transfer, but its English form is quarantined from Russian language curriculum.

## MERA Multi boundary
MERA Multi is a Russian multimodal benchmark and is reserved for evaluation, not training.
Published MERA Multi terms prohibit use of benchmark sets for model training.
This makes it valuable as a future unexposed Russian multimodal exam.

## Regression after G258
254 passed / 9 failed in 5.75s.
All 9 failures are unchanged missing historical G207/G137/G151/G153 artifact FileNotErrors.
No new semantic/runtime assertion failures.

## Recommended next Russian corpora
Training candidates, subject to exact split/license verification before ingestion:
- Russian LibriSpeech / RuLibriSpeech: Russian audio+transcript.
- Common Voice Russian: diverse Russian voices/audio+transcript.
- FLEURS ru_ru only: compact Russian speech+text.
- Golos: very large Russian speech corpus, but more restrictive license; treat separately.

For images, prefer raw pixels with Russian teacher labels or build a controlled synthetic visual nursery ourselves.
Do not use MERA benchmark examples for training.
