---
topic: CQRS (Command Query Responsibility Segregation)
tags: architecture, patterns, scalability
ai_summary: CQRS separates write (command) models from read (query) models so each can scale and optimize independently. It fits domains with asymmetric read/write complexity.
---

# CQRS (Command Query Responsibility Segregation)

## 1. Core Concept
CQRS uses different models/paths for updating state versus reading it. Writes enforce invariants on a transactional model; reads use denormalized projections. It solves conflicting optimization needs between complex writes and high-volume queries.

## 2. Architecture & Data Flow
1. Client sends commands to the write side.
2. Write model validates and persists.
3. Events/updates propagate to read projections asynchronously.
4. Queries hit read DB/cache shaped for UI/API needs.
5. Clients tolerate brief read lag or use read-your-writes techniques.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Independent scaling and schema design for reads vs writes.
  * Clearer command semantics and auditability when paired with events.
* **Disadvantages/Risks:**
  * More moving parts and eventual consistency complexity.
  * Easy to over-engineer simple CRUD domains.

## 4. Alternatives
**Single model CRUD** with indexes/caches; **event sourcing** (often paired with CQRS but not required).

## 5. Team Guidelines & Use Cases
**SHOULD** consider CQRS when read models diverge heavily from write invariants. **SHOULD NOT** apply CQRS everywhere as a default microservice template.
