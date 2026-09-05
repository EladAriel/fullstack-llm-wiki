---
topic: Strangler Fig Pattern
tags: architecture, migration, legacy
ai_summary: The strangler fig pattern incrementally replaces a legacy system by routing slices of traffic to new implementations. It reduces big-bang migration risk.
---

# Strangler Fig Pattern

## 1. Core Concept
Named after vines that gradually envelop a tree, this pattern places a facade in front of legacy and peels off functionality piece by piece. It solves risky all-at-once rewrites.

## 2. Architecture & Data Flow
1. Put a routing facade/proxy in front of the legacy system.
2. Identify a bounded feature to reimplement.
3. Route that slice to the new service; keep the rest on legacy.
4. Sync data as needed during coexistence.
5. Repeat until legacy can be decommissioned.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Continuous delivery of value with rollback per slice.
  * Lower risk than a full rewrite cutover.
* **Disadvantages/Risks:**
  * Prolonged dual-running increases cost and complexity.
  * Data synchronization during coexistence can be thorny.

## 4. Alternatives
**Big-bang rewrite** (rarely justified); **branch by abstraction** inside a monolith without an edge facade.

## 5. Team Guidelines & Use Cases
**SHOULD** strangler-migrate critical legacy when you can carve clear seams. **SHOULD NOT** run forever in dual mode without a decommission plan.
