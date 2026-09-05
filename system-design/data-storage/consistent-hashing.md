---
topic: Consistent Hashing
tags: distributed-systems, partitioning, caching
ai_summary: Consistent hashing maps keys to nodes on a ring so that adding/removing nodes moves only a small fraction of keys. It underpins distributed caches and many shard routers.
---

# Consistent Hashing

## 1. Core Concept
Consistent hashing places nodes and keys on a circular hash space; a key belongs to the next node clockwise (often with virtual nodes). It solves massive remapping when cluster membership changes under naive modulo hashing.

## 2. Architecture & Data Flow
1. Hash each node (and vnodes) onto the ring.
2. Hash the key; walk clockwise to find the owner.
3. Optionally replicate to the next N distinct nodes for durability.
4. On node add/remove, only neighboring key ranges move.
5. Clients or proxies keep a membership view and refresh on changes.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Minimizes data movement during scale events.
  * Supports heterogeneous node capacity via vnode weighting.
* **Disadvantages/Risks:**
  * Without vnodes, load can be uneven.
  * Membership churn and gossip delays can cause temporary misrouting.

## 4. Alternatives
**Range partitioning** (ordered keys, good for scans) and **rendezvous hashing (HRW)** as another minimal-remapping scheme.

## 5. Team Guidelines & Use Cases
**SHOULD** use consistent hashing for distributed caches and partitioners with elastic node counts. **SHOULD NOT** ignore hot-key mitigation—hashing alone does not fix popularity skew.
