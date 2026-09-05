---
topic: Health Checks and Heartbeats
tags: reliability, operations, networking
ai_summary: Health checks and heartbeats detect failed or stuck processes so traffic can be routed away. Liveness vs readiness probes distinguish restart needs from temporary unavailability.
---

# Health Checks and Heartbeats

## 1. Core Concept
Health checks periodically verify a process can serve; heartbeats signal liveness to peers/coordinators. They solve silent failures where a process is up but not useful.

## 2. Architecture & Data Flow
1. Platform probes /healthz (liveness) and /ready (readiness).
2. Failed liveness restarts the process.
3. Failed readiness removes it from load balancers.
4. Distributed systems send heartbeats to leases/failure detectors.
5. Alerting fires when check failure rates burn error budgets.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Automates failover and self-healing.
  * Prevents routing to starting/broken instances.
* **Disadvantages/Risks:**
  * Overly deep checks can cascade failures (dependencies down → all pods unready).
  * Aggressive timeouts cause flapping.

## 4. Alternatives
**Passive health** via error rates at the LB; **synthetic monitoring** from outside the cluster.

## 5. Team Guidelines & Use Cases
**SHOULD** separate liveness (process sane) from readiness (able to serve). **SHOULD NOT** make liveness depend on downstream dependencies.
