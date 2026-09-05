---
topic: Backend for Frontend (BFF)
tags: architecture, apis, frontend
ai_summary: A BFF is an API layer tailored to a specific client experience (web, mobile, partner). It aggregates and shapes backend data to reduce chatty UI coupling.
---

# Backend for Frontend (BFF)

## 1. Core Concept
Instead of one generic API for all clients, each client type gets a dedicated backend that speaks its UI’s language. It solves overfetching, awkward payloads, and coupling many UIs to internal microservices.

## 2. Architecture & Data Flow
1. Client calls its BFF only.
2. BFF authenticates the user session/device context.
3. BFF fans out to internal services and aggregates/shapes responses.
4. Returns a screen-oriented payload.
5. Ownership usually sits with the client team.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Faster UI iteration without breaking other clients.
  * Hides microservice sprawl from frontends.
* **Disadvantages/Risks:**
  * Duplication across BFFs if not carefully shared.
  * Risk of BFFs becoming mini-monoliths of business rules.

## 4. Alternatives
**GraphQL gateway** as a flexible general API; **single public API + client-side aggregation** (more chattiness).

## 5. Team Guidelines & Use Cases
**SHOULD** use BFFs when web and mobile needs diverge strongly. **SHOULD NOT** reimplement core domain invariants in every BFF—call domain services.
