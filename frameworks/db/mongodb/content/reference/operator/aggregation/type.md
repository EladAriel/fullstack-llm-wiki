---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/type.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# $type  (expression operator)

## Definition

> **Seealso:** - :expression:`$isNumber` - checks if the argument is a number.
- :query:`$type (Query) <$type>` - filters fields based on BSON type.

## Behavior

### `$type`

Unlike the :query:`$type` query operator, which matches array elements based on their BSON type, the :expression:`$type` aggregation operator does not examine array elements. Instead, when passed an array as its argument, the `$type` aggregation operator returns the type of the argument, i.e. `"array"`.

If the argument is a field that is missing in the input document, :expression:`$type` returns the string `"missing"`.

The following table shows the :expression:`$type` output for several common types of expressions:

> **Note:** In the case of a literal array such as `[ 1, 2, 3 ]`,
enclose the expression in an outer set
of array brackets to prevent MongoDB from parsing
`[ 1, 2, 3 ]` as an
`argument list <agg-quick-ref-operator-expressions>`
with three arguments (`1, 2, 3`). Wrapping the array
`[ 1, 2, 3 ]` in a :expression:`$literal` expression
achieves the same result.
See :ref:`operator expression syntax forms
<agg-quick-ref-operator-expressions>` for more information.

### Available Types

.. include:: /includes/fact-bson-types.rst

If the argument is a field that is missing in the input document, :expression:`$type` returns the string `"missing"`.

## Example

This example uses a `collection <collection>` named `coll` with the following `documents <document>`:

The following aggregation operation uses the `$type` operator to display the type of field `a` for all documents as part of the :pipeline:`$project` stage.

### Existence Check

`Expressions <aggregation-expressions>` do not support the :query:`$exists` operator. To evaluate whether or not a field exists in an expression, you can use the `missing` type.

The following aggregation operation uses the `missing` type to add an `a` field to documents from the `coll` collection above that are missing the `a` field. Notice that a document where `a: null` is not the same as a document where the `a` field is missing.
