---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/tools/insight/release-notes/v.2.30.0.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: RedisInsight v2.30.0, July 2023
linkTitle: v2.30.0 (July 2023)
date: 2023-07-27 00:00:00 +0000
description: RedisInsight v2.30
weight: 1
---
## 2.30 (July 2023)
This is the General Availability (GA) release of RedisInsight 2.30.

### Highlights
Introducing support for [triggers and functions](https://github.com/RedisGears/RedisGears/) that bring application logic closer to your data and give Redis powerful features for event-driven data processing

### Details

**Features and improvements**

[#2247](https://github.com/RedisInsight/RedisInsight/pull/2247), [#2249](https://github.com/RedisInsight/RedisInsight/pull/2249), [#2273](https://github.com/RedisInsight/RedisInsight/pull/2273), [#2279](https://github.com/RedisInsight/RedisInsight/pull/2279) Support for [triggers and functions](https://github.com/RedisGears/RedisGears/) that add the capability to execute server-side functions triggered by events or data operations to:
 - Speed up applications by running the application logic where the data lives
 - Eliminate the need to maintain the same code across different applications by moving application functionality inside the Redis database
 - Maintain consistent data when applications react to any keyspace change
 - Improve code resiliency by backing up and replicating triggers and functions along with the database

Triggers and functions work with a JavaScript engine, which lets you take advantage of JavaScript’s vast ecosystem of libraries and frameworks and modern, expressive syntax.
