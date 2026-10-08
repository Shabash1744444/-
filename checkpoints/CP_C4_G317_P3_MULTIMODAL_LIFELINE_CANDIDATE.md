# C4 G317-P3 — MULTIMODAL LIFE-LINE CANDIDATE

Status: CANDIDATE / NOT CANONICAL
Date: 2026-10-08
Parent: G316-P2 continuous dialogue candidate.

## Purpose
Add a small amount of multimodal grounding to the SAME continuous life-line and semantic context, without turning similarity into identity or sensory observations into graph truth.

## Runtime change
- `observe_sensory()` now records `SENSORY_OBSERVATION` in `life_events`;
- unresolved input stays `UNRESOLVED` / `PERCEPTUAL_CANDIDATE`;
- a previously named sensory concept may make its existing semantic entity contextually AVAIL;
- sensory context never supplies COMMIT authority;
- explicit sensory naming is journaled as `SENSORY_NAMING`;
- raw vectors remain inside the sensory organ, not the semantic graph.

## Modality separation
New semantic channels are separate from G307 phoneme/grapheme channels:
- `VISION_OBJECT`;
- `AUDIO_LABEL`;
- `SYMBOL_LABEL`.

G307 sound-symbol links remain exactly 6.
PHONEME != AUDIO_LABEL.
GRAPHEME != SYMBOL_LABEL.
VECTOR SIMILARITY != IDENTITY.
SENSORY CONTEXT != WORLD TRUTH.

## Development RED
The first curriculum used 8 synchronized bundles per concept.
Frozen development exam: 9/12.
`вопрос` and `ответ` deliberately confusable stimuli collapsed to one sensory concept.
That run was not saved or promoted.

After diagnosis, training density was set to 16 bundles/concept. Because the development exam had already been inspected, it was retired from final evaluation.

## Final unseen exam
A new final heldout was frozen BEFORE the final training run:
- 4 existing semantic entities: `мяч`, `книга`, `вопрос`, `ответ`;
- 3 modalities each;
- 2 unseen noisy variants each;
- total 24 heldout observations.

Baseline named resolutions: 0/24.
After training: 24/24.
Cold reload: 24/24.
Four distinct sensory concepts remained distinct, including `вопрос` vs `ответ`.

## Graph / prior-layer isolation
Semantic graph before: 10,721 entities / 10,769 facts / order 22,288.
Semantic graph after: 10,721 entities / 10,769 facts / order 22,288.
No world fact was added by multimodal training.
G306 spatial, G307 sound-symbol, G308 contact/effort and G309 support/fall organs were byte-structurally retained through the training/cold cycle.
Grounder concepts: 12 -> 16.

## Continuous-life re-attack
A recognized multimodal `мяч` observation:
- emitted `SENSORY_OBSERVATION / GROUNDED`;
- made the existing `мяч` semantic entity available to context;
- allowed pronoun reference `нем -> мяч`;
- caused zero semantic-graph mutation.

## Constitutional re-attack
On exact G317 state, `Кошка это слон` is stored only as source assertion; `KNOWLEDGE` and `WORLD` remain UNKNOWN.
Transport split still holds: `receive_user_event()` returns PENDING with no reply/mutation; cognition may occur later.

## Validation
Focused P0-P3 suite: 35/35 PASS.
Full regression: 462/481 PASS.
19 failures are unchanged FileNotFoundError historical fixtures/models.
New semantic/runtime assertion failures: 0.

## Artifacts
Model: `child_g317_p3_multimodal_lifeline_candidate.c4m`
Bytes: 1998549
SHA256: `0c62250f7845df1a52ea080434ee6eba84771e8d6715611a0dad840ca6d83810`

## Next
P4: dialogue deliberation — multiple EVAL interpretations/action candidates, DRIVE arbitration, and optional/delayed public output without introducing a request/response law.
