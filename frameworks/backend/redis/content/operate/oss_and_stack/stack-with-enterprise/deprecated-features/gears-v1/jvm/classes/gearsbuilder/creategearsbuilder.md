---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/creategearsbuilder.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: CreateGearsBuilder
alwaysopen: false
categories:
- docs
- operate
- stack
description: Creates a new GearsBuilder object.
linkTitle: CreateGearsBuilder
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/creategearsbuilder/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public static <I extends java.io.Serializable> GearsBuilder<I> CreateGearsBuilder​(
    gears.readers.BaseReader<I> reader)

public static <I extends java.io.Serializable> GearsBuilder<I> CreateGearsBuilder​(
    gears.readers.BaseReader<I> reader, 
    java.lang.String desc)
```

Creates a new `GearsBuilder` object. Use this function instead of a `GearsBuilder` constructor to avoid type warnings.

## Parameters

Type Parameters:

| Name | Description |
|------|-------------|
| I | The template type of the returned builder. The reader determines the type. |

Parameters:

| Name | Type | Description |
|------|------|-------------|
| desc | string | The description |
| reader | BaseReader<I> | The pipe reader |

## Returns

Returns a new GearsBuilder object.

## Example

```java
GearsBuilder.CreateGearsBuilder(reader);
```