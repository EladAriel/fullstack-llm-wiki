---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/meta.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# $meta (expression operator)

## Definition

## Behavior

### Text Score Metadata `$meta: "textScore"`

Requires $text Search `````````````````````

- The `{ $meta: "textScore" }` expression must be used in
conjunction with :query:`$text`. For example:

- In aggregation, you must specify a :pipeline:`$match` stage
with a `$text` query in the pipeline to use the `{ $meta: "textScore" }` expression in later stage(s). If you do not specify the `$text` query in the :pipeline:`$match` stage, the operation fails.

- In find, you must specify the `$text` operator in the
query predicate to use `{ $meta: "textScore" }`. If you do not specify the `$text` operator in the query predicate, the operation fails.

.. include:: /includes/text-search-legacy-atlas-section.rst

Availability ````````````

- In aggregation, the `{ $meta: "textScore" }` expression can
be included in various stages that accept aggregation expressions, such as :pipeline:`$project`, :pipeline:`$group` :pipeline:`$sort`, etc.

- In find, the `{ $meta: "textScore" }` expression can be
included in `projection <find-projection>` and in :method:`~cursor.sort()`.

Usage In Projection ```````````````````

- The `{ $meta: "textScore" }` expression can be a part of the
`projection` document to include the text score metadata.

- The :expression:`$meta` expression can be present in either an
inclusion or an exclusion projection.

- If you set the expression to a field name that already exists
in the document, the projected metadata value overwrites the existing value.

Filter on Text Score ````````````````````

- In aggregation, following a stage that outputs a field with
the text score value, you can specify a query condition or operate on the field in subsequent stages. For example, see `/tutorial/text-search-in-aggregation`.

- In find, you cannot specify a query condition on the text
score. Use aggregation instead.

Usage In Sort `````````````

- The `{ $meta: "textScore" }` expression can be used as a
part of a sort operation to sort by the text score metadata; i.e.,

- In aggregation, :pipeline:`$sort` stage.
- In find, :method:`~cursor.sort()` method.
- The `"textScore"` metadata sorts in descending order.
- To use in a sort operation, set the `{ $meta: "textScore" }`
expression to an arbitrary field name. The field name is disregarded by the query system.

Sort without Projection ```````````````````````

- In aggregation, you can sort the resulting documents by ``{
$meta: "textScore" }` without also having to project the `textScore``.

- In find, you can sort the resulting documents by `{ $meta: "textScore" }`
without also having to project the `textScore`.

Sort with Projection ````````````````````

- In aggregation, if you include the :expression:`{ $meta: "textScore" }
<$meta>` expression in both the projection and sort, the projection and sort can have different field names for the expression. The field name in the sort is disregarded by the query system.

- In find, if you include the :expression:`{ $meta: "textScore" } <$meta>`
expression in both the projection and sort, the projection and sort can have different field names for the expression. The field name in the sort is disregarded by the query system.

### Index Key Metadata $meta: "indexKey" (Aggregation and Find)

Usage `````

- The `{ $meta: "indexKey" }` expression is for debugging purposes
only and not for application logic.

- The `{ $meta: "indexKey" }` expression is preferred over
:method:`cursor.returnKey()`.

Availability ````````````

- **In aggregation**, the `{ $meta: "indexKey" }` expression can
be included in various stages that accept aggregation expressions, such as :pipeline:`$project`, :pipeline:`$group` :pipeline:`$sortByCount`, etc., but not :pipeline:`$sort`. However, with an aggregation pipeline, you can first project the `{ $meta: "indexKey" }` expression (such as in a :pipeline:`$project`, :pipeline:`$addFields`, etc. ) and then, sort by that field in a subsequent :pipeline:`$sort` stage.

- **In find**, the `{ $meta: "indexKey" }` expression is only
available as part of the `projection` document.

Return Value ````````````

- The value returned depends on how the database decides to
represent values in an index and may change across versions. The represented value may not be the actual value for the field.

- The value returned depends on the execution plan chosen by the
system. For example, if there are two possible indexes which can be used to answer the query, then the value of the "indexKey" metadata depends on which index is selected.

- If an index is :red:`not` used, the `{ $meta: "indexKey" }`
expression does not return a value and the field is not included as part of the output.

## Examples

subsection Examples section by keywords.
