---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/shard/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Shard object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents a database shard
hideListLinks: true
linkTitle: shard
weight: $weight
url: '/operate/rs/7.8/references/rest-api/objects/shard/'
---

An API object that represents a Redis shard in a database.

| Name | Type/Value | Description |
|------|------------|-------------|
| uid | string | Cluster unique ID of shard |
| assigned_slots | string | Shards hash slot range |
| backup | [backup]({{< relref "/operate/rs/7.8/references/rest-api/objects/shard/backup" >}}) object | Current status of scheduled periodic backup process |
| bdb_uid | integer | The ID of the database this shard belongs to |
| bigstore_ram_weight | number | Shards RAM distribution weight |
| detailed_status | 'busy'<br />'down'<br />'importing'<br />'loading'<br />'ok'<br />'timeout'<br />'trimming'<br />'unknown' | A more detailed status of the shard |
| loading | [loading]({{< relref "/operate/rs/7.8/references/rest-api/objects/shard/loading" >}}) object | Current status of dump file loading |
| node_uid | string | The ID of the node this shard is located on |
| redis_info | redis_info object | A sub-dictionary of the [Redis INFO command]({{< relref "/commands/info" >}}) |
| report_timestamp | string | The time in which the shard's info was collected (read-only) |
| role | 'master'<br />'slave' | Role of this shard |
| status | 'active'<br />'inactive'<br />'trimming' | The current status of the shard |
| sync | [sync]({{< relref "/operate/rs/7.8/references/rest-api/objects/shard/sync.md" >}}) object | Shard's current sync status and progress |
