---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/data-pipelines/transform-examples/redis-writing-to-multiple-keys.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Writing to multiple keys
alwaysopen: false
categories:
  - docs
  - integrate
  - rs
  - rdi
description: null
group: di
linkTitle: Writing to multiple keys
summary: Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 100
---

If you want to write results to multiple keys, you can do so by defining multiple `redis.write` subsections in the `output` section of the job file. Each instance of `redis.write` can specify a different key, data format, and other parameters. For example, you can create two different keys for the same data, one with a default key format and another with a custom key format and mapping.

```yaml
name: Write to multiple keys with different formats
output:
  - uses: redis.write
    with:
      # Setting data_type to JSON and using the default key format
      data_type: json

  - uses: redis.write
    with:
      data_type: json

      # Defining a custom key format
      key:
        language: jmespath
        expression: concat(['events-simplified:id:', id])

      # And defining a custom mapping
      mapping:
        - id: id
        - name: name
        - location: location
```
