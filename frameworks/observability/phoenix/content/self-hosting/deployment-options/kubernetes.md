---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/self-hosting/deployment-options/kubernetes.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.942083Z"
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


