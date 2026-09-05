---
topic: NoSQL Databases
tags: database, storage, scaling
ai_summary: NoSQL covers document, key-value, wide-column, and graph stores optimized for scale and flexible models. They trade some relational features for partition-friendly access patterns.
---

# NoSQL Databases

## 1. Core Concept
NoSQL databases abandon or relax the classic relational model to optimize specific access patterns, availability, or horizontal scale. They solve problems where schema flexibility, massive key lookups, or partition-local operations dominate.

## 2. Architecture & Data Flow
1. Model data around query patterns (document per aggregate, KV per key, wide rows).
2. Partition by key across nodes (often consistent hashing).
3. Replicate partitions with configurable consistency.
4. Application handles joins/denormalization that SQL would do server-side.
5. Secondary indexes or search engines complement primary access paths.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Easier horizontal scale for simple key-centric workloads.
  * Flexible documents speed product iteration for evolving payloads.
* **Disadvantages/Risks:**
  * Less built-in multi-record transaction support in many systems.
  * Poor access-pattern design causes expensive scans and hot partitions.

## 4. Alternatives
**Relational SQL** for complex joins/invariants; **search engines** (OpenSearch/Elastic) when full-text relevance is the primary need.

## 5. Team Guidelines & Use Cases
**SHOULD** choose NoSQL when access patterns are clear and partition keys are well understood. **SHOULD NOT** pick NoSQL only “for scale” before measuring SQL limits and modeling query paths.
