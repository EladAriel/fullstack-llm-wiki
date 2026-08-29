---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsfuture/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.263107Z"
---
# _Index

---
Title: GearsFuture
alwaysopen: false
categories:
- docs
- operate
- stack
description: Allows asynchronous processing of records.
hideListLinks: true
linkTitle: GearsFuture
weight: 60
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsfuture/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
bannerChildren: true
---

The `GearsFuture` class allows asynchronous processing of records in another thread.

You can use a `GearsFuture` object with the following [`GearsBuilder`]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder" >}}) functions:

- [`asyncFilter`]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/asyncfilter" >}})
- [`asyncForeach`]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/asyncforeach" >}})
- [`asyncMap`]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/asyncmap" >}})

## Functions

{{<table-children columnNames="Function,Description" columnSources="LinkTitle,Description" enableLinks="LinkTitle">}}