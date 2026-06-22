---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/bdb/replica_sources_status.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: BDB replica sources status field
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the bdb replica_sources status field used with Redis Enterprise
  Software REST API calls.
linkTitle: replica_sources status
weight: $weight
url: '/operate/rs/7.8/references/rest-api/objects/bdb/replica_sources_status/'
---

The `replica_sources` status field relates to the [Replica Of]({{< relref "/operate/rs/7.8/databases/import-export/replica-of/create.md" >}}) feature, which enables the creation of a Redis database (single- or multi-shard) that synchronizes data from another Redis database (single- or multi-shard).

The status field represents the Replica Of sync status for a specific sync source.

Possible status values:

| Status | Description | Possible next status |
|--------|-------------|----------------------|
| 'out-of-sync' | Sync process is disconnected from source and trying to reconnect | 'syncing' |
| 'syncing' | Sync process is in progress | 'in-sync' <br />'out-of-sync' |
| 'in-sync' | Sync process finished successfully, and new commands are syncing on a regular basis | 'syncing' <br />'out-of-sync'

{{< image filename="/images/rs/rest-api-replica-sources-status.png#no-click" alt="Replica sources status" >}}
