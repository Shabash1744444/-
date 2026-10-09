# C4 / D1 CAPACITY LAB — P0 REPRESENTATION COLLISION (2026-10-09)

**Scope:** independent read-only experiment on the ACTUAL saved L1/D1 .c4m and D1 57-module runtime; NOT D2 training, NOT generic C4 architectural impossibility.

## Physical input evidence

- L1 `C4_G329_L1_LEARNED_ORGANISM_20261009.c4m`: SHA256 `bba87b3d1b7c48f929236868c2244d05153532b4b173c8d7768783dadc6ef7ce`; cold 10908 facts.
- D1 `C4_G329_D1_DIALOGUE_POLICY_20261009.c4m`: SHA256 `86986428afd7bd6957f57bea30596a5ccbb361647c2bf0bd29cbc6d1ddd1aa01`; cold 11821 facts.
- D1 native runtime SHA256 `0125e17eb4e889b5de8dd4e9b4f657e89ba0e71f2c26324c4612dee975c8a52e`.
- Reproduced 112/125 positive D1 heldout, **15 unique** heldout utterance surfaces (EXTERNALLY provided STORY frames).
- Reproduced D2: 8/8 ordinary `user_message` output/parse pairs identical L1 vs D1; still **RED**.
- NEW: 54/54 combinations of `speaker` (3) × `epistemic_mode` (3) × `time` (3) × `polarity` (2) yielded **exactly identical** D1 `reply_act` AND surface reply for a fixed `а что дальше`, fixed `mode/goal/previous_reply_act/focus/place`. No model mutation.

## Formal scope of proof

The trained D1 reply-act model is `g(frame,intent) = argmax_a Σ_{f∈_context_features(frame,intent)} W(a,f)`.
Current `_context_features` omits `speaker`, `epistemic_mode`, `time`, `polarity`, and concrete focus identity (only presence flag included).

If two situations differ ONLY on omitted dimensions, their feature sets are identical. Therefore **for ANY D1 parameter weights and any number of training examples**, D1 must select the same speech act. If a benchmark demands two different correct acts in a balanced such pair, the accuracy of this D1 hypothesis class is <=50% on those conflicting cases. This is a **representational ceiling of the current D1 organ**, NOT a theorem limiting C4Graph, four constitutional owners, or future learnable operators.

The 54 variants have NOT been independently assigned distinct correct labels; do not falsely call them 54 errors. They are indistinguishability/collision witnesses.

D1 has just six stored reply-act patterns. This restricts its output class to those six actions and teacher templates until another class/generative mechanism is taught.

## Files

Full physical reproducible research pack in user Library:
`/C4_Candidates/G331_NATIVE_COGNITION/C4_CAPACITY_LIMIT_P0_2026_10_09/C4_CAPACITY_P0_PROBE_2026-10-09.zip`.
ZIP SHA256 `50b219ac006e323f2c0c5446c812a4e53793adbd3fc86a1e86a75213a944e81b`.
Contains `c4_d1_capacity_probe.py`, `C4_D1_CAPACITY_PROBE_RESULTS.json`, `README_C4_ARCHITECTURE_LIMIT_LAB_2026-10-09.md`. Matching README independently in Library folder.

## Next falsifiable experiment

P1: freeze natural `user_message` dialogues & independent semantic labels; train a NEW copied C4M with learnable text→scene/referent/perspective→speech-act through the actual C4 owner cycle, not external `frame`. Compare same new code (untrained vs trained), shuffled teacher labels, withheld WHOLE operator families, cold reload, additional world and adversarial inputs. Preserve all four owner laws, single native graph, source lineage, original C4M and C004 Android physical gate separately. Do not inflate scores using 80 handlers, Python literal question mappings, or teacher as oracle at eval time.

**P0:** D1 representational limit established. General C4 ceiling UNKNOWN. No new D2 C4M was trained or written in this pass.
