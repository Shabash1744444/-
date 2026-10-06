# NEXT CHAT HANDOFF — C4 G258

Read CURRENT_STATE.md and all methodology files, especially LANGUAGE_ISOLATION_METHODOLOGY.md.

## Exact canonical baseline
- child_g258_russian_language_firewall_green.c4m
- 1485478 bytes
- SHA256 97d91d65b98171f16d398e9939b69a20de1b183546dbd429115f5a85cbb302cd
- generation G258

Verify exact bytes/SHA before training.
Persistent recovery: /C4_Canonical/ first.

## Language policy
Russian is the active natural-language curriculum.

Preserve:
LANGUAGE FORM != SEMANTIC CONCEPT
foreign source text != Russian lexical/syntactic training
translation != copying
transliteration != translation
accidental mixture != code-switching
source first-person != C4 SELF

OmniCaption is overwhelmingly English and remains teacher-only:
- abstract multimodal relations may transfer
- English word/syntax patterns must not be used as Russian grammar examples

Future bilingual learning must be an explicit separate phase after Russian grounding is stable.

## MERA Multi
Do NOT train on MERA Multi benchmark sets.
Use them only as held-out Russian multimodal evaluation under their published terms.

## G258
130/130 admitted, cold 20/20, runtime changes 0.
Regression 254/263 with only the same missing historical artifacts.

## Recommended next data
Prefer Russian raw sensory corpora:
- RuLibriSpeech
- Common Voice RU
- FLEURS ru_ru
- Golos only after license constraints are explicitly accepted

For vision, either find a genuinely trainable Russian image-text dataset with clear license or generate a controlled raw-image nursery and attach Russian labels ourselves.

Continue Dostoevsky, speech nursery and raw sensory work in parallel.
