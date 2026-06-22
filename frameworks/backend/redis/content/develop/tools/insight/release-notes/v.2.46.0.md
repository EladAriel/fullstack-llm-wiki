---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/tools/insight/release-notes/v.2.46.0.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: RedisInsight v2.46.0, March 2024
linkTitle: v2.46.0 (March 2024)
date: 2024-03-28 00:00:00 +0000
description: RedisInsight v2.46
weight: 1
---
## 2.46 (March 2024)
This is the General Availability (GA) release of RedisInsight 2.46.

### Highlights
- New formatters for 32-bit and 64-bit vector embeddings for a more human-readable representation in the Browser
- Cleaner layout on the main page with quick access to JSON and search & query tutorials and Redis Cloud in-app sign-up


### Details

**Features and improvements**
- [#2843](https://github.com/RedisInsight/RedisInsight/pull/2843), [#3185](https://github.com/RedisInsight/RedisInsight/pull/3185) Adding new formatters for 32-bit and 64-bit vector embeddings to visualize them as arrays in Browser for a simpler and more intuitive representation.
- [#3069](https://github.com/RedisInsight/RedisInsight/pull/3069) UX enhancements in the database list page for an improved user experience, leading to a cleaner layout and easier navigation.
- [#3151](https://github.com/RedisInsight/RedisInsight/pull/3151) Launch RedisInsight with the previously used window size.

**Bugs**
- [#3152](https://github.com/RedisInsight/RedisInsight/pull/3152), [#3156](https://github.com/RedisInsight/RedisInsight/pull/3156) A fix to [support the * wildcard](https://github.com/RedisInsight/RedisInsight/issues/3146) in Stream IDs.
- [#3174](https://github.com/RedisInsight/RedisInsight/pull/3174) Display invalid JSONs as unformatted values when a JSON view is set in Workbench results.
