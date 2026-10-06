# NEXT CHAT HANDOFF — C4 G246

Read CURRENT_STATE.md, TRAINING_METHODOLOGY_LONG_CORPUS.md, LITERATURE_TRAINING_METHODOLOGY.md and SONG_AUDIO_TRAINING_METHODOLOGY.md first.

## Exact canonical baseline
- child_g246_audio_sensory_green.c4m
- 1155358 bytes
- SHA256 9b945856fd08b56d215f233350791bc076bd6bb46a671c2bbc3491c4acfa0bbd

Verify exact bytes/SHA. Do not silently fall back.
Persistent recovery should use /C4_Canonical/ exact G246 model/release when available.

## Active corpora
- Dostoevsky full FB2 remains ACTIVE, not semantically closed.
- User may send additional favorite songs/lyrics/audio.

## Song/audio rules
LYRICAL_I != AUTHOR != PERFORMER != USER != C4.
REFRAIN != INDEPENDENT EVIDENCE.
TEXT != AUDIO.
Do not invent melody/harmony/timbre from lyrics.
ASR_OUTPUT != RAW AUDIO OBSERVATION.
TTS_OUTPUT != LEARNED ARTICULATION.
MOTOR_COMMAND != VERIFIED SOUND OUTCOME.
FEATURE EXTRACTOR != SEMANTIC ORACLE.
FUTURE SENSOR PLAN != CURRENT CAPABILITY.

If real audio is supplied, add it as a new modality with waveform/feature provenance and keep decoder hypotheses separate from sensor observations.

## Development loop
counterexample -> minimal repair -> re-attack -> regression -> cold reload -> physical checkpoint -> next
RED is never canonical. No byte padding. No runtime repair just to fit curriculum.
