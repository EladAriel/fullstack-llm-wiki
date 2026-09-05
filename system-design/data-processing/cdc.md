---
topic: Change Data Capture (CDC)
tags: data, integration, streaming
ai_summary: CDC streams database row changes into downstream systems in near real time. It powers caches, search indexes, and analytics without dual writes.
---

# Change Data Capture (CDC)

## 1. Core Concept
CDC reads the database transaction log (or triggers) and emits insert/update/delete events. It solves keeping derived systems synchronized without burdening app code with dual writes.

## 2. Architecture & Data Flow
1. Connector tails WAL/binlog with a consistent offset.
2. Changes are published to a stream with schema metadata.
3. Consumers update search, caches, warehouses, or other DBs.
4. Snapshots bootstrap initial state before streaming.
5. Schema changes require compatible evolution handling.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Avoids brittle dual-write application logic.
  * Low-latency propagation from the system of record.
* **Disadvantages/Risks:**
  * Operational coupling to DB log formats and permissions.
  * Consumers must handle out-of-order and tombstones carefully.

## 4. Alternatives
**Transactional outbox** from app writes; **periodic ETL dumps** for non-urgent sync.

## 5. Team Guidelines & Use Cases
**SHOULD** use CDC to feed search/analytics from OLTP. **SHOULD NOT** treat CDC streams as a substitute for well-defined domain events when business meaning differs from row diffs.
