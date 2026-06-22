---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/write-behind/reference/data-transformation-block-types/remove_field.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: remove_field
aliases: null
alwaysopen: false
categories:
  - docs
  - integrate
  - rs
  - rdi
description: Remove fields
group: di
linkTitle: remove_field
summary:
  Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 10
---

Remove fields

**Option 1 (alternative):**
Remove multiple fields

**Properties**

| Name                         | Type       | Description | Required |
| ---------------------------- | ---------- | ----------- | -------- |
| [**fields**](#option1fields) | `object[]` | Fields<br/> | yes      |

**Additional Properties:** not allowed

**Example**

```yaml
source:
  server_name: redislabs
  schema: dbo
  table: emp
transform:
  - uses: remove_field
    with:
      fields:
        - field: credit_card
        - field: name.mname
```

**Option 2 (alternative):**
Remove one field

**Properties**

| Name      | Type     | Description | Required |
| --------- | -------- | ----------- | -------- |
| **field** | `string` | Field<br/>  | yes      |

**Additional Properties:** not allowed  
**Example**

```yaml
source:
  server_name: redislabs
  schema: dbo
  table: emp
transform:
  - uses: remove_field
    with:
      field: credit_card
```

<a name="option1fields"></a>

## Option 1: fields\[\]: array

Fields

**Items**

**Item Properties**

| Name      | Type     | Description | Required |
| --------- | -------- | ----------- | -------- |
| **field** | `string` | Field<br/>  | yes      |

**Item Additional Properties:** not allowed

**Example**

```yaml
- {}
```
