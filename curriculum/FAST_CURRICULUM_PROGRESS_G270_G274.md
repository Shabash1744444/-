# C4 FAST CURRICULUM PROGRESS — G270 -> G274

Date: 2026-10-07

Core law:

> Growth is accepted only when later capability grows faster than direct storage.

| Generation | Block | Direct lessons | Held-out / novel transfer | Ratio | Model bytes |
|---|---|---:|---:|---:|---:|
| G270 | noun lemma morphology | 158 | 260 | 1.646 | 1,756,887 |
| G272 | verb morphology | 128 | 756 | 5.906 | 1,773,947 |
| G273 | adjective morphology | 99 | 780 | 7.879 | 1,787,794 |
| G274 | dense semantic taxonomy | 114 | 472 | 4.140 | 1,805,052 |

G271 is a runtime safety generation, not weight training.

From G270 to G274 the persistent model grew by only 48,165 bytes while adding the verb, adjective and semantic transfer blocks. Ratios are block-local and are not one homogeneous benchmark.

## Operational rules learned
1. Before adding a lemma, scan for collisions with admitted and useful generated surfaces.
2. Homographs that need context go to quarantine; do not destructively merge them.
3. Teach only missing productive morphology positions; use ablation to minimize anchor lessons.
4. Count transfer only on held-out arrangements or truths absent at baseline.
5. After every block: negative controls -> cold reload -> cumulative earlier-skill re-attack -> runtime regression.
6. Dense semantic cells should prefer taxonomy/root facts over repeated per-word properties.
7. Polysemous bare labels should be replaced by sense-specific labels until contextual sense resolution exists.

Next: active-gap utility / teacher-cost scheduler, then guided reading over small unseen texts.
