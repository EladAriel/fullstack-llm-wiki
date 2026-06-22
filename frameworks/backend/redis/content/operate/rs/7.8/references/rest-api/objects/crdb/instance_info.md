---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/crdb/instance_info.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
