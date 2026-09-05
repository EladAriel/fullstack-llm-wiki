---
topic: Reverse Proxy
tags: networking, edge, security
ai_summary: A reverse proxy accepts client requests and forwards them to internal servers, adding TLS, caching, routing, and shielding. It is the usual edge entry to application tiers.
---

# Reverse Proxy

## 1. Core Concept
A reverse proxy sits in front of origin servers on behalf of clients. Unlike a forward proxy (client-chosen), clients target the proxy’s public endpoint. It solves TLS termination, request routing, compression, and hiding internal topology.

## 2. Architecture & Data Flow
1. Client sends HTTPS to the proxy.
2. Proxy terminates TLS, applies WAF/auth/rate limits as configured.
3. Routes by path/host to upstream services.
4. May cache responses or buffer slow clients.
5. Returns the upstream response with added headers (request IDs, cache status).

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Consolidates cross-cutting edge concerns.
  * Simplifies certificate management and origin protection.
* **Disadvantages/Risks:**
  * Misrouting or buffer settings can amplify outages.
  * Extra hop adds latency if not co-located carefully.

## 4. Alternatives
**API gateway** (API-product focused policies) and **service mesh sidecars** (east-west traffic policy instead of north-south edge).

## 5. Team Guidelines & Use Cases
**SHOULD** terminate public TLS at a reverse proxy/CDN tier. **SHOULD NOT** expose app containers directly to the internet without an edge proxy in normal deployments.
