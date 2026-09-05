---
topic: Scalability (Horizontal vs Vertical)
tags: scaling, capacity, architecture
ai_summary: Scalability is the ability of a system to handle growth in load by adding resources. Horizontal scaling adds more machines; vertical scaling adds more power to existing machines.
---

# Scalability (Horizontal vs Vertical)

## 1. Core Concept
Scalability describes how a system grows as traffic, data, or compute demand increases. Vertical scaling (scale-up) upgrades CPU, RAM, or disk on one node. Horizontal scaling (scale-out) adds more nodes behind load distribution. The engineering problem is sustaining target latency and availability as usage grows without unbounded cost or complexity.

## 2. Architecture & Data Flow
1. Measure bottlenecks (CPU, memory, I/O, network, locks).
2. For vertical scale, replace or resize the instance and migrate traffic with downtime or blue/green.
3. For horizontal scale, put a load balancer or partition key in front of N identical (or sharded) workers.
4. Ensure the app is stateless or externalize session/state so any node can serve a request.
5. Autoscale based on metrics (CPU, queue depth, RPS) with cool-downs to avoid thrash.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Horizontal scaling improves fault isolation and can grow nearly linearly for stateless workloads.
  * Vertical scaling is simple operationally for early-stage systems and single-writer databases.
* **Disadvantages/Risks:**
  * Vertical scaling hits hardware ceilings and creates larger blast radius on failure.
  * Horizontal scaling requires distributed coordination, data partitioning, and often redesign of sticky state.

## 4. Alternatives
Compare with **capacity reservation / overprovisioning** (pay for headroom instead of elastic scale) and **workload shedding / rate limiting** (protect the system by rejecting excess instead of adding capacity).

## 5. Team Guidelines & Use Cases
**SHOULD** prefer horizontal scale for stateless APIs and workers once a single box is near its ceiling. **SHOULD NOT** assume every database or legacy service can scale out without sharding or read replicas—validate state and write paths first.
