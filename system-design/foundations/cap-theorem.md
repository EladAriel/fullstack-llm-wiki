---
topic: CAP Theorem
tags: distributed-systems, consistency, availability
ai_summary: CAP states that during a network partition a distributed system must choose between consistency and availability. It frames datastore and replication trade-offs under failure.
---

# CAP Theorem

## 1. Core Concept
The CAP theorem says that in the presence of a network **P**artition, a distributed data system cannot simultaneously guarantee strong **C**onsistency and **A**vailability. It solves the problem of clarifying which guarantees remain when nodes cannot communicate.

## 2. Architecture & Data Flow
1. Replicate data across nodes for durability and locality.
2. When a partition occurs, some nodes cannot confirm latest writes.
3. CP systems refuse or block conflicting operations until quorum is restored.
4. AP systems accept writes on both sides and reconcile later (version vectors, CRDTs, last-write-wins).
5. Outside partitions, many systems optimize for both latency and consistency (see PACELC).

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Gives a shared vocabulary for datastore selection under failure modes.
  * Forces explicit product decisions about stale reads vs write rejection.
* **Disadvantages/Risks:**
  * Often oversimplified as a permanent C-vs-A choice rather than a partition-time trade-off.
  * Does not capture latency trade-offs when the network is healthy.

## 4. Alternatives
**PACELC** extends CAP: if Partition then A/C else Latency vs Consistency. **BASE** (Basically Available, Soft state, Eventual consistency) is an AP-leaning design style vs ACID.

## 5. Team Guidelines & Use Cases
**SHOULD** use CAP language when choosing multi-region databases and defining partition behavior. **SHOULD NOT** claim a system “ignores CAP”; document partition behavior and client-visible anomalies instead.
