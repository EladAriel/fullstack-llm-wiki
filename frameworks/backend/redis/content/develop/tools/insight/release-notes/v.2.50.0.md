---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/tools/insight/release-notes/v.2.50.0.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Redis Insight v2.50.0, May 2024
linkTitle: v2.50.0 (May 2024)
date: 2024-05-30 00:00:00 +0000
description: Redis Insight v2.50
weight: 1

---
## 2.50 (May 2024)
This is the General Availability (GA) release of Redis Insight 2.50.

### Highlights
- New tutorial exploring several common Redis use cases with paired-up sample data that will get you started quicker with your empty database.
- Performance and UX enhancements for the JSON data structure for smoother data rendering and interaction in the Browser.

### Details

**Features and improvements**
- [#3402](https://github.com/RedisInsight/RedisInsight/pull/3402) New tutorial exploring several common Redis use cases with paired-up sample data that will get you started quicker with your empty database.
- [#3251](https://github.com/RedisInsight/RedisInsight/pull/3251) UX enhancements for the JSON data structure in the Browser to prevent collapsing the entire structure when updating a JSON value. Includes performance optimizations for loading JSON documents containing numerous objects.
- [#3161](https://github.com/RedisInsight/RedisInsight/pull/3161), [#3171](https://github.com/RedisInsight/RedisInsight/pull/3171) Added a quick access button to sign in to your Redis Cloud account from anywhere within Redis Insight, to import existing databases or create a new account with a free database. Integration with your Redis Cloud account is currently available only in the desktop Redis Insight version.
- [#3349](https://github.com/RedisInsight/RedisInsight/pull/3349) Changed the sorting order in the Tree view to lexicographical.
