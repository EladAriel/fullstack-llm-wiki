---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/objects/bdb_group.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: BDB group object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents a group of databases with a shared memory pool
linkTitle: bdb_group
weight: $weight
url: '/operate/rs/7.22/references/rest-api/objects/bdb_group/'
---

An API object that represents a group of databases that share a memory pool.

| Name | Type/Value | Description |
|------|------------|-------------|
| uid          | integer          | Cluster unique ID of the database group |
| members      | array of strings | A list of UIDs of member databases (read-only) |
| memory_size  | integer          | The common memory pool size limit for all databases in the group, expressed in bytes |
