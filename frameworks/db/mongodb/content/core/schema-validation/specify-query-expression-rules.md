---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/schema-validation/specify-query-expression-rules.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================================

# Specify Validation With Query Operators

You can specify validation using query operators such as :query:`$eq` and :query:`$gt` to compare fields.

A common use case for schema validation with query operators is when you want to create dynamic validation rules that compare multiple field values at runtime. For example, if you have a field that depends on the value of another field and need to ensure that those values are correctly proportional to each other.

## Restrictions

- You can't specify the following :ref:`query operators
<query-selectors>` in a `validator` object:

- :query:`$expr` with :expression:`$function` expressions
- :query:`$near`
- :query:`$nearSphere`
- :query:`$text`
- :query:`$where`
- You can't specify schema validation for:
- Collections in the `admin`, `local`, and `config` databases
- `System collections <metadata-system-collections>`
## Context

Consider an application that tracks customer orders. The orders have a base price and a :abbr:`VAT (Value Added Tax)`. The `orders` collection contains these fields to track total price:

- `price`
- `VAT`
- `totalWithVAT`
## Steps

The following procedure creates a schema validation with query operators to ensure that `totalWithVAT` matches the expected combination of `price` and `VAT`.

## Additional Information

You can combine query operator validation with `JSON Schema validation <schema-validation-json>`.

.. include:: /includes/schema-validation-combine-validation-types.rst

## Learn More

- To see all query operators available in MongoDB, see
`query-selectors`.

- To learn more about the `$expr` operator, which allows the use of
aggregation expressions within the query language, see :query:`$expr`.
