---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/tools/insight/release-notes/v.2.14.0.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.819789Z"
---
# V.2.14.0

---
Title: RedisInsight v2.14.0, November 2022
linkTitle: v2.14.0 (Nov 2022)
date: 2022-11-28 00:00:00 +0000
description: RedisInsight v2.14.0
weight: 3
aliases:
- /develop/connect/insight/release-notes/v.2.14.0/
---
## 2.14.0 (November 2022)
This is the General Availability (GA) release of RedisInsight 2.14.

### Highlights
- Support for [search capabilities](https://redis.io/docs/stack/search/) in Browser: Create secondary index via dedicated form, run queries and full-text search in Browser or Tree views
- Ability to resize the column width of key values when displaying hashes, lists, and sorted sets
- Command processing time displayed as part of the result in Workbench


### Details
**Features and improvements**
- [#1345](https://github.com/RedisInsight/RedisInsight/pull/1345), [#1346](https://github.com/RedisInsight/RedisInsight/pull/1346), [#1376](https://github.com/RedisInsight/RedisInsight/pull/1376) Added support for [search capabilities](https://redis.io/docs/stack/search/) in Browser tool. Create secondary index of your data using a dedicated form. Conveniently run your queries and full-text search against the preselected index and display results in Browser or Tree views. 
- [#1385](https://github.com/RedisInsight/RedisInsight/pull/1385) Resize the column width of key values when displaying hashes, lists, and sorted sets
- [#1354](https://github.com/RedisInsight/RedisInsight/pull/1407) Do not scroll to the end of results when double-clicking a command output in CLI
- [#1347](https://github.com/RedisInsight/RedisInsight/pull/1347) Display command processing time as part of the result in Workbench (time taken to process the command by both RedisInsight backend and Redis)
- [#1351](https://github.com/RedisInsight/RedisInsight/pull/1351) Display the namespaces section in the Database analysis report when no namespaces were found
