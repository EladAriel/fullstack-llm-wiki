---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/execute.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Execute
alwaysopen: false
categories:
- docs
- operate
- stack
description: Runs a Redis command. A more flexible version of executeArray.
linkTitle: execute
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/execute/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public static java.lang.Object execute​(java.lang.String... command)
```

Runs a Redis command, similar to [`executeArray`]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/executeArray" >}}). However, the `execute` function is more flexible. Unlike `executeArray`, the list of string arguments does not have to be an explicit `String[]` object. It allows function calls like this: <nobr>`execute("SET", "key", "value")`.</nobr>

## Parameters

| Name | Type | Description |
|------|------|-------------|
| command | string | A Redis command |

## Returns

Returns the command result. It could be a string or an array of strings, depending on the command.

## Examples

Without `String[]`:

```java
GearsBuilder.execute("SET", "age:maximum", "100");
```

With `String[]`:

```java
GearsBuilder.execute(new String[]{"SET", "age:maximum", "100"});
```
