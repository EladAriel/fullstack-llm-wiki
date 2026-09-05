---
topic: DNS (Domain Name System)
tags: networking, discovery, routing
ai_summary: DNS maps human-readable names to addresses and service endpoints. It is foundational for routing, failover, and traffic steering across regions.
---

# DNS (Domain Name System)

## 1. Core Concept
DNS is a hierarchical distributed lookup system that resolves names to records (A/AAAA, CNAME, MX, TXT, SRV). Beyond hostname lookup, it solves service discovery and coarse traffic control (failover, weighted/geo routing).

## 2. Architecture & Data Flow
1. Client queries a recursive resolver.
2. Resolver walks root → TLD → authoritative nameservers.
3. Response is cached according to TTL.
4. Application connects to returned IPs; load balancers or anycast may sit behind those names.
5. Health-checked failover DNS updates or switches records when endpoints fail.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Universal, highly cached, and operationally familiar.
  * Enables blue/green and multi-region steering without client code changes.
* **Disadvantages/Risks:**
  * TTL and client caching delay failover.
  * DNS is not a fine-grained load balancer or auth layer.

## 4. Alternatives
**Service discovery** (Consul, Kubernetes DNS/Endpoints) for internal mesh; **anycast IP** for network-layer failover without waiting on DNS TTLs.

## 5. Team Guidelines & Use Cases
**SHOULD** use short-enough TTLs for failover-critical names and health-checked DNS where supported. **SHOULD NOT** rely on DNS alone for fast L7 load shedding or per-request routing.
