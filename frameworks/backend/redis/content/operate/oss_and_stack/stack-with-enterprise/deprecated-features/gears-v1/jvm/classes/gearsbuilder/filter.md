---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/filter.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Filter
alwaysopen: false
categories:
- docs
- operate
- stack
description: Filters out records in the pipe based on a given condition.
linkTitle: filter
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/filter/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public GearsBuilder<T> filter​(
    gears.operations.FilterOperation<T> filter)
```

Filters out records in the pipe based on a given condition.

The filter operation should contain a conditional statement and return a boolean for each record:
- If `true`, the record will continue through the pipe. 
- If `false`, it filters out the record.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| filter | FilterOperation<T> | A function that checks a condition for each record in the pipe. Returns a boolean. |

## Returns

Returns a GearsBuilder object with the same template type as the input builder.

## Example

Get all records that contain the substring "person:":

```java
GearsBuilder.CreateGearsBuilder(reader).
    filter(r->{
        return r.getKey().contains("person:");
});
```