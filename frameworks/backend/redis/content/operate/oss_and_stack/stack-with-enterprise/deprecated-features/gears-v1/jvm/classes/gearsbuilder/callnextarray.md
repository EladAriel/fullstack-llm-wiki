---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/callnextarray.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: CallNextArray
alwaysopen: false
categories:
- docs
- operate
- stack
description: Calls the next execution that overrides the command or the original command
  itself.
linkTitle: callNextArray
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/callnextarray/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public static native java.lang.Object callNextArray(
    java.lang.String[] command)
```

When you override a Redis command with the [`CommandOverrider`]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/commandoverrider" >}}), use `callNextArray` to run the next execution that overrides the command or the original command itself.

It accepts an array of strings, which represents the command arguments.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| args | array of strings | Redis command arguments |

## Returns

Returns the command result. It could be a string or an array of strings, depending on the command.

## Example

```java
GearsBuilder.callNextArray(new String[]{"restaurant:1", "reviews", "50"});
```