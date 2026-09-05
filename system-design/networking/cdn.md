---
topic: Content Delivery Network (CDN)
tags: networking, caching, latency
ai_summary: A CDN caches and serves content from edge locations close to users to cut latency and origin load. It is primary for static assets and increasingly for dynamic edge logic.
---

# Content Delivery Network (CDN)

## 1. Core Concept
A CDN is a geographically distributed cache/proxy network. Users hit a nearby PoP; cache hits never reach origin. It solves long-haul latency, origin overload, and some DDoS absorption for cacheable content.

## 2. Architecture & Data Flow
1. DNS/anycast sends the client to a nearby PoP.
2. PoP checks cache keyed by URL/headers.
3. On miss, PoP fetches from origin (or mid-tier), stores per TTLs/cache-control.
4. Invalidation/purge APIs remove stale objects after deploys.
5. Optional edge compute runs lightweight request logic.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Dramatically lowers TTFB for static and semi-static content.
  * Shields origin from traffic spikes.
* **Disadvantages/Risks:**
  * Cache invalidation complexity and stale content risk.
  * Dynamic personalized content often bypasses or fragments the cache.

## 4. Alternatives
**App-level caching** (Redis) for personalized data; **multi-region active-active origins** for uncacheable dynamic APIs.

## 5. Team Guidelines & Use Cases
**SHOULD** put fingerprinted static assets on a CDN with long TTL. **SHOULD NOT** cache authenticated private responses at shared edges without careful cache-key and security design.
