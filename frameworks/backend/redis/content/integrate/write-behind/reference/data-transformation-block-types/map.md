---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/write-behind/reference/data-transformation-block-types/map.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: map
aliases: null
alwaysopen: false
categories:
  - docs
  - integrate
  - rs
  - rdi
description: Map a record into a new output based on expressions
group: di
linkTitle: map
summary:
  Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 10
---

Map a record into a new output based on expressions

**Properties**

| Name                          | Type               | Description                                   | Required |
| ----------------------------- | ------------------ | --------------------------------------------- | -------- |
| [**expression**](#expression) | `object`, `string` | Expression<br/>                               | yes      |
| **language**                  | `string`           | Language<br/>Enum: `"jmespath"`, `"sql"`<br/> | yes      |

**Additional Properties:** not allowed

**Example**

```yaml
source:
  server_name: redislabs
  schema: dbo
  table: emp
transform:
  - uses: map
    with:
      expression:
        first_name: first_name
        last_name: last_name
        greeting: >-
          'Hello ' || CASE WHEN gender = 'F' THEN 'Ms.' WHEN gender = 'M' THEN 'Mr.'
          ELSE 'N/A' END || ' ' || full_name
        country: country
        full_name: full_name
      language: sql
```

**Example**

```yaml
source:
  table: customer
transform:
  - uses: map
    with:
      expression: |
        {
          "CustomerId": customer_id,
          "FirstName": first_name,
          "LastName": last_name,
          "Company": company,
          "Location":
          {
            "Street": address,
            "City": city,
            "State": state,
            "Country": country,
            "PostalCode": postal_code
          },
          "Phone": phone,
          "Fax": fax,
          "Email": email
        }
      language: jmespath
```

<a name="expression"></a>

## expression: object

Expression

**No properties.**
