# CURRENT STATE

Date: 2026-10-07
Canonical weights: G307
Canonical runtime: G307

Weights:
- child_g307_sound_grapheme_words_green.c4m
- 1,988,842 bytes
- SHA256 648ba7eeaf1f1f1af038949e228b1e9a37afd115ff6920952533143bbda8350f

Runtime:
- C4_RUNTIME_G307_SOUND_GRAPHEME_WORDS_GREEN_2026-10-07.zip
- 307,584 bytes
- SHA256 b18c746f61fa9e4ec6af5323657ac6af0ede64b5b30a4ef4a51c5c1a1731c7ca

Combined:
- C4_G307_RUNTIME_PLUS_G307_WEIGHTS_2026-10-07.zip
- 2,266,334 bytes
- SHA256 4068e8c8c7a6128747433e3c92bb5795b1f33faed385784c27d3d3e095285f49

## G306
Verified synthetic 3D motor priors.

## G307
Sound / grapheme / word-form grounding:
- 6 phoneme-side concepts;
- 6 grapheme-side concepts;
- 24 repeated sound↔glyph alignments;
- PHONEME != GRAPHEME;
- many-to-many mapping allowed;
- 5 words learned as separate audio and glyph sequences converging on one word entity;
- noisy heldout 5/5 audio + 5/5 glyph;
- SQLite 5/5 + 5/5;
- proposition fact/evidence store unchanged by lexical-form training;
- G306 spatial effects retained 10/10;
- G302 reasoning retained 44/44 direct + 24/24 restraint in memory/SQLite.

Full runtime regression:
409 passed + 16 missing-file environment failures in memory;
409 passed + 16 missing-file environment failures in SQLite;
new semantic failures 0.

## Current objective
Continue synthetic physics with contact/collision and effort/mass-like resistance; then expand audio/visual form grounding and connect application-room sensor adapters.
