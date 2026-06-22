---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/tools/insight/release-notes/v.2.44.0.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: RedisInsight v2.44.0, February 2024
linkTitle: v2.44.0 (February 2024)
date: 2024-02-29 00:00:00 +0000
description: RedisInsight v2.44
weight: 1
---
## 2.44 (February 2024)
This is the General Availability (GA) release of RedisInsight 2.44.

### Highlights
- Added support for SSH tunneling for clustered databases, unblocking some users who want to migrate from RESP.app to RedisInsight.
- UX optimizations in the Browser layout to make it easier to leverage [search and query](https://redis.io/docs/interact/search-and-query/?utm_source=redisinsight&utm_medium=main&utm_campaign=redisinsight_release_notes) indexes.

### Details

**Features and improvements**
- [#2711](https://github.com/RedisInsight/RedisInsight/pull/2711), [#3040](https://github.com/RedisInsight/RedisInsight/pull/3040) Connect to your clustered Redis database via SSH tunnel using a password or private key in PEM format.
- [#3030](https://github.com/RedisInsight/RedisInsight/pull/3030), [#3070](https://github.com/RedisInsight/RedisInsight/pull/3070) UX optimizations in the Browser layout to enlarge the "Filter by Key" input field in the Browser and optimize the display of long [search and query](https://redis.io/docs/interact/search-and-query/?utm_source=redisinsight&utm_medium=main&utm_campaign=redisinsight_release_notes) indexes.
- [#3033](https://github.com/RedisInsight/RedisInsight/pull/3033), [#3036](https://github.com/RedisInsight/RedisInsight/pull/3036) Various improvements for custom [tutorials](https://github.com/RedisInsight/Tutorials), including visual highlighting of Redis code blocks and strengthening security measures for bulk data uploads by providing an option to download and preview the list of commands for upload.
- [#3010](https://github.com/RedisInsight/RedisInsight/pull/3010) Enhancements to prevent authentication errors caused by [certain special characters](https://github.com/RedisInsight/RedisInsight/issues/3019) in database passwords. 

**Bugs**
- [#3029](https://github.com/RedisInsight/RedisInsight/pull/3029) A fix for cases when autofill [prevents](https://github.com/RedisInsight/RedisInsight/issues/3026) the form to auto-discover Redis Software Cluster database from being submitted.
