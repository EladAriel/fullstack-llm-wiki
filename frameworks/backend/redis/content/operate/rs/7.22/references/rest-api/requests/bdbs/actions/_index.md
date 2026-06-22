---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/requests/bdbs/actions/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
url: '/operate/rs/7.22/references/rest-api/requests/bdbs/actions/'
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
| [PUT]({{<relref "/operate/rs/7.22/references/rest-api/requests/bdbs/actions/rebalance#put-bdbs-actions-rebalance">}}) | `/v1/bdbs/{uid}/actions/rebalance` | Rebalance database shards |

## Recover

| Method | Path | Description |
|--------|------|-------------|
| [GET]({{<relref "/operate/rs/7.22/references/rest-api/requests/bdbs/actions/recover#get-bdbs-actions-recover">}}) | `/v1/bdbs/{uid}/actions/recover` | Get database recovery plan  |
| [POST]({{<relref "/operate/rs/7.22/references/rest-api/requests/bdbs/actions/recover#post-bdbs-actions-recover">}}) | `/v1/bdbs/{uid}/actions/recover` | Recover database  |

## Resume traffic
| Method | Path | Description |
|--------|------|-------------|
| [POST]({{<relref "/operate/rs/7.22/references/rest-api/requests/bdbs/actions/resume_traffic#post-bdbs-actions-resume-traffic">}}) | `/v1/bdbs/{uid}/actions/resume_traffic` | Resume database traffic |

## Stop traffic
| Method | Path | Description |
|--------|------|-------------|
| [POST]({{<relref "/operate/rs/7.22/references/rest-api/requests/bdbs/actions/stop_traffic#post-bdbs-actions-stop-traffic">}}) | `/v1/bdbs/{uid}/actions/stop_traffic` | Stop database traffic |
