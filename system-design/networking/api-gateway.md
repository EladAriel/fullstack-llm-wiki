---
topic: API Gateway
tags: networking, apis, microservices
ai_summary: An API gateway is a single entry point that routes and polices client API calls to backend services. It centralizes auth, rate limits, and request aggregation for external APIs.
---

# API Gateway

## 1. Core Concept
An API gateway fronts one or more backend services for external (and sometimes internal) clients. It solves the problem of duplicating auth, routing, transformation, and monetization concerns across every microservice.

## 2. Architecture & Data Flow
1. Client calls gateway endpoint.
2. Gateway authenticates/authorizes, applies rate limits and schemas.
3. Routes to the owning service(s); may aggregate BFF-style fan-out.
4. Transforms protocols/payloads if needed.
5. Emits metrics/logs/traces for the external API surface.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Consistent edge policy for a public API program.
  * Hides internal service topology and versions.
* **Disadvantages/Risks:**
  * Risk of a bloated “god gateway” with business logic.
  * Extra hop and operational dependency for all traffic.

## 4. Alternatives
**Reverse proxy + service mesh** for simpler routing; **Backend for Frontend (BFF)** per client type instead of one universal gateway aggregator.

## 5. Team Guidelines & Use Cases
**SHOULD** keep gateways focused on cross-cutting API concerns. **SHOULD NOT** implement core domain business rules in the gateway.
