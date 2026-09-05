---
topic: Consensus Algorithms (Raft / Paxos)
tags: distributed-systems, consensus, coordination
ai_summary: Consensus protocols let distributed nodes agree on a single value or log despite failures. Raft and Paxos underpin strongly consistent coordination and replicated state machines.
---

# Consensus Algorithms (Raft / Paxos)

## 1. Core Concept
Consensus algorithms ensure a cluster agrees on operations (usually an ordered log) even if some nodes crash or messages delay. They solve leader election, configuration changes, and consistent replication for control planes and databases.

## 2. Architecture & Data Flow
1. Nodes elect a leader with quorum votes.
2. Leader proposes log entries to followers.
3. Entry commits once a majority persists it.
4. State machine applies committed entries in order.
5. Minority partitions cannot commit conflicting history.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Strong consistency and clear failure semantics under majority rule.
  * Foundation for reliable metadata stores and failover.
* **Disadvantages/Risks:**
  * Majority requirement limits availability under large outages.
  * Cross-region consensus adds significant latency.

## 4. Alternatives
**Primary-backup with async replication** (weaker durability); **gossip CRDTs** when conflict-free eventual merges suffice.

## 5. Team Guidelines & Use Cases
**SHOULD** rely on consensus-backed stores for cluster metadata, locks, and configuration. **SHOULD NOT** run chatty application data paths through a global consensus group.
