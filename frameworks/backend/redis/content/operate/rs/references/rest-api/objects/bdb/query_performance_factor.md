---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/bdb/query_performance_factor.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
---

Configures [query performance factor]({{<relref "/operate/oss_and_stack/stack-with-enterprise/search/query-performance-factor">}}) and related fields.

| Field | Type/Value | Description |
|-------|------------|-------------|
| active | boolean (default: false) | If true, enables query performance factor for the database |
| scaling_factor | integer (range: 0-16) (default: 0) | Scales the magnitude of the query performance factor |

