# C004-R1 START — segregate WebView and C4-private executor
Date: 2026-10-09
Base C4 HEAD: 3e650f32a27a0f54a7ec40ec702435bfbf29494b
Android Emu experimental ref: experiments/c4-c004-native-host, 0ba500e28bb406a1a6fb391ae55f233fe1249f29
Observed implementation: public @JavascriptInterface executeRoomAction() and Java-private C4 dispatch both invoke the same entry point and accept a caller-chosen requestId. A WebView call with reserved C4 trial:* ID can mutate sandbox or consume replay guard before the trusted C4 request arrives. This is a host-boundary integrity risk, not proof of existing real-device exploitation.

Frozen requirement before edit: reject C4-owned request IDs via public JavaScript method; private Java dispatch must call a non-@JavascriptInterface executor. Preserve normal user room actions. Check outcome and native C4 credits remain verified only by private Java->Python route. Build APK, check CI, keep C004 DEVICE PENDING until physical phone trace.
Previous C003 remains DONE; C004 integrated, device unverified. No C4M mutation. If interrupted, inspect both repos branch HEAD and this START.
