---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/requests/shards/actions/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Shard actions requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: REST API requests to perform shard actions
headerRange: '[1-2]'
hideListLinks: true
linkTitle: actions
weight: $weight
---

## Migrate

| Method | Path | Description |
|--------|------|-------------|
| [POST]({{<relref "/operate/rs/references/rest-api/requests/shards/actions/migrate#post-multi-shards">}}) | `/v1/shards/actions/migrate` | Migrate multiple shards |
| [POST]({{<relref "/operate/rs/references/rest-api/requests/shards/actions/migrate#post-shard">}}) | `/v1/shards/{uid}/actions/migrate` | Migrate a specific shard |
