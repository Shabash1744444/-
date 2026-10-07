# CP C4 G294 RUNTIME RELATION ALGEBRA GREEN

Date: 2026-10-07
Parent runtime: G293 SQLite Store Green
Canonical weights: exact G292, unchanged

Safe read-only algebra:
- PART_OF <-> HAS_PART
- BEFORE <-> AFTER
- SYNONYM symmetric
- ANTONYM symmetric
- OPPOSITE symmetric

Both positive and negative polarity are preserved.
Direct contradiction against an algebraically derived reading yields CONFLICT.
Derived readings are never persisted as facts/evidence.

Forbidden inferences explicitly tested:
- PART_OF transitivity
- HAS -> HAS_PART
- MEANS symmetry
- ROLE symmetry/inheritance

Focused:
12/12 memory
12/12 SQLite

Full:
360/369 memory
360/369 SQLite

All nine failures are unchanged missing historical FileNotFoundError artifacts.
