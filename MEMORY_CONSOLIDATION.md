# C4 Memory Consolidation

Normative note: long-term C4 should use HOT/WARM/COLD memory tiers, disk-backed persistent storage, provenance-preserving deduplication, schema extraction, and tested compression. SUMMARY != ORIGINAL EVIDENCE. SCHEMA != OBSERVATION. COMPRESSION != NEW TRUTH. Persistent state may exceed RAM; keep a hot working set in memory and cold state on disk. Promote compression changes only after regression, held-out transfer, provenance, retraction, size, latency, and cold-reload tests.
