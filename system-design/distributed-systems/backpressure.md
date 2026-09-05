---
topic: Backpressure
tags: reliability, streaming, traffic
ai_summary: Backpressure signals upstream producers to slow down when consumers cannot keep up. It prevents unbounded queues and memory exhaustion.
---

# Backpressure

## 1. Core Concept
Backpressure is flow control from a busy consumer toward producers. It solves the mismatch between produce rate and process rate that otherwise causes OOM or multi-minute lag.

## 2. Architecture & Data Flow
1. Consumer monitors queue depth, lag, or in-flight limits.
2. When saturated, it stops pulling, closes windows, or returns 429/503.
3. Producers block, buffer with limits, or drop per policy.
4. Protocols (TCP windows, reactive streams, gRPC) may carry credit-based control.
5. Autoscale may add consumers before applying hard reject policies.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Keeps systems stable under overload.
  * Makes overload visible instead of hiding it in infinite buffers.
* **Disadvantages/Risks:**
  * Pushing back can propagate latency upstream to users.
  * Requires coordinated policies across many services.

## 4. Alternatives
**Unbounded buffering** (dangerous); **load shedding/dropping** oldest or newest data when freshness matters more than completeness.

## 5. Team Guidelines & Use Cases
**SHOULD** bound all queues and define what happens at the limit. **SHOULD NOT** “fix with an infinite buffer” as a scalability strategy.
