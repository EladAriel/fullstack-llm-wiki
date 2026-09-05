---
topic: TLS Termination
tags: networking, security, edge
ai_summary: TLS termination decrypts HTTPS at an edge component so backends can speak plain HTTP on a trusted network. It centralizes certificates and reduces app crypto overhead.
---

# TLS Termination

## 1. Core Concept
TLS termination is decrypting TLS at a proxy/load balancer. Optionally, re-encrypt to upstream (TLS passthrough or TLS bridging). It solves certificate management complexity and CPU cost on every app instance.

## 2. Architecture & Data Flow
1. Client completes TLS handshake with the terminator.
2. Terminator presents certs (often automated via ACME).
3. Decrypted request is forwarded on a private network (HTTP or mTLS).
4. Response is encrypted back to the client.
5. Certificate rotation happens at the edge without app redeploys.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Centralized cert lifecycle and cipher policy.
  * Lower CPU on application pods for high-QPS HTTP.
* **Disadvantages/Risks:**
  * Traffic is plaintext behind the terminator unless re-encrypted.
  * Terminator compromise exposes request contents.

## 4. Alternatives
**TLS passthrough** to apps (end-to-end encrypt) and **mTLS service mesh** for east-west encryption after edge termination.

## 5. Team Guidelines & Use Cases
**SHOULD** terminate public TLS at the edge and use mTLS or private networking inland as required by threat model. **SHOULD NOT** run expired certs or shared wildcard secrets in every microservice.
