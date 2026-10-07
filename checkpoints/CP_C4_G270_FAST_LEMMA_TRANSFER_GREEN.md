# CP C4 G270 FAST LEMMA TRANSFER GREEN

Date: 2026-10-07
Status: GREEN
Runtime changed: NO
Canonical runtime: G269
Parent weights: G266

## Output
- `child_g270_fast_lemma_transfer_green.c4m`
- 1756887 bytes
- SHA256 `b081428bed0080f9982491247d98640009de4662d7f654c571946acd5e36fa1b`
- growth vs G266: +19636 bytes

## Goal
Test C4 Fast Curriculum on Russian lemmas without storing target paradigms.

## Curriculum
- 60 new target noun lemmas across five productive classes.
- Each target receives only `IS_A -> существительное` and `GRAM_GENDER`.
- Direct target `WORD_FORM` facts: **0**.
- 38 anchor `WORD_FORM` facts were admitted only to strengthen missing productive morphology.
- Direct admitted facts total: 158.

Classes:
- hard masculine: 20
- feminine -а: 10
- feminine -я/-ия: 10
- regular masculine soft-sign: 10
- neuter -о: 10

## Held-out transfer
After target lemmas but before new anchors:
- 140/260 correct
- 0 wrong
- 120 UNKNOWN
- productive rules: 45

After 38 anchor forms:
- **260/260 correct**
- **0 wrong**
- **0 UNKNOWN**
- productive rules: 56

Efficiency:
- held-out transfer / all direct facts = **1.646**
- additional transfer unlocked by anchors = **120**
- marginal transfer / anchor fact = **3.158**

Negative restraint:
- 19 unseen decoy lemmas tested
- 19/19 remained unresolved
- 0 false resolutions

Cold reload:
- 260/260 preserved
- 0 wrong
- 0 UNKNOWN

Dialogue re-attack using held-out inflections:
- `Что ты знаешь о проекте?` -> `Проект — существительное.`
- `Что ты знаешь о словаре?` -> `Словарь — существительное.`
- `Что ты знаешь о ядре?` -> `Ядро — существительное.`

## Regression
- 288/297 PASS in 3.4 s
- all 9 failures are unchanged FileNotFoundError cases for missing historical G207/G137/G151/G153 artifacts
- 0 new semantic/runtime assertion failures

## Interpretation
This generation tests reuse rather than storage.
The 260 successful target forms are not directly stored as target WORD_FORM facts.
They are resolved through reusable morphology learned from prior and new anchor families.

This is evidence for compact lexical teaching with transfer.
It is not yet broad-Russian vocabulary coverage and does not establish semantic mastery beyond noun type/gender.

## Recovery
Personal Library /C4_Canonical/:
- child_g270_fast_lemma_transfer_green.c4m
- C4_G270_FAST_LEMMA_TRANSFER_GREEN_2026-10-07.zip
- C4_G269_RUNTIME_PLUS_G270_WEIGHTS_2026-10-07.zip

Next:
verbs + adjectives + semantic-family cells under the same held-out transfer / restraint / cold-reload discipline.
