---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/positional-filtered.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# \$[<identifier>] (update operator)

## Definition

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

### Restrictions

The `arrayFilters` option cannot include the following query operators:

- :query:`$expr`
- :query:`$text`
- :query:`$where`
### `upsert`

If an `upsert` operation results in an insert, the `query` must include an `exact equality match <array-match-exact>` on the array field in order to use `$[<identifier>]` in the update statement.

For example, the following upsert operation, which uses `$[<identifier>]` in the update document, specifies an exact equality match condition on the array field:

```javascript
db.collection.updateOne(
   { myArray: [ 0, 1 ] },
   { $set: { "myArray.$[element]": 2 } },
   { arrayFilters: [ { element: 0 } ], upsert: true }
)
```

If no such document exists, the operation would result in an insert of a document that resembles the following:

```javascript
{ "_id" : ObjectId(...), "myArray" : [ 2, 1 ] }
```

If the upsert operation did not include an exact equality match and no matching documents were found to update, the upsert operation would error. For example, the following operations would error if no matching documents were found to update:

```javascript
db.array.updateOne(
   { }, 
   { $set: { "myArray.$[element]": 10 } },
   { arrayFilters: [ { element: 9 } ], upsert: true }
)
```

The operation would return an error that resembles the following:

```javascript
MongoServerError: The path 'myArray' must exist in the document in order to apply array updates.
```

### Nested Arrays

The filtered positional operator `$[<identifier>]` can be used for queries which traverse more than one array and nested arrays.

For an example, see `position-nested-arrays-filtered`.

## Examples

### Update All Array Elements That Match `arrayFilters`

Create the `students` collection:

```javascript
db.students.insertMany( [
   { "_id" : 1, "grades" : [ 95, 92, 90 ] },
   { "_id" : 2, "grades" : [ 98, 100, 102 ] },
   { "_id" : 3, "grades" : [ 95, 110, 100 ] }
] )
```

To update all elements that are greater than or equal to `100` in the `grades` array, use the filtered positional operator :update:`$[\<identifier\>]` with the `arrayFilters`:

```javascript
db.students.updateMany(
   { },
   { $set: { "grades.$[element]" : 100 } },
   { arrayFilters: [ { "element": { $gte: 100 } } ] }
)
```

The positional `$[<identifier>]` operator acts as a placeholder for all elements in the array field that match the conditions specified in `arrayFilters`.

After the operation, the `students` collection contains the following documents:

```javascript
{ "_id" : 1, "grades" : [ 95, 92, 90 ] }
{ "_id" : 2, "grades" : [ 98, 100, 100 ] }
{ "_id" : 3, "grades" : [ 95, 100, 100 ] }
```

### Update All Documents That Match `arrayFilters` in an Array

The :update:`$[\<identifier\>]` operator facilitates updates to arrays that contain embedded documents.  To access the fields in the embedded documents, use the `dot notation <document-dot-notation>` with the :update:`$[\<identifier\>]`.

```javascript
db.collection.updateMany(
   { <query selector> },
   { <update operator>: { "array.$[<identifier>].field" : value } },
   { arrayFilters: [ { <identifier>: <condition> } } ] }
)
```

Create the `students2` collection:

```javascript
db.students2.insertMany( [
   {
      "_id" : 1,
      "grades" : [
         { "grade" : 80, "mean" : 75, "std" : 6 },
         { "grade" : 85, "mean" : 90, "std" : 4 },
         { "grade" : 85, "mean" : 85, "std" : 6 }
      ]
   },
   {
      "_id" : 2,
      "grades" : [
         { "grade" : 90, "mean" : 75, "std" : 6 },
         { "grade" : 87, "mean" : 90, "std" : 3 },
         { "grade" : 85, "mean" : 85, "std" : 4 }
      ]
   }
] )
```

To modify the value of the `mean` field for all elements in the `grades` array where the grade is greater than or equal to `85`, use the positional `$[<identifier>]` operator and `arrayFilters`:

```javascript
db.students2.updateMany(
   { },
   { $set: { "grades.$[elem].mean" : 100 } },
   { arrayFilters: [ { "elem.grade": { $gte: 85 } } ] }
)
```

After the operation, the collection has the following documents:

```javascript
{
   "_id" : 1,
   "grades" : [
      { "grade" : 80, "mean" : 75, "std" : 6 },
      { "grade" : 85, "mean" : 100, "std" : 4 },
      { "grade" : 85, "mean" : 100, "std" : 6 }
   ]
}
{
   "_id" : 2,
   "grades" : [
      { "grade" : 90, "mean" : 100, "std" : 6 },
      { "grade" : 87, "mean" : 100, "std" : 3 },
      { "grade" : 85, "mean" : 100, "std" : 4 }
   ]
}
```

### Update All Array Elements that Match Multiple Conditions

Create the `students3` collection:

