---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/collect.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.268795Z"
---
# Collect

---
Title: Collect
alwaysopen: false
categories:
- docs
- operate
- stack
description: Collects all records to the origin shard.
linkTitle: collect
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/collect/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public GearsBuilder<T> collect()
```

Collects all of the records to the shard where the RedisGears job started.

## Parameters
 
None

## Returns

Returns a GearsBuilder object with the same template type as the input builder.

## Example

```java
GearsBuilder.CreateGearsBuilder(reader).collect();
```