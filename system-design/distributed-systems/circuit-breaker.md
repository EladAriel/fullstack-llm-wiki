---
topic: Circuit Breaker
tags: reliability, resilience, microservices
ai_summary: A circuit breaker stops calling a failing dependency after an error threshold, then probes for recovery. It prevents cascading failures and thread exhaustion.
---

# Circuit Breaker

## 1. Core Concept
The circuit breaker pattern wraps remote calls with states: closed (normal), open (fail fast), half-open (trial requests). It solves cascading latency and resource pile-ups when a dependency is down.

## 2. Architecture & Data Flow
1. Track success/failure rates for a dependency.
2. Trip open when threshold exceeded; fail fast locally.
3. After a timeout, allow limited half-open probes.
4. On probe success, close; on failure, reopen.
5. Combine with timeouts, bulkheads, and fallbacks.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Protects caller resources during dependency outages.
  * Gives dependencies time to recover.
* **Disadvantages/Risks:**
  * Mis-tuned thresholds cause flapping or prolonged outages.
  * Fallbacks can return stale/wrong data if not designed carefully.

## 4. Alternatives
**Timeouts + retries with budget** alone; **load shedding** at the callee; **hedged requests** for latency, not outages.

## 5. Team Guidelines & Use Cases
**SHOULD** put circuit breakers on sync calls to unstable or third-party dependencies. **SHOULD NOT** retry aggressively against an open circuit.
