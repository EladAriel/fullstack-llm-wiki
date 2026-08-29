---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/data-pipelines/transform-examples/redis-write-same-key.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.179893Z"
---
---
Title: Write to the same key from multiple jobs
alwaysopen: false
categories:
- docs
- integrate
- rs
- rdi
description: null
group: di
linkTitle: Write to the same key
summary: Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 100
---

Use this pattern when two or more jobs write related source entities, such as
`customer` and `address`, to the same Redis JSON document.

When multiple jobs write to the same Redis key, a delete event from any of the
source entities can delete the key from the target. To work around this, use
[`row_format: full`]({{< relref "/integrate/redis-data-integration/data-pipelines/transform-examples/redis-row-format#full" >}})
so the job can inspect the
[`opcode`]({{< relref "/integrate/redis-data-integration/data-pipelines/transform-examples/redis-opcode-example" >}}),
convert delete events into update events before writing to Redis, and write JSON
documents with `on_update: merge`.

{{< note >}}
Use the same key expression in all jobs that write to the shared Redis key. For
delete events, read key values from `before` or `key` because `after` is `null`.
{{< /note >}}

## Customer job

```yaml
# jobs/customer.yaml
name: customers

source:
  table: customers

output:
  - uses: redis.write
    with:
      data_type: json
      on_update: merge
      key:
        expression: concat(['customer:', id])
        language: jmespath

```

## Address job

For delete events from the `addresses` table, this job sets all fields to `null`
to instruct RDI to remove them from the target JSON document. This behavior is
available in RDI 1.15.0 or later when native JSON merge is enabled and the target
database uses RedisJSON 2.6.0 or later.

```yaml
# jobs/addresses.yaml
name: addresses

source:
  table: addresses
  row_format: full

transform:
  - uses: add_field
    with:
      fields:
        # For create/update records, we take the new values as is.
        # If the record is a deletion, we set all fields to null.
        - field: after
          expression: |
            (opcode != 'd' && after) 
              || 
            from_entries(to_entries(before)[].{key: key, value: `null`})
          language: jmespath

        # Treat deletes as updates so that we can use the same output configuration
        - field: opcode
          expression: opcode == 'd' && 'u' || opcode
          language: jmespath

  # If you have overlapping field names (for example, FK and PK have the same name, or both tables have
  # a field called "id"), you may want to remove the field from the after object to prevent it
  # from overwriting the PK.
  - uses: remove_field
    with:
      field: after.id

output:
  - uses: redis.write
    with:
      data_type: json
      on_update: merge
      key:
        expression: concat(['customer:', after.customer_id || before.customer_id])
        language: jmespath
```
