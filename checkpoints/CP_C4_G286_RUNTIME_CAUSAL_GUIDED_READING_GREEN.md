# CP C4 G286 RUNTIME CAUSAL GUIDED READING GREEN

Runtime artifact:
C4_RUNTIME_G286_CAUSAL_GUIDED_READING_GREEN_2026-10-07.zip
SHA256 b51670f57fa3a3d953ac3d096203b4015fdcb74eb18ad43c872018b8e1daa896

Counterexample:
G281 skipped ordinary causal prose even though the reasoner already supported CAUSES.

Repair:
GuidedReaderRU accepts CAUSES only when both endpoint concepts already exist and stores the object as entity relation with EXTERNAL_CORPUS provenance. Unknown endpoints are skipped without mutation.

Regression:
339/348, only 9 known missing historical artifacts.
