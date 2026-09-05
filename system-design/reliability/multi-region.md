---
topic: Multi-Region Architecture
tags: scaling, availability, networking
ai_summary: Multi-region architectures deploy services in geographically separate regions for latency and disaster resilience. Data replication topology determines consistency and failover.
---

# Multi-Region Architecture

## 1. Core Concept
Running in multiple cloud regions protects against regional outages and brings compute closer to users. The hard problem is data: how to replicate, conflict, and fail over without corrupting state.

## 2. Architecture & Data Flow
1. Deploy stateless services in two+ regions behind geo-DNS/anycast.
2. Choose data mode: active-passive (primary region writes), active-active (multi-writer), or regional pin.
3. Replicate data asynchronously or via consensus globally (rare/expensive).
4. Route users to nearest healthy region.
5. Practice region evacuation runbooks.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Higher availability and better global latency.
  * Regulatory data residency options with regional pinning.
* **Disadvantages/Risks:**
  * Significant cost and operational complexity.
  * Cross-region consistency and conflict resolution are hard.

## 4. Alternatives
**Multi-AZ single region** (covers most failure domains cheaper); **static DR cold standby** for lower tiers.

## 5. Team Guidelines & Use Cases
**SHOULD** go multi-region when business RTO/RPO or latency truly requires it. **SHOULD NOT** invent active-active multi-writer data before exhausting multi-AZ and read-local designs.
