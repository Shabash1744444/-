# C4 SENSORY TRAINING METHODOLOGY

Normative from G251 onward.

## 1. Principle
A sensor front-end may compress physical signals into stable measurable structure.
It must not silently solve the semantic task for C4.

raw signal -> low-level structure -> temporal relations -> hypotheses -> learned association -> meaning

Do not replace this with:
raw signal -> ready-made human sentence.

## 2. Provenance levels
Keep distinct:
RAW ARTIFACT
DECODED SIGNAL
DERIVED FEATURE
EXTERNAL ANALYZER HYPOTHESIS
TEACHER LABEL
C4 LEARNED ASSOCIATION
C4 SELF-ACQUIRED SENSOR SKILL

DERIVED FEATURE != RAW OBSERVATION.
EXTERNAL ANALYZER != C4 ORGAN.

## 3. Audio
Waveform, STFT, pitch/formant candidates, onset, energy, recurrence and similar features are measurements with method/window provenance.

FEATURE ESTIMATE != GROUND TRUTH
ACOUSTIC FEATURE != LYRICS
ACOUSTIC FEATURE != EMOTION
RECURRENCE != CHORUS automatically
SAME CATEGORY != IDENTICAL WAVEFORM

ASR output may be a teacher hypothesis but never raw hearing.
TTS output may be an actuator/tool but never proof of learned articulation.

## 4. Speech nursery
Start with controlled synthetic stimuli so target generation physics is inspectable.
Keep:
generator command != resulting waveform
target label != autonomously discovered category
synthetic tutor != human voice

Desired loop:
teacher target -> auditory representation -> C4 chosen motor command -> synthesizer -> actual sound -> self-hearing -> error/comparison -> C4 update.

Only call pronunciation learned when C4 itself chooses/refines commands on held-out targets.

## 5. Vision/video
Keep:
VIDEO FILE != SAMPLED FRAME STREAM
PIXEL CHANGE != OBJECT MOTION
EDGE DENSITY != OBJECT COUNT
CO-TIMED AUDIO/VISUAL != CAUSAL RELATION
FRAME SAMPLE != COMPLETE EVENT HISTORY
COMPRESSION ARTIFACT != WORLD FEATURE necessarily

Low-level useful candidates:
edges
regions
color relations
motion coherence
temporal persistence
occlusion/reappearance
depth cues
audio-visual timing

Object/action words should be learned associations, not hidden classifier truth.

## 6. Semantic video
Semantic labels require explicit provenance:
- user/teacher demonstration
- environment receipt
- repeated cross-view structure
- external classifier hypothesis

Never mark a caption-generator sentence as C4 visual observation.

## 7. Multimodal binding
TEXT != AUDIO != IMAGE != VIDEO != MOTOR PROGRAM != MEANING.
One concept may link these layers, but linkage itself must be learned/evidenced.

SONG-LEVEL TEXT+AUDIO BINDING != TOKEN-LEVEL ALIGNMENT.
IMAGE LABEL != OBJECT PERMANENCE.
MOTOR COMMAND != VERIFIED OUTCOME.

## 8. Exams
Use held-out raw/synthetic signals.
Hide filename/title/label metadata where testing sensory generalization.
Test:
category invariance
recurrence
temporal order
cross-modal correspondence
restraint under ambiguity
self-vs-external provenance

## 9. Development discipline
counterexample -> minimal repair -> re-attack -> regression -> cold reload -> physical checkpoint -> next

RED never canonical.
Do not modify runtime merely to force a sensory lesson through.

## 10. Audiovisual association semantics
From G253 onward, preserve multiple semantic layers:
SENSOR / DIRECT / NARRATIVE / SYMBOLIC / ASSOCIATIVE / AFFECTIVE / PHILOSOPHICAL / EPISTEMIC.

NARRATIVE is one layer and must not be forced onto montage/poetry when association structure is richer.
ASSOCIATION != CAUSATION.
SYMBOL != SINGLE FIXED MEANING.
VISUAL MOTIF != OBJECTIVE AUTHOR INTENT.
MUSIC-LYRIC CONGRUENCE is interpretive unless separately evidenced.
AFFECTIVE READING != measured emotion of author/listener.

An interpretation should retain support links back to source cues.
Several interpretations may coexist.
Rank by support/provenance instead of forcing one reading.

## 11. Screen recording / nested media
SCREEN CAPTURE FILE != DEPICTED MEDIA WORLD.
PLAYER UI != ARTWORK CONTENT.
CAPTURE TIME != DEPICTED EVENT TIME.
PLAYBACK ORDER != STORY CHRONOLOGY necessarily.
Seek/replay/loop can repeat frames without a repeated depicted event.

Preserve nested context boundaries where possible:
device UI -> player/container -> depicted artwork/world.

## 12. Unknown lyrics
Audio with vocals does not produce a verified transcript by itself.
ASR/phonetic guesses remain external hypotheses.
LYRICS UNKNOWN -> do not invent transcript.
Future verified transcript may be linked retrospectively to preserved AV observations.
RETROSPECTIVE LINKING != RETROACTIVE OBSERVATION.


## 13. Controlled synthetic vision nursery
From G265 onward, synthetic image corpora may be generated when the environment provides exact ground truth.

Keep distinct:
RAW_IMAGE
DERIVED_LOW_LEVEL_FEATURE
TEACHER_GROUND_TRUTH
C4_STORED_ASSOCIATION
C4_AUTONOMOUS_RECOGNITION

RAW_IMAGE != DERIVED_FEATURE.
DERIVED_FEATURE != TEACHER_LABEL.
TEACHER_LABEL != AUTONOMOUS VISION.

Reserve held-out raw stimuli whose labels are not entered into C4. Hide filenames/metadata during exams.
Synthetic transfer does not establish real-photo transfer.

## 14. Object permanence and observability
From G266 onward distinguish world state from current observability.

WORLD_STATE != OBSERVABILITY.
OBSERVATION_MISSING != WORLD_OBJECT_MISSING.
PREDICTION != OBSERVATION.

In a controlled simulator an ENV_OBJECT_ID may be an environment receipt for identity through occlusion.
Real video normally lacks such a receipt; re-identification after occlusion must remain a hypothesis supported by temporal/visual evidence.
Object disappearance from frame != destruction.
Reappearance of a similar object != guaranteed identity.
