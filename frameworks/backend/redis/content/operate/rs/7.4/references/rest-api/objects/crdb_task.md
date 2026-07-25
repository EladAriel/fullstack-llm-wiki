---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/objects/crdb_task.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: CRDB task object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents a CRDB task
linkTitle: crdb_task
weight: $weight
url: '/operate/rs/7.4/references/rest-api/objects/crdb_task/'
---

An object that represents an Active-Active (CRDB) task.

| Name | Type/Value | Description |
|------|------------|-------------|
| id | string | CRDB task ID (read-only) |
| crdb_guid | string | Globally unique Active-Active database ID (GUID) (read-only) |
| ended | string | Timestamp when the task ended (read-only) |
| errors | {{<code>}}
[{
  "cluster_name": string,
  "description": string,
  "error_code": string
}, ...] {{</code>}} | Details for errors that occurred on a cluster |
| operation | string | The operation that is running (read-only) |
| progress | {{<code>}}
{
  "clusters": [{
    "name": string,
    "progress": string
  }, ...],
  "worker": string
} {{</code>}} | • `name`: The instance cluster name<br />• `progress`: The step the instance coordinator is running<br />• `worker`: The step the worker is running |
| started | string | Timestamp when the task started (read-only) |
| status | 'queued' <br />'started' <br />'finished' <br />'failed' | CRDB task status (read-only) |
| worker_name | string | The worker that runs the task (read-only) |
