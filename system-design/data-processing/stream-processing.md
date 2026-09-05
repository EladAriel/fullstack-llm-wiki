---
topic: Stream Processing
tags: processing, streaming, realtime
ai_summary: Stream processing continuously transforms unbounded event streams with low latency. It powers real-time analytics, fraud checks, and incremental pipelines.
---

# Stream Processing

## 1. Core Concept
Stream processors ingest events as they arrive, maintain state, and emit derived streams or actions. They solve freshness requirements that batch windows cannot meet.

## 2. Architecture & Data Flow
1. Events land on a log/topic.
2. Stream job consumes with offsets and keyed state stores.
3. Windowing/aggregations update continuously.
4. Results write to sinks (DB, indexes, alerts).
5. Checkpointing enables recovery with defined processing guarantees.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Seconds-level freshness for analytics and reactions.
  * Smooth resource usage vs giant batch peaks.
* **Disadvantages/Risks:**
  * State, late data, and exactly-once sinks are complex.
  * Harder operational debugging than batch jobs.

## 4. Alternatives
**Micro-batch**; **request-time computation** for rare queries; **CDC + materialized views**.

## 5. Team Guidelines & Use Cases
**SHOULD** stream when product value depends on near-real-time signals. **SHOULD NOT** build streaming for tiny volumes where a cron job meets the SLA with less complexity.
