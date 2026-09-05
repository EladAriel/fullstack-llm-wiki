---
topic: Sidecar Pattern
tags: architecture, patterns, infrastructure
ai_summary: A sidecar colocates a helper process with the main app container to provide platform features like proxying, logging, or secrets. It separates infrastructure concerns from business code.
---

# Sidecar Pattern

## 1. Core Concept
The sidecar pattern attaches an auxiliary container/process in the same network namespace as the app. It solves cross-cutting operational needs without baking them into every language runtime.

## 2. Architecture & Data Flow
1. Deploy app + sidecar as a unit (pod).
2. App talks to localhost sidecar for proxy/telemetry/secrets.
3. Sidecar talks to the broader mesh/control plane.
4. Lifecycle hooks manage startup ordering and drains.
5. Upgrading sidecars can ship platform features independently of app code.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Consistent infrastructure features across polyglot services.
  * Keeps business containers smaller and focused.
* **Disadvantages/Risks:**
  * Extra CPU/memory per pod and more complex networking.
  * Troubleshooting spans two processes.

## 4. Alternatives
**Library SDKs** embedded in-process; **node agents** shared per host; **ambient mesh** modes without per-pod proxies.

## 5. Team Guidelines & Use Cases
**SHOULD** use sidecars for fleet-wide mTLS/metrics when a mesh is adopted. **SHOULD NOT** put business logic in sidecars.
