---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/bootstrap/node_identity.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Node identity object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the node_identity object used with Redis Software
  REST API calls.
linkTitle: node_identity
weight: $weight
---

| Name | Type/Value | Description |
|------|------------|-------------|
| bigstore_driver | 'rocksdb' | Bigstore driver name or none (deprecated, use the [cluster object]({{< relref "/operate/rs/references/rest-api/objects/cluster" >}})'s `bigstore_driver` instead) |
| bigstore_enabled | boolean (default: false) | If `true`, then flash storage is enabled on this node for [Redis Flex and Auto Tiering]({{<relref "/operate/rs/databases/flash">}}) databases. Configurable during [bootstrapping]({{<relref "/operate/rs/references/rest-api/requests/bootstrap#post-bootstrap">}}). After bootstrapping, it is read-only. |
| identity | [identity]({{< relref "/operate/rs/references/rest-api/objects/bootstrap/identity" >}}) object | Node identity |
| limits | [limits]({{< relref "/operate/rs/references/rest-api/objects/bootstrap/limits" >}}) object | Node limits |
| paths | [paths]({{< relref "/operate/rs/references/rest-api/objects/bootstrap/paths" >}}) object | Storage paths object |
