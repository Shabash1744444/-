# C4 LEXICAL GRAPH SCALE TARGETS

Date: 2026-10-07
Status: engineering hypothesis / curriculum target, NOT proof of emergence.

## Why
Russian should not be represented as a flat list of words.
The target is a typed lexical-semantic graph whose connectivity supports composition and transfer.

WORD COUNT != LANGUAGE UNDERSTANDING.
EDGE COUNT != EMERGENCE.
But insufficient connectivity guarantees fragmentation.

## Node scale
OpenCorpora documents roughly 180,000 lemmas and separately represents word forms and links between lemmas.

Use ~180k lemma nodes as a practical broad-Russian reference scale, not a claim that Russian has exactly 180k words.
Language is open-ended; proper names, technical terms and neologisms extend it.

## Non-uniform semantic density target
Do not give every lemma equal degree.

Tier A CORE:
20,000 high-frequency/general lemmas
target ~30 useful typed semantic edges each
~= 600,000 semantic edges

Tier B COMMON:
60,000 lemmas
target ~12 semantic edges each
~= 720,000 semantic edges

Tier C LONG TAIL:
100,000 lemmas
target ~3 semantic edges each
~= 300,000 semantic edges

Semantic total target:
~= 1,620,000 directed/typed semantic relations.

Candidate relation families:
SYNONYM / ANTONYM / HYPERNYM / HYPONYM
PART_OF / HAS_PART
CAUSE / EFFECT
AFFORDANCE
TYPICAL_AGENT / TYPICAL_PATIENT
PROPERTY
LOCATION / TIME
COLLOCATION
REGISTER
IDIOM
POLYSEMY/SENSE
ANALOGY
CONTRAST
SOURCE/PROVENANCE

No generic untyped RELATED edge as a substitute.

## Morphological graph
If a broad lemma has on average ~8 useful lemma<->form/feature links:
180,000 * 8 ~= 1,440,000 morphological/form links.

Combined rough lexical+morphological target:
1.62M + 1.44M ~= 3.06M typed links.

This number is an engineering scale estimate, not a mandatory exact target.

## Graph-connectivity sanity check
For an Erdos-Renyi-style undirected random graph, the connectivity threshold is roughly:

E ~= N ln(N) / 2.

For N=180,000:
ln(N) ~= 12.1
E ~= 1.09M undirected edges.

This is ONLY a mathematical sanity check.
A typed semantic graph is not random.
Connectivity alone does not imply intelligence or emergence.
Still, a 1.6M semantic-edge target is in the regime where a broad undirected projection can be richly connected rather than a collection of isolated lexical islands.

## Why 100 MB becomes meaningful
Recent C4 growth gives a rough serialized cost around 120-130 bytes per admitted relation in the current ZIP/JSON-like representation (heuristic only; lessons are not guaranteed one-to-one with physical edges).

At ~125 B/link:
3.06M links ~= 365 MiB incremental storage.

If serialization is compacted to ~32 B/link:
3.06M links ~= 93 MiB.

At ~24 B/link:
~= 70 MiB.

Therefore the 100 MB milestone can be made meaningful by storage engineering:
- intern every string once;
- integer entity IDs;
- compact relation codes;
- shared provenance tables;
- delta/varint encoding;
- deduplicated morphology paradigms;
- optional compressed adjacency blocks.

The storage representation may change WITHOUT changing C4 physics if graph semantics/provenance are preserved.

## Emergence hypothesis
Hypothesis:
richer behavior may appear when many previously isolated concepts gain short typed paths through a sufficiently dense graph.

Test it, do not assume it.

Measure versus graph growth:
- unseen analogy transfer;
- composition across 2/3/4 hops;
- lexical generalization;
- novel paraphrase understanding;
- word-sense disambiguation;
- new concept induction;
- average/median path length in useful semantic projection;
- connected-component size;
- clustering by relation type;
- error propagation;
- latency.

A capability counts only when it appears on held-out surfaces and survives cold reload.

## Priority
Dense CORE vocabulary is more valuable than uniformly sparse coverage.
First make 20k common lemmas deeply connected.
Then broaden to 80k.
Then extend to ~180k long tail.

Do not spend 100 MB on obscure words while ordinary Russian composition still fails.


## Prototype scaling correction from Claude G268
Measured G266 prototype:
- archive ~1.7 MB;
- 9,173 facts;
- graph_hot JSON ~11 MB;
- live Python graph/state ~43 MB;
- lexical index ~6 MB after optimization.

Naive x59 archive growth (~100MB):
- ~540k facts;
- ~650MB graph_hot JSON;
- ~2.5GB live Python graph/state;
- ~0.4GB lexical index.

Therefore prior byte-per-edge estimates based only on .c4m archive size are insufficient for mobile feasibility.
Track BOTH:
- persistent/on-disk compressed bytes;
- expanded live-memory bytes.

The long-range ~3M-link lexical target may require far more than 100MB in the current format.
100-300MB remains a useful persistent-state milestone only after storage compaction/lazy loading.

## Storage metric
For every scale checkpoint record:
archive bytes
expanded persistent graph bytes
resident set size after load
hot-cache size
index size
cold-load latency
first-query latency
steady-query latency

Capability-per-byte should use total deployed footprint, not archive size alone.
