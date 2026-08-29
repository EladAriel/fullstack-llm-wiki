---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/objects/shard/sync.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.702282Z"
---
# Sync

---
Title: Sync object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the sync object used with Redis Software REST API
  calls.
linkTitle: sync
weight: $weight
url: '/operate/rs/8.0/references/rest-api/objects/shard/sync/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| progress  | integer        | Number of bytes remaining in current sync |
| status    | 'in_progress'<br />'idle'<br />'link_down' | Indication of the shard's current sync status |
