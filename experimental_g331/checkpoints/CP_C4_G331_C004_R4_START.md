# C004-R4 START — protect source-root independence
Date: 2026-10-09.
BASE_HEAD: 7a67b894b5e4db17d4a3c65420f0f24c5137f0ac.
Status START (not DONE); full C004 still Android DEVICE PENDING, C003 last full DONE.

Frozen RED from native C004-R3 runtime:
Single C4LivingRuntime, same host session c4-same-host; two independently labeled TAKE proposals for BALL and BLOCK with two successful private host-style callbacks. Both callbacks have the SAME original Android host session; before fix `outcome_root` values include per-action ID, so `REFLECT` reports 2 `independent_sim_roots`. This is a false *source independence* claim even when the interventions have distinct trial receipts. SOURCE ROOT != CAUSAL TRIAL ID.
Target:
- `outcome_root` identifies original host/session source (correlated), independent of action ID.
- `receipt_id` (unique per action) and `outcome_trial_id` preserve distinct interventions, temporal/replay records.
- G215 trust: source cannot be rewarded or penalized merely for agreeing/disagreeing with current C4 beliefs.
- Read-only historical C4M compatibility: preserve previously stored roots; never migrate by silently asserting new independence.
- Run original held-out pair, compare two sessions vs same session, complete directed+constitutional regressions, C4M cold and CI source sha, checkpoint.
Do not create second organism, ignore old graph, bypass EVAL/COMMIT/DRIVE/MEDIATE, or claim device LIVE.
