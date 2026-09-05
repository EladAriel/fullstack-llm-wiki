---
topic: Consistency Models
tags: consistency, distributed-systems, database
ai_summary: Consistency models define which orderings and visibilities of reads/writes clients may observe. They range from linearizability to eventual consistency and guide API and datastore design.
---

# Consistency Models

## 1. Core Concept
A consistency model is a contract for how concurrent and distributed operations appear to clients. Strong models (linearizability, sequential consistency) make systems behave like a single copy; weaker models (causal, eventual, read-your-writes) allow more performance and availability. They solve ambiguous “is this data correct?” questions across replicas.

## 2. Architecture & Data Flow
1. Client issues reads/writes to one or more replicas.
2. Replication protocol propagates updates (sync/async, quorum, primary-backup).
3. Model determines when a write becomes visible and whether stale reads are allowed.
4. Clients may use session guarantees, fencing tokens, or etags to narrow anomalies.
5. Conflict resolution runs when concurrent writes diverge under weak models.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Precise models enable correct application reasoning and testing.
  * Weaker models unlock lower latency and higher availability.
* **Disadvantages/Risks:**
  * Weak models introduce subtle anomalies (lost updates, stale reads, non-monotonic reads).
  * Strong models increase coordination cost and reduce availability under partition.

## 4. Alternatives
Compare **linearizability** (strongest practical single-object model) vs **eventual consistency** (AP-friendly). **Causal consistency** sits in between for many collaborative apps.

## 5. Team Guidelines & Use Cases
**SHOULD** pick the weakest model that still preserves invariants (payments need stronger guarantees than like-counters). **SHOULD NOT** mix ad-hoc caches with a strongly consistent DB without defining freshness rules.
