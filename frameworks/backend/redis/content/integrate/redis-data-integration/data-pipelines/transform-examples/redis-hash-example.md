---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/data-pipelines/transform-examples/redis-hash-example.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Write to a Redis hash
aliases: /integrate/redis-data-integration/ingest/data-pipelines/transform-examples/redis-hash-example/
alwaysopen: false
categories:
- docs
- integrate
- rs
- rdi
description: null
group: di
linkTitle: Write to a Redis hash
summary: Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 30
---

In the following example, the data is captured from the source table named `invoice` and is written to the Redis database as hash keys. The `connection` is an optional parameter that refers to the corresponding connection name defined in `config.yaml`. 
When you specify the `data_type` parameter for the job, it overrides the system-wide setting `target_data_type` defined in `config.yaml`. 

In this case, the result will be Redis hashes with key names based on the key expression (for example, `invoice_id:1`) and with an expiration of 100 seconds.
If you don't supply an `expire` parameter, the keys will never expire. 

```yaml
name: Write invoice to hash
source:
  schema: public
  table: invoice
output:
  - uses: redis.write
    with:
      connection: target
      data_type: hash
      key:
        expression: concat(['invoice_id:', InvoiceId])
        language: jmespath
      expire: 100
```
