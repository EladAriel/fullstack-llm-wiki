---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/set.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================

# $set (update operator)

## Definition

> **Note:** The following page refers to the update operator :update:`$set`.
For the aggregation stage, see :pipeline:`$set`.

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :update:`$set` operator expression has the following form:

```javascript
{ $set: { <field1>: <value1>, ... } }
```

.. include:: /includes/use-dot-notation.rst

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

If the field does not exist, :update:`$set` adds a new field with the specified value if the new field does not violate a type constraint. If you specify a dotted path for a non-existent field, :update:`$set` creates the embedded documents as needed to fulfill the dotted path to the field.

If you specify multiple field-value pairs, :update:`$set` updates or creates each field.

.. include:: /includes/extracts/update-operation-empty-operand-expressions-set.rst

### Advantages of $set

The `$set` operator provides the following advantages compared to full document replacement:

- **Targeted Updates**: `$set` modifies only the specified fields,
ensuring efficient updates by avoiding unnecessary writes and overhead when you work with large documents.

- **Efficient Oplog Entries**: `$set` optimizes replication by writing only the
updated fields to the `oplog` instead of the entire document. This process reduces the size of oplog entries and allows nodes to replicate changes more efficiently.

- **Simplified Logic**: Applications using `$set` do not need to compute
changed fields before they send an update. MongoDB reduces complexity by handling the delta computation internally.

## Examples

.. include:: /includes/sample-data-usage.rst

### Set Top-Level Fields

The following example uses the :update:`$set` operator to add the `label` and `status` fields to the matching movie document:

The operation returns the following result:

### Set Fields in Embedded Documents

The following example uses dot notation to update the `highlight` field of the `imdb` embedded document in the matching movie:

The operation returns the following result:

> **Important:** The preceding example uses dot notation to update the `highlight`
field of the embedded `imdb` document. The following format
instead replaces the entire embedded document, removing all
other fields from `imdb`:
.. code-block:: javascript
   :copyable: false
   db.movies.updateOne(
      { title: "The Dark Knight" },
      { $set: { imdb: { highlight: "Critics' Choice" } } }
   )

### Set Elements in Arrays

The following example uses the :update:`$set` operator to update the first element (array index `0`) of the `genres` array in the matching movie document:

The operation returns the following result:

For additional update operators for arrays, see `/reference/operator/update-array`.

> **Seealso:** - :method:`db.collection.updateMany()`
- :method:`db.collection.findAndModify()`
