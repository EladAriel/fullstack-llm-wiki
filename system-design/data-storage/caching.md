---
topic: Caching
tags: caching, performance, latency
ai_summary: Caching stores frequently accessed data in a fast layer to reduce latency and backend load. Designs include cache-aside, read-through, write-through, and write-back.
---

# Caching

## 1. Core Concept
A cache keeps a subset of data closer/faster than the source of truth. It solves repeated expensive reads (DB, CPU, network) by trading freshness and memory for speed.

## 2. Architecture & Data Flow
1. Client requests data.
2. Cache-aside: app checks cache → on miss loads DB → populates cache.
3. Read-through/write-through embed load/store in the cache library.
4. TTLs and explicit invalidation bound staleness.
5. Eviction (LRU/LFU/etc.) reclaims memory under pressure.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Major latency and cost wins for read-heavy workloads.
  * Protects databases from hot-key stampedes when paired with locking/singleflight.
* **Disadvantages/Risks:**
  * Stale reads and invalidation bugs cause subtle correctness issues.
  * Cache stampedes and thundering herds can amplify outages.

## 4. Alternatives
**CDN caching** for public HTTP assets; **materialized DB views** for complex but somewhat fresh query results; **bigger/faster primary DB** when hit rates would be poor.

## 5. Team Guidelines & Use Cases
**SHOULD** cache read-heavy, idempotent data with explicit TTL/invalidation ownership. **SHOULD NOT** cache strongly transactional balances without a defined consistency story.
