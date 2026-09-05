---
topic: Latency and Throughput
tags: performance, latency, throughput
ai_summary: Latency is the time to complete one request; throughput is how many requests complete per unit time. Systems must balance per-request speed against overall capacity.
---

# Latency and Throughput

## 1. Core Concept
Latency is end-to-end delay (often p50/p95/p99). Throughput is completed work per second (RPS, QPS, messages/sec). The engineering problem is meeting interactive responsiveness while maximizing useful work under resource limits.

## 2. Architecture & Data Flow
1. Instrument request timelines (queue wait, compute, I/O, network).
2. Reduce latency with caching, connection reuse, indexes, and locality.
3. Increase throughput with concurrency, batching, pipelining, and parallelism.
4. Watch queueing: Little’s Law links concurrency, latency, and throughput.
5. Load-test to find the cliff where latency explodes as throughput saturates.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Separating the two metrics prevents optimizing averages while ignoring tail latency.
  * Batching and async pipelines can raise throughput without proportional hardware.
* **Disadvantages/Risks:**
  * Aggressive batching or queueing increases latency.
  * Optimizing only p50 can leave p99 failures that dominate user experience.

## 4. Alternatives
Compare **synchronous request/response** (low latency target) vs **async job processing** (high throughput, higher completion latency).

## 5. Team Guidelines & Use Cases
**SHOULD** publish latency percentiles and throughput budgets for critical APIs. **SHOULD NOT** trade unbounded queues for “higher throughput” without backpressure and SLOs on wait time.
