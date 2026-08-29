---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/crdb/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.503527Z"
---
# _Index

---
Title: CRDB object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents an Active-Active database
hideListLinks: true
linkTitle: crdb
weight: $weight
url: '/operate/rs/7.8/references/rest-api/objects/crdb/'
---

An object that represents an Active-Active database.

| Name | Type/Value | Description |
|------|------------|-------------|
| guid | string | The global unique ID of the Active-Active database |
| causal_consistency | boolean | Enables causal consistency across CRDT instances |
| default_db_config| [CRDB database_config]({{< relref "/operate/rs/7.8/references/rest-api/objects/crdb/database_config" >}}) object | Default database configuration applied to all instances in the CRDB object. In most cases, instances should use the same configuration. If you need to override `default_db_config` or add configuration values for specific instances, you can use `db_config` in individual [instance objects]({{< relref "/operate/rs/7.8/references/rest-api/objects/crdb/instance_info" >}}). |
| encryption | boolean | Encrypt communication |
| featureset_version | integer | Active-Active database active FeatureSet version
| instances | array of [CRDB instance_info]({{< relref "/operate/rs/7.8/references/rest-api/objects/crdb/instance_info" >}}) objects | |
| local_databases | {{<code>}}[{
  "bdb_uid": string,
  "id": integer
}, ...] {{</code>}} | Mapping of instance IDs for local databases to local BDB IDs |
| managed_by | string | The component that manages the Active-Active database |
| modules | {{<code>}}[{
  "featureset_version": integer,
  "module_name": string
}, ...] {{</code>}} | Modules used by the Active-Active database |
| name | string | Name of Active-Active database |
| protocol_version | integer | Active-Active database active protocol version |
| volatile_config_fields | array of strings | A list of database configuration fields that will be set even if unchanged |
