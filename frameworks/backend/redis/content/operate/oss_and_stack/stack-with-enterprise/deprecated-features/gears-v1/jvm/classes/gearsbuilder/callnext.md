---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/callnext.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.265197Z"
---
# Callnext

---
Title: CallNext
alwaysopen: false
categories:
- docs
- operate
- stack
description: Calls the next execution that overrides the command or the original command
  itself. A more flexible version of callNextArray.
linkTitle: callNext
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/callnext/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public static java.lang.Object callNext(java.lang.String... args)
```

When you override a Redis command with the [`CommandOverrider`]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/commandoverrider" >}}), use `callNext` to run the next execution that overrides the command or the original command itself.

It is a more flexible version of [`callNextArray`]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/callNextArray" >}}) since the list of string arguments does not have to be an explicit `String[]` object. This allows function calls like: <nobr>`callNext("key", "value")`.</nobr>

## Parameters

| Name | Type | Description |
|------|------|-------------|
| args | string | Redis command arguments |

## Returns

Returns the command result. It could be a string or an array of strings, depending on the command.

## Examples

Without `String[]`:

```java
GearsBuilder.callNext("restaurant:1", "reviews", "50");
```

With `String[]`:

```java
GearsBuilder.callNext(new String[]{"restaurant:1", "reviews", "50"});
```
