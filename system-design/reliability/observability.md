---
topic: Observability (Metrics, Logs, Traces)
tags: observability, reliability, operations
ai_summary: Observability uses metrics, logs, and traces to infer internal system state from external outputs. It enables debugging distributed systems and SLO-driven operations.
---

# Observability (Metrics, Logs, Traces)

## 1. Core Concept
Metrics quantify aggregates, logs record discrete events, traces follow a request across services. Together they solve “why is it broken?” in systems too complex to inspect directly.

## 2. Architecture & Data Flow
1. Instrument code and infra with consistent labels and trace context.
2. Agents/collectors export to backends.
3. Dashboards and alerts evaluate SLOs.
4. On incident, metrics locate symptoms; traces find latency spans; logs explain errors.
5. Sampling and retention balance cost vs fidelity.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Faster incident response and performance optimization.
  * Enables error budgets and capacity planning.
* **Disadvantages/Risks:**
  * High cardinality and retention can explode cost.
  * Poor instrumentation creates false confidence.

## 4. Alternatives
**Only logs** (insufficient at scale); **synthetic monitoring alone** (misses deep internal failure modes).

## 5. Team Guidelines & Use Cases
**SHOULD** adopt metrics+logs+traces for production microservices with trace context propagation. **SHOULD NOT** alert on every raw metric—alert on user-impacting SLOs.
