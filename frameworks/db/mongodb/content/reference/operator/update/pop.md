---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/pop.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================

# $pop (update operator)

## Definition

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

The :update:`$pop` operation fails if the `<field>` is not an array.

If the :update:`$pop` operator removes the last item in the `<field>`, the `<field>` will then hold an empty array.

.. include:: /includes/extracts/update-operation-empty-operand-expressions-pop.rst

## Examples

### Remove the First Item of an Array

Create the `students` collection:

```javascript
db.students.insertOne( { _id: 1, scores: [ 8, 9, 10 ] } )
```

The following example removes the first element, 8, from the `scores` array:

```javascript
db.students.updateOne( { _id: 1 }, { $pop: { scores: -1 } } )
```

The first element, 8, has been removed from the `scores` array:

```javascript
{ _id: 1, scores: [ 9, 10 ] }
```

### Remove the Last Item of an Array

Add the following document to the `students` collection:

```javascript
db.students.insertOne( { _id: 10, scores: [ 9, 10 ] } )
```

The following example removes the last element, 10, from the `scores` array by specifying `1` in the :update:`$pop` expression:

```javascript
db.students.updateOne( { _id: 10 }, { $pop: { scores: 1 } } )
```

The last element, 10, has been removed from the `scores` array:

```javascript
{ _id: 10, scores: [ 9 ] }
```

> **Seealso:** - :method:`db.collection.updateMany()`
- :method:`db.collection.findAndModify()`
