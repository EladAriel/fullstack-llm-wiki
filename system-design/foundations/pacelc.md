---
topic: PACELC Theorem
tags: distributed-systems, consistency, latency
ai_summary: PACELC extends CAP: under partition choose Availability or Consistency; else choose Latency or Consistency. It explains why strongly consistent systems pay latency even when healthy.
---

# PACELC Theorem

## 1. Core Concept
PACELC says: if there is a **P**artition, trade **A** vs **C**; **E**lse trade **L**atency vs **C**onsistency. It solves the blind spot in CAP by explaining normal-operation cost of cross-node coordination.

## 2. Architecture & Data Flow
1. Healthy path: synchronous replication or quorum reads/writes add RTT for stronger consistency.
2. Weaker consistency allows local reads/writes with lower latency.
3. On partition: CP path blocks; AP path continues with divergence.
4. Tunable systems (e.g., quorum R + W) let operators slide along the L/C axis per operation.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Better mental model for multi-AZ and multi-region latency costs.
  * Supports per-query consistency tuning instead of one global choice.
* **Disadvantages/Risks:**
  * More knobs increase misconfiguration risk.
  * Teams may still under-specify client-visible consistency expectations.

## 4. Alternatives
Plain **CAP** for partition-only discussions; **consistency models** (linearizability, causal, eventual) for precise semantics.

## 5. Team Guidelines & Use Cases
**SHOULD** document both partition mode and healthy-path latency/consistency for shared stores. **SHOULD NOT** force global strong consistency for every read when local/eventual reads meet the product need.
