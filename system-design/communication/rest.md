---
topic: REST APIs
tags: apis, communication, http
ai_summary: REST uses HTTP resources, methods, and status codes for synchronous service interfaces. It is the default public API style due to simplicity and broad tooling.
---

# REST APIs

## 1. Core Concept
RESTful APIs expose resources via URLs and manipulate them with HTTP verbs, leveraging status codes and caching headers. They solve language-agnostic service communication with ubiquitous HTTP infrastructure.

## 2. Architecture & Data Flow
1. Client sends HTTP request to a resource URL.
2. Gateway/service authenticates and authorizes.
3. Handler loads/updates domain state.
4. Response returns JSON/encoded body with cache validators.
5. Idempotent methods and pagination conventions shape large collections.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Simple, cacheable, universally supported.
  * Easy to debug with standard HTTP tools.
* **Disadvantages/Risks:**
  * Chatty multi-resource pages without aggregation.
  * Weak formal contracts unless OpenAPI is enforced.

## 4. Alternatives
**gRPC** for efficient internal RPC; **GraphQL** for flexible client-driven queries.

## 5. Team Guidelines & Use Cases
**SHOULD** use REST for public HTTP APIs and simple CRUD services. **SHOULD NOT** invent non-HTTP semantics that ignore verbs, status codes, and idempotency norms.
