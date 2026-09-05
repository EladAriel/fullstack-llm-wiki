---
topic: Authentication and Authorization
tags: security, apis, architecture
ai_summary: Authentication verifies identity; authorization decides permitted actions. System design must place these checks consistently at edges and service boundaries.
---

# Authentication and Authorization

## 1. Core Concept
AuthN establishes who the caller is (session, token, mTLS). AuthZ evaluates policies (RBAC, ABAC, ReBAC) against that identity. They solve protecting APIs and data from anonymous or over-privileged access.

## 2. Architecture & Data Flow
1. Client authenticates with IdP (OAuth/OIDC, SAML, passwords).
2. Edge validates tokens/sessions.
3. Identity propagates via signed tokens or internal identity headers/mTLS.
4. Services enforce fine-grained authz on resources.
5. Audit logs record access decisions for sensitive operations.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Central IdP improves UX and security controls.
  * Explicit authz prevents accidental public data leaks.
* **Disadvantages/Risks:**
  * Token confusion and inconsistent enforcement across services.
  * Overly central “auth service” round-trips can add latency/SPOF if misdesigned.

## 4. Alternatives
**Network-only trust** (insufficient alone); **mutual TLS without user-level authz** (machine identity only).

## 5. Team Guidelines & Use Cases
**SHOULD** authenticate at the edge and re-enforce authz in each sensitive service. **SHOULD NOT** pass mutable `userId` headers without cryptographic service identity.
