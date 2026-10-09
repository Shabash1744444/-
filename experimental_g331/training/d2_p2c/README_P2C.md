# C4 G331 / D2-P2C — learned relational roles + negation, limited proof

**2026-10-09. Research candidate, not human dialogue. C4 ≠ Singularity OS.**

## Which physical organism?
- Source: exact D2-P1 trained graph `C4_G329_D2_P1_GROUNDED_STORY_CANDIDATE.c4m`, SHA256 `f8ed0e709b565ae0b437b8b273cd70c75762ed09ebb5cbe31bf099e6a412309c`, 12,767 cold facts. It is unchanged.
- Output: `C4_D2_P2C_RELBINDER_NEGATION_CANDIDATE.c4m`, 15,863 facts, 3,096 new LANGUAGE_CONVENTION parameter records (source one dependent EXTERNAL_CORPUS/TEACHER root), 2,783,142 bytes.
- Same single native `c4child/C4Graph/C4LivingRuntime`, previous 58 modules plus `d2_relational.py` = 59 Python modules. Four owners remain the constitutional authority; there is no parallel graph and no LLM behind the response.

## Scope of acquired skill
A structured, supervised online multiclass utterance classifier and Viterbi sequence-role tagger acquire the relationship among `HOLDER`, `SUBJECT`, `ATTRIBUTE`, `POLARITY` (not one regex per named phrase). It outputs a **sourced candidate** with type `BELIEF` or `NARRATOR`, not a WORLD fact. `user_message()` calls the trained candidate, records EVAL and COMMIT_NOOP, and DEFERS public speech: **no trained general relational verbalizer yet**. This is deliberate, not conversational fluency. Structural validity rejects multiple conflicting spans/nested beliefs rather than silently flattening them.

Learning corpus: 1,880 synthetic labelled episodes (1,100 affirmative role cases + 480 negated cases + 300 unrelated examples), 9 epochs; correlated synthetic training utterances do not count as independent source roots. No Qwen/Gemma inference, no human judges.

## Frozen test series, measured on exact graph

| Model | Familiar constructions, novel entity+attribute | Familiar constructions, novel entity, trained attribute | Totally unseen constructions, novel entities | Negations, new entities |
|---|---:|---:|---:|---:|
| P2A first attempt | 0/120 | not measured | 0/100 | not trained |
| P2B learned roles, no negation | 96/120 | 106/120 | 32/100 | 4 dangerous polarity confusions in fixed probe |
| P2C learned roles and polarity | **106/120** | **119/120** | **11/100** | **63/80** |
| P2C source model no new relation weights | 0/120 | 0/120 | 0/100 | 0/80 |
| P2C shuffled kind labels, correct span labels retained | 0/120 | 0/120 | 5/100 | 1/80 |

P2C cold reload gives EXACTLY the same test scores. Previous D1 restricted heldout remains **112/125**; legacy D2-P1 four tests and new P2C five tests: **9/9 PASS**. Original P1 graph facts structurally unchanged. No independent blind human benchmarking or real Android phone run for this release.

### Negative control reveals interference and limits
The P2B predecessor interpreted `Мира не думает, что куб синий` as a positive BELIEF, even though WORLD was not committed. P2C correctly returns `polarity=NEGATED`, `HOLDER=мира`, `SUBJECT=куб`, `ATTRIBUTE=синий`. Original four risky negated examples now separate negative polarity from the proposition, and four multi-clause/nested belief controls return ABSTAIN. **P2C is not a semantic-safety guarantee**: 17/80 separate negations still do not bind all roles; new syntax falls sharply 32/100 → 11/100 when adding negation, indicating potential interference/insufficient curriculum capacity. Do not hide this regression, do not call this full D2 GREEN.

### Why this is not hardcoded answers
The inference code has no test names, objects, teacher templates, regex conditions for specific negation words or if-string answer tables. It defines generic categorical roles and a trainable utterance/sequence scorer. Training cases supply gold token labels, including `POLARITY`, from one curated synthetic teacher source. The role definitions, tagger, and fixed rejection of multiply-bound roles are **algorithmic inductive biases**, not self-discovered operators. A true open-ended operator learner/general renderer is still missing.

## Portably reproduce

Install Python 3.11+ and pytest. Unzip full native runtime `C4_D2_P2C_NATIVE_RUNTIME_59_MODULES.zip`. Extract source D2-P1 `.c4m` from its own release. To exactly reproduce P2C:

```bash
PYTHONPATH=runtime python train_p2.py \
  --input C4_G329_D2_P1_GROUNDED_STORY_CANDIDATE.c4m \
  --output C4_D2_P2C_RELBINDER_NEGATION_CANDIDATE.c4m \
  --dataset P2C_FROZEN_DATA.json --report P2C_REPORT.json

C4_P2_PARENT=C4_G329_D2_P1_GROUNDED_STORY_CANDIDATE.c4m \
C4_P2_MODEL=C4_D2_P2C_RELBINDER_NEGATION_CANDIDATE.c4m \
C4_P2_REPORT=P2C_REPORT.json PYTHONPATH=runtime pytest -q test_p2c.py
```

Scripts, P2A failed dataset/report, P2B role-only dataset/report, P2C data/report, compatible graph and full runtime are included in the proof ZIP. The original G329, L1, D1, D2-P1 `.c4m` files are not overwritten.

## Next falsifiable P2-D3 architectural experiment

**Continuous graph learning without catastrophic interference**: use a reusable typed-relation operator, learned compositional variable binding, context-aware polarity and nested representation of other people's beliefs. Train in two phases with replay/consolidation **of dependent training data that does NOT acquire independent evidence**; compare mixed curriculum vs sequential curriculum on fixed old and new test families. No test phrase patches or replacing core with Qwen. Freeze independent blind dialogues before teacher distillation, compare to compute-/memory-matched small transformer baseline, then set explicit go/no-go for a non-transformer replacement. Full D2, multidomain/multimodal speech, and C004 Android physical receipt are STILL RED/PENDING.