---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/bootstrap/node_identity.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

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
url: '/operate/rs/7.8/references/rest-api/objects/bootstrap/node_identity/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| bigstore_driver | 'rocksdb' | Bigstore driver name or none (deprecated, use the [cluster object]({{< relref "/operate/rs/7.8/references/rest-api/objects/cluster" >}})'s `bigstore_driver` instead) |
| bigstore_enabled | boolean (default: false) | If `true`, then flash storage is enabled on this node for [Auto Tiering]({{<relref "/operate/rs/7.8/databases/auto-tiering">}}) databases. Configurable during [bootstrapping]({{<relref "/operate/rs/7.8/references/rest-api/requests/bootstrap#post-bootstrap">}}). After bootstrapping, it is read-only. |
| identity | [identity]({{< relref "/operate/rs/7.8/references/rest-api/objects/bootstrap/identity" >}}) object | Node identity |
| limits | [limits]({{< relref "/operate/rs/7.8/references/rest-api/objects/bootstrap/limits" >}}) object | Node limits |
| paths | [paths]({{< relref "/operate/rs/7.8/references/rest-api/objects/bootstrap/paths" >}}) object | Storage paths object |
