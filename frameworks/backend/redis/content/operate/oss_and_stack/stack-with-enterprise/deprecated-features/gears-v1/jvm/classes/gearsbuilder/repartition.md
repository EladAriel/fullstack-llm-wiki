---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/repartition.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.268971Z"
---
# Repartition

---
Title: Repartition
alwaysopen: false
categories:
- docs
- operate
- stack
description: Moves records between shards according to the extracted data.
linkTitle: repartition
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/repartition/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public GearsBuilder<T> repartition​(
	gears.operations.ExtractorOperation<T> extractor)
```

Moves records between the shards. The extracted data determines the new shard location for each record.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| extractor | <nobr>ExtractorOperation<T></nobr> | Extracts a specific value from each record |

## Returns

Returns a GearsBuilder object with a new template type.

## Example

Repartition by value:

```java
GearsBuilder.CreateGearsBuilder(reader).
   	repartition(r->{
   		return r.getStringVal();
});
```