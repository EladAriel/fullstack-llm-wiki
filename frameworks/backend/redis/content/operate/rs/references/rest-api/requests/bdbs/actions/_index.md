---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/requests/bdbs/actions/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Database actions requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Database action requests
headerRange: '[1-2]'
hideListLinks: true
linkTitle: actions
weight: $weight
---

## Backup

| Method | Path | Description |
|--------|------|-------------|
| [PUT]({{< relref "./backup_reset_status#put-bdbs-actions-backup-reset-status" >}}) | `/v1/bdbs/{uid}/actions/backup_reset_status` | Reset database backup status |

## Export

| Method | Path | Description |
|--------|------|-------------|
| [PUT]({{< relref "./export_reset_status#put-bdbs-actions-export-reset-status" >}}) | `/v1/bdbs/{uid}/actions/export_reset_status` | Reset database export status |
| [POST]({{< relref "./export#post-bdbs-actions-export" >}}) | `/v1/bdbs/{uid}/actions/export` | Initiate database export |

## Import

| Method | Path | Description |
|--------|------|-------------|
| [PUT]({{< relref "./import_reset_status#put-bdbs-actions-import-reset-status" >}}) | `/v1/bdbs/{uid}/actions/import_reset_status` | Reset database import status |
| [POST]({{< relref "./import#post-bdbs-actions-import" >}}) | `/v1/bdbs/{uid}/actions/import` | Initiate manual dataset import |

## Optimize shards placement

| Method | Path | Description |
|--------|------|-------------|
| [GET]({{< relref "./optimize_shards_placement#get-bdbs-actions-optimize-shards-placement" >}}) | `/v1/bdbs/{uid}/actions/optimize_shards_placement` | Get optimized shards placement for a database  |

## Rebalance

| Method | Path | Description |
|--------|------|-------------|
| [PUT]({{<relref "/operate/rs/references/rest-api/requests/bdbs/actions/rebalance#put-bdbs-actions-rebalance">}}) | `/v1/bdbs/{uid}/actions/rebalance` | Rebalance database shards |

## Recover

| Method | Path | Description |
|--------|------|-------------|
| [GET]({{<relref "/operate/rs/references/rest-api/requests/bdbs/actions/recover#get-bdbs-actions-recover">}}) | `/v1/bdbs/{uid}/actions/recover` | Get database recovery plan  |
| [POST]({{<relref "/operate/rs/references/rest-api/requests/bdbs/actions/recover#post-bdbs-actions-recover">}}) | `/v1/bdbs/{uid}/actions/recover` | Recover database  |

## Resume traffic
| Method | Path | Description |
|--------|------|-------------|
| [POST]({{<relref "/operate/rs/references/rest-api/requests/bdbs/actions/resume_traffic#post-bdbs-actions-resume-traffic">}}) | `/v1/bdbs/{uid}/actions/resume_traffic` | Resume database traffic |

## Stop traffic
| Method | Path | Description |
|--------|------|-------------|
| [POST]({{<relref "/operate/rs/references/rest-api/requests/bdbs/actions/stop_traffic#post-bdbs-actions-stop-traffic">}}) | `/v1/bdbs/{uid}/actions/stop_traffic` | Stop database traffic |
