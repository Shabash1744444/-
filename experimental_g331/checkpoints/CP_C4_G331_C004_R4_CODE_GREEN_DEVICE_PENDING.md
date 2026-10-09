# C4 G331 — C004-R4 CODE GREEN / DEVICE PENDING
Date 2026-10-09.
**Cycle status:** R4 code DONE; C004 as a whole NOT DONE; C003 is last full DONE. Device Android still NOT ATTESTED.

## Frozen RED
Two native host-style TAKE completions in the **same Android session**, with unique action IDs and unique receipts, were recorded with `outcome_root=host_room_session:<session>:<action_id>`. C4 REFLECT incorrectly reported **2 independent_sim_roots**. Per-intervention receipt ID is NOT an independent source root. Original R3 local result recorded two distinct roots, 2 counted. This could multiply evidence from one host and contaminate strategy scores.

## Repair on existing organism
- Native `c4child/runtime.py` host receipt now uses `outcome_root=host_room_session:<session_id>`, independent of action ID.
- Native `c4child/structured_cognition.py` adds `outcome_trial_id=<unique receipt_id>` alongside current `receipt_id`. Multiple trials remain distinct and cold-persisted without spuriously claiming different source origins. `_score_actions` already deduplicates per source root.
- No second database, empty organism, source-trust punishment, WORLD promotion, external memory, or language shortcut. Historic already-persisted per-action roots are not silently rewritten; their lineage remains marked as recorded in the old version, and require a later explicit provenance migration to reassess.
- Different host sessions yield different source roots, although even separate sessions are only a necessary distinction, NOT statistical proof of independent upstream sources.

## Evidence
- C004-R4 three directed local tests PASS for same session (2 receipts, 1 source), different sessions, compact C4M cold reload.
- Existing G329 10,781-fact real .c4m loaded, two local constructed host-style SIM completions share a root, save/cold original facts still 10,781, native host token does not survive reload; original source SHA256 `dfe4b40211b1ce2d3400e95217ecc9210fc1f0a93076ee42a51e55f0be0b090f` unchanged.
- GitHub Actions native constitutional CI [37882337180](https://github.com/Shabash1744444/-/actions/runs/37882337180) SUCCESS: **126 PASS, 2 SKIP**; check SHA256 source `593ab5f86259ea9f88aa6482a94881be298009e9982ee55f6e6147c37a680350` runtime, `2cf8f693416c1c99833248dea47cdb64a1662bfa3f70b607b03d0a3b69645bbe` cognition, pinned 56 native modules, module overlay and source comparison, archive generation and constitution gate. Unproven autonomous_pretrain remained BLOCKED.
- Local ZIP: `C4_G331_C004_R4_NATIVE_RUNTIME.zip` SHA256 `9dd72f1d5bfc57c6c1ad757503b46ec0dbde637fc4ded285e3e59c6d8173eaa3`. Stored Library `/C4_Candidates/G331_NATIVE_COGNITION/C004_R4/`. Source runtime and tests committed GitHub branch, not canonical.
- Current Android APP branch `Shabash1744444/Emu` `experiments/c4-c004-native-host` HEAD `a528129a8ed7b6a675ee49d9f8c0ecaf0cfd6952`; no changes by R4.

## IMPORTANT unresolved
Physical Android native action→world mutation→private host witness→SIM credit→cold reload, replay/stale session checks remain untested on user device. More broad linguistic and cognitive goals (genuine human-like conversation, unseen transfer, self-learning) are not established by this patch or the CI count. No physical Android-C004 completion or C005 start should be asserted. Next: user phone run paired experimental APK and R4 runtime with backup .c4m, export room trace and cognitive trace. If no phone log, leave C004 OPEN / DEVICE PENDING. Preserve constitutional obligations, roots and transaction/cascade safety.
