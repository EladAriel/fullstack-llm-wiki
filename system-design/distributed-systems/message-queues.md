---
topic: Message Queues
tags: messaging, async, decoupling
ai_summary: Message queues buffer work between producers and consumers to decouple services and smooth load. They enable asynchronous processing with retry and durability options.
---

# Message Queues

## 1. Core Concept
A message queue stores messages until consumers process them. It solves tight coupling, traffic spikes, and reliability of background work by persisting tasks independently of producer uptime.

## 2. Architecture & Data Flow
1. Producer sends a message to a queue/topic partition.
2. Broker persists (memory/disk) and acknowledges per durability settings.
3. Consumer pulls or receives push delivery.
4. On success, ack/commit offset; on failure, retry or dead-letter.
5. Scaling adds consumers within a competing-consumer group.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Smooths spikes and isolates failures between services.
  * Enables retries and durable async workflows.
* **Disadvantages/Risks:**
  * End-to-end latency increases vs synchronous calls.
  * Poison messages, ordering, and exactly-once semantics add complexity.

## 4. Alternatives
**Pub/sub topics** for broadcast; **synchronous RPC** when the caller must fail/succeed inline; **workflow engines** for long-running orchestrations.

## 5. Team Guidelines & Use Cases
**SHOULD** queue non-interactive work (emails, image processing, webhooks). **SHOULD NOT** hide critical user-facing failures in an unmonitored queue without SLAs and DLQs.
