---
topic: OLTP vs OLAP
tags: database, analytics, storage
ai_summary: OLTP systems serve transactional operational workloads; OLAP systems serve analytical scans and aggregations. Separating them protects production latency while enabling BI.
---

# OLTP vs OLAP

## 1. Core Concept
OLTP (Online Transaction Processing) optimizes many small reads/writes with indexes and ACID. OLAP (Online Analytical Processing) optimizes large scans, columnar storage, and aggregations. The problem is that analytics queries can destroy OLTP latency if colocated.

## 2. Architecture & Data Flow
1. OLTP DB handles application transactions.
2. Changes stream via CDC/ETL into a warehouse/lakehouse.
3. OLAP engine stores columnar, partitioned data.
4. BI tools query replicas/warehouses, not the primary OLTP node.
5. SLAs differ: OLTP is latency-sensitive; OLAP is throughput/scan-sensitive.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Isolates analytical load from user-facing transactions.
  * Each system can use the optimal storage engine.
* **Disadvantages/Risks:**
  * Data pipelines introduce lag and operational surface.
  * Two models of the truth can drift without governance.

## 4. Alternatives
**HTAP** databases attempting both; **read replicas** as a lightweight but limited analytics offload.

## 5. Team Guidelines & Use Cases
**SHOULD** offload heavy reporting from primary OLTP early. **SHOULD NOT** run unbounded table scans on production primaries for dashboards.
