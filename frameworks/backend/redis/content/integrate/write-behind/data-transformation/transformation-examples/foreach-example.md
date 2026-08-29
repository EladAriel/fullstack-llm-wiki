---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/write-behind/data-transformation/transformation-examples/foreach-example.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.194794Z"
---
# Foreach Example

---
Title: Write-behind foreach example
aliases:
- /integrate/redis-data-integration/data-transformation/examples/foreach-example/
- /integrate/redis-data-integration/ingest/data-transformation/examples/foreach-example/
- /integrate/redis-data-integration/write behind/foreach-example/
- /integrate/redis-data-integration/write-behind/foreach-example/
- /integrate/redis-data-integration/write-behind/data-transformation/transformation-examples/foreach-example/
alwaysopen: false
categories:
- docs
- integrate
- rs
- rdi
description: null
group: di
linkTitle: Write-behind foreach
summary: Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 30
---


The `foreach` section is used to explode a list of objects or arrays to rows in a selected target.
The `foreach` expression is structured as `<field_name>:<JMESPath expression>`.
The following example uses the `add_field` transformation to prepare the input JSON to the desired structure. Then, it applies `foreach` to write each `order` object as a relational database record using `keys` and `mapping`.
In this example, the `JMESPath` function `to_string` is used to flatten an array of objects, `specs`, to a string.

```yaml
source:
  redis:
    key_pattern: orderdetail:*
    trigger: write-behind
    exclude_commands: ["json.del"]
transform:
  - uses: add_field
    with:
      fields:
        - field: my_orders
          language: jmespath
          expression: |
            orders[*].{
              code: code
              periodStartTime: periodStartTime
              periodEndTime: periodEndTime
              specs: to_string(specs)
            }
output:
  - uses: relational.write
    with:
      connection: mssql
      schema: dbo
      table: OrderMaster
      keys:
        - Code: orderDetail.code
      mapping:
        - DeliveryDate: orderDetail.deliveryDate
        - ProductCode: orderDetail.productCode
        - CountryCode: orderDetail.countryCode
  - uses: relational.write
    with:
      connection: mssql
      schema: dbo
      table: Order
      foreach: "order: my_orders[]"
      keys:
        - Code: order.code
      mapping:
        - OrderDetailCode: orderDetail.code
        - PeriodStartTime: order.periodStartTime
        - PeriodEndTime: order.periodEndTime
        - Specs: order.specs

```