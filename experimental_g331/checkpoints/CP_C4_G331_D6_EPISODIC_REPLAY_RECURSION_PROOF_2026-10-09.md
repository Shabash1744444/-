# CP C4 G331 — D6 EpISODIC REPLAY AND ITERATION MICRO-PROOF (2026-10-09)

**STATUS: NARROW RETROSPECTIVE REINTERPRETATION POSITIVE, NO-NEW-INFO LOOP NEGATIVE, GENERAL LANGUAGE / SELF-COGNITION NOT PROVEN. NO canonical architectural changes.**

## Sources physically used (NOT fabricated replay simulations)
- Actual native D3 `C4_D3_64_NESTED_LEARNED_CANDIDATE_NONCANONICAL.c4m`, sha256 `0dff2f5caceee3b536a55cfe15057ad73b2438cacffc470cb26a6d5c419e7cca`, 16522 cold fact records.
- Actual native D5 `C4_D5_LEARNED_EDGE_RESEARCH_ONLY.c4m`, sha256 `b7b2dd0f826bbc217f2a5499e53ba554a61c415817fe5d1f2c5313f2caa81036`, 16731 cold fact records.
- Existing 32 synthetic D3 heldout reversed-syntax old raw episodes, indexed as real C4 `episodic_memory.index_event`, no WORLD claims; D5 manual 10 old examples and 6 unrelated old inputs.
- D6 `PRE_REGISTERED_PROTOCOL.md` checksum `eb08570a508200a7eb786f8f019a7423611acf1acf3b96de526cad3d6829d460`. All datasets are HISTORICAL, not independently new/blind. Training of D3/D5 happened before this study; D6 does not train a new C4 model.

## Native C4 outcomes
- Old D3 fixed AST parse on 32 old raw reversed messages: 0/32 exact.
- D5 existing trained token+graph-edge operator **re-reading the exact same 32 original raw messages**: 21/32 exact; 21 previously unparsed source episodes are now interpretable. This is retrospective benefit from IMPROVED SKILL and reaccess to original RAW bytes, not proof that repeating thoughts creates knowledge.
- Unchanged D5 deterministic inference at iteration budgets 1,2,3,5,10,30,100: identical **21/32 at every budget**. No improvement from repetition alone.
- Original native episodic_memory `retrieve` on topic-only questions (shared subjects across events), top 2 results hit correct historical event only 12/32; full source-text-as-query ORACLE upper-bound 32/32, not user-realistic. Evidence retrieval/context selection itself needs to improve.
- Old human-authored sample 4/10 exact and 1/6 unrelated samples gives spurious CANDIDATE; C4 still not general natural language.
- Native D3 and D5 C4M SHA preserved, graph fact-count and audit lengths before==after, all past raw source anchors retained, historical interpretations versioned only in separate research file, no new WORLD claim, dependent source interpretation not fresh evidence.

## Separate toy mathematical graph-propagation experiment — NOT original C4 learner
- 60 independent synthetic training DAGs one-hop relation labels; train one scalar `w` by least-squares: w=1.0. Given an already observed adjacency A, iterate h_(k+1)=clip(max(h_k,w A^T h_k),0,1), start one-hot.
- Frozen 200 different random DAGs, gold question reachable in <=4 links: passes 0/1/2/3/4/5/10/30/100 produce exact graphs 17/31/66/124/200/194/194/194/194 out of 200.
- Four passes suffice for fixed four-hop question; extra passes overshoot the bounded question and reduce accuracy. The graph topology and message-passing functional form are supplied by programmer (generic inductive bias); this is NOT proof C4 learned natural syntax or itself acquired reasoning algorithms.

## Math/meaning for next investigation
Immutable source episode E_i=(raw,source_root,time,scope). Multiple interpretation versions H_i^v are DERIVED_FROM E_i, not independent roots; proposed inner recursion Z_(k+1)=F_theta(Z_k,E_i,Retrieve(G_t,Z_k),G_t,delta_t). DRIVE uses expected information gain versus compute/corruption cost to decide replay selection and stop. EVAL interpretation != factual admission; COMMIT source rules unchanged; MEDIATE for external receipts. A non-injective lossy state H=f(E) cannot be inverted solely by repeatedly applying H-level deterministic postprocessing; retaining/retrieving original E is a necessary precondition to reconsider discarded distinctions.

## Evidence, tests, and recovery
- `python -m pytest test_d6.py -q` **4 passed**, no unexpected XFAIL. Full historical corpus suite and Android physical C004 not rerun, remain pending.
- Self-contained 77-entry ZIP `C4_D6_EPISODIC_REPLAY_RECURSIVE_MICRO_PROOF_2026-10-09.zip` sha256 `6d3d69d4c86016268c33aace3d8016eeb8f312c5c6ced602792d367bdf60b2e1`, size 5509117 bytes, all entries verified. Contains exact D3 and D5 `.c4m`, native ~60-module runtime, frozen prior exam cases, scripts, native episodic tests, versioned result ledger, scalar learned toy and hash manifest.
- Physically saved in Library `/C4_Candidates/G331_NATIVE_COGNITION/D6_EPISODIC_REPLAY_RECURSION_2026_10_09/` along with readable README and JSON reports.
- NO claim C4 can replace an LLM; experimental archive only. Next truly decisive gate: autonomous DRIVE selection of original past events; trained retrieval and joint semantic graph learner, independent human-authored new heldouts frozen BEFORE training, owner traces, cold reload and normal user_message response; compare matched cost 1 vs k passes and prior source errors. No Qwen mass distillation yet.

**User emphasized past messages and old graphs must be revisitable in continuous recursive self-cognition even during idle, and repeated insight may arise over multiple graph passes. The experiment tests narrow prerequisites and limitations rather than overclaiming general cognition.**