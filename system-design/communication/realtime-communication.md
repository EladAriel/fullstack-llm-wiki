---
topic: Real-Time Communication (WebSockets, SSE, Long Polling)
tags: communication, realtime, networking
ai_summary: WebSockets, Server-Sent Events, and long polling deliver low-latency server updates to clients. Choice depends on bidirectional needs, proxies, and scale.
---

# Real-Time Communication (WebSockets, SSE, Long Polling)

## 1. Core Concept
Interactive apps need server push beyond request/response. WebSockets provide full-duplex channels; SSE is server-to-client over HTTP; long polling holds requests until events arrive. They solve live feeds, collab cursors, and notifications.

## 2. Architecture & Data Flow
1. Client upgrades to WebSocket or opens SSE/long-poll.
2. Gateway sticky-routes or uses a pub/sub backplane for multi-instance fan-out.
3. App publishes events to the backplane.
4. Owning connection node pushes to the client.
5. Heartbeats detect dead connections and reconnect with backoff.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Low-latency updates without constant client polling.
  * Better UX for collaborative and live data products.
* **Disadvantages/Risks:**
  * Stateful connections complicate horizontal scale.
  * Proxies/load balancers need timeout and sticky configuration.

## 4. Alternatives
**Short polling** (simpler, higher overhead); **push notifications** for mobile background delivery.

## 5. Team Guidelines & Use Cases
**SHOULD** use SSE for one-way feeds and WebSockets for bidirectional interaction. **SHOULD NOT** open unbounded connections without auth, fan-out design, and idle timeouts.
