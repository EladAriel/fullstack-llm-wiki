---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/map.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.265378Z"
---
# Map

---
Title: Map
alwaysopen: false
categories:
- docs
- operate
- stack
description: Maps records one-to-one.
linkTitle: map
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/map/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public <I extends java.io.Serializable> GearsBuilder<I> map​(
	gears.operations.MapOperation<T,​I> mapper)
```

Maps each input record in the pipe to an output record, one-to-one.

## Parameters
 
Type parameters:

| Name | Description |
|------|-------------|
| I | The template type of the returned builder |

Function parameters:

| Name | Type | Description |
|------|------|-------------|
| mapper | <nobr>MapOperation<T,​I></nobr> | For each input record, returns a new output record |

## Returns

Returns a GearsBuilder object with a new template type.

## Example

Map each record to its string value:

```java
GearsBuilder.CreateGearsBuilder(reader).
 		map(r->{
    		return r.getStringVal();
});
```
