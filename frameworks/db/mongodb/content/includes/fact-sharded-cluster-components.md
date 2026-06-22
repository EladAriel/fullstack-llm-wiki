---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-sharded-cluster-components.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

A MongoDB `sharded cluster` consists of the following components:

- `shard <shards-concepts>`: Each shard contains a
subset of the sharded data. Each shard must be deployed as a `replica set`.

- `/core/sharded-cluster-query-router`: The `mongos` acts as a
query router, providing an interface between client applications and the sharded cluster.

- `config servers <sharding-config-server>`: Config
servers store metadata and configuration settings for the cluster. Config servers must be deployed as a replica set (CSRS).
