---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/data-pipelines/transform-examples/redis-sorted-set-example.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Write to a Redis sorted set
aliases: /integrate/redis-data-integration/ingest/data-pipelines/transform-examples/redis-sorted-set-example/
alwaysopen: false
categories:
- docs
- integrate
- rs
- rdi
description: null
group: di
linkTitle: Write to a Redis sorted set
summary: Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 30
---

In the example below, data is captured from the source table named `invoice` and is written to a Redis sorted set. The `connection` is an optional parameter that refers to the corresponding connection name defined in `config.yaml`. When
you specify the `data_type` parameter for the job, it overrides the system-wide setting `target_data_type` defined in `config.yaml`.

{{< note >}}The `sorted_set` data type is supported by the classic processor only.
The Flink processor currently supports only `hash` and `json` outputs.{{< /note >}}

When writing to sorted sets, you must provide two additional arguments, `member` and `score`. These specify the field names that will be used as a member and a score to add an element to a sorted set. In this case, the result will be a Redis sorted set named `invoices:sorted` based on the key expression and with an expiration of 100 seconds for each set member. If you don't supply an `expire` parameter, the keys will never expire.

```yaml
name: Write invoices to sorted set by total
source:
  schema: public
  table: invoice
output:
  - uses: redis.write
    with:
      connection: target
      data_type: sorted_set
      key:
        expression: "`invoices:sorted`"
        language: jmespath
      args:
        score: Total
        member: InvoiceId
      expire: 100
```

Since sorted sets in Redis are inherently sorted, you can easily get the top N invoices by total invoice amount using the command below (the range 0..9 gets the top 10 invoices):

```
ZREVRANGE invoices:sorted 0 9 WITHSCORES
```
