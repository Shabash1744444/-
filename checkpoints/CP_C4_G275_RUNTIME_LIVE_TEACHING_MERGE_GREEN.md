# CP C4 G275 RUNTIME LIVE TEACHING MERGE GREEN

Date: 2026-10-07
Status: GREEN
Parent runtime: G271
Canonical weights: G274 (unchanged)

## Source branch reviewed
An external Claude runtime branch implemented:
- live lexical teaching from ordinary dialogue;
- structured definition decomposition;
- open teaching questions across restart;
- Russian speech inflection/agreement;
- first/second-person dialogue;
- atomic autosave.

The external branch was NOT adopted directly. On exact G274 it reopened a previously closed morphology failure: productive verb surfaces could resolve to the noun concept `сеть`.

Its disposable acceptance-test token is test data only. It is not vocabulary, is not present in canonical G274 weights, and is not present in the G275 package.

## Three-way merge
G275 preserves:
- G271 explicit-verb morphology guard;
- G269/G271 discourse bridge and dialogue history;
- human-safe initiative / no machine-label leakage;
while adding:
- live teaching intent;
- structured definition learning;
- persisted open teaching state;
- Russian speech forms / agreement;
- first/second-person dialogue;
- atomic autosave.

Merge priority rules:
- explicit teaching act > generic discourse promise;
- evidence-aware explanation owns `Почему?` when a graph chain exists;
- pending self-confirmation yes/no belongs to teaching state;
- human mode keeps one-question waiting discipline.

## Validation
Full merged suite:
- 317/326 PASS
- 9 unchanged historical FileNotFoundError cases (G207/G137/G151/G153)
- 0 new semantic/runtime assertion failures

Exact G274 compatibility:
- G270 nouns 260/260
- G272 verbs 756/756
- G273 adjectives 780/780
- G274 semantic derivations 472/472
- verb/noun collision controls preserved
- homograph quarantine preserved
- canonical G274 SHA unchanged by probes

Temporary live-teaching probe used a disposable nonce on a COPY of G274:
- teaching announcement recognized;
- definition stored as graph structure rather than one opaque string;
- immediate recall PASS;
- autosave/reopen recall PASS;
- canonical weights not modified.

## Artifact
- C4_RUNTIME_G275_LIVE_TEACHING_MERGE_GREEN_2026-10-07.zip
- 324818 bytes
- SHA256 `1c7243de518c12cff4a27572cf2e423bd77c5bd6cf70925748e86ce698ef9a68`

Combined recovery:
- C4_G275_RUNTIME_PLUS_G274_WEIGHTS_2026-10-07.zip
- 2113082 bytes
- SHA256 `10943a16639f4fa6b17eef0e107c1ccf16b864e1a616c0294153e515efde4c5d`

## New hard boundary
TEST TOKEN != VOCABULARY KNOWLEDGE.

## Next
ActiveGaps / Teacher Cost benchmark on G275 runtime + G274 weights.
