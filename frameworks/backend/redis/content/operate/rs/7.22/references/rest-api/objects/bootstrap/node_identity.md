---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/objects/bootstrap/node_identity.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.415700Z"
---
# Node_Identity

---
Title: Node identity object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the node_identity object used with Redis Enterprise Software
  REST API calls.
linkTitle: node_identity
weight: $weight
url: '/operate/rs/7.22/references/rest-api/objects/bootstrap/node_identity/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| bigstore_driver | 'rocksdb' | Bigstore driver name or none (deprecated, use the [cluster object]({{< relref "/operate/rs/7.22/references/rest-api/objects/cluster" >}})'s `bigstore_driver` instead) |
| bigstore_enabled | boolean (default: false) | If `true`, then flash storage is enabled on this node for [Auto Tiering]({{<relref "/operate/rs/7.22/databases/auto-tiering">}}) databases. Configurable during [bootstrapping]({{<relref "/operate/rs/7.22/references/rest-api/requests/bootstrap#post-bootstrap">}}). After bootstrapping, it is read-only. |
| identity | [identity]({{< relref "/operate/rs/7.22/references/rest-api/objects/bootstrap/identity" >}}) object | Node identity |
| limits | [limits]({{< relref "/operate/rs/7.22/references/rest-api/objects/bootstrap/limits" >}}) object | Node limits |
| paths | [paths]({{< relref "/operate/rs/7.22/references/rest-api/objects/bootstrap/paths" >}}) object | Storage paths object |
