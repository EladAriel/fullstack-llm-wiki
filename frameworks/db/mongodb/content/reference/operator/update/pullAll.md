---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/pullAll.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================

# $pullAll (update operator)

## Definition

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

If a `<value>` to remove is a document or an array, :update:`$pullAll` removes only the elements in the array that match the specified `<value>` exactly, including order.

.. include:: /includes/extracts/update-operation-empty-operand-expressions-pull-all.rst

## Examples

Create the `survey` collection:

```javascript
db.survey.insertOne( { _id: 1, scores: [ 0, 2, 5, 5, 1, 0 ] } )
```

The following operation removes all instances of the values "0" and "5" from the `scores` array:

```javascript
db.survey.updateOne( { _id: 1 }, { $pullAll: { scores: [ 0, 5 ] } } )
```

After the update, the `scores` field no longer has any instances of "0" or "5".

```javascript
{ "_id" : 1, "scores" : [ 2, 1 ] }
```

> **Seealso:** - :method:`db.collection.updateMany()`
- :method:`db.collection.findAndModify()`
