---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/shardsidreader.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: ShardsIDReader
alwaysopen: false
categories:
- docs
- operate
- stack
description: Gets the shard ID for each shard in a database.
linkTitle: ShardsIDReader
weight: 60
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/readers/shardsidreader/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

The `ShardsIDReader` creates a single record on each shard that represents the current shard's ID.
 
Use this reader when you want to run an operation on each shard in the database.

## Parameters

None

## Output records

Creates a record for each shard with the shard's cluster identifier.

## Example

```java
ShardsIDReader reader = new ShardsIDReader();
```