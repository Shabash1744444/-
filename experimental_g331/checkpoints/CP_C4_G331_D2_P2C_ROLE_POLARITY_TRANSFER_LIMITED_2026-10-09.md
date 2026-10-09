# C4 G331 — D2-P2A/B/C ROLE / POLARITY CAPACITY EXPERIMENT
**Date 2026-10-09; candidate, NOT free dialogue; D2 still RED. C4 != Singularity OS.**

## Parent / exact physical artifacts
Parent: trained D2-P1 `C4_G329_D2_P1_GROUNDED_STORY_CANDIDATE.c4m`, SHA256 `f8ed0e709b565ae0b437b8b273cd70c75762ed09ebb5cbe31bf099e6a412309c`, cold graph 12767 facts. **Parent untouched**.
New candidate: `C4_D2_P2C_RELBINDER_NEGATION_CANDIDATE.c4m` 2,783,142 bytes, SHA256 `36e9fb9c54691d1ba7a0625e88d65d85017d60d4e4a021d320ecbd8a064ee385`, cold 15863 facts (+3096 genuine graph LANGUAGE_CONVENTION learned weight entries, one dependent EXTERNAL_CORPUS/TEACHER root).
Runtime: `C4_D2_P2C_NATIVE_RUNTIME_59_MODULES.zip`, 59 original-plus-new Python modules, SHA256 `538b5cda146c97efc2853ee4993cee6e1266bee8aa50fb03519dc909283373de`.
Full self-contained proof with weights, runtime, training source, frozen data, negative P2A and P2B reports, test and manifest: `C4_D2_P2C_RELATIONAL_COMPOSITION_PROOF_2026-10-09.zip`, SHA256 `0520a10ae17dcf787c2d42b06f9570a16ff2b233b13685781fc8ebfe20f5cd5e`.
All three binaries physically saved in Library `/C4_Candidates/G331_NATIVE_COGNITION/D2_P2C_RELATIONAL_POLARITY_2026_10_09/`. Executable source also committed in `experimental_g331/training/d2_p2c/`; ZIP is for binary distribution.

## Learned operation and lawful boundaries
Universal multiclass text intent + first-order Viterbi role sequence scorer with learned graph-resident parameters. Inputs from ordinary native `C4LivingRuntime.user_message`, no externally supplied semantic frames, no teacher inference at test time. Learns roles `HOLDER/SUBJECT/ATTRIBUTE/POLARITY`; outputs typed `BELIEF` vs `NARRATOR`, POSITIVE/NEGATED.
Current runtime records `EVAL_D2_RELATION`, `COMMIT_NOOP`, `DRIVE_D2_RELATIONAL_DEFER`: **NO generated reply** when semantic candidate has no learned speech renderer; no WORLD mutation. No claim of conversational fluency or autonomously invented operations.
In a first test an owner trace `kind` was accidentally overwritten by `extra.kind`; code was repaired to `relation_kind` and directed tests re-run 9/9 PASS. No silent false GREEN.

## Frozen results and failure chronology
- P2A: first shallow role attempt 0/120 new referents and 0/100 new constructions. Preserved as RED.
- P2B: broader supervised role-binding: 96/120 trained constructions with new entities & attributes; 106/120 novel entities with trained attribute; 32/100 entirely unseen construction families. Polarity not learned; **4/4** dangerous negative examples falsely treated as positive BELIEF/NARRATOR candidates (never WORLD-committed).
- P2C: 1880 correlated synthetic lessons (1100 positive, 480 negated, 300 unrelated), 9 epochs; 106/120, 119/120, **11/100 unseen constructions (regression)**, 63/80 unseen negated examples. Previously-dangerous four negation examples now correctly typed `NEGATED` while two nested/contrasting belief inputs conservatively ABSTAIN. 22/26 exploratory unsupported inputs abstain; remaining four are properly typed NEGATED, but this is not a formal adversarial safety proof.
- P2C same new code and parent without P2C learned weights: 0 on all positive heldout sets. Shuffled class-teacher labels (with correct slot tags retained) on P2C: 0/120, 0/120, 5/100, 1/80. Do not misreport this as entire supervision shuffle.
- P2C cold reload retains all scores; all parent fact objects unchanged, C4 native persistent runtime state and organs unchanged. Legacy D1 synthetic test still **112/125**; previous D2-P1 4 directed + new P2C 5 directed = **9/9 PASS** local. Full 139-case historical suite NOT rerun here; physical Android device not tested.
- P2B and P2C were **separately trained from the same D2-P1 parent**; decline 32→11 is an interference/curriculum trade-off, NOT evidence of sequential catastrophic forgetting. No independently authored human dialogue audit.

## Architectural interpretation
D1 old capacity limit partly repaired by a generic relational-role binder and learned negation. `BELIEF(actor, proposition)` differs from `NARRATOR(story, proposition)`; polarity is a type, no self-asserted world evidence. However completely new Russian syntactic families stay weak and more training objectives impair previous generalization. Multiple nested perspectives, pronoun coreference, dialogue initiative, general relational reply realization, causal planning, audio and arbitrary user language are UNPROVEN. Hence **not yet established C4 can replace an LLM**.

## Next experiment and future Omni teacher condition
Freeze independent dialogue benchmarks and introduce a reusable graph/relational composition learner with scope, higher-order variables, and loss balancing/rehearsal. Before declaring replacement, require independently scored, held-out natural multi-turn conversation (syntax families and roles disjoint), spontaneous questions, correction and old/new retention, truthful UNKNOWN, cold restart, and compare quality/latency/memory against a small transformer with no hidden teacher at runtime.
Only if evidenced, Qwen-Omni may be teacher generating text/audio/video synthetic *episodes + semantic targets*, **not** responder behind C4, not independent evidence, and not direct weight-copy distillation; validate with external outcomes and source-dependency roots.
C004 phone sandbox action/receipt still DEVICE_PENDING; original C4 Graph canonical and four-law constitution unchanged.
