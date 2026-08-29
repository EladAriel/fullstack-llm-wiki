---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/requests/shards/actions/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.496325Z"
---
# _Index

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
url: '/operate/rs/7.8/references/rest-api/requests/shards/actions/'
---

## Migrate

| Method | Path | Description |
|--------|------|-------------|
| [POST]({{<relref "/operate/rs/7.8/references/rest-api/requests/shards/actions/migrate#post-multi-shards">}}) | `/v1/shards/actions/migrate` | Migrate multiple shards |
| [POST]({{<relref "/operate/rs/7.8/references/rest-api/requests/shards/actions/migrate#post-shard">}}) | `/v1/shards/{uid}/actions/migrate` | Migrate a specific shard |
