# C4 G223 — FRONTIER EFFICIENCY + DIRTY WORLD START

Base: G222 canonical GREEN
Model: child_g222_dirty_evidence_collision.c4m
Bytes: 453660
SHA256: d0c1c16409715fe456cdfd36804771d2fa6dbaf76ab1f83fb6be707f734dfd3c

## Goal
Test whether curriculum selection can reduce directly taught lessons while preserving held-out structural learning and epistemic robustness.

## Two simultaneous pressures
1. Dirty mixed-world: true lessons, shared-ancestry misinformation, genuinely independent plausible errors, later independent corrections.
2. Frontier scheduler prototype: rank candidate lessons by expected information gain around UNKNOWN/conflict/near-complete structures instead of random/full teaching.

## Required comparison
Use the same generated ground truth and held-out exam for baseline curriculum and frontier-selected curriculum. Do not credit UNKNOWN restraint as positive transfer.

Track separately:
- candidate lessons
- actually taught lessons
- new correct positive held-out inferences
- negative structural controls
- contamination/admission failures
- correction/recovery failures
- cold reload
- runtime changes
- model bytes

## GREEN
Frontier must reach comparable held-out correctness with fewer taught lessons and no worse contamination/recovery. No byte padding. No unsupported do(X), conditional causality, or schema->primitive CAUSES claims.

Status: STARTED, NOT GREEN.
