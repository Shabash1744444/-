# C4 DEVELOPMENTAL TRAINING METHODOLOGY

Normative from 2026-10-07 onward.

## Goal
C4 is not trained by maximizing corpus size. The target is a compact persistent learner that acquires concepts, transfers them to unseen surfaces, preserves provenance/uncertainty, keeps SELF/OTHER/SOURCE/WORLD distinct, initiates useful questions and continues learning without self-contamination.

NO BYTE PADDING.
MORE FACTS != MORE INTELLIGENCE.
TRAINING VOLUME != TRANSFER.

## Runtime vs weights
Runtime carries reusable abilities/physics:
- graph/admission/retraction/provenance;
- causal/epistemic invariants;
- Russian morphology/syntax/reference;
- discourse state, ellipsis and speech acts;
- semantic retrieval and answer planning;
- curiosity/initiative arbitration;
- checkpoint/persistence/autosave;
- sensor/actuator adapters and receipts;
- abstraction/analogy operators;
- consolidation/compression/forgetting;
- safe learning protocol.

Weights carry acquired experience/content:
- vocabulary and actual usage;
- facts and source-linked claims;
- literature/science/history/math;
- SELF history;
- multimodal associations;
- conversation-derived knowledge;
- future game-world lore and personal biography.

RUNTIME BUG != WEIGHT DEFICIT.
WEIGHT GAP != RUNTIME BUG.
Do not train around a runtime bottleneck.
Do not hardcode corpus facts into runtime.

## Development loop
counterexample -> classify -> minimal repair -> re-attack -> full regression -> cold reload -> physical checkpoint -> next

Failure classes:
R representation missing
E representation exists but consumer edge/path is wrong
M organ/capability limitation
I implementation bug
T training/coverage gap

RED never canonical.

## Skill acquisition criterion
A taught sentence is not mastery.

Preferred:
TRAINED EXAMPLE -> STRUCTURE ACQUIRED -> NOVEL SURFACE -> CORRECT TRANSFER -> NEAR-MISS RESTRAINT -> COLD RELOAD -> RETEST.

Language construction: must transfer to unseen vocabulary/context.
Concept: definition repetition is insufficient; require application + counterexample + boundary.
Sensory: teacher-label retrieval is insufficient; require held-out signal generalization without metadata leakage.

## Live teaching
Current C4 can learn in dialogue but language parsing is immature. Teach atomically.

Good:
"Слово — часть языка."

Bad:
a long paragraph containing many definitions, rules, pronouns and examples.

Cycle:
teacher statement -> C4 interpretation -> one natural gap/question -> teacher answer -> re-evaluation -> one transfer example -> store -> later recall/retest.

If one lesson creates many malformed gaps, stop adding content and reduce to atomic relations.

## Teaching channels
Keep distinct:
LEXICAL
MORPHOLOGICAL
SYNTACTIC
DISCOURSE
WORLD
SELF
SOCIAL
PHILOSOPHICAL
SENSORY

Do not route everything through one generic REMEMBER path.

## Russian-first progression
RU-0 morphology: lemma/forms, gender/number/case, person/tense/aspect, derivation, agreement.
RU-1 simple propositions: entity/property/action/role, negation, quantity, location, time.
RU-2 reference/dialogue: я/ты/он/она/это/тот, previous-turn reference, ellipsis, adjacency pairs, speech acts.
RU-3 composition: subordination, conditionals, cause/consequence, reported speech, modality, argument structure.
RU-4 pragmatic/figurative: metaphor, idiom, irony, sarcasm, implicature, rhetorical questions, register.
RU-5 long discourse: narrator changes, multi-paragraph argument, topic return, nested quotations, unreliable narrator.

Russian remains primary. Foreign-language form may not contaminate Russian syntax/lexicon. Cross-language transfer goes through semantic abstractions.

## Books
BOOK != TRUTH.
AUTHOR != NARRATOR.
CHARACTER != AUTHOR.
FICTIONAL WORLD FACT != EXTERNAL WORLD FACT.

Every book chunk should yield:
language structures + concepts + provenance + ambiguity + counterexamples + transfer exams.
Do not merely dump raw text.

## Dense knowledge cells
Useful concepts may have typed projections:
LEXICAL / MORPHOLOGICAL / SYNTACTIC / SEMANTIC / PRAGMATIC / TEMPORAL / CAUSAL / SOCIAL / AFFECTIVE / PHILOSOPHICAL / EPISTEMIC / SOURCE / SENSORY / SELF-WORLD.

More layers help only when typed.

## Initiative
UNKNOWN/GAP -> estimate usefulness -> select ONE public human-readable question -> ASK -> WAIT -> update gap -> next.

Many internal gaps may coexist.
Normally only one becomes an external question at a time.
OPAQUE INTERNAL ID != HUMAN QUESTION.
ASK WAIT STATE != GAP RESOLUTION.

## Major milestone
The key milestone is not a byte count. It is:
C4 can learn from a person without a developer translating every lesson.

Target:
unknown word/concept -> useful question -> human explanation -> C4 paraphrase -> new example -> correction/confirmation -> store -> later transfer after restart.

## Scale milestones
Observe at ~2 / 5 / 10 / 30 / 100 MB.
At each record:
exact bytes/SHA, facts/entities/evidence, runtime version, transfer, Russian language tests, dialogue continuity, retraction/contamination, latency, persistence, held-out sensory tests.

If size grows without capability growth, stop and diagnose.

## Runtime development
Deep runtime audit (Claude-style) is encouraged, but changes must obey:
- expose/reuse existing kernel knowledge;
- improve language/discourse/search/verbalization;
- do not weaken epistemic laws;
- do not hardcode corpus facts;
- questions must not create entities/facts;
- lexical retrieval must not become truth;
- every change gets regression + real-device re-attack.

## Game/NPC benchmark
A resident needs world physics, local history, personal memory, relationships, goals, source-specific knowledge, uncertainty, learning and continuity.

Future benchmark:
one C4 resident lives 100 simulated game-days.
Measure persistent identity/history, rumor-vs-observation, adaptation and non-reset learning.

Commercial breakthrough remains a hypothesis until long-horizon tests exist.
