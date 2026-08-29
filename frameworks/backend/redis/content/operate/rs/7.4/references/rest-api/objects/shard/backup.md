---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/objects/shard/backup.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.784754Z"
---
# Backup

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
url: '/operate/rs/7.4/references/rest-api/objects/shard/backup/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| progress  | number, (range: 0-100) | Shard backup progress (percentage) |
| status    | 'exporting'<br />'succeeded'<br />'failed' | Status of scheduled periodic backup process |
