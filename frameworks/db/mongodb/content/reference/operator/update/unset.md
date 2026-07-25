---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/unset.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

========================

# $unset (update operator)

## Definition

> **Note:** The following page refers to the update operator :update:`$unset`.
For the aggregation stage, see :pipeline:`$unset`.

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :update:`$unset` operator has the following form:

```javascript
{ $unset: { <field1>: "", ... } }
```

The specified value in the :update:`$unset` expression (that is, `""`) does not impact the operation.

.. include:: /includes/use-dot-notation.rst

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

If the field does not exist, then :update:`$unset` does nothing (that is, no operation).

When used with :update:`$` to match an array element, :update:`$unset` replaces the matching element with `null` rather than removing the matching element from the array. This behavior keeps consistent the array size and element positions.

.. include:: /includes/extracts/update-operation-empty-operand-expressions-unset.rst

## Example

.. include:: /includes/sample-data-usage.rst

The following example uses the :update:`$unset` operator to remove the `label` and `status` fields from the matching movie document:

The operation returns the following result:

> **Seealso:** :method:`db.collection.updateMany()`
:method:`db.collection.findAndModify()`
