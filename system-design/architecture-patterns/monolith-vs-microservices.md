---
topic: Monolith vs Microservices
tags: architecture, microservices, organization
ai_summary: A monolith deploys as one unit; microservices split independently deployable services by domain. The choice hinges on team scale, deployment independence, and operational maturity.
---

# Monolith vs Microservices

## 1. Core Concept
Monoliths colocated modules share a process/DB boundary. Microservices split bounded contexts into separately deployed services communicating over the network. The problem is balancing delivery speed, complexity, and scaling independence.

## 2. Architecture & Data Flow
1. Monolith: single build artifact, in-process calls, often one primary DB.
2. Microservices: service-per-capability, own data where possible, sync/async remote calls.
3. Gateways and meshes handle cross-cutting traffic policy.
4. Distributed observability becomes mandatory for microservices.
5. Evolution path often starts modular monolith → extract services at pain points.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Monolith: simpler tracing, transactions, and local refactors.
  * Microservices: independent scale/deploy and clearer team ownership boundaries.
* **Disadvantages/Risks:**
  * Monolith: can become a deployment bottleneck and tangled dependency ball.
  * Microservices: distributed failure modes, ops overhead, and data consistency challenges.

## 4. Alternatives
**Modular monolith** (strong module boundaries, one deploy); **mini-services** / service-oriented hybrids.

## 5. Team Guidelines & Use Cases
**SHOULD** default to a modular monolith until team/scale pressures justify extraction. **SHOULD NOT** split microservices by technical layers alone (e.g., “the DAO service”).
