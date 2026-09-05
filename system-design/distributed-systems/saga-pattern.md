---
topic: Saga Pattern
tags: transactions, microservices, event-driven
ai_summary: Sagas manage multi-step business transactions with local commits plus compensating actions on failure. They replace distributed 2PC in microservice architectures.
---

# Saga Pattern

## 1. Core Concept
A saga breaks a long-running business process into a sequence of local transactions. If a step fails, previously completed steps run compensations. It solves cross-service workflows without locking all resources in a distributed transaction.

## 2. Architecture & Data Flow
1. Orchestrator (or choreography) starts step 1 local TX and emits success.
2. Each subsequent service performs its local TX.
3. On failure at step k, compensations for steps k-1…1 execute.
4. State machine tracks progress and retries.
5. Idempotent handlers make retries safe.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * High availability vs 2PC; no global locks.
  * Fits natural business processes with explicit undo paths.
* **Disadvantages/Risks:**
  * Compensations are hard (and sometimes impossible) to design perfectly.
  * Intermediate states are visible to users (eventual consistency).

## 4. Alternatives
**2PC/TCC** for rare strong atomic needs; **single-service transaction** by consolidating the write boundary.

## 5. Team Guidelines & Use Cases
**SHOULD** use sagas for cross-service orders, provisioning, and multi-step bookings. **SHOULD NOT** pretend compensations equal true ACID rollback for money movement without careful ledger design.
