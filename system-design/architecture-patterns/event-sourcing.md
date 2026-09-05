---
topic: Event Sourcing
tags: architecture, events, storage
ai_summary: Event sourcing stores state as an append-only sequence of domain events and rebuilds current state by replaying them. It provides a complete audit log and temporal queries.
---

# Event Sourcing

## 1. Core Concept
Instead of persisting only latest row state, event sourcing appends immutable events (“ItemAdded”). Current state is a fold over the stream (with snapshots). It solves auditability, debugging, and reconstructing historical state.

## 2. Architecture & Data Flow
1. Command handler validates against current aggregate state.
2. New events append to the event store.
3. Aggregates rehydrate via snapshot + newer events.
4. Projections subscribe to build read models.
5. Upcasters evolve old event schemas carefully.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Full audit trail and time-travel debugging.
  * Natural integration with event-driven consumers.
* **Disadvantages/Risks:**
  * Operational complexity: replay, schema evolution, GDPR erasure.
  * Not intuitive for teams used to mutable CRUD tables.

## 4. Alternatives
**State + change data capture (CDC)** for audit-ish streams; **append-only audit tables** without making events the primary store.

## 5. Team Guidelines & Use Cases
**SHOULD** use event sourcing for domains that need rich history and complex state transitions. **SHOULD NOT** event-source every entity; prefer selective aggregates.
