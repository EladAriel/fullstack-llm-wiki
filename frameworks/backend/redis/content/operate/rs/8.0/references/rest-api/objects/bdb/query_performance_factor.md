---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/objects/bdb/query_performance_factor.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.704172Z"
---
# Query_Performance_Factor

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

