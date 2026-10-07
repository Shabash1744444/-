# CURRENT STATE

Date: 2026-10-07
Canonical GREEN weights generation: G274
Canonical runtime generation: G275

Current organism:
- child_g274_dense_semantic_core_green.c4m
- 1805052 bytes
- SHA256 6e566b67e54504fbdb9f2924bdba0ed330dce5ce525acb97234d5dd33676c20e

Canonical runtime:
- C4_RUNTIME_G275_LIVE_TEACHING_MERGE_GREEN_2026-10-07.zip
- 324818 bytes
- SHA256 1c7243de518c12cff4a27572cf2e423bd77c5bd6cf70925748e86ce698ef9a68

Combined:
- C4_G275_RUNTIME_PLUS_G274_WEIGHTS_2026-10-07.zip
- 2113082 bytes
- SHA256 10943a16639f4fa6b17eef0e107c1ccf16b864e1a616c0294153e515efde4c5d

Persistent binary recovery: personal Library /C4_Canonical/.

## G274 weights remain unchanged
Fast Curriculum cumulative state:
- nouns: 260/260
- verbs: 756/756
- adjectives: 780/780
- semantic derivations: 472/472

G274 SHA was verified unchanged before/after G275 probes.

## G275 runtime
External live-teaching work was reviewed but not adopted wholesale.
Direct use reopened a closed failure where productive verb forms could resolve to noun `сеть`.

G275 three-way merge keeps G271 safety and canonical discourse while adding:
- explicit teaching announcements;
- definitions decomposed into graph relations;
- pending teaching/self-check state across restart;
- Russian speech inflection/agreement;
- first/second-person dialogue;
- atomic autosave.

The external disposable acceptance-test token remains test-only and is not vocabulary knowledge.

## Validation
Full merged suite:
- 317/326 PASS
- 9 unchanged historical FileNotFoundError cases
- 0 new semantic/runtime assertion failures

Exact G274 compatibility:
- 260/260 noun forms
- 756/756 verb forms
- 780/780 adjective forms
- 472/472 semantic derivations
- verb/noun guard preserved
- homograph quarantine preserved

## Normative boundaries
TEST TOKEN != VOCABULARY KNOWLEDGE
HOMOGRAPH != IDENTITY
ORTHOGRAPHIC SUFFIX != LEXICAL POS
SPEECH FORM != GRAPH FACT
AUTOSAVE != NEW EVIDENCE

## Immediate next work
G276 candidate: ActiveGaps / Teacher Cost.
Goal: C4 should choose questions by expected downstream learning value rather than asking every gap.

Benchmark:
unseen text -> gaps -> utility ranking -> one teacher question -> structural answer -> re-evaluation -> held-out competency.

Do not increase corpus scale until Teacher Cost starts falling.
