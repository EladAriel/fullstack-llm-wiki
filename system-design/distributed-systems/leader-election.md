---
topic: Leader Election
tags: distributed-systems, coordination, availability
ai_summary: Leader election chooses one node to coordinate work such as writes or scheduling. It prevents conflicting primaries while allowing failover when the leader dies.
---

# Leader Election

## 1. Core Concept
Leader election designates a single active coordinator among peers. It solves split responsibility problems (dual writes, duplicate schedulers) while enabling automatic failover.

## 2. Architecture & Data Flow
1. Candidates race using consensus, locks (ZooKeeper/etcd), or gossip leases.
2. Winner holds a lease/fencing token.
3. Followers redirect writes or wait for tasks.
4. On lease expiry/failure detection, a new election runs.
5. Old leader must respect fencing to avoid split-brain actions.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Simplifies single-writer and singleton job semantics.
  * Enables automated failover without human intervention.
* **Disadvantages/Risks:**
  * False failure detection can thrash leadership.
  * Without fencing, two leaders may briefly act (split-brain).

## 4. Alternatives
**Leaderless quorum protocols** (Dynamo-style); **static primary** with manual failover for tiny systems.

## 5. Team Guidelines & Use Cases
**SHOULD** elect leaders for singleton schedulers and primary-writer DBs with fencing tokens. **SHOULD NOT** build custom election on heartbeats alone without a quorum/lease store.
