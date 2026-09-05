---
topic: Relational (SQL) Databases
tags: database, storage, transactions
ai_summary: Relational databases store structured data in tables with schemas, SQL queries, and ACID transactions. They are the default system of record for strong invariants and complex queries.
---

# Relational (SQL) Databases

## 1. Core Concept
SQL databases organize data into normalized tables with declared schemas, constraints, and joins. They solve consistent multi-row updates and ad-hoc relational querying under a transactional model.

## 2. Architecture & Data Flow
1. Client begins a transaction and issues SQL.
2. Query planner uses indexes/statistics to access rows.
3. Concurrency control (locking/MVCC) isolates concurrent transactions.
4. WAL/redo ensures durability on commit.
5. Replicas may serve reads; primary typically handles writes.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Strong consistency and mature tooling for integrity constraints.
  * Expressive queries and joins without denormalizing everything upfront.
* **Disadvantages/Risks:**
  * Horizontal write scaling is hard without sharding.
  * Rigid schemas and join-heavy designs can become bottlenecks at extreme scale.

## 4. Alternatives
**NoSQL document/KV stores** for flexible schemas and simpler scale-out; **NewSQL / distributed SQL** for relational semantics with sharding.

## 5. Team Guidelines & Use Cases
**SHOULD** use relational DBs for core business entities with rich relationships and invariants. **SHOULD NOT** use a single monolithic SQL database as an unbounded event dump or analytics warehouse.
