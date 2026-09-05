---
topic: Database Indexing
tags: database, performance, storage
ai_summary: Indexes are auxiliary data structures that speed lookups and sorting at the cost of write overhead and storage. B-trees and hash indexes are the most common forms.
---

# Database Indexing

## 1. Core Concept
An index maps keyed values to row locations so the engine avoids full table scans. Indexing solves high-latency queries on large tables by trading extra storage and slower writes for faster reads.

## 2. Architecture & Data Flow
1. Declare indexes on selective columns or composites matching WHERE/ORDER BY/JOIN keys.
2. On write, the engine updates table heap/clustered structure and each secondary index.
3. Planner chooses index scan, bitmap scan, or sequential scan by cost.
4. Covering indexes can satisfy queries without touching base rows.
5. Monitor bloat, unused indexes, and write amplification.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Orders-of-magnitude faster point lookups and range scans when selective.
  * Enforces uniqueness constraints.
* **Disadvantages/Risks:**
  * Every extra index slows inserts/updates/deletes.
  * Wrong indexes waste space and can mislead the planner.

## 4. Alternatives
**Materialized views** for expensive prejoined read models; **application-level caches** for ultra-hot keys.

## 5. Team Guidelines & Use Cases
**SHOULD** index foreign keys and high-selectivity filter columns used in production queries. **SHOULD NOT** create many overlapping indexes “just in case”—prove need with EXPLAIN and slow-query logs.
