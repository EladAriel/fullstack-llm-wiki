---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/set.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# $set (aggregation stage)

## Definition

> **Note:** The following page refers to the aggregation stage
:pipeline:`$set`. For the update operator :update:`$set`, see :update:`$set`.

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

:pipeline:`$set` has the following form:

```javascript
{ $set: { <newField>: <expression>, ... } }
```

Specify the name of each field to add and set its value to an `aggregation expression <aggregation-expressions>` or an empty object. For more information on expressions, see `aggregation-expressions`.

> **Important:** If the name of the new field is the same as an existing field name
(including `_id`), `$set` overwrites the existing value
of that field with the value of the specified expression.

## Behavior

- :pipeline:`$set` appends new fields to existing documents. You can
include one or more `$set` stages in an aggregation operation.

- `$set` accepts the embedding of objects where you can set a value to
an aggregation expression or to an empty object. For example, the following nested objects are accepted:

```javascript
  {$set: { a: { b: { } } } }

To add a field or fields to embedded documents (including documents in
arrays) use the dot notation. See :ref:`example
<set-add-field-to-embedded>`.
```

- To add an element to an existing array field with :pipeline:`$set`, use
with :expression:`$concatArrays`. See `example <set-add-element-to-array>`.

## Examples

## Learn More

To learn more about related pipeline stages, see the :pipeline:`$addFields` guide.
