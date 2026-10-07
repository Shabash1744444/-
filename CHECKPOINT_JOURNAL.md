# CHECKPOINT JOURNAL

Highlights:
G270 noun morphology.
G271 POS safety.
G272 verb transfer.
G273 adjective transfer.
G274 dense semantics.
G275 live teaching.
G276 ActiveGaps.
G277 guided measurement.
G278 guided reading.
G279 guided prose.
G280 everyday core.
G281 lexical gaps without lemma guessing.
G282 16 action-context lexemes; 31/31 unseen forms after six reusable anchors.
G283 32 more contextual lexemes; 52/52 unseen forms with no new anchors.
G284 semantic family consolidation: 37 known concepts -> 6 families; 148 strict-new inherited relations / 67 direct = 2.209. First standardized run with source manifest and held-out frozen before lessons.

Current weights SHA256 efcdf9c63116fc056bf3fc19deeda83e62b08f922fe4123136b5a733f8b3a95b
Current runtime SHA256 eb1572c417c25eb7e6ef5a9d2b620b5692ada859ff5011931a561625aa18bc04

Workflow:
exact parent -> source manifest -> frozen held-out -> source-scoped run queue -> one gap -> one answer -> rerank -> held-out -> restraint -> full regression -> cold reload -> cumulative -> physical checkpoint -> next.
