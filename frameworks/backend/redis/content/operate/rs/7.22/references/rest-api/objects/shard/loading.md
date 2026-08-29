---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/objects/shard/loading.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.413384Z"
---
# Loading

---
Title: Loading object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the loading object used with Redis Enterprise Software REST
  API calls.
linkTitle: loading
weight: $weight
url: '/operate/rs/7.22/references/rest-api/objects/shard/loading/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| progress  | number, (range: 0-100) | Percentage of bytes already loaded |
| status    | 'in_progress'<br />'idle' | Status of the load of a dump file (read-only) |
