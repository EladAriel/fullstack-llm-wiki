---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/objects/crdb/instance_info.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.695847Z"
---
# Instance_Info

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
url: '/operate/rs/8.0/references/rest-api/objects/crdb/instance_info/'
---

An object that represents Active-Active instance info.

| Name | Type/Value | Description |
|------|------------|-------------|
| id | integer | Unique instance ID |
| cluster | [CRDB cluster_info]({{< relref "/operate/rs/8.0/references/rest-api/objects/crdb/cluster_info" >}}) object | |
| compression | integer | Compression level when syncing from this source |
| db_config | [CRDB database_config]({{< relref "/operate/rs/8.0/references/rest-api/objects/crdb/database_config" >}}) object | Database configuration for this specific instance. Use `db_config` only when you need to override or add configuration values that differ from the `default_db_config` in the main [CRDB object]({{< relref "/operate/rs/8.0/references/rest-api/objects/crdb" >}}). For a list of which settings must be identical across all instances and which to set per instance, see the [CRDB database config object]({{<relref "/operate/rs/8.0/references/rest-api/objects/crdb/database_config">}}) reference. |
| db_uid | string | ID of local database instance. This field is likely to be empty for instances other than the local one. |
