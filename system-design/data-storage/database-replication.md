---
topic: Database Replication
tags: database, availability, replication
ai_summary: Replication copies data to multiple database nodes for high availability and read scale. Primary-replica and multi-primary topologies define write ownership and lag behavior.
---

# Database Replication

## 1. Core Concept
Replication keeps multiple copies of a dataset in sync. It solves durability (survive node loss), read scaling, and geographic locality, at the cost of lag and failover complexity.

## 2. Architecture & Data Flow
1. Primary accepts writes and records them to a log (WAL/binlog).
2. Replicas apply the log asynchronously or synchronously.
3. Reads may be routed to replicas with freshness awareness.
4. On primary failure, orchestrator promotes a replica and redirects clients.
5. Split-brain prevention uses fencing, quorum, or STONITH-style controls.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Fast failover and improved read throughput.
  * Geographic replicas reduce read latency for distant users.
* **Disadvantages/Risks:**
  * Async replicas serve stale data; sync replication adds write latency.
  * Failover bugs can cause data loss or dual writes.

## 4. Alternatives
**Sharding** for write scale-out; **multi-region distributed databases** with consensus per partition.

## 5. Team Guidelines & Use Cases
**SHOULD** run at least one replica for production systems of record with tested failover. **SHOULD NOT** silently send strongly consistency-sensitive reads to lagged replicas.
