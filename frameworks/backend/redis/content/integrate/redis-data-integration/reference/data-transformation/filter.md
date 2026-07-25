---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-data-integration/reference/data-transformation/filter.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: filter
aliases: /integrate/redis-data-integration/ingest/reference/data-transformation/filter/
alwaysopen: false
categories:
  - docs
  - integrate
  - rs
  - rdi
description: Filter records
group: di
linkTitle: filter
summary:
  Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 10
---

Filter records

**Properties**

| Name           | Type     | Description                                                                                                                                                                                            | Required |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| **expression** | `string` | Expression<br/>                                                                                                                                                                                        | yes      |
| **language**   | `string` | Language<br/>Enum: `"jmespath"`, `"sql"`<br/>                                                                                                                                                          | yes      |
| **cache**      | `object` | Cache the result of the filter expression. See [`cache`]({{< relref "/integrate/redis-data-integration/reference/data-transformation/cache" >}}) for the property list. **Flink processor only.**<br/> | no       |

**Additional Properties:** not allowed

**Example**

```yaml
source:
  schema: dbo
  table: emp
transform:
  - uses: filter
    with:
      language: sql
      expression: age>20
```
