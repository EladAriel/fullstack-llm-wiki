---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/objects/suffix.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Suffix object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents a DNS suffix
linkTitle: suffix
weight: $weight
url: '/operate/rs/8.0/references/rest-api/objects/suffix/'
---

An API object that represents a DNS suffix in the cluster.

| Name | Type/Value | Description |
|------|------------|-------------|
| default | boolean | Suffix is the default suffix for the cluster (read-only) |
| internal | boolean | Does the suffix point to internal IP addresses (read-only) |
| mdns | boolean | Support for multicast DNS (read-only) |
| name | string | Unique suffix name that represents its zone (read-only) |
| slaves | array of strings | Frontend DNS servers to be updated by this suffix |
| use_aaaa_ns | boolean | Suffix uses AAAA NS entries (read-only) |