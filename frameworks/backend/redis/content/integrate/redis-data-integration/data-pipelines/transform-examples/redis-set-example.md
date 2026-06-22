---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/data-pipelines/transform-examples/redis-set-example.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Write to a Redis set
aliases: /integrate/redis-data-integration/ingest/data-pipelines/transform-examples/redis-set-example/
alwaysopen: false
categories:
- docs
- integrate
- rs
- rdi
description: null
group: di
linkTitle: Write to a Redis set
summary: Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 30
---

In the example below, data is captured from the source table named `invoice` and is written to a Redis set. The `connection` is an optional parameter that refers to the corresponding connection name defined in `config.yaml`. When you specify the
`data_type` parameter for the job, it overrides the system-wide setting `target_data_type` defined in `config.yaml`.

{{< note >}}The `set` data type is supported by the classic processor only.
The Flink processor currently supports only `hash` and `json` outputs.{{< /note >}}

When writing to a set, you must supply an extra argument, `member`, which specifies the field that will be written. In this case, the result will be a Redis set with key names based on the key expression (for example, `invoices:Germany`, `invoices:USA`) and with an expiration of 100 seconds. If you don't supply an `expire` parameter, the keys will never expire.    

```yaml
name: Write invoices to set by country
source:
  schema: public
  table: invoice
output:
  - uses: redis.write
    with:
      connection: target
      data_type: set
      key:
        expression: concat(['invoices:', BillingCountry])
        language: jmespath
      args:
        member: InvoiceId
      expire: 100
```
