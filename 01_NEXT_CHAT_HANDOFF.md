# NEXT CHAT HANDOFF — C4 G282 WEIGHTS + G281 RUNTIME

Weights:
- child_g282_guided_action_terms_green.c4m
- 1860329 bytes
- SHA256 c1fabfa4028d993de7614c2dd321aab0bb2f99d8fb13011781d1048dffbeb243

Runtime:
- C4_RUNTIME_G281_LEXICAL_GAPS_GREEN_2026-10-07.zip
- SHA256 eb1572c417c25eb7e6ef5a9d2b620b5692ada859ff5011931a561625aa18bc04

Combined:
- C4_G281_RUNTIME_PLUS_G282_WEIGHTS_2026-10-07.zip
- SHA256 9c73640ceb484315e58571d748ec03488934567d864e2fd453f184e45dc1f70d

Recovery: /C4_Canonical/.

G281 clean regression: 335/344, same 9 missing historical files only.

G282:
- 50 action sentences
- 16 contextual lexical gaps
- 16 teacher definitions / 48 words
- no guessed lemmas
- 0 target WORD_FORM
- 31/31 held-out after 6 non-target anchors
- cold 31/31
- full cumulative GREEN

Next: scale contextual lexical learning with larger mixed guided passages. Keep raw-form questions conservative; do not add lemma prediction.
