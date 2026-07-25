---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/objects/bdb/query_performance_factor.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Query performance factor object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Configuration object for query performance factor
linkTitle: query_performance_factor
weight: $weight
url: '/operate/rs/8.0/references/rest-api/objects/bdb/query_performance_factor/'
---

Configures [query performance factor]({{<relref "/operate/oss_and_stack/stack-with-enterprise/search/query-performance-factor">}}) and related fields.

| Field | Type/Value | Description |
|-------|------------|-------------|
| active | boolean (default: false) | If true, enables query performance factor for the database |
| scaling_factor | integer (range: 0-16) (default: 0) | Scales the magnitude of the query performance factor |

