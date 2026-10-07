# C4 CONTEXTUAL SURFACE RESOLUTION NOTE

Status: FUTURE LANGUAGE RUNTIME / CURRICULUM, NOT IMPLEMENTED IN CANONICAL G289.

Goal:
understand typos, reductions, colloquial spellings and intentionally distorted forms without blindly "correcting" the user or turning the noisy surface into permanent lexical truth.

Core pipeline candidate:
RAW SURFACE
-> candidate lexical interpretations
-> local phrase compatibility
-> sentence-level compatibility
-> discourse/topic compatibility
-> speaker/idiosyncratic usage evidence
-> confidence-ranked interpretation
-> meaning/pragmatics

Important:
EDIT DISTANCE != IDENTITY.
UNKNOWN LEXEME != TYPO.
TYPO HYPOTHESIS != LEXICAL FACT.
SURFACE FORM != INTENDED LEXEME.
NORMALIZATION != CORRECTION.
NONSTANDARD != ERROR.

A typo may resemble many known words. Candidate narrowing should use several independent signals:
- character/edit similarity;
- keyboard-neighbor/transposition patterns;
- morphology;
- neighboring words and syntactic compatibility;
- sentence semantics;
- current discourse/topic;
- prior speaker-specific usage.

If one interpretation dominates, it may be used transiently for comprehension while the raw surface remains preserved.
If several remain plausible, keep ambiguity or ASK.
Do not store the resolved typo as a permanent synonym unless later evidence supports that lexical relation.

This note complements PRAGMATICS_PROSODY_ATOMIC_CURRICULUM_NOTE.md.
