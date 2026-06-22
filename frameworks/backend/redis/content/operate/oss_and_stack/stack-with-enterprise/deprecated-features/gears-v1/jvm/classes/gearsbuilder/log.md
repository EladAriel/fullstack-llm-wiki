---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/log.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Log
alwaysopen: false
categories:
- docs
- operate
- stack
description: Writes a log message to the Redis log file.
linkTitle: log
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/log/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public static void log​(java.lang.String msg)

public static void log​(java.lang.String msg, LogLevel level)
```

Writes a log message to the Redis log file. If you do not specify a `LogLevel`, it will default to `NOTICE`.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| msg | string | The message to write to the log |
| level | LogLevel | The log level (DEBUG, NOTICE, VERBOSE, WARNING) |

## Returns

None

## Example

```java
GearsBuilder.log(
    "Setting keys to expire after 1 month", 
    LogLevel.WARNING
);
```