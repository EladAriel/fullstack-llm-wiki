---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/data-pipelines/transform-examples/redis-hash-example.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.181323Z"
---
# Redis Hash Example

---
Title: Write to a Redis hash
aliases:
- /integrate/redis-data-integration/ingest/data-pipelines/transform-examples/redis-hash-example/
- /integrate/redis-data-integration/data-transformation/examples/redis-hash-example/
- /integrate/redis-data-integration/ingest/data-transformation/examples/redis-hash-example/
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
