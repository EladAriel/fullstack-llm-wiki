---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: GearsBuilder
alwaysopen: false
categories:
- docs
- operate
- stack
description: Creates a RedisGears pipeline of operations to transform data.
hideListLinks: true
linkTitle: GearsBuilder
toc: 'false'
weight: 60
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
bannerChildren: true
---

The `GearsBuilder` class allows you to create a pipeline of RedisGears functions that transform data.

It requires a reader to supply data to the pipe.

To create a `GearsBuilder` object, follow this example code:

```java
BaseReader reader = ...; // Initialize the reader
builder = GearsBuilder.CreateGearsBuilder(reader);
```

## Functions

{{<table-children columnNames="Function,Description" columnSources="LinkTitle,Description" enableLinks="LinkTitle">}}