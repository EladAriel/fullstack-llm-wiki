---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/shard/backup.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Backup object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the backup object used with Redis Enterprise Software REST
  API calls.
linkTitle: backup
weight: $weight
url: '/operate/rs/7.8/references/rest-api/objects/shard/backup/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| progress  | number, (range: 0-100) | Shard backup progress (percentage) |
| status    | 'exporting'<br />'succeeded'<br />'failed' | Status of scheduled periodic backup process |
