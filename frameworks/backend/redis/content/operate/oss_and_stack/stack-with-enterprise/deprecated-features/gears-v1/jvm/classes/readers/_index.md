---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.263681Z"
---
# _Index

---
Title: RedisGears readers
alwaysopen: false
categories:
- docs
- operate
- stack
description: Extracts data from the database and creates records to pass through a
  RedisGears pipeline.
hideListLinks: true
linkTitle: Readers
weight: 60
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/readers/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
bannerChildren: true
---

A reader extracts data from the database and creates records.

The [`GearsBuilder.CreateGearsBuilder(reader)`]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/creategearsbuilder" >}}) function takes a reader as a parameter and passes the generated records through a pipeline of RedisGears functions.

## Classes

{{<table-children columnNames="Class,Description" columnSources="LinkTitle,Description" enableLinks="LinkTitle">}}