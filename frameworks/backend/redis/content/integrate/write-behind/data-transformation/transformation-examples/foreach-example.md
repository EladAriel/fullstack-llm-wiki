---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/write-behind/data-transformation/transformation-examples/foreach-example.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Write-behind foreach example
aliases: null
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