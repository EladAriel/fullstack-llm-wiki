---
topic: Cache Eviction Policies
tags: caching, memory, performance
ai_summary: Eviction policies decide which cache entries to drop when memory is full. LRU, LFU, FIFO, and TTL-based strategies optimize different access patterns.
---

# Cache Eviction Policies

## 1. Core Concept
When a cache reaches capacity, an eviction policy selects victims to delete. The problem is maximizing hit rate under limited memory for a given workload shape.

## 2. Architecture & Data Flow
1. Insert/update entries with metadata (recency, frequency, size, expiry).
2. On memory pressure, policy ranks candidates (LRU list, LFU counters, random, SLRU/ARC hybrids).
3. Evict until allocation succeeds.
4. TTL expiry may remove entries independently of capacity.
5. Metrics track hit rate, evictions, and scan resistance.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Good policy fit can double effective hit rate without more RAM.
  * TTL eviction bounds staleness even for hot keys.
* **Disadvantages/Risks:**
  * LRU fails on scans that churn the working set.
  * LFU can retain stale popular keys too long without aging.

## 4. Alternatives
**Admission policies** (TinyLFU) that refuse low-value inserts; **sizing/partitioning caches** per workload instead of one shared policy.

## 5. Team Guidelines & Use Cases
**SHOULD** pick LRU/ARC-like defaults for general web app caches and measure hit rate. **SHOULD NOT** rely on unbounded caches in process memory without eviction and monitoring.
