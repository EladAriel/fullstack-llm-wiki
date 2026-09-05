---
topic: Service Discovery
tags: networking, microservices, discovery
ai_summary: Service discovery lets clients locate healthy instances of a service in dynamic environments. Mechanisms include DNS, registries, and platform endpoints APIs.
---

# Service Discovery

## 1. Core Concept
In elastic infrastructure, IPs change constantly. Service discovery maintains a directory of instances and health so callers can find targets without hardcoding addresses.

## 2. Architecture & Data Flow
1. Service registers on startup with a registry or platform control plane.
2. Health checks update readiness.
3. Clients query DNS/registry/mesh and cache results.
4. Load balancing chooses an instance.
5. Deregistration on shutdown or failed checks removes stale targets.

## 3. Trade-offs (Pros & Cons)
* **Advantages:**
  * Enables autoscaling and replaceable compute.
  * Central health view for routing.
* **Disadvantages/Risks:**
  * Stale registry entries cause connection errors.
  * Another critical dependency for request paths.

## 4. Alternatives
**Static config** for tiny fixed fleets; **service mesh sidecar DNS/xDS** as the discovery+LB plane.

## 5. Team Guidelines & Use Cases
**SHOULD** use platform-native discovery (K8s Services) unless multi-cluster needs demand a richer registry. **SHOULD NOT** hardcode pod IPs in clients.
