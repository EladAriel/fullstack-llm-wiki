---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/commands/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.261898Z"
---
# _Index

---
Title: RedisGears JVM commands
alwaysopen: false
categories:
- docs
- operate
- stack
description: 
hideListLinks: true
linkTitle: Commands
toc: 'false'
weight: 40
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/commands/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
bannerChildren: true
---

Use a Redis client like `redis-cli` to send commands to the RedisGears JVM plugin.

## JVM plugin commands

{{<table-children columnNames="Command,Description" columnSources="LinkTitle,Description" enableLinks="LinkTitle">}}

{{<note>}}
Ignore any commands that start with `RG.PY` while using the JVM plugin. The `RG.PY` commands are for the Python plugin.
{{</note>}}