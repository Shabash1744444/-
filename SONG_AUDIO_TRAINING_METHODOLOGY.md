# C4 SONG / AUDIO TRAINING METHODOLOGY

Normative for lyric + future audio learning.

## Text-song layer
LYRICAL_I != AUTHOR != PERFORMER != USER != C4.
SONG TEXT != EXTERNAL WORLD OBSERVATION.
REFRAIN repetition != independent evidence.
METAPHOR != PHYSICAL PROPERTY.
TEACHER INTERPRETATION != SOURCE TEXT.
User liking a song is CREATOR_REPORTED preference, not factual authority over lyric claims.

## Missing-audio rule
TEXT != AUDIO.
Do not invent melody, harmony, tempo, key, instrumentation, timbre, singer identity, or acoustic emotion from lyrics alone.
Absent acoustic modality remains UNKNOWN.

## Future audio observation
Raw/recorded audio begins as waveform/time-series observation.
Useful low-level features may include:
- sample rate/time
- spectral energy / FFT / STFT
- onset/offset/duration
- f0/pitch candidates
- harmonics/partials
- spectral envelope/formants
- RMS/dB with explicit reference/assumptions
- rhythm/tempo candidates
- uncertainty and sensor provenance

WAVEFORM != MEANING.
FEATURE EXTRACTOR != SEMANTIC ORACLE.
SPECTROGRAM != SOUND ITSELF.

## Speech
ASR_OUTPUT != RAW AUDIO OBSERVATION.
ASR hypothesis can be a teacher/reference but must retain decoder provenance and confidence.
PHONEME != WAVEFORM.
FORMANT != PHONEME LABEL.

## Voice learning
TTS_OUTPUT != LEARNED ARTICULATION.
MOTOR_COMMAND != VERIFIED SOUND OUTCOME.
Learning loop:
teacher acoustic token -> observation -> target structure -> motor attempt -> self-produced sound -> self-hearing -> comparison -> update.

SELF-GENERATED OBSERVATION != INDEPENDENT EXTERNAL EVIDENCE.

## Multimodal
A future concept may connect visual/acoustic/spatial/motor/language/causal/temporal layers.
NO SINGLE MODALITY IS THE WHOLE OBJECT.
Audio/visual co-occurrence supports binding hypotheses but CO-OCCURRENCE != IDENTITY/CAUSALITY.

## Current capability
G246 has conceptual/mathematical foundations only.
No live microphone, vision organ, or learned articulatory motor loop is currently connected.
FUTURE SENSOR PLAN != CURRENT CAPABILITY.


## Real-audio grounding protocol (G247+)
When actual audio files are supplied, preserve three distinct layers:

1. AUDIO ARTIFACT
- exact file/hash/container identity
- encoded samples/metadata
- recording artifact provenance

2. DERIVED ACOUSTIC MEASUREMENT
- duration/sample timing
- spectral summaries
- onset/tempo hypotheses
- harmonic/percussive decomposition
- pitch/chroma/formant candidates
- analyzer method + uncertainty

3. SEMANTIC / MUSICAL INTERPRETATION
- lyrics
- song identity
- emotion/style/theme
- listener preference
- metaphor/philosophy

AUDIO_ARTIFACT != ANALYZER_FEATURE != SEMANTIC INTERPRETATION.
FEATURE ESTIMATE != GROUND TRUTH.
ACOUSTIC FEATURE != EMOTION/LYRICS/INTENT.

## Audio identity hierarchy
Do not collapse:
BYTE IDENTITY
RECORDING/MASTER IDENTITY
PERFORMANCE IDENTITY
SONG/COMPOSITION IDENTITY

The same song can exist in different encodings.
Similar acoustics + same title support an identity hypothesis but do not prove byte/master identity.

## Cross-modal song binding
TEXT != AUDIO.
Song-level text/audio identity may be learned from user labels, metadata, temporal alignment or repeated evidence.
SONG-LEVEL BINDING != TOKEN/PHONEME-LEVEL ALIGNMENT.

A supplied transcript is a teacher/source layer. It does not prove C4 itself decoded the waveform.

If exact audio for a titled lyric is absent:
AUDIO = UNKNOWN.
Never substitute a thematically similar recording.

## Real audio does not equal live hearing
Consuming analyzer-derived observations from stored MP3 files is grounded audio learning, but:
STORED AUDIO ANALYSIS != CONTINUOUS MICROPHONE ORGAN.
Do not claim live hearing until physical streaming sensor input exists.

## Music and preference
User liking a song is authoritative about reported preference, not about why the song is liked and not about truth of the lyrics.
LIKES SONG != BELIEVES EVERY LYRIC.
LIKE LABEL != KNOWN CAUSAL FEATURE OF PREFERENCE.

## Next falsifiable ladder
1. detect recurring structure/motifs from audio without title labels;
2. segment events and repetitions;
3. align external transcript as a separate teacher hypothesis;
4. cluster repeated acoustic tokens/vowels;
5. bind symbol/text to acquired acoustic category;
6. motor attempt -> produced audio -> self-hearing -> compare -> update.

ASR can assist as teacher/reference but ASR SUCCESS != C4 LEARNED HEARING.


## Temporal recurrence protocol (G249+)
A static whole-track feature vector is not enough for musical structure.
Preserve ordered temporal observations.

Recommended low-level path:
waveform -> onset/beat candidates -> time-frequency/pitch-class representation -> local temporal windows -> similarity/recurrence candidates.

RECURRENCE CANDIDATE != CHORUS LABEL.
RECURRENCE != EXACT REPETITION.
HIGH CHROMA SIMILARITY != SAME LYRICS/TIMBRE/BYTES.
LOCAL RECURRENCE != WHOLE-TRACK IDENTITY.

Do not use source title or transcript to define a repeat during the sensory test.
After recurrence is detected, source text may be used in a separate alignment/interpretation stage.

## Measurement disagreement
Real sensory measurements can disagree because of:
- analysis window
- estimator
- meter/half-time/double-time ambiguity
- section changes
- noise/compression

Store:
VALUE + METHOD + WINDOW + SOURCE + UNCERTAINTY.

A later estimate does not automatically supersede an earlier one.
DIFFERENT ESTIMATORS/WINDOWS CAN DISAGREE without either being fraud or without requiring immediate runtime repair.

## Autonomy boundary
G249 recurrence was computed by an external low-level signal analyzer and then taught to C4.
This is useful grounded sensory input but is not proof that C4 runtime has independently implemented motif detection.

DERIVED TOOL OBSERVATION != SELF-ACQUIRED SENSOR ALGORITHM.

The next stronger test is held-out audio recurrence/segmentation where semantic labels and timestamps are withheld.
