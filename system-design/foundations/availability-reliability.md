---
topic: Availability and Reliability
tags: availability, reliability, sre
ai_summary: Availability measures the fraction of time a system is usable; reliability measures correct continuous operation over time. Both drive redundancy, failover, and error-budget design.
---

# Availability and Reliability

## 1. Core Concept
Availability is uptime from the client’s perspective (successful requests / total requests over a window). Reliability is the probability the system performs its required function without failure for a period. The problem they solve is designing for failure so users still get correct service within agreed SLOs.

## 2. Architecture & Data Flow
1. Define SLIs (latency, error rate, freshness) and SLOs.
2. Remove single points of failure with redundancy (multi-AZ, replicas).
3. Detect failure via health checks and route around bad nodes.
4. Fail over with controlled promotion (leader election, DNS, LB).
5. Recover with backups, replays, and runbooks; track error budget burn.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Explicit SLOs turn vague “always up” goals into engineering trade-offs.
  * Redundancy and automated failover reduce mean time to recovery (MTTR).
* **Disadvantages/Risks:**
  * Higher availability targets grow cost and operational complexity nonlinearly.
  * Over-redundancy can hide bugs until rare correlated failures (region outage, bad deploy).

## 4. Alternatives
Contrast with **disaster recovery (DR)** focus (RPO/RTO for rare catastrophes) and **graceful degradation** (serve partial features instead of hard availability of everything).

## 5. Team Guidelines & Use Cases
**SHOULD** set SLOs per critical user journey and design failover for that budget. **SHOULD NOT** chase five-nines for internal tools where cost exceeds impact.
