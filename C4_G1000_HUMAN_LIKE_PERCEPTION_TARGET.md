# C4 G1000 TARGET — HUMAN-LIKE PERCEPTION COVERAGE

Status: DEVELOPMENT TARGET
Date: 2026-10-07
Canonical start point for this target: G292 weights + G289 runtime.

## Goal

By approximately G1000, C4 should not merely store more knowledge.

The target is broad, trap-resistant perception and interpretation:
raw input -> candidate interpretations -> context -> meaning -> pragmatics -> epistemic status -> response/action.

"Human-like perception" here is an engineering target, not a claim of human consciousness.

It means:
- robust understanding of clean and dirty language;
- tolerance to typos, reductions, slang, deliberate distortion and ASR noise;
- discourse/topic/context narrowing;
- ambiguity preservation when context is insufficient;
- multimodal grounding when text alone is underspecified;
- pragmatic and prosodic interpretation;
- source/conflict/provenance awareness;
- strong UNKNOWN behavior;
- resistance to cross-relation traps and plausible false statements;
- ability to learn new concepts without assuming unknown == error;
- comprehension separated from generation style.

## Current relation registry

C4 currently declares 37 graph relation types:

NAME
LOCATION
COLOR
WHEELS
VALUE
LIKES
HAS
IS_A
PART_OF
CAN
PROPERTY
OPPOSITE
CAUSES
BEFORE
AFTER
MEANS
SYNONYM
ANTONYM
WORD_FORM
HAS_PART
USED_FOR
FOUNDATIONAL
RULE
ROLE
SUCCESSOR
HAS_SIDES
HAS_CORNERS
GRAM_GENDER
PREDICATE_RELATION
QUERY_RELATION
PREDICATE_PRESENT_FORM
PREDICATE_PAST_FORM
EVENT_PREDICATE
EVENT_SUBJECT
EVENT_OBJECT
EVENT_TENSE
EVENT_POLARITY

Not every relation should inherit or compose in the same way.
A major G293-G1000 objective is to learn and test each relation's legitimate algebra and its forbidden inferences.

## Mandatory coverage dimensions for every important relation family

For each relation/capability, do not count "supported" until tests cover:

1. direct positive
2. direct negative
3. UNKNOWN
4. multi-valued vs functional cardinality
5. source/provenance
6. contradiction/conflict
7. correction/retraction
8. cold persistence
9. composition/transfer where valid
10. explicit non-composition where invalid
11. cross-relation confusion traps
12. lexical/morphological variation
13. dirty-surface variation
14. discourse/context dependence
15. speaker/source dependence
16. adversarial plausible falsehood
17. question must not create truth
18. derived != direct evidence
19. confidence/ambiguity behavior
20. cumulative regression

## Development bands

### G293-G380 — Relation algebra and traps
Systematically cover under-tested world relations:
HAS, HAS_PART, PART_OF, ROLE, MEANS, BEFORE/AFTER, LOCATION, OPPOSITE/SYNONYM/ANTONYM, functional VALUE/COLOR/etc.
Measure which relations are transitive, symmetric, inverse, inherited, contextual, or explicitly non-composable.
Build cross-relation trap packs.

### G381-G480 — Dirty language / surface resolution
Typos, transpositions, missing letters, glued/split words, keyboard-neighbor errors, colloquial reductions, deliberate distortion, slang, fillers.
Candidate narrowing should use:
surface similarity -> morphology -> local words -> sentence -> discourse/topic -> speaker-specific history.
No correction guess becomes permanent lexical truth automatically.

### G481-G580 — Discourse and deixis
Pronouns, ellipsis, reference, "это/то/вон там/другой/его/её", topic continuity, repair turns, interruptions, conversational grounding.
Text interpretation must be allowed to remain unresolved until world/context evidence arrives.

### G581-G680 — Pragmatics and prosody
Separate:
surface, lexical identity, speech act, valence, arousal, stance, addressee, prosody, discourse, world context, social register, confidence.
Train minimal contrasts:
same words/different intonation; different words/same pragmatic act.
UNDERSTAND != EMIT.

### G681-G760 — Source, conflict, correction, uncertainty
Trusted/untrusted/unknown sources, conflicting teachers, revisions, time-varying facts, reported speech, fiction/world scope, rumor, quotation, hypothesis.
Nothing becomes absolute truth merely because it is grammatical or authoritative-looking.

### G761-G840 — Multimodal grounding
Audio/text alignment, visual reference, object permanence, noisy sensor evidence, cross-modal disagreement.
RAW SIGNAL != TEACHER LABEL.
PROSODY != EMOTION.
DEIXIS may require scene state.

### G841-G920 — Long mixed material
Longer ordinary text, books, conversations, technical explanations, interruptions and irrelevant material.
C4 should extract useful structure, dedup known content, ask for high-value gaps, and leave unsupported material unresolved.

### G921-G1000 — Adversarial integration
Mixed attacks across all prior dimensions:
typo + slang + ambiguous reference + source conflict + false causal inference + sarcasm + missing context + multimodal disagreement.
No single benchmark family should dominate.
Focus on generalization and correct abstention.

## Promotion target near G1000

Do not call the perception stage mature merely because generation number reaches 1000.

Require:
- relation coverage matrix with no critical untested family;
- sustained cumulative retention;
- low false-inference rate under adversarial mixed tests;
- dirty-input comprehension without graph pollution;
- topic/discourse narrowing;
- ambiguity preserved when evidence is insufficient;
- source/conflict/retraction integrity;
- multimodal context able to resolve text that text alone cannot;
- comprehension independent from emission/style policy;
- teacher cost continuing to decline on structurally familiar new domains.

## Principle

The target is not:
"always guess what a human meant."

The target is:
"recover meaning when evidence supports it, keep alternatives when several fit, and remain UNKNOWN when the evidence is insufficient."

That is the intended C4 analogue of robust human-like perception.
