---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/flatmap.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: FlatMap
alwaysopen: false
categories:
- docs
- operate
- stack
description: Maps a single input record to one or more output records.
linkTitle: flatMap
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/flatmap/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public <I extends java.io.Serializable> GearsBuilder<I> flatMap​(
	gears.operations.FlatMapOperation<T,​I> flatmapper)
```

Maps a single input record to one or more output records.

The FlatMap operation must return an [`Iterable`](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html). RedisGears 
splits the elements from the `Iterable` object and processes them as individual records.

## Parameters
 
Type parameters:

| Name | Description |
|------|-------------|
| I | The template type of the returned builder object |

Function parameters:

| Name | Type | Description |
|------|------|-------------|
| flatmapper | <nobr>FlatMapOperation<T,​I></nobr> | For each input record, returns one or more output records |

## Returns

Returns a GearsBuilder object with a new template type.

## Example

```java
GearsBuilder.CreateGearsBuilder(reader).flatMap(r->{
   	return r.getListVal();
}); 
```