---
topic: Rate Limiting
tags: networking, reliability, traffic
ai_summary: Rate limiting caps how many requests a client can make in a time window to protect shared resources. Algorithms include token bucket, leaky bucket, and sliding windows.
---

# Rate Limiting

## 1. Core Concept
Rate limiting enforces quotas per key (IP, user, API key, tenant). It solves noisy-neighbor, abuse, and overload problems by shedding excess traffic early.

## 2. Architecture & Data Flow
1. Identify a partition key for the client/tenant.
2. On each request, consult a counter/bucket store (local or Redis).
3. Algorithm decides allow vs reject (token bucket, fixed/sliding window, concurrency limit).
4. Return 429 with retry-after when limited.
5. Optionally apply different limits per endpoint and tier.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Protects downstream databases and third-party quotas.
  * Creates fair multi-tenant behavior.
* **Disadvantages/Risks:**
  * Distributed counters add latency and eventual inaccuracy.
  * Poor key design can lock out NAT-shared users or miss abusive actors.

## 4. Alternatives
**Load shedding** based on server saturation; **admission control / concurrency limits** that ignore wall-clock rate and focus on in-flight work.

## 5. Team Guidelines & Use Cases
**SHOULD** rate-limit public and expensive endpoints with clear client feedback. **SHOULD NOT** use only global process-local limits in multi-instance deployments without a shared store or coordinated policy.
