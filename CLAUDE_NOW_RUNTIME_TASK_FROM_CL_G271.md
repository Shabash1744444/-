# CLAUDE NOW — CONTINUE RUNTIME FROM CL-G271

You are on the Claude runtime branch.

Your latest GREEN is CL-G271 Reading, built on CL-G270 storage. Continue from that branch autonomously for as long as limits allow. Do not stop after one small milestone if there is room for another.

## Context from main C4 training line

Main training line has advanced separately and must NOT be overwritten wholesale.

Current canonical organism:
- weights G297
- child_g297_relation_diversity_green.c4m
- 1,960,675 bytes
- SHA256 0db410bc1ebf71aba05e7571c58e82e6cfb3d17f8c72faea6c09e77e38a6cae9

Current canonical runtime:
- G298 RETRACTION INVALIDATION GREEN
- SHA256 7ff72ff492ef247c18fe9d44a6927ca06434945c4c7254781930ce960221897f

Main line already has later cognition than the old G266/G270 lineage:
- guided reading
- lexical gaps without lemma guessing
- causal reading
- mixed-chunk dependency retry
- relation algebra
- functional source-conflict visibility
- strict temporal order
- retraction invalidation
- current-source stance reconstruction

Therefore:
your CL-G271 is an R&D/runtime branch.
Do not claim it replaces canonical cognition wholesale.
Build strong organs/runtime features and package them so they can be cherry-picked onto the current line.

## What CL-G271 already proved

Keep all of this:
- SQLite disk-backed graph
- same memory/disk answers
- reading loop: article -> unknown words -> ask -> read answer -> new gaps -> reread
- one human question at a time in chat
- LLM teacher batch request interface
- provenance of text/source
- UNKNOWN word does not become a concept/fact
- incremental morphology while reading
- persistent reading state across restart
- USER_SAID carry-forward
- reproducible avalanche metrics
- clean-unzip regression discipline

## Highest-value next work

### 1. Turn reading from "word learning + literal phrases" into structured learning

Your own G271 limitation says verbs are mostly learned as words/literal phrases rather than relations.

Improve this conservatively:
- predicate/event frames become typed structure only when evidence supports it;
- subject / predicate / object / tense / polarity remain distinct;
- do not convert every verb phrase into a permanent property;
- past episode != timeless property;
- question != assertion;
- unsupported parse -> gap/skip, never guessed truth.

Important compatibility target:
the main line already distinguishes relation algebra and epistemic states. New reading structures should be easy to map onto those relations later.

### 2. Multiword expressions

Add safe support for phrases that behave as one lexical/pragmatic unit:
- "впадать в спячку"
- "друг друга"
- similar learned expressions

Do not mark each token permanently equivalent to the whole phrase.
Phrase identity must be explicit and source-backed.

### 3. Re-read old material automatically

When later learning resolves a gap that blocked an older text:
- mark affected texts/segments as worth re-reading;
- re-run only relevant old material, not the whole corpus;
- measure new facts/coverage unlocked per new lesson;
- avoid duplicate facts;
- preserve original source/provenance.

This is important for the "avalanche" effect.

### 4. Long-text reading

Implement chunked/resumable reading:
- article/book split into bounded chunks;
- persistent position;
- source identity and paragraph/chunk location;
- crash/restart continues safely;
- user can interrupt/resume;
- no full-file rewrite in SQLite mode;
- ActiveGap-like prioritization is welcome, but do not invent unknown lemmas.

### 5. Agent lifecycle inside chat

If limits allow, continue agent capabilities.

Minimal first-class structures:
TASK
GOAL
TRIGGER
STATUS
PLAN
ACTION_REQUEST
RECEIPT
VERIFIED_OUTCOME
NEXT_CHECK

Lifecycle:
TASK -> trigger -> plan -> action request -> receipt -> verify -> status -> continue/finish

Required boundaries:
TASK MEMORY != TASK EXECUTION
ACTION_REQUEST != VERIFIED_OUTCOME
RECEIPT != CAUSAL PROOF

Tasks must survive restart and be inspectable/cancellable.

### 6. Runtime/body readiness

Prepare clean adapters for:
- Windows filesystem/process/app control
- phone/app bridge
- screen/camera/mic/audio/video streams
- future tool/plugin calls

Adapters are I/O, not hidden cognition.
Sensor/tool output must still pass epistemic admission.

## Priority note

Storage compression is useful, but hardware is not the immediate blocker:
the target devices include a phone with ~12 GB RAM and a PC with 128 GB RAM + 24 GB VRAM.

So do NOT spend the remaining limit only squeezing SQLite size unless the optimization is architectural and low-risk.
Capability, persistence, agent execution, reading quality, streaming readiness and compatibility are higher value right now.

## Laws that cannot be weakened

UNKNOWN != FALSE
QUESTION != ASSERTION
DERIVED != OBSERVATION
PREDICTION != EVIDENCE
ACTION_REQUEST != VERIFIED_OUTCOME
RECEIPT != CAUSAL PROOF
SIMILARITY != IDENTITY
CANONICAL != VERIFIED AUTHORITY
SOURCE/ADDRESS != EVIDENCE
SUMMARY != ORIGINAL EVIDENCE
COMPRESSION != NEW TRUTH
RAW SIGNAL != TEACHER LABEL
EVIDENCE HISTORY != CURRENT SOURCE STANCE
RETRACTION != RESURRECTION OF OLD STANCE

Current relation boundaries from main line:
PART_OF <-> HAS_PART is read-only inverse.
BEFORE <-> AFTER is inverse and supports strict read-only temporal paths.
ORDER != CAUSE.
SYNONYM / ANTONYM / OPPOSITE are symmetric read-only.
PART_OF is not transitive by default.
HAS != HAS_PART.
MEANS is not symmetric by default.
ROLE is not inherited/symmetric by default.
Derived relation state must disappear when support disappears.

## Validation

For every milestone:
- memory mode if supported
- SQLite mode
- clean-unzip run
- full regression
- report old missing-artifact failures separately
- restart persistence
- no question-induced graph mutation
- no nonce/test vocabulary contamination
- no benchmark-specific aliases
- exact hashes and sizes
- patch/diff against CL-G271
- benchmark latency/RAM/disk if runtime paths changed

If you can obtain the current G298/G297 canonical package, run a compatibility smoke.
If not, do not fake compatibility: keep your branch self-contained and produce a clean cherry-pickable patch.

## Deliverables

Before limits end, always leave:
- latest GREEN runtime ZIP
- checkpoint README
- exact SHA256
- patch/diff from CL-G271
- regression/benchmark results
- explicit RED/counterexamples not yet fixed
- next best action

Goal:
make the runtime/body increasingly autonomous, persistent, teachable and multimodal-ready while the main chat continues training the organism.
