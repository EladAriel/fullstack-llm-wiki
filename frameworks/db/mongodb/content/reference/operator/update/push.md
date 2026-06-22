---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/push.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# $push (update operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :update:`$push` operator has the form:

```javascript
{ $push: { <field1>: <value1>, ... } }
```

.. include:: /includes/use-dot-notation.rst

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

If the field is absent in the document to update, :update:`$push` adds the array field with the value as its element.

If the field is **not** an array, the operation fails.

If the value is an array, :update:`$push` appends the whole array as a single element. To add each element of the value separately, use the :update:`$each` modifier with :update:`$push`. For an example, see `example-push-each`. For a list of modifiers available for :update:`$push`, see `push-modifiers`.

.. include:: /includes/extracts/update-operation-empty-operand-expressions-push.rst

## Modifiers

You can use the :update:`$push` operator with the following modifiers:

When used with modifiers, the :update:`$push` operator has the form:

```javascript
{ $push: { <field1>: { <modifier1>: <value1>, ... }, ... } }
```

The processing of the :update:`$push` operation with modifiers occur in the following order, regardless of the order in which the modifiers appear:

#. Update array to add elements in the correct position.

#. Apply sort, if specified.

#. Slice the array, if specified.

#. Store the array.

## Examples

.. include:: /includes/sample-data-usage.rst

### Append a Value to an Array

The following example uses the :update:`$push` operator to append `"Classic"` to the `genres` array in the matching movie document:

The operation returns the following result:

### Append a Value to Arrays in Multiple Documents

The following example uses the :update:`$push` operator to append `"Acclaimed"` to the `genres` array in all matching movie documents:

The operation returns the following result:

### Append Multiple Values to an Array

Use :update:`$push` with the :update:`$each` modifier to append multiple values to the array field.

The operation returns the following result:

### Use `$push` Operator with Multiple Modifiers

.. include:: /includes/example-push-with-multiple-modifiers.rst

> **Seealso:** - :method:`db.collection.updateMany()`
- :method:`db.collection.findAndModify()`
