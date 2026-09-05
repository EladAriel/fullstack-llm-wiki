---
topic: Quorum Reads and Writes
tags: distributed-systems, consistency, replication
ai_summary: Quorum systems require overlapping majorities of replicas for reads and writes so that the latest value is observed. Tunable R/W quorums balance latency and consistency.
---

# Quorum Reads and Writes

## 1. Core Concept
With N replicas, a write quorum W and read quorum R such that R + W > N ensure read sets intersect write sets. Quorums solve the need for consistency without contacting every replica every time.

## 2. Architecture & Data Flow
1. Client or coordinator sends a write to N replicas, waits for W acks.
2. Reads query R replicas and pick the newest timestamp/version.
3. Read repair or anti-entropy fixes lagging replicas.
4. Sloppy quorums may write to hinted handoff nodes during failures.
5. Operators tune N/R/W per latency and durability goals.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Tunable consistency without full broadcast on every op.
  * Survives minority replica failures.
* **Disadvantages/Risks:**
  * Higher R/W increases latency and reduces availability.
  * Clock/version conflicts still need resolution rules.

## 4. Alternatives
**Primary-backup** (all writes to leader); **full synchronous replication to all nodes** (simpler but less available).

## 5. Team Guidelines & Use Cases
**SHOULD** use R + W > N for data that must not return arbitrarily stale values. **SHOULD NOT** assume W=1, R=1 is safe for critical financial state.
