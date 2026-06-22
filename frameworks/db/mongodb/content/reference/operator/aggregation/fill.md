---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/fill.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# $fill (aggregation stage)

## Definition

## Syntax

The :pipeline:`$fill` stage has this syntax:

```none
{
   $fill: {
      partitionBy: <expression>,
      partitionByFields: [ <field 1>, <field 2>, ... , <field n> ],
      sortBy: {
         <sort field 1>: <sort order>,
         <sort field 2>: <sort order>,
         ...,
         <sort field n>: <sort order>
      },
      output: {
         <field 1>: { value: <expression> },
         <field 2>: { method: <string> },
         ...
      }
   }
}
```

The :pipeline:`$fill` stage takes a document with these fields:

## Behavior and Restrictions

### `partitionByFields` Restrictions

:pipeline:`$fill` returns an error if any field name in the `partitionByFields <fill-partitionBy-fields>` array:

- Evaluates to a non-string value.
- Begins with `$`.
### `linear` Behavior

The `linear` fill method fills `null` and missing fields using |linear-interpolation| based on the surrounding non-`null` values in the sequence.

- For each document where the field is `null` or missing,
`linearFill` fills those fields in proportion to the missing value range between surrounding non-`null` values according to the `sortBy <fill-sortBy>` order. To determine the values for missing fields, `linearFill` uses:

- The difference of surrounding non-`null` values.
- The number of `null` fields to fill between the surrounding
values.

- The `linear` method can fill multiple consecutive `null` values
if those values are preceded and followed by non-`null` values according to the `sortBy <fill-sortBy>` order.

- `null` values that are not preceded and followed by non-`null`
values remain `null`.

- To use the `linear` fill method, you must also use the :ref:`sortBy
<fill-sortBy>` field to sort your data.

- When using the `linear` fill method, :pipeline:`$fill` returns an
error if there are any repeated values in the `sortBy <fill-sortBy>` field in a single partition.

For a complete example using the `linear` fill method, see `fill-example-linear`.

### `locf` Behavior

`locf` stands for last observation carried forward.

- If a field being filled contains both `null` and non-null values,
`locf` sets the `null` and missing values to the field's last known non-null value according to the `sortBy <fill-sortBy>` order.

- If the field contains only `null` or missing values in a
`partition <fill-partitionBy>`, `locf` sets the field value to `null` for that partition.

- `null` and missing field values that appear before non-null values
in the sort order remain `null`.

- To use the `locf` fill method, you must also use the :ref:`sortBy
<fill-sortBy>` field to sort your data.

For a complete example using the `locf` fill method, see `fill-example-locf`.

### Comparison of `$fill` and Aggregation Operators

To fill `null` and missing field values within a document you can use:

- The :pipeline:`$fill` stage.
When you use the :pipeline:`$fill` stage, the field you specify in the output is the same field used as the source data.

- The :group:`$linearFill` and :group:`$locf` aggregation operators.
When you :group:`$linearFill` or :group:`$locf`, you can set values for a different field than the field used as the source data.

## Examples
