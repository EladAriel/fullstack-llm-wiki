---
topic: Failover Strategies
tags: reliability, availability, operations
ai_summary: Failover switches traffic from a failed component to a standby or peer. Strategies range from automatic multi-AZ failover to manual disaster recovery.
---

# Failover Strategies

## 1. Core Concept
Failover is the controlled promotion/redirection when a primary path fails. It solves continuity when instances, AZs, or regions become unavailable.

## 2. Architecture & Data Flow
1. Detect failure (health checks, quorum loss, error budgets).
2. Choose target (standby replica, alternate region).
3. Promote/reconfigure data plane (DNS, LB, leader election).
4. Fence the old primary to prevent split-brain.
5. Verify, then run failback when safe.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Reduces MTTR versus manual rebuilds.
  * Supports tiered RPO/RTO objectives.
* **Disadvantages/Risks:**
  * Automated failover can amplify partial network faults.
  * Unused standbys still cost money (active-passive).

## 4. Alternatives
**Active-active multi-primary** (no single failover, more conflict handling); **stateless rebuild from scratch** for ephemeral workers.

## 5. Team Guidelines & Use Cases
**SHOULD** regularly game-day test failover for datastores and critical paths. **SHOULD NOT** assume DNS-only failover meets aggressive RTO without measuring TTL and client behavior.
