# C4 G270 FAST LEMMA TRANSFER PILOT

Status: executed GREEN curriculum.

## Principle
Do not store target paradigms.

For each target lemma:
1. create/resolve the lemma concept;
2. type it as `существительное`;
3. teach grammatical gender;
4. withhold all target WORD_FORM values;
5. probe unseen inflections through RussianMorphologyV1;
6. add only small anchor families where productive transforms are missing;
7. re-probe with decoys;
8. cold reload;
9. full regression;
10. physical checkpoint.

## G270 result
- 60 new target noun lemmas
- 0 direct target WORD_FORM facts
- 38 anchor WORD_FORM facts
- 260/260 held-out target forms resolved after training
- 0 false decoy resolutions
- cold reload preserved 260/260
- runtime unchanged

## Rule
A lexical batch is useful only when it increases held-out transferable language behavior faster than it increases directly stored target forms.

Next batches must report:
- direct lessons
- held-out transfer
- correctly UNKNOWN
- false inference
- bytes added
- cold reload
- regression
- teacher cost
