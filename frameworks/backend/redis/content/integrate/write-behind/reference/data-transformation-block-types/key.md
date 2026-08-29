---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/write-behind/reference/data-transformation-block-types/key.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.200876Z"
---
# Key

---
Title: key
aliases:
- /integrate/redis-data-integration/reference/data-transformation-block-types/key/
- /integrate/redis-data-integration/write-behind/reference/data-transformation-block-types/key/
alwaysopen: false
categories:
  - docs
  - integrate
  - rs
  - rdi
description: Set the Redis key for this data entry
group: di
linkTitle: key
summary:
  Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 10
---

Set the Redis key for this data entry

**Properties**

| Name           | Type     | Description                                   | Required |
| -------------- | -------- | --------------------------------------------- | -------- |
| **expression** | `string` | Expression<br/>                               | yes      |
| **language**   | `string` | Language<br/>Enum: `"jmespath"`, `"sql"`<br/> | yes      |

**Additional Properties:** not allowed

**Example**

```yaml
source:
  server_name: redislabs
  schema: dbo
  table: emp
key:
  expression: concat([InvoiceId, '.', CustomerId])
  language: jmespath
```
