---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/shard/loading.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Loading object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the loading object used with Redis Software REST
  API calls.
linkTitle: loading
weight: $weight
---

| Name | Type/Value | Description |
|------|------------|-------------|
| progress  | number, (range: 0-100) | Percentage of bytes already loaded |
| status    | 'in_progress'<br />'idle' | Status of the load of a dump file (read-only) |
