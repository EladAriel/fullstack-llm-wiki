---
topic: Event-Driven Architecture
tags: architecture, event-driven, messaging
ai_summary: Event-driven architecture coordinates services through events representing state changes rather than direct synchronous calls. It improves decoupling and scalability of workflows.
---

# Event-Driven Architecture

## 1. Core Concept
EDA structures systems so components communicate primarily via events (“order placed”) instead of commanding each other synchronously. It solves brittle point-to-point coupling and enables asynchronous reactions at scale.

## 2. Architecture & Data Flow
1. Service commits state change and emits an event (ideally via outbox).
2. Broker distributes the event.
3. Consumers update their own state, trigger processes, or emit further events.
4. Choreography lets each service react; orchestration uses a workflow leader.
5. Observability requires correlation IDs across the event chain.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Loose coupling and independent deployability.
  * Natural fit for audit logs and real-time reactions.
* **Disadvantages/Risks:**
  * Debugging distributed flows is harder.
  * Eventual consistency requires careful UX and idempotency.

## 4. Alternatives
**Request-driven microservices** (sync APIs); **modular monolith** with in-process domain events when distribution is unnecessary.

## 5. Team Guidelines & Use Cases
**SHOULD** adopt EDA for cross-team workflows that can tolerate async completion. **SHOULD NOT** event-wash simple CRUD apps into unreadable webs of topics.
