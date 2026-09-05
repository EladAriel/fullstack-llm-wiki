---
topic: GraphQL
tags: apis, communication, frontend
ai_summary: GraphQL lets clients specify exactly the data graph they need in one request. It reduces overfetching for complex UIs while centralizing a schema.
---

# GraphQL

## 1. Core Concept
GraphQL exposes a typed schema of queries, mutations, and subscriptions. Clients ask for precise field trees. It solves mobile/web overfetching and round-trip chattiness against many REST endpoints.

## 2. Architecture & Data Flow
1. Client sends a query document to the GraphQL endpoint.
2. Server validates against the schema.
3. Resolvers fetch fields, often batching with DataLoader patterns.
4. Response mirrors the query shape.
5. Persisted queries and complexity limits protect the server.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Clients evolve UI data needs without many backend versions.
  * Single endpoint aggregates microservice data carefully.
* **Disadvantages/Risks:**
  * Caching and authorization are harder than simple REST paths.
  * Unbounded queries can create expensive resolver trees.

## 4. Alternatives
**BFF REST aggregators**; **gRPC + gateway** for internal efficiency with client-specific REST.

## 5. Team Guidelines & Use Cases
**SHOULD** use GraphQL when multiple clients need varied shapes of the same graph. **SHOULD NOT** treat GraphQL as a DB query language exposed without authz and cost limits.
