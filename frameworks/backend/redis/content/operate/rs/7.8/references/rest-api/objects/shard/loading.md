---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/shard/loading.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

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
url: '/operate/rs/7.8/references/rest-api/objects/shard/loading/'
---

| Name | Type/Value | Description |
|------|------------|-------------|
| progress  | number, (range: 0-100) | Percentage of bytes already loaded |
| status    | 'in_progress'<br />'idle' | Status of the load of a dump file (read-only) |
