---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/bdb/syncer_sources.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Syncer sources object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the syncer_sources object used with Redis Enterprise Software
  REST API calls.
linkTitle: syncer_sources
weight: $weight
url: '/operate/rs/7.8/references/rest-api/objects/bdb/syncer_sources/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| uid | integer | Unique ID of this source |
| client_cert | string | Client certificate to use if encryption is enabled |
| client_key | string | Client key to use if encryption is enabled |
| compression | integer, <nobr>(range: 0-6)</nobr> | Compression level for the replication link |
| encryption | boolean | Encryption enabled/disabled |
| lag | integer | Lag in milliseconds between source and destination (while synced) |
| last_error | string | Last error encountered when syncing from the source |
| last_update | string | Time when we last received an update from the source |
| rdb_size | integer | The source's RDB size to be transferred during the syncing phase |
| rdb_transferred | integer | Number of bytes transferred from the source's RDB during the syncing phase |
| replication_tls_sni | string | Replication TLS server name indication |
| server_cert | string | Server certificate to use if encryption is enabled |
| status | string | Sync status of this source |
| uri | string | Source Redis URI |
