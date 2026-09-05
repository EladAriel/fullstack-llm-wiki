---
topic: Load Balancing
tags: networking, scaling, traffic
ai_summary: Load balancers distribute traffic across multiple backends to improve capacity and availability. Algorithms and health checks determine fairness and failover behavior.
---

# Load Balancing

## 1. Core Concept
A load balancer (LB) fronts a pool of instances and selects a healthy target for each connection or request. It solves uneven load, single-instance limits, and seamless replacement of backends.

## 2. Architecture & Data Flow
1. Client connects to the LB VIP/hostname.
2. LB terminates or forwards L4/L7 traffic.
3. Selection algorithm chooses a backend (round-robin, least-conn, hash, weighted).
4. Health checks remove failing targets.
5. Optional sticky sessions, TLS termination, retries, and circuit breaking apply.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Enables horizontal scale and rolling deploys.
  * Central place for TLS, health checks, and basic traffic policy.
* **Disadvantages/Risks:**
  * LB can become a bottleneck or SPOF if not itself redundant.
  * Sticky sessions hinder perfect scale-out and failover.

## 4. Alternatives
**Client-side load balancing** (service mesh / gRPC balancers) and **DNS round-robin** (simpler but weaker health awareness).

## 5. Team Guidelines & Use Cases
**SHOULD** put redundant LBs in front of stateless services with active health checks. **SHOULD NOT** use session stickiness unless state cannot be externalized.
