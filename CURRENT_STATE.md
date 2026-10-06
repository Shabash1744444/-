# CURRENT STATE

Date: 2026-10-06
Canonical GREEN generation: G265
Current organism: child_g265_synthetic_vision_grounding_green.c4m
Size: 1707998 bytes
SHA256: 6e62f3839ea41a13a9f420f0e579f549d3b1c95a766d93de01c076ea19a0d8de

## Active direction
Russian-first deep language + multimodal abstraction + raw sensory nursery.
English OmniCaption lexical/syntactic form remains quarantined; only abstract relations transfer.

## G263 — OmniCaption abstraction pass 3
Parent: G262.
- 117/117 admitted
- 0 rejected
- cold 14/14
- 1602113 bytes
- SHA256 8267844a7169641ea52382cc122c08a223e2eaf7f7f53ad4eec2853a30dd5b7c
- runtime changes 0

Adds:
- event boundaries
- multi-step procedures
- attempt vs success
- incomplete observation
- modality conflict
- attention/highlight vs world property
- number/graph vs measured quantity
- map/schema/model vs object
- background/foreground
- multi-source information
- social coordination
- example/counterexample learning
- multimodal evidence dependence
- Russian semantic bridge through language firewall

## G264 — Russian sensory reasoning transfer
Parent: G263.
- 84/84 admitted
- 0 rejected
- cold 14/14
- 1619770 bytes
- SHA256 aef1f49725358a46915955affe0e4c5ac58ad6055a735e576990fb818e072b3a
- runtime changes 0

Purpose:
Verify G263 abstractions on novel Russian scenes rather than OmniCaption-specific wording.

Transfer includes:
procedure, attempt/success, noisy/missing signal, modality conflict, attention, graph/schema, background, source chains, group motives, category learning, evidence independence, SELF/time and Russian-only explanation.

## G265 — synthetic raw-image nursery — CURRENT GREEN
Parent: G264.
- physical corpus: 108 PNG images, 128x128
- train split: 72
- held-out split: 36
- factors: круг/квадрат/треугольник; красный/зелёный/синий; слева/центр/справа; малый/большой; partial occlusion yes/no
- Russian teacher labels only
- exact raw-image SHA256 + low-level derived measurements stored in manifest

Training:
- 748/748 admitted
- 0 rejected
- cold 10/10
- 1707998 bytes
- SHA256 6e62f3839ea41a13a9f420f0e579f549d3b1c95a766d93de01c076ea19a0d8de
- runtime changes 0

Hard boundaries:
RAW_IMAGE != DERIVED_FEATURE
DERIVED_FEATURE != TEACHER_LABEL
TEACHER_LABEL != C4_AUTONOMOUS_RECOGNITION
SYNTHETIC TRANSFER != REAL-PHOTO GENERALIZATION
FILE NAME/METADATA must be hidden during held-out sensory tests.

Important RED:
First G265 exam was RED 9/10 because the harness itself called _eid on a held-out label and thereby created the entity it intended to prove absent. That RED was not promoted. Only the test was fixed; G265 was regenerated from clean G264. Runtime unchanged.

## Regression after G265
254 passed / 9 failed in 5.84s.
All 9 failures are unchanged FileNotFoundError cases for missing historical G207/G137/G151/G153 artifacts.
No new semantic/runtime assertion failures.

## Normative loop
counterexample -> minimal repair -> re-attack -> regression -> cold reload -> physical checkpoint -> next

RED never canonical.
No runtime change merely to make curriculum fit.
No byte padding.

## Next
Continue from exact G265.
High-value next steps:
- held-out visual tests without filename/teacher-label leakage
- richer synthetic visual scenes: multiple objects, occlusion/reappearance, containment, motion
- Russian speech/audio grounding
- OmniCaption abstraction mining only through language firewall
- Dostoevsky/complex Russian discourse in parallel
