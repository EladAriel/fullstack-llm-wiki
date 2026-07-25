---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/shard/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
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
---

An API object that represents a Redis shard in a database.

| Name | Type/Value | Description |
|------|------------|-------------|
| uid | string | Cluster unique ID of shard |
| assigned_slots | string | Shards hash slot range |
| backup | [backup]({{< relref "/operate/rs/references/rest-api/objects/shard/backup" >}}) object | Current status of scheduled periodic backup process |
| bdb_uid | integer | The ID of the database this shard belongs to |
| bigstore_ram_weight | number | Shards RAM distribution weight |
| detailed_status | 'busy'<br />'down'<br />'importing'<br />'loading'<br />'ok'<br />'timeout'<br />'trimming'<br />'unknown' | A more detailed status of the shard |
| loading | [loading]({{< relref "/operate/rs/references/rest-api/objects/shard/loading" >}}) object | Current status of dump file loading |
| node_uid | string | The ID of the node this shard is located on |
| redis_info | redis_info object | A sub-dictionary of the [Redis INFO command]({{< relref "/commands/info" >}}) |
| report_timestamp | string | The time in which the shard's info was collected (read-only) |
| role | 'master'<br />'slave' | Role of this shard |
| status | 'active'<br />'inactive'<br />'trimming' | The current status of the shard |
| sync | [sync]({{< relref "/operate/rs/references/rest-api/objects/shard/sync.md" >}}) object | Shard's current sync status and progress |
