# C4 PRAGMATICS / PROSODY ATOMIC CURRICULUM NOTE

Status: FUTURE LANGUAGE + MULTIMODAL CURRICULUM
Date: 2026-10-07

## Core principle

Do not map surface profanity/slang directly to one emotion or one intent.

Examples:
- "пиздец" may express shock, admiration, horror, amusement, frustration, emphasis, or social alignment.
- "заебись" may be sincere positive evaluation, sarcastic negative stance, relief, surprise, or emphatic confirmation.
- "да заебал" may be genuine irritation, joking protest, affectionate teasing, boundary-setting, or escalating conflict.
- elongated forms such as "заебииииись" add prosodic/emphatic evidence but do not uniquely determine valence or intent.

Atomic interpretation should separate at least:
1. SURFACE FORM
2. LEXICAL/CONCEPTUAL CONTENT
3. SPEECH ACT / PRAGMATIC FUNCTION
4. AFFECT VALENCE
5. AROUSAL / INTENSITY
6. STANCE (approval, rejection, irony, uncertainty, mockery, solidarity...)
7. TARGET / ADDRESSEE
8. PROSODY / INTONATION / DURATION / STRESS
9. DISCOURSE CONTEXT
10. WORLD / SITUATIONAL CONTEXT
11. SOCIAL RELATION / REGISTER
12. CONFIDENCE / AMBIGUITY

Do not collapse these axes into a single "sentiment" field.

## Important boundaries

SURFACE FORM != INTENT
PROFANITY != NEGATIVE AFFECT
PROSODY != EMOTION
ELONGATION != POSITIVE OR NEGATIVE
INTONATION != TRUTH
SLANG != ERROR
NONSTANDARD != UNKNOWN
UNDERSTAND != EMIT
COMPREHENSION POLICY != GENERATION STYLE

Prosody is evidence about interpretation, not authority.

## Example

Input:
"заебииииись"

Possible candidate interpretations may differ by:
- rising/falling contour
- duration and stress
- previous turn
- facial expression/video context
- current task outcome
- speaker relationship

The same lexical surface can therefore map to different pragmatic structures without changing lexical identity.

## Training approach

Train minimal contrasts, not phrase memorization.

Example curriculum unit:
A. same lexical surface + different prosody/context -> different pragmatic interpretation
B. different surfaces + same pragmatic function -> same higher-level act
C. same words + different addressee/target -> different social meaning
D. profanity removed but prosody/context preserved -> pragmatic act should remain recoverable when possible
E. prosody removed -> uncertainty should increase rather than forcing one interpretation

Use positive, negative, ambiguous and abstention cases.

## Multimodal path

RAW AUDIO
-> PHONETIC SURFACE
-> lexical candidates
-> prosodic features
-> discourse/world context
-> pragmatic candidates
-> confidence/ambiguity
-> selected interpretation or ASK/UNKNOWN

Never store a transient pronunciation/prosodic guess as permanent lexical truth.

## Generation boundary

C4 may understand a form that generation policy never chooses to emit.

A future generation layer may condition on:
- user preference
- relationship/register
- safety/policy
- persona/style
- current affective stance

This layer must not alter comprehension truth.

## Goal

Robustly understand real human speech:
typos, slang, profanity, reductions, intentional distortion, irony, emphasis, fillers, deixis and emotional prosody
without forcing every surface into a canonical spelling or one fixed sentiment.
