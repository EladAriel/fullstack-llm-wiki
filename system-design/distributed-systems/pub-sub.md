---
topic: Publish-Subscribe Messaging
tags: messaging, event-driven, decoupling
ai_summary: Pub/sub delivers each published event to multiple independent subscribers. It enables fan-out event-driven architectures without producers knowing consumers.
---

# Publish-Subscribe Messaging

## 1. Core Concept
In pub/sub, publishers emit events to a topic; any number of subscribers receive copies (or partition shares). It solves one-to-many notification and independent evolution of consumer groups.

## 2. Architecture & Data Flow
1. Publisher writes an event to a topic.
2. Broker retains events per policy (duration/size).
3. Each subscription/consumer group tracks its own offset/cursor.
4. Consumers process independently and scale per group.
5. Schema registry/contracts reduce breaking changes.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Producers stay decoupled from consumer count and logic.
  * Multiple teams can react to the same domain events.
* **Disadvantages/Risks:**
  * Harder to reason about global ordering and failure cascades.
  * Fan-out multiplies downstream load.

## 4. Alternatives
**Point-to-point queues** for single-worker task distribution; **webhook callbacks** for simple external integrations.

## 5. Team Guidelines & Use Cases
**SHOULD** use pub/sub for domain events many systems must observe. **SHOULD NOT** treat pub/sub as a queryable source of truth without retention and compaction strategy.
