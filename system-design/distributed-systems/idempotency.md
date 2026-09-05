---
topic: Idempotency
tags: reliability, apis, messaging
ai_summary: Idempotency ensures repeating the same operation yields the same effect, enabling safe retries. It is essential for networks that may deliver requests more than once.
---

# Idempotency

## 1. Core Concept
An idempotent operation can be applied multiple times without changing the result beyond the first application. It solves duplicate requests caused by retries, at-least-once messaging, and client double-submits.

## 2. Architecture & Data Flow
1. Client sends an idempotency key with a write request.
2. Server stores key → result in a durable table.
3. Duplicates return the original result without re-applying side effects.
4. Consumers of messages dedupe by event ID/offset.
5. Keys expire after a safe retention window.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Makes retries and failover safe.
  * Prevents double charges and duplicate side effects.
* **Disadvantages/Risks:**
  * Requires durable dedupe storage and key discipline.
  * Poorly chosen keys can collapse distinct operations together.

## 4. Alternatives
**Exactly-once sinks** in stream processors (still usually rely on idempotent writes); **synchronous user confirmation** flows (insufficient alone on unreliable networks).

## 5. Team Guidelines & Use Cases
**SHOULD** require idempotency keys on payment and create endpoints and make consumers idempotent. **SHOULD NOT** retry non-idempotent writes without dedupe.
