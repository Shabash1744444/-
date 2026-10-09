# C4 G331 / D4 — FALSIFIABLE CONTINUAL-LEARNING EXPERIMENT (RED)
Date: 2026-10-09. Scope: scientific test only, no production architecture update.

## Status: RED (NOT DONE / NOT CANONICAL)
- This pass evaluates whether existing trained relation-role binder can add negation while retaining a first skill and transferring to withheld syntax. It does NOT show C4 replacing an LLM.
- Uses the exact original `C4_G329_D2_P1_GROUNDED_STORY_CANDIDATE.c4m`, SHA256 `f8ed0e709b565ae0b437b8b273cd70c75762ed09ebb5cbe31bf099e6a412309c`, with unchanged 59-module P2C runtime SHA256 `538b5cda146c97efc2853ee4993cee6e1266bee8aa50fb03519dc909283373de`.
- The independent 340-case (120 positive +120 negative +100 entirely new syntax) synthetic challenge was physically frozen BEFORE training. SHA256 `42385c3807e41fd38815e09ebba921e41bffd907c9f078c8da9ae0489916409d`. Separate four nested perspective stressors. No evaluation surface included in teaching lessons.
- Preregistered gates: >=90/120 positive retention; >=90/120 negative; >=50/100 new syntax; strict source/world integrity.

## Actual experiment
Phase A: 1,100 positive +300 OTHER ×4 epochs, 5,600 example updates. Phase B: 480 negated +300 OTHER ×7 epochs, 5,460 updates. Replay variant replaces 120 OTHER with 120 old positive examples, keeping 5,460 phase-B update budget. Joint comparator 11,280 updates (220 extra, recorded). Online structured sequence perceptron is UNCHANGED, no new answer handlers or external LLM.

One original-order success on independently frozen challenge:
- After A: old positive 105/120, negative 0/120, novel grammar 27/100.
- A→B naive: 60/120, 57/120, 27/100.
- A→B replay: 105/120, 118/120, 27/100.
- Joint: 105/120, 91/120, 14/100.
- Prior historical P2C model, unrelated training regime: 116/120, 106/120, 22/100.

## Falsification across three further shuffle seeds
| Seed | Old positive naive/replay | Negative naive/replay | New grammar naive/replay |
|---|---:|---:|---:|
| 11 | 56/120 → 56/120 | 28/120 → 40/120 | 29/100 → 26/100 |
| 23 | 113/120 → 72/120 | 104/120 → 95/120 | 14/100 → 19/100 |
| 37 | 62/120 → 110/120 | 82/120 → 113/120 | 13/100 → 31/100 |

Across four orders replay improved positive retention only 2/4 (1 tie, 1 worse), and negative transfer 3/4 (1 worse). NO regime reached preregistered new syntax threshold 50/100. Four seeds and synthetic curriculum are not sufficient for a stable statistical generalization claim. Initial impressive result MUST NOT be reported as a general methodology.

## Actual physical experiment artifacts / integrity
- One experimental **noncanonical** replay `.c4m` output SHA256 `04495a5f558a0974d7084b4597529ccc897c71a2558de88cccf0f7e365188480`, 2,765,328 bytes.
- Cold graph: 15,745 facts: 12,767 preserved parent facts + 2,978 supervised language-parameter facts with ONE dependent EXTERNAL_CORPUS/TEACHER root. No WORLD promotion.
- Full directed local test run: **14 PASS**, comprising five D4, four D2-P1 and five D2-P2C tests. Old D1 supervised synthetic score retained 112/125. Historical complete regression and real Android room action/receipt gate NOT RUN, so C004 remains DEVICE_PENDING.
- Original core/parent `.c4m` / original C4 law semantics / Android UI unchanged.
- Self-contained 84-entry ZIP, CRC checked: `C4_D4_FALSIFIABLE_CAPACITY_REPLAY_RED_2026-10-09.zip` SHA256 `a93d590dab58305deaaa5b1a82b67d05a9135dd0c768e46c7dead8765cde1468`.
- Persistent Library folder `/C4_Candidates/G331_NATIVE_COGNITION/D4_FALSIFICATION_2026_10_09/` with ZIP, README and preregistration. Archive includes both source and trained models, native runtime, train/test datasets, code, all seed scores, frozen SHA and complete logs.

## Exact structural limitation (not a generic limit on C4)
The current `c4child/d2_relational.py` emits only BELIEF/NARRATOR with one holder, subject, attribute and polarity (fixed ROLES/TAGS; only one span per role), so full nested `A thinks B believes X` cannot be represented in this output regardless of weight budget. Four deliberately nested controls all returned ABSTAIN. This is safe restraint but NOT understanding.

## Decision
Full D4 remains RED; do not train Omni-Qwen on massive synthetic content, do not call C4 an LLM replacement, do not greenlight broad architectural expansion. A future NEW experiment must independently verify learnable typed nested compositions and withheld syntactic families, retain old skills across multiple seeds, and produce real general language output without teacher inference or ad hoc string rules. Stop broad work until a narrow proof passes.