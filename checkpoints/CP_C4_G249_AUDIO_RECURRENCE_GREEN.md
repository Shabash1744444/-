# CP C4 G249 AUDIO RECURRENCE GREEN

Date: 2026-10-06
Status: GREEN

Canonical output:
- child_g249_audio_recurrence_green.c4m
- 1247711 bytes
- SHA256 b28f2fe078b896e768f9b20efb112a1b51aa5bc40a596d9f9c9bdaacc1b71e46

Parent:
- G248 child_g248_song_multimodal_green.c4m
- 1220480 bytes
- SHA256 93486415f2306c104ec70a4f5ef85fa905c51ff5eaaee5a25df68d7b4bc8ae20

Training:
- 162/162 admitted
- 0 rejected
- cold 14/14
- runtime changes 0

Method:
- real MP3 waveform
- onset/beat estimation
- beat-synchronous chroma CENS
- 8-beat windows, stride 2
- nonlocal cosine recurrence similarity
- no title/lyric labels used to define repeated pairs

Key results:
- strong nonlocal recurrence candidates in April and Ledyanoy Vozduh
- both Vglyadyvayas vverkh artifacts show closely matching recurrence timing patterns
- Defragmentaciya tempo estimate conflict retained with method provenance (~92 G247 sampled excerpts vs ~117 G249 full-track beat analysis)

Hard boundaries:
RECURRENCE CANDIDATE != CHORUS LABEL
HIGH CHROMA SIMILARITY != SAME LYRICS/TIMBRE/BYTES
MEASUREMENT != METHOD-INDEPENDENT TRUTH
DERIVED TOOL OBSERVATION != SELF-ACQUIRED SENSOR ALGORITHM

Regression:
- 254/263 passed in 5.08s
- same 9 missing historical artifact FileNotFoundErrors
- no new semantic/runtime assertion failures
