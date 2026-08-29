---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/foreach.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.267339Z"
---
# Foreach

---
Title: Foreach
alwaysopen: false
categories:
- docs
- operate
- stack
description: For each record in the pipe, runs some operations.
linkTitle: foreach
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/foreach/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public GearsBuilder<T> foreach​(
    gears.operations.ForeachOperation<T> foreach)
```

Defines a set of operations to run for each record in the pipe.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| foreach | ForeachOperation<T> | The set of operations to run for each record |

## Returns

Returns a GearsBuilder object with a new template type.

## Example

For each person hash, add a new full_name field that combines their first and last names:

```java
GearsBuilder.CreateGearsBuilder(reader).foreach(r->{
    String firstName = r.getHashVal().get("first_name");
    String lastName = r.getHashVal().get("last_name");
   	r.getHashVal().put("full_name", firstName + lastName);
}); 
```