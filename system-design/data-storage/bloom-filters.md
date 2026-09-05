---
topic: Bloom Filters
tags: algorithms, caching, storage
ai_summary: A Bloom filter is a probabilistic set membership structure with false positives but no false negatives. It cheaply skips unnecessary disk or network lookups.
---

# Bloom Filters

## 1. Core Concept
A Bloom filter hashes elements into a bit array. Querying may say “maybe present” or “definitely absent.” It solves expensive negative lookups (cache miss → DB) by quickly ruling out absences.

## 2. Architecture & Data Flow
1. Allocate an m-bit array and k hash functions sized for expected n and false-positive rate.
2. On insert, set k bits.
3. On lookup, check k bits—all set means maybe present; any clear means absent.
4. Used before DB/SSTable access or as a cache admission hint.
5. Counting/scalable variants exist but cost more memory.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Tiny memory footprint for huge keyspaces.
  * Guarantees no false negatives for standard filters.
* **Disadvantages/Risks:**
  * False positives cause extra work.
  * Cannot delete entries in the classic non-counting filter.

## 4. Alternatives
**Cuckoo filters** (support delete, different memory trade-offs); **exact hash sets** when memory allows zero false positives.

## 5. Team Guidelines & Use Cases
**SHOULD** use Bloom filters in front of expensive existence checks at scale (LSM reads, large sparse keyspaces). **SHOULD NOT** use them where false positives are unsafe without a definitive follow-up check.
