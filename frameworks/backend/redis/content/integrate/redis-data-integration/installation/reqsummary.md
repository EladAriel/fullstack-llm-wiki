---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/installation/reqsummary.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Requirements summary
alwaysopen: false
categories:
- docs
- integrate
- rs
- rdi
description: Requirements and recommendations for RDI installations.
group: di
hideListLinks: false
linkTitle: Requirements summary
summary: Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 5
---

The sections below summarize the software and hardware requirements for
an RDI installation.

## Hardware requirements for VM installation

{{< embed-md "rdi-vm-reqs.md" >}}

## OS requirements for VM installation

{{< embed-md "rdi-os-reqs.md" >}}

## Kubernetes/OpenShift supported versions

{{< embed-md "rdi-k8s-reqs.md" >}}

## RDI database requirements

{{< embed-md "rdi-db-reqs.md" >}}

## Supported source databases

{{< embed-md "rdi-supported-source-versions.md" >}}
