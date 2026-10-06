# CP C4 G265 SYNTHETIC VISION NURSERY GREEN

Date: 2026-10-06
Status: GREEN

Parent:
- G264 child_g264_ru_sensor_reasoning_transfer_green.c4m
- 1619770 bytes
- SHA256 aef1f49725358a46915955affe0e4c5ac58ad6055a735e576990fb818e072b3a

Output:
- child_g265_synthetic_vision_grounding_green.c4m
- 1707998 bytes
- SHA256 6e62f3839ea41a13a9f420f0e579f549d3b1c95a766d93de01c076ea19a0d8de

Synthetic corpus:
- 108 physical PNG stimuli, 128x128
- 72 train
- 36 held-out and not entered as labeled examples
- Russian teacher labels only

Training:
- 748/748 admitted
- 0 rejected
- cold 10/10
- runtime-law changes 0

RED note:
First held-out absence check polluted itself by invoking _eid for the held-out label. RED output not promoted. Harness-only fix, clean rerun from G264.

Regression:
- 254 passed / 9 failed
- all 9 unchanged missing historical artifacts
- no new semantic/runtime assertion failures

Release:
- C4_G265_SYNTHETIC_VISION_GREEN_2026-10-06.zip
- SHA256 e4c655531141c67122dd05e4518f121a58a26902409919784af673c29157a3f6