```javascript
db.students3.insertMany( [
   {
      "_id" : 1,
      "grades" : [
         { "grade" : 80, "mean" : 75, "std" : 6 },
         { "grade" : 85, "mean" : 100, "std" : 4 },
         { "grade" : 85, "mean" : 100, "std" : 6 }
      ]
   },
   {
      "_id" : 2,
      "grades" : [
         { "grade" : 90, "mean" : 100, "std" : 6 },
         { "grade" : 87, "mean" : 100, "std" : 3 },
         { "grade" : 85, "mean" : 100, "std" : 4 }
      ]
   }
] )
```

To modify the value of the `std` field for all elements in the `grades` array where both the grade is greater than or equal to `80` and the `std` is greater than or equal to `5`, use the positional `$[<identifier>]` operator and `arrayFilters`:

```javascript
db.students3.updateMany(
   { },
   { $inc: { "grades.$[elem].std" : -1 } },
   { arrayFilters: [ { "elem.grade": { $gte: 80 }, "elem.std": { $gte: 5 } } ] }
)
```

After the operation, the collection has the following documents:

```javascript
{  "_id" : 1,
   "grades" : [
      { "grade" : 80, "mean" : 75, "std" : 5 },
      { "grade" : 85, "mean" : 100, "std" : 4 },
      { "grade" : 85, "mean" : 100, "std" : 5 }
   ]
}
{
   "_id" : 2,
   "grades" : [
      { "grade" : 90, "mean" : 100, "std" : 5 },
      { "grade" : 87, "mean" : 100, "std" : 3 },
      { "grade" : 85, "mean" : 100, "std" : 4 }
   ]
}
```

### Update Array Elements Using a Negation Operator

Create the `alumni` collection:

```javascript
db.alumni.insertMany( [
   {
      "_id": 1,
      "name": "Christine Franklin",
      "degrees": [
         { "level": "Master" },
         { "level": "Bachelor" }
      ],
  },
   {
      "_id": 2,
      "name": "Reyansh Sengupta",
      "degrees": [ { "level": "Bachelor" } ],
   }
] )
```

To modify all elements in the `degrees` array that do not have `"level": "Bachelor"`, use the positional :update:`$[\<identifier\>]` operation with the :query:`$ne` query operator:

```javascript
db.alumni.updateMany(
   { },
   { $set : { "degrees.$[degree].gradcampaign" : 1 } },
   { arrayFilters : [ {"degree.level" : { $ne: "Bachelor" } } ] }
)
```

After the operation, the collection has the following documents:

```javascript
{
 _id: 1,
 name: 'Christine Franklin',
 degrees: [ 
    { level: 'Master', gradcampaign: 1 },
    { level: 'Bachelor' }
 ]
},
{
 _id: 2,
 name: 'Reyansh Sengupta',
 degrees: [ { level: 'Bachelor' } ]
}
```

### Update Nested Arrays in Conjunction with `$[]`

The `$[<identifier>]` filtered positional operator, in conjunction with the :update:`$[]` all positional operator, can be used to update nested arrays.

Create a collection `students4` with the following document:

```javascript
db.students4.insertOne(
   { "_id" : 1,
      "grades" : [
        { type: "quiz", questions: [ 10, 8, 5 ] },
        { type: "quiz", questions: [ 8, 9, 6 ] },
        { type: "hw", questions: [ 5, 4, 3 ] },
        { type: "exam", questions: [ 25, 10, 23, 0 ] },
      ]
   }
)
```

The following updates the values that are greater than or equal to `8` in the nested `grades.questions` array if the associated `grades.type` field is `quiz`.

```javascript
db.students4.updateMany(
   {},
   { $inc: { "grades.$[t].questions.$[score]": 2 } },
   { arrayFilters: [ { "t.type": "quiz" }, { "score": { $gte: 8 } } ] }
)
```

> **Note:** Don't add spaces around the array identifiers. If you use
`grades.$[ t ].questions.$[ score ]` in the previous example, the
example fails.

After the operation, the collection has the following document:

```javascript
{
   "_id" : 1,
   "grades" : [
      { "type" : "quiz", "questions" : [ 12, 10, 5 ] },
      { "type" : "quiz", "questions" : [ 10, 11, 6 ] },
      { "type" : "hw", "questions" : [ 5, 4, 3 ] },
      { "type" : "exam", "questions" : [ 25, 10, 23, 0 ] }
   ]
}
```

To update all values that are greater than or equal to `8` in the nested `grades.questions` array, regardless of `type`:

```javascript
db.students4.updateMany(
   {},
   { $inc: { "grades.$[].questions.$[score]": 2 } },
   { arrayFilters: [  { "score": { $gte: 8 } } ] }
)
```

> **Seealso:** - :update:`$[]`
- :method:`db.collection.updateMany()`
- :method:`db.collection.findAndModify()`
- :query:`$elemMatch`

## Learn More

For examples that use the :update:`$[<identifier>]` operator to update arrays, see `array-updates-mql`.
