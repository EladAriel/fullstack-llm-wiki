---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/log.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.267684Z"
---
# Log

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