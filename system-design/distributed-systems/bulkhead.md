---
topic: Bulkhead Pattern
tags: reliability, isolation, resilience
ai_summary: Bulkheads isolate resources into compartments so failure in one area cannot consume all capacity. They limit blast radius across tenants, dependencies, or workloads.
---

# Bulkhead Pattern

## 1. Core Concept
Named after ship compartments, bulkheads partition threads, connections, queues, or clusters. They solve noisy-neighbor and shared-fate problems where one slow dependency starves everything.

## 2. Architecture & Data Flow
1. Identify failure domains (per dependency, tenant, or endpoint group).
2. Assign dedicated pools/limits (thread pools, connection pools, pod counts).
3. Reject excess in one bulkhead without blocking others.
4. Monitor utilization per compartment.
5. Optionally isolate at infrastructure level (separate clusters/accounts).

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Contains resource exhaustion blasts.
  * Preserves critical paths when noncritical paths overload.
* **Disadvantages/Risks:**
  * Idle capacity in one bulkhead cannot always help another (lower packing efficiency).
  * More pools mean more tuning and ops complexity.

## 4. Alternatives
**Global concurrency limits** (simpler, less isolation); **separate microservices/clusters** for hard isolation.

## 5. Team Guidelines & Use Cases
**SHOULD** isolate thread/connection pools per critical dependency. **SHOULD NOT** share one unbounded executor across all outbound I/O.
