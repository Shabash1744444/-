# CP C4 G273 FAST ADJECTIVE TRANSFER GREEN

Date: 2026-10-07
Status: GREEN
Parent weights: G272
Runtime: G271

## Curriculum
- 78 target adjective lemmas.
- classes: hard -ый, soft -ий, regular/stressed -ой, velar -кий/-гий/-хий.
- direct target WORD_FORM facts: 0.
- anchor WORD_FORM facts: 16.
- direct facts total: 99.

## Transfer
Before anchors: 528/780 correct, 252 UNKNOWN, 0 wrong.
After anchors: 780/780 correct, 0 UNKNOWN, 0 wrong.

- transfer/direct = 7.879
- newly unlocked = 252
- marginal transfer/anchor = 15.750

## Homograph quarantine
Do not force lexical identity when a new lemma collides with an already useful surface.
Quarantined from the clean morphology exam:
- `целый` because `целое` already has an independent concept;
- `лёгкий` because `лёгкое` already has an independent concept;
- `дорогой` because the same surface is an inflected form of `дорога`.

These require contextual POS/sense disambiguation, not destructive merge.

## Output
- child_g273_fast_adjective_transfer_green.c4m
- 1787794 bytes
- growth vs G272: +13847 bytes
- SHA256 f22cdfa4a62811692374cb8bdeec31140652bfb3a65a083917d87ed58b380550
