---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/sort.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# $sort (update operator)

> **Note:** The following page refers to the update modifier :update:`$sort`.
For the aggregation stage, see :pipeline:`$sort`.

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

The :update:`$sort` modifier can sort array elements that are not documents. In previous versions, the :update:`$sort` modifier required the array elements be documents.

If the array elements are documents, the modifier can sort by either the whole document or by a specific field in the documents. In previous versions, the :update:`$sort` modifier can only sort by a specific field in the documents.

Trying to use the :update:`$sort` modifier without the :update:`$each` modifier results in an error. The :update:`$sort` no longer requires the :update:`$slice` modifier. For a list of modifiers available for :update:`$push`, see `push-modifiers`.

## Examples

### Sort Array of Documents by a Field in the Documents

Create the `students` collection:

```javascript
db.students.insertOne(
   {
     "_id": 1,
     "quizzes": [
       { "id" : 1, "score" : 6 },
       { "id" : 2, "score" : 9 }
     ]
   }
)
```

The following update appends additional documents to the `quizzes` array and then sorts all the elements of the array by the ascending `score` field:

```javascript
db.students.updateOne(
   { _id: 1 },
   {
     $push: {
       quizzes: {
         $each: [ { id: 3, score: 8 }, { id: 4, score: 7 }, { id: 5, score: 6 } ],
         $sort: { score: 1 }
       }
     }
   }
)
```

> **Important:** documents and does not reference the containing array field
`quizzes`; i.e. `{ score: 1 }` and **not** `{ "quizzes.score": 1}`

After the update, the array elements are in order of ascending `score` field:

```javascript
{
  "_id" : 1,
  "quizzes" : [
     { "id" : 1, "score" : 6 },
     { "id" : 5, "score" : 6 },
     { "id" : 4, "score" : 7 },
     { "id" : 3, "score" : 8 },
     { "id" : 2, "score" : 9 }
  ]
}
```

### Sort Array Elements That Are Not Documents

Add the following document to the `students` collection:

```javascript
db.students.insertOne( { "_id" : 2, "tests" : [  89,  70,  89,  50 ] } )
```

The following operation adds two more elements to the `tests` array and sorts the elements:

```javascript
db.students.updateOne(
   { _id: 2 },
   { $push: { tests: { $each: [ 40, 60 ], $sort: 1 } } }
)
```

The updated document has the elements of the `tests` array in ascending order:

```javascript
{ "_id" : 2, "tests" : [  40,  50,  60,  70,  89,  89 ] }
```

### Update Array Using Sort Only

Add the following document to the `students` collection:

```javascript
db.students.insertOne( { "_id" : 3, "tests" : [  89,  70,  100,  20 ] } )
```

To update the `tests` field to sort its elements in descending order, specify the `{ $sort: -1 }` and specify an empty array `[]` for the :update:`$each` modifier. For example:

```javascript
db.students.updateOne(
   { _id: 3 },
   { $push: { tests: { $each: [ ], $sort: -1 } } }
)
```

The example sorts the `tests` field values in descending order:

```javascript
{ "_id" : 3, "tests" : [ 100,  89,  70,  20 ] }
```

### Use `$sort` with Other `$push` Modifiers

.. include:: /includes/example-push-with-multiple-modifiers.rst

The order of the modifiers in the query does not change the order that the modifiers are applied. For details, see `push-modifiers`.
