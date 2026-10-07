# CP C4 G281 RUNTIME LEXICAL GAPS GREEN

Date: 2026-10-07
Status: GREEN
Parent runtime: G278
Weights changed: NO

## Purpose
Unknown inflected terms inside supported action/predicate objects become learning gaps, not guessed lemmas.

## Physics
- unknown surface is represented as `surface:<raw>`, never as a new world entity;
- no lemma candidate is asserted;
- C4 asks for dictionary form + meaning;
- gap closes only after teacher creates/defines a real lexeme and existing morphology maps raw surface to it;
- repeated surfaces aggregate downstream causes for ActiveGaps;
- lexical gaps persist across save/reopen.

## Negative controls
`печи, пути, времени, семени, матери, дочери, луки` do not fabricate `печа, пута, времена, семена, матера, дочера, лука`.

## Validation
- focused 7/7
- clean full suite 335/344
- only 9 known missing historical artifact failures
- G280 cumulative fully GREEN

Runtime artifact:
- C4_RUNTIME_G281_LEXICAL_GAPS_GREEN_2026-10-07.zip
- 285041 bytes
- SHA256 eb1572c417c25eb7e6ef5a9d2b620b5692ada859ff5011931a561625aa18bc04

Hard law: LEXICAL HYPOTHESIS != LEMMA FACT.
