---
topic: ACID vs BASE
tags: database, consistency, transactions
ai_summary: ACID emphasizes transactional correctness on a single system of record; BASE emphasizes availability and soft state with eventual consistency. Choosing between them shapes data integrity vs scale.
---

# ACID vs BASE

## 1. Core Concept
ACID (Atomicity, Consistency, Isolation, Durability) describes traditional transactional guarantees. BASE (Basically Available, Soft state, Eventual consistency) describes designs that prioritize availability and partition tolerance with deferred reconciliation. The problem is matching integrity needs to distribution and scale constraints.

## 2. Architecture & Data Flow
1. ACID path: begin transaction, apply multiple row changes under a concurrency control protocol, commit/abort atomically.
2. BASE path: accept writes quickly, propagate asynchronously, resolve conflicts with application logic or CRDTs.
3. Hybrid systems use local ACID transactions plus eventual cross-service propagation (outbox, sagas).

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * ACID simplifies correctness for financial and inventory invariants.
  * BASE enables global scale and high write availability.
* **Disadvantages/Risks:**
  * Distributed ACID is expensive and often unavailable across services.
  * BASE shifts complexity into conflict handling and user-visible lag.

## 4. Alternatives
**Sagas** and **transactional outbox** provide cross-service workflows without distributed 2PC. **CQRS** separates strongly consistent write models from eventually consistent read models.

## 5. Team Guidelines & Use Cases
**SHOULD** keep hard money/inventory invariants inside one ACID boundary when possible. **SHOULD NOT** force distributed 2PC across microservices for convenience—prefer explicit eventual workflows.
