# RUNTIME CURRENT — G268 SURFACE / VERBALIZER REPAIR

Canonical weights remain G266.

## Files
Runtime:
C4_RUNTIME_G268_SURFACE_VERBALIZER_GREEN_2026-10-07.zip
SHA256 db02d7f9c4da15cfbcc38ef4a3110e696e611eaaef90e3612effa84761cf60bb

Runtime + G266 weights:
C4_G268_RUNTIME_PLUS_G266_WEIGHTS_2026-10-07.zip
SHA256 ad93604fb662da091e696a31e7f66cf7794ea51a6fd71efaa32892cea69dc1aa

Weights:
child_g266_object_permanence_green.c4m
SHA256 1fbbf2c26c8253dab51c5e7555bbb0656a36ca0de98a7874a5589556017b3ea6

## What G268 fixes
Android screenshots exposed three runtime-surface failures after G267:
1. basic greeting still fell into unresolved-language output;
2. user sentence `Я не понимаю тебя` leaked internal SELF grounding;
3. initiative verbalized opaque graph labels like g223/node A/B.

G268 adds:
- basic Russian social/discourse acts;
- correct speaker perspective for user misunderstanding reports;
- discourse-pronoun/internal-ID filtering;
- public-label firewall for autonomous initiative;
- suppression of unrenderable internal gaps while preserving human-readable questions.

## Validation
- G267+G268 dialogue tests: 14/14 PASS.
- full source suite: 268 PASS / 9 FAIL.
- all 9 failures are unchanged missing historical G207/G137/G151/G153 model files.
- real G266 screenshot re-attack passed.

G268 changes runtime only. Weights remain G266.
