---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/positional-all.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================

# \$[] (update operator)

## Definition

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

### `upsert`

If an `upsert` operation results in an insert, the `query` must include an `exact equality match <array-match-exact>` on the array field in order to use the `$[]` positional operator in the update statement.

For example, the following upsert operation, which uses `$[]` in the update document, specifies an exact equality match condition on the array field:

```javascript
db.collection.updateOne(
   { myArray: [ 5, 8 ] },
   { $set: { "myArray.$[]": 10 } },
   { upsert: true }
)
```

If no such document exists, the operation would result in an insertion of the following document:

```javascript
{ "_id" : ObjectId(...), "myArray" : [ 10, 10 ] }
```

If the upsert operation did not include an exact equality match and no matching documents were found to update, the upsert operation would error.

For example, the following operations would error if no matching documents were found to update:

```javascript
db.emptyCollection.updateOne(
   { },
   { $set: { "myArray.$[]": 10 } },
   { upsert: true }
)

db.emptyCollection.updateOne(
   { myArray: 5 },
   { $set: { "myArray.$[]": 10 } },
   { upsert: true }
)
```

### Nested Arrays

The `$[]` operator can be used for queries that traverse more than one array and nested arrays.

For an example, see `position-nested-arrays`.

## Examples

### Update All Elements in an Array

Create the `students` collection:

```javascript
db.students.insertMany( [
   { "_id" : 1, "grades" : [ 85, 82, 80 ] },
   { "_id" : 2, "grades" : [ 88, 90, 92 ] },
   { "_id" : 3, "grades" : [ 85, 100, 90 ] }
] )
```

To increment all elements in the `grades` array by `10` for all documents in the collection, use the all positional :update:`$[]` operator:

```javascript
db.students.updateMany(
   { },
   { $inc: { "grades.$[]": 10 } },
)
```

The all positional :update:`$[]` operator acts as a placeholder for all elements in the array field.

After the operation, the `students` collection contains the following documents:

```javascript
{ "_id" : 1, "grades" : [ 95, 92, 90 ] }
{ "_id" : 2, "grades" : [ 98, 100, 102 ] }
{ "_id" : 3, "grades" : [ 95, 110, 100 ] }
```

### Update All Documents in an Array

The :update:`$[]` positional operator facilitates updates to arrays that contain embedded documents. To access the fields in the embedded documents, use the `dot notation <document-dot-notation>` with the :update:`$[]` operator.

```javascript
db.collection.updateOne(
   { <query selector> },
   { <update operator>: { "array.$[].field" : value } }
)
```

Create the `students2` collection:

```javascript
db.students2.insertMany( [
   {
      "_id" : 1,
      "grades" : [
         { "grade" : 80, "mean" : 75, "std" : 8 },
         { "grade" : 85, "mean" : 90, "std" : 6 },
         { "grade" : 85, "mean" : 85, "std" : 8 }
      ]
   },
   {
      "_id" : 2,
      "grades" : [
         { "grade" : 90, "mean" : 75, "std" : 8 },
         { "grade" : 87, "mean" : 90, "std" : 5 },
         { "grade" : 85, "mean" : 85, "std" : 6 }
      ]
   }
] )
```

To modify the value of the `std` field for all elements in the `grades` array, use the positional :update:`$[]` operator:

```javascript
db.students2.updateMany(
   { },
   { $inc: { "grades.$[].std" : -2 } },
)
```

After the operation, the collection has the following documents:

```javascript
{
   "_id" : 1,
   "grades" : [
      { "grade" : 80, "mean" : 75, "std" : 6 },
      { "grade" : 85, "mean" : 90, "std" : 4 },
      { "grade" : 85, "mean" : 85, "std" : 6 }
   ]
}
{
   "_id" : 2,
   "grades" : [
      { "grade" : 90, "mean" : 75, "std" : 6 },
      { "grade" : 87, "mean" : 90, "std" : 3 },
      { "grade" : 85, "mean" : 85, "std" : 4 }
   ]
}
```

### Update Arrays Specified Using a Negation Query Operator

Create the `results` collection:

```javascript
db.results.insertMany( [
   { "_id" : 1, "grades" : [ 85, 82, 80 ] },
   { "_id" : 2, "grades" : [ 88, 90, 92 ] },
   { "_id" : 3, "grades" : [ 85, 100, 90 ] }
] )
```

To increment all elements in the `grades` array by `10` for all documents **except** those with the value `100` in the `grades` array, use the all positional :update:`$[]` operator:

```javascript
db.results.updateMany(
   { "grades" : { $ne: 100 } },
   { $inc: { "grades.$[]": 10 } },
)
```

The all positional :update:`$[]` operator acts as a placeholder for all elements in the array field.

After the operation, the `students` collection contains the following documents:

```javascript
{ "_id" : 1, "grades" : [ 95, 92, 90 ] }
{ "_id" : 2, "grades" : [ 98, 100, 102 ] }
{ "_id" : 3, "grades" : [ 85, 100, 90 ] }
```

### Update Nested Arrays in Conjunction with `$[<identifier>]`

The `$[]` positional operator, in conjunction with filter :update:`$[\<identifier\>]` positional operator can be used to update nested arrays.

Create a collection `students3` with the following documents:

```javascript
db.students3.insertMany( [
   { "_id" : 1,
      "grades" : [
        { type: "quiz", questions: [ 10, 8, 5 ] },
        { type: "quiz", questions: [ 8, 9, 6 ] },
        { type: "hw", questions: [ 5, 4, 3 ] },
        { type: "exam", questions: [ 25, 10, 23, 0 ] },
      ]
   }
] )
```

To update all values that are greater than or equal to `8` in the nested `grades.questions` array, regardless of `type`:

```javascript
db.students3.updateMany(
   {},
   { $inc: { "grades.$[].questions.$[score]": 2 } },
   { arrayFilters: [  { "score": { $gte: 8 } } ] } 
)
```

The updated documents look like this:

```javascript
{
  _id: 1,
  grades: [
    { type: 'quiz', questions: [ 12, 10, 5 ] },
    { type: 'quiz', questions: [ 10, 11, 6 ] },
    { type: 'hw', questions: [ 5, 4, 3 ] },
    { type: 'exam', questions: [ 27, 12, 25, 0 ] }
  ]
}
```

> **Seealso:** - :update:`$[\<identifier\>]`
- :method:`db.collection.updateMany()`
- :method:`db.collection.findAndModify()`
- :query:`$elemMatch`

## Learn More

For examples that use the :update:`$[]` operator to update arrays, see `array-updates-mql`.
