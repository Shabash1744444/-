# RUNTIME CURRENT — G294 RELATION ALGEBRA GREEN

Canonical runtime: G294.
Canonical weights: G292.

Runtime:
C4_RUNTIME_G294_RELATION_ALGEBRA_GREEN_2026-10-07.zip
297,804 bytes
SHA256 3ce81d00f50a0cde28eef0d7e05bbe329f2665f41494a5a12fb9bd1b67998f32

Weights SHA256:
d5631373fbdf24f2bf7a8068ca768edc0a4e94765e5b43035c90c3712aa2d246

Combined SHA256:
914873776a59e9e5f7ef75410e4191a357ff9825c5c05b558e49872a91af1e68

G294 = G293 storage/runtime + conservative read-only relation algebra.

Safe algebra:
PART_OF <-> HAS_PART
BEFORE <-> AFTER
SYNONYM symmetric
ANTONYM symmetric
OPPOSITE symmetric

Hard boundaries:
INVERSE RELATION != NEW FACT.
SYMMETRIC READING != NEW EVIDENCE.
PART_OF != TRANSITIVE BY DEFAULT.
HAS != HAS_PART.
MEANS != SYMMETRIC.
ROLE != INHERITED BY DEFAULT.

Validation:
memory 360/369; SQLite 360/369.
All nine failures are unchanged historical missing artifacts.
