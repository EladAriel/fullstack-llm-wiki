---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/kubernetes/8.0/recommendations/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Configuration recommendations
alwaysopen: false
categories:
- docs
- operate
- kubernetes
description: Best practices and configuration recommendations for Redis Enterprise on Kubernetes deployments.
hideListLinks: false
linkTitle: Recommendations
weight: 80
url: '/operate/kubernetes/8.0/recommendations/'
---

Follow these best practices and configuration recommendations to optimize your Redis Enterprise deployment on Kubernetes for performance, reliability, and scalability.

## Infrastructure recommendations

Configure your Kubernetes infrastructure for optimal Redis Enterprise performance:

- [Node resources]({{< relref "/operate/kubernetes/8.0/recommendations/node-resources" >}}) - CPU, memory, and resource allocation recommendations
- [Node selection]({{< relref "/operate/kubernetes/8.0/recommendations/node-selection" >}}) - Best practices for selecting and configuring Kubernetes nodes
- [Persistent volumes]({{< relref "/operate/kubernetes/8.0/recommendations/persistent-volumes" >}}) - Storage configuration and persistent volume recommendations

## Deployment recommendations

Optimize your Redis Enterprise deployment configuration:

- [Sizing on Kubernetes]({{< relref "/operate/kubernetes/8.0/recommendations/sizing-on-kubernetes" >}}) - Guidelines for sizing clusters and databases
- [Pod stability]({{< relref "/operate/kubernetes/8.0/recommendations/pod-stability" >}}) - Ensure stable pod operations and prevent disruptions

## Performance optimization

Configure your deployment for optimal performance and reliability based on your workload requirements and infrastructure capabilities.
