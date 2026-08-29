---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/self-hosting/deployment-options/kubernetes.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.914265Z"
---
# Kubernetes

---
title: "Kubernetes (kustomize)"
description: Phoenix can be deployed on Kubernetes with PostgreSQL using kustomize.
---

## Prerequisites

You must have a working Kubernetes cluster accessible via `kubectl`.

## PostgreSQL with Kustomize

The kustomize deployment uses PostgreSQL as the database backend. This is the recommended approach for production deployments.

Clone the Arize-Phoenix repository:

```bash
git clone https://github.com/Arize-ai/phoenix.git
```

From the repository root, apply the kustomize configuration:

```csharp
kubectl apply -k kustomize/base
```

This will deploy:

* Phoenix application configured to use PostgreSQL

* PostgreSQL database with persistent storage


