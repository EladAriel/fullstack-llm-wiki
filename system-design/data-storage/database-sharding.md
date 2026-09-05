---
topic: Database Sharding
tags: database, scaling, partitioning
ai_summary: Sharding partitions data across multiple database instances by a shard key to scale writes and storage. It introduces cross-shard complexity for queries and transactions.
---

# Database Sharding

## 1. Core Concept
Sharding (horizontal partitioning) splits rows into subsets stored on different nodes. It solves single-primary write and storage ceilings when vertical scale and read replicas are insufficient.

## 2. Architecture & Data Flow
1. Choose a shard key with even distribution and locality for common queries.
2. Router or client embeds key → shard mapping (range, hash, directory).
3. Single-shard queries go to one node; scatter-gather handles cross-shard reads.
4. Resharding migrates ranges/buckets as data grows.
5. Cross-shard transactions use sagas/2PC or are avoided by design.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Scales write throughput and dataset size beyond one machine.
  * Fault isolation: one shard’s outage need not take down all data.
* **Disadvantages/Risks:**
  * Cross-shard joins and transactions become hard.
  * Hot keys/shards and resharding are operationally painful.

## 4. Alternatives
**Vertical partitioning** (split tables/services by domain); **distributed SQL** that manages shards under a relational API.

## 5. Team Guidelines & Use Cases
**SHOULD** shard only after proving a single primary (plus replicas) cannot meet write/storage needs. **SHOULD NOT** pick high-cardinality random keys that destroy locality for the main query paths.
