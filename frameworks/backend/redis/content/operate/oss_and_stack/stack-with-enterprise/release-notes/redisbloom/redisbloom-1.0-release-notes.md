---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisbloom/redisbloom-1.0-release-notes.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: RedisBloom 1.0 release notes
alwaysopen: false
categories:
- docs
- operate
- stack
description: First GA release of RedisBloom.
linkTitle: v1.0 (September 2017)
min-version-db: 4.0.0
min-version-rs: 5.0.0
weight: 100
---
## Requirements

RedisBloom v1.0.3 requires:

- Minimum Redis compatibility version (database): 4.0
- Minimum Redis Enterprise Software version (cluster): 5.0

## v1.0.3 (December 2017)

This contains a single fix, issue #[19](https://github.com/RedisBloom/RedisBloom/issues/19).

From this version onwards, `EXISTS`/`MEXISTS` returns 0 if the (Redis) key does not exist in the database.  Earlier versions returned an error.

## v1.0.2 (November 2017)

This fixes a build issue (fixed s3 config in circle yaml).

## v1.0.0 (September 2017)

This is the first GA release of ReBloom.
