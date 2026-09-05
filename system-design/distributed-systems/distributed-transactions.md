---
topic: Distributed Transactions (2PC)
tags: transactions, distributed-systems, consistency
ai_summary: Two-phase commit coordinates atomic commits across multiple participants. It provides all-or-nothing semantics at the cost of blocking and availability risks.
---

# Distributed Transactions (2PC)

## 1. Core Concept
Distributed transactions make multiple resources commit or abort together. Two-phase commit (2PC) uses a prepare phase then a commit phase driven by a coordinator. It solves cross-database atomicity when a single local transaction is impossible.

## 2. Architecture & Data Flow
1. Coordinator sends PREPARE to participants.
2. Each participant votes YES (durably prepared) or NO.
3. If all YES, coordinator sends COMMIT; else ABORT.
4. Participants acknowledge final outcome.
5. On coordinator crash, prepared participants may block until recovery.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Strong atomicity across heterogeneous resources.
  * Familiar ACID-like outcome for multi-resource updates.
* **Disadvantages/Risks:**
  * Blocking and poor availability under coordinator/participant failures.
  * High latency from multiple round trips and locks held while prepared.

## 4. Alternatives
**Sagas** (compensating transactions); **transactional outbox + async messaging** for eventual consistency across services.

## 5. Team Guidelines & Use Cases
**SHOULD** avoid 2PC across microservices except rare tightly controlled cases. **SHOULD NOT** hold prepared locks across user-interactive network calls.
