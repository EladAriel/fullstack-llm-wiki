---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisbloom/redisbloom-1.0-release-notes.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
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
