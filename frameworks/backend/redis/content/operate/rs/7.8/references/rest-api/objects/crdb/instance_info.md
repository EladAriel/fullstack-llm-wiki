---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/crdb/instance_info.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: CRDB instance info object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents Active-Active instance info
linkTitle: instance_info
weight: $weight
url: '/operate/rs/7.8/references/rest-api/objects/crdb/instance_info/'
---

An object that represents Active-Active instance info.

| Name | Type/Value | Description |
|------|------------|-------------|
| id | integer | Unique instance ID |
| cluster | [CRDB cluster_info]({{< relref "/operate/rs/7.8/references/rest-api/objects/crdb/cluster_info" >}}) object | |
| compression | integer | Compression level when syncing from this source |
| db_config | [CRDB database_config]({{< relref "/operate/rs/7.8/references/rest-api/objects/crdb/database_config" >}}) object | Database configuration for this specific instance. Use `db_config` only when you need to override or add configuration values that differ from the `default_db_config` in the main [CRDB object]({{< relref "/operate/rs/7.8/references/rest-api/objects/crdb" >}}). |
| db_uid | string | ID of local database instance. This field is likely to be empty for instances other than the local one. |
