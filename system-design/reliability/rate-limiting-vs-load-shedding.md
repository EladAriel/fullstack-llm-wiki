---
topic: Load Shedding
tags: reliability, traffic, scaling
ai_summary: Load shedding deliberately drops or rejects work when a system is overloaded to protect critical capacity. Unlike client quotas, it reacts to server saturation.
---

# Load Shedding

## 1. Core Concept
Load shedding is admission control based on server health (CPU, queue time, hedged overload) rather than only per-client quotas. It solves survival under unexpected traffic or dependency slowdowns.

## 2. Architecture & Data Flow
1. Monitor saturation signals (queue latency, thread pool utilization).
2. When thresholds trip, reject low-priority requests first.
3. Return fast failures (503) with retry hints.
4. Preserve capacity for health checks and critical endpoints.
5. Combine with autoscaling, but shed during scale-up delay.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Prevents total collapse and multi-hour recovery.
  * Keeps critical user journeys alive under stress.
* **Disadvantages/Risks:**
  * Users see errors; fairness policies can be contentious.
  * Bad signals cause premature shedding.

## 4. Alternatives
**Rate limiting** (per-client fairness); **autoscaling alone** (too slow for sudden spikes).

## 5. Team Guidelines & Use Cases
**SHOULD** implement server-side shedding for public tiers and expensive endpoints. **SHOULD NOT** queue unboundedly hoping more capacity appears.
