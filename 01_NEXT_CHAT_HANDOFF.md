# NEXT CHAT HANDOFF — C4 G249

Read CURRENT_STATE.md, TRAINING_METHODOLOGY_LONG_CORPUS.md, LITERATURE_TRAINING_METHODOLOGY.md and SONG_AUDIO_TRAINING_METHODOLOGY.md first.

## Exact canonical baseline
- child_g249_audio_recurrence_green.c4m
- 1247711 bytes
- SHA256 b28f2fe078b896e768f9b20efb112a1b51aa5bc40a596d9f9c9bdaacc1b71e46
- generation G249

Verify exact bytes/SHA before training.
Never silently fall back to G248/G246/G244 or reconstruct from prose.

Persistent recovery:
- personal Library /C4_Canonical/ should contain exact G248 model/release
- audio source corpus should be in /C4_Corpora/Audio_Ruslan_Likes_G247/
- project/conversation artifacts are fallback only

## What changed after G246
G247 consumed eight REAL MP3 artifacts through a physical feature-extraction pass.
G248 bound text/audio only where user context actually supports identity.

C4 therefore has:
- actual measured acoustic observations from real recordings
- song-level multimodal bindings for April and Ledyanoy Vozduh
- text-only semantic cell for Otkrytyy Kosmos because no exact matching MP3 was identified

This is NOT live hearing.
This is NOT proof of waveform-to-lyrics recognition.

## G247 rules
AUDIO FILE != LIVE PERFORMANCE
FEATURE ESTIMATE != GROUND TRUTH
ACOUSTIC FEATURE != EMOTION/LYRICS/INTENT
AUDIO_ARTIFACT != ANALYZER_FEATURE != SEMANTIC INTERPRETATION
BYTE IDENTITY != RECORDING IDENTITY != PERFORMANCE IDENTITY != SONG IDENTITY
SAME TITLE + ACOUSTIC SIMILARITY != BYTE IDENTITY

Two Вглядываясь вверх files are distinct artifacts and nearest acoustic-profile pair in the batch; do not merge them blindly.

## G248 rules
TEXT != AUDIO
SONG-LEVEL BINDING != TOKEN-LEVEL ALIGNMENT
LIKES SONG != BELIEVES EVERY LYRIC
HYPERBOLE != PHYSICAL LAW
PERSONIFICATION != VERIFIED AGENT
AUDIO MISSING -> UNKNOWN
Never borrow a thematically similar track as another song's audio.

April:
- text + AUDIO_G247_APREL
- exact token alignment unknown

Ledyanoy Vozduh:
- text + AUDIO_G247_LEDYANOY_VOZDUH
- exact token alignment unknown
- atom/molecule/cell vs phrase/thought/verse is cross-domain analogy
- superluminal lyric is hyperbole
- deterministic lyric is viewpoint, not universe law

Otkrytyy Kosmos:
- user-supplied text + rich science/philosophy/language layers
- exact audio absent from current batch
- keep audio UNKNOWN

## Active literature
Dostoevsky remains ACTIVE; do not abandon it.
Continue from G248 while choosing whether next GREEN block is literature or audio based on user input.

## Development loop
counterexample -> minimal repair -> re-attack -> regression -> cold reload -> physical checkpoint -> next

RED never canonical.
No runtime repair merely to fit curriculum.
No byte padding.

## Latest regression
254/263 passed.
All 9 failures are unchanged missing historical G207/G137/G151/G153 artifact FileNotFoundErrors.
No new semantic/runtime assertion failure.

## Next true audio experiments
Prefer falsifiable tests:
1. motif/repetition detection from audio without semantic labels;
2. segment boundaries and recurrence;
3. external transcript alignment as teacher hypothesis, never raw observation;
4. repeated vowel/token clustering;
5. later teacher says/shows A -> acoustic target -> motor attempt -> self-hearing -> correction.

Do not claim C4 hears/speaks until those loops physically exist.


## G249 temporal-audio addition
G249 analyzed the eight real MP3 files for recurrence without using title/lyrics to define the repeat pairs.

Method:
- beat-synchronous chroma CENS
- 8-beat windows
- cosine recurrence similarity
- temporally nearby windows excluded from candidate search

Preserve:
RECURRENCE CANDIDATE != CHORUS LABEL.
HIGH CHROMA SIMILARITY != SAME LYRICS/TIMBRE/BYTES.
DERIVED TOOL OBSERVATION != SELF-ACQUIRED SENSOR ALGORITHM.

Useful observations:
- April and Ledyanoy Vozduh contain strong nonlocal recurrence candidates.
- Both distinct Vglyadyvayas vverkh files show closely matching recurrence timings.
- Defragmentaciya has method-dependent conflicting tempo estimates (~92 BPM in G247 sampled analysis versus ~117 BPM in G249 full-track beat analysis). Do NOT choose a winner without resolving method/metrical ambiguity; preserve both with provenance.

Next recommended falsifier:
Use audio unseen by the recurrence curriculum, withhold labels, and test whether the same preprocessing+reasoning path can recognize recurrence/variation without memorized timestamps.
