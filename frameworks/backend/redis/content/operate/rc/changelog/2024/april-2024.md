---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/changelog/2024/april-2024.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.310449Z"
---
# April 2024

---
Title: Redis Cloud changelog (April 2024)
aliases:
- /operate/rc/changelog/april-2024/
alwaysopen: false
categories:
- docs
- operate
- rc
description: New features, enhancements, and other changes added to Redis Cloud during
  April 2024.
highlights: Nano billing unit, Essentials subscriptions through AWS Marketplace
linktitle: April 2024
tags:
- changelog
weight: 55
---

## New features

### Nano billing unit

We added a Nano billing unit for Pro databases with a maximum size of 500 MB and a maximum throughput of 500 ops/sec. Use it to create smaller databases for a lower cost.

### Essentials subscriptions through AWS Marketplace

You can now use your [AWS Marketplace]({{< relref "/operate/rc/cloud-integrations/gcp-marketplace/" >}}) account to pay for your Essentials subscriptions as well as your Pro subscriptions.

## Enhancements

### Search and query throughput in ops/sec

You can now set the throughput for databases with Search and query in operations per second (ops/sec), like all other Redis databases. This will let you seamlessly scale your query workload in and out as needed. 

## Deprecations

- Setting throughput by `number-of-shards` is now deprecated for the `POST /v1/subscriptions/{subscriptionId}/databases` REST API endpoint and will be removed soon. We recommend changing the throughput measurement to `operations-per-second` when you create databases using the Redis Cloud API.