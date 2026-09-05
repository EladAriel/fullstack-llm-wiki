---
topic: Retries and Exponential Backoff
tags: reliability, networking, resilience
ai_summary: Retries reattempt failed operations; exponential backoff spaces attempts to reduce overload. Jitter prevents synchronized retry storms.
---

# Retries and Exponential Backoff

## 1. Core Concept
Transient failures (network blips, 503s) often succeed on retry. Exponential backoff increases delay between attempts; jitter randomizes delays. Together they solve flaky networks without stampedes.

## 2. Architecture & Data Flow
1. Classify errors as retryable vs permanent.
2. Retry with capped exponential delays and jitter.
3. Enforce max attempts and overall deadline.
4. Propagate idempotency keys on write retries.
5. Prefer client-side + server load shedding over infinite retries.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Improves success rate under brief faults.
  * Backoff/jitter protect recovering services.
* **Disadvantages/Risks:**
  * Retries amplify load during outages (retry storms).
  * Can duplicate side effects without idempotency.

## 4. Alternatives
**Fail fast + circuit breaker**; **hedged requests** for tail latency on idempotent reads; **async queues** that naturally retry.

## 5. Team Guidelines & Use Cases
**SHOULD** retry idempotent reads and explicitly idempotent writes with budgets. **SHOULD NOT** blindly retry all 4xx errors or stack unbounded retries at every layer.
