---
topic: Write-Ahead Logging (WAL)
tags: database, durability, storage
ai_summary: A write-ahead log durably records changes before applying them to primary storage structures. It enables crash recovery and replication feeds.
---

# Write-Ahead Logging (WAL)

## 1. Core Concept
WAL (or redo log) appends intended mutations to sequential storage before updating pages/files. After a crash, redo brings data files to a consistent committed state. It solves durability and powers replication.

## 2. Architecture & Data Flow
1. Transaction produces log records.
2. On commit, log is fsynced (per durability settings).
3. Dirty pages flush asynchronously.
4. Recovery replays log from last checkpoint.
5. Replicas may stream the same log.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Strong durability with sequential write performance.
  * Enables point-in-time recovery and replication.
* **Disadvantages/Risks:**
  * Sync commits add latency.
  * Log disk saturation stalls all writes.

## 4. Alternatives
**Async durability** (risk data loss); **event sourcing** as an application-level log-first design.

## 5. Team Guidelines & Use Cases
**SHOULD** keep WAL disks fast and monitored for production databases. **SHOULD NOT** disable fsync in production to “gain performance” without accepting data-loss risk.
