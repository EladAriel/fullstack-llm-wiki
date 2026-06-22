---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/requests/shards/actions/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
url: '/operate/rs/7.22/references/rest-api/requests/shards/actions/'
---

## Migrate

| Method | Path | Description |
|--------|------|-------------|
| [POST]({{<relref "/operate/rs/7.22/references/rest-api/requests/shards/actions/migrate#post-multi-shards">}}) | `/v1/shards/actions/migrate` | Migrate multiple shards |
| [POST]({{<relref "/operate/rs/7.22/references/rest-api/requests/shards/actions/migrate#post-shard">}}) | `/v1/shards/{uid}/actions/migrate` | Migrate a specific shard |
