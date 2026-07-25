---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/count.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Count
alwaysopen: false
categories:
- docs
- operate
- stack
description: Counts the number of records in the pipe.
linkTitle: count
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/count/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public GearsBuilder<java.lang.Integer> count()
```

Counts the number of records in the pipe and returns the total as a single record.

## Parameters
 
None

## Returns

Returns a GearsBuilder object with a new template type of `Integer`.

## Example

```java
GearsBuilder.CreateGearsBuilder(reader).count();
```