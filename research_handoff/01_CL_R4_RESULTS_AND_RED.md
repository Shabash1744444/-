# CL-R4 / CL-R4.1 — measured evidence, RED, no invented victories
Date: 2026-10-10. Source: Claude CL-R4_REPORT.md inside archived research package. Source is **not** independently confirmed by the following GitHub commit; refer to raw artifacts.

## Experiment architecture
Experimental module clr4/c4life in separate Claude research tree; original G331 / D8 unchanged. Machine loop: world clock tick -> MEDIATE input + proven channel -> COMMIT classify -> accepted state change -> DRIVE choose informational experiment, extend representation, abstract learned operator, review, resolve open goal, ask teacher, rest/wake -> append to hash-chain journal -> snapshots and tail verification. Owner-specific capabilities. Distinguishes step/world_t/narrated_t/due_t/wall; wall clock excluded from hash. Replay should not invent new observations. Immediate abort on divergent replay.

S structural learner: finite typed operator induction based on independent prospective/prequential evidence, sleeping experts, target-specific Bayesian model, expected information gain / BALD, operation library. Operator becomes reusable only with credits in >=2 different goals. W learned shared neural modules, routing, ensemble, sleep/replay and parameter updates with lineage. H hybrid **not implemented**.

## Reported original frozen V1 results, seeds 101–103
- LIFE A–G: S 0 incorrect responses on 3/3 seeds for defined synthetic exam.
- Real kill -9 3/3: journal, derived state and user messages bitwise match uninterrupted run (same frozen code).
- World-to-world operation transfer E: S with learned library 6/6 correct on new entity-feature vectors, S_NOLIB 0/6 (UNKNOWN) across 3 seeds. This tests representation transfer between two authored toy domains, not general language or different physics.
- OP renamed-world: original V1 had 34–56% observation savings on tested tasks. Not robust in next freeze.
- Mechanism acquisition speed original S vs W: median 16.8x fewer *transitions to certification*, not 16.8x faster CPU or total training time. Wrong confident assertions in LIFE + OP probes: S 217/160682=0.135%, W 463/96081=0.482–0.485% depending exact aggregation text. These are NOT 0% across all experiments.
- Lesson withdrawal reported 34.7x cheaper CPU for S than W in V1. W often does full-life rebuild on retraction.
- Native organs RuleInductionOrgan and experiment selector emulated via S adapters: 28/28 runnable tests; seven missing historical models. CL runtime regression 383/395 reported, not all green.
- 4200-step autonomy (seed104) with journal and kill; separate long-term episode; 'real time' running at ~2 ticks/second, not proof of spontaneous open-world general intelligence.
- Auditor verified 51 journals, 1 defect W (certification lacking evidence list); not flawless.

## CL-R4.1 new freeze seeds 105–107, 40 jobs all exit 0
Confirmed by Claude:
- LIFE S 0 wrong for 3 new seeds; proper rest/recovery and kill -9 bitwise same.
- E world-to-world transfer 6/6 with library vs 0/6 without, now 6 total seeds of 6 for small invented worlds.
- B1 reactive always-busy baseline no longer emits false unsolicited 'corrections' about past facts after world changes. S REVIEW now actually happens and avoids this observed failure.
- Noise false certification reduced but NOT eliminated: 27 wrong on one of 3 seeds instead of 44 wrong over all three in preceding experiment; 'two identical repeats' does not exclude 50/50 noise (chance 1/4).
- P8 source-list invariant STILL FALSIFIED by W seed107: after source retraction, full-life replay rebuilt numeric model but failed to rebuild list of evidence witnesses attached to certified mechanism. Similar latent S path possible. High-priority epistemic flaw.
- P2 speed-of-transfer threshold '>=30%' on renamed clone passed on just 1 of 3 seeds: observed 43%, 14%, 25%. Early certificate of shorter wrong candidate interferes.
- Some other predictions pass, but CPU and RAM have trade-offs. S uses more memory than W in the original study. For corrected CPU numbers, consult original R4.1 tables; do not re-use V1 factors uncritically.
- Old V1 4200-step living history cannot be resumed in newer R4.1 binary. It *fails closed*, keeping old history intact; same V1 code continues it bitwise. Cross-code upgrade != learning inside a stable kernel. Migration must preserve original journal and semantic lineage and mark CODE_UPGRADE; do NOT blindly re-execute old decisions under new rules.
- 16/16 clean-unzip verification reported by Claude; final main archive was rebuilt with SHA prefix 75d172b8, but this new main ZIP has NOT been received in the current chat at handoff time. An earlier local main ZIP exists with SHA b63927fc174a0770d3248f0f3e995d344f9891232db1f3cf8476a751cfd44011; DO NOT present it as final 75d release.

## Closed and open assumptions
CLOSED within narrow experiments:
- Some durable cognition occurs absent incoming messages; DRIVE can re-query old uncompleted tasks, plan interventions and rest/wake.
- Learned structured operations are actually reused to solve separate, synthetically authored entity-world tasks in the reported cross-world exam.
- Same-code crash continuity demonstrated under specified tests.
NOT PROVEN:
- Free Russian dialog, multimodal sensor understanding, AGI, useful real physical-world generalization.
- Invention of brand new **types** of operations (e.g. counting or variable arity aggregation). Only composition within typed available operator family.
- Universal explanation/general-purpose abstraction not tailored to small class of crafted toy causal worlds.
- Perfect witness safety after replay; W/S retraction P8 RED.
- Robust renamed-world acceleration on 3/3 confirmation seeds.
- Hot upgrade / cross-code lifetime migration.
- Independent human-generated external exam; toy worlds written by Claude.

## Required next gates CL-R5
(1) Journal-driven migration between code versions without re-deciding historical admissions: read old immutable events, verify hashes, rebuild new derived projection, store CODE_UPGRADE and dual-audit; preserve previous branch for comparison.
(2) Repair W witness reconstruction on any full replay and test S hidden sibling; no certified knowledge lacking valid witnesses.
(3) Replace 'two confirming repeats' by predeclared statistical evidence/contrast protocol resistant to noisy worlds and adversarial seeds; falsification first.
(4) Challenge premature certificates and poisoned learned operators; evaluate at least 10+ heldout seeds and independent worlds of distinctly different law/observability, delayed reward, interventions; track both precision and coverage, cost.
(5) External LLM teacher protocol: independently causal simulation; LLM lessons are claims, visual descriptions sourced annotations; cost-aware questioning. No single model writes world and judges itself.
(6) Keep ongoing independent assessment of native G331 admission gate risks: spoofed TEACHER authority (R9); registered-relationship scope changes on cold process (R10).
(7) Pre-register capability metrics for genuinely acquired new OPERATOR TYPE beyond composition and for world transfer. Human/independent blind author.
(8) Build free dialogue training separately; do not conflate native parsing score with competence.

## Honest accounting
16.8x refers to transition count in *one* frozen V1 setting, not 16.8x universally and not CPU speed. 6/6 operator transfer is narrow but real within source claims. 0 wrong LIFE does not imply 0 incorrect overall. '40 jobs rc=0' means exit code success, not 40/40 cognitive successes. H not built. Missing artifacts are NOT passes. Repro hashes of frozen code are not safety proofs against a shared bug or data leakage.
