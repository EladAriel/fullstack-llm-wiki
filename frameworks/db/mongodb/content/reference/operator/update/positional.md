---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/positional.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# \$ (update operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The positional :update:`$` operator has the form:

```javascript
{ "<array>.$" : value }
```

When you use update operations, such as :method:`db.collection.updateOne()` and :method:`db.collection.findAndModify()`, both of the following conditions must be true:

- The positional :update:`$` operator acts as a placeholder for
the **first** element that matches the `query document`.

- The `array` field **must** appear as part of the ``query
document``.

For example:

```javascript
db.collection.updateOne(
   { <array>: value ... },
   { <update operator>: { "<array>.$" : value } }
)
```

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

### upsert

Do not use the `$` operator in `upsert` operations. If the update query does not match any existing documents, the upsert fails because the `$` operator requires a matching array element.

### Nested Arrays

You cannot use the positional :update:`$` operator for queries that traverse more than one array, such as queries that traverse arrays nested within other arrays, because the replacement for the :update:`$` placeholder is a single value.

### Unsets

When you use the positional :update:`$` operator with the :update:`$unset` operator, the positional operator does not remove the matching element from the array. Instead, it sets the element to `null`.

### Negations

If the query matches the array using a negation operator, such as :query:`$ne`, :query:`$not`, or :query:`$nin`, then you cannot use the positional operator to update values from this array.

You can use the positional operator if the negated portion of the query is inside an :query:`$elemMatch` expression.

### Multiple Array Matches

The positional :update:`$` update operator behaves ambiguously when you filter on multiple array fields.

When the server executes an update method, it first runs a query to determine which documents to update. If the update filters documents on multiple array fields, the positional :update:`$` update operator might not update the correct position in the array.

For more information, see the `example <multiple-array-match>`.

## Examples

### Update Values in an Array

Create the `students` collection with the following documents:

```javascript
db.students.insertMany( [
   { "_id" : 1, "grades" : [ 85, 80, 80 ] },
   { "_id" : 2, "grades" : [ 88, 90, 92 ] },
   { "_id" : 3, "grades" : [ 85, 100, 90 ] }
] )
```

To update the first element whose value is `80` to `82` in the in the `grades` array, use the positional :update:`$` operator if you do not know the position of the element in the array:

> **Important:** You must include the array field as part of the `query` document.

```javascript
db.students.updateOne(
   { _id: 1, grades: 80 },
   { $set: { "grades.$" : 82 } }
)
```

The positional :update:`$` operator acts as a placeholder for the **first match** of the update `query document <read-operations-query-document>`.

After the operation, the `students` collection contains the following documents:

```javascript
db.students.insertMany ( [
   { _id : 1, "grades" : [ 85, 82, 80 ] },
   { _id : 2, "grades" : [ 88, 90, 92 ] },
   { _id : 3, "grades" : [ 85, 100, 90 ] }
] )
```

### Update Documents in an Array

The positional :update:`$` operator allows updates to arrays that have embedded documents. Use the positional :update:`$` operator to access fields in embedded documents. Use `dot notation <document-dot-notation>` on the :update:`$` operator.

```javascript
db.collection.updateOne(
   { <query selector> },
   { <update operator>: { "array.$.field" : value } }
)
```

Consider the following document in the `students` collection whose `grades` element value is an array of embedded documents:

```javascript
db.students.insertOne( [
   {
      _id: 4,
      grades: [
         { grade: 80, mean: 75, std: 8 },
         { grade: 85, mean: 90, std: 5 },
         { grade: 85, mean: 85, std: 8 }
      ]
   }
] )
```

Use the positional :update:`$` operator to update the `std` field of the first array element that matches the `grade` equal to `85` condition:

> **Important:** You must include the array field as part of the `query` document.

```javascript
db.students.updateOne(
   { _id: 4, "grades.grade": 85 },
   { $set: { "grades.$.std" : 6 } }
)
```

After the operation, the document has the following updated values:

```javascript
{ 
   "_id" : 4,
   "grades" : [
      { "grade" : 80, "mean" : 75, "std" : 8 },
      { "grade" : 85, "mean" : 90, "std" : 6 },
      { "grade" : 85, "mean" : 85, "std" : 8 }
   ]
}
```

### Update Embedded Documents Using Multiple Field Matches

Use the :update:`$` operator to update the first array element that matches multiple query criteria specified with the :query:`$elemMatch` operator.

Consider the following document in the `students` collection whose `grades` field value is an array of embedded documents:

```javascript
db.students.insertOne( [
   {
     _id: 5,
      grades: [
         { grade: 80, mean: 75, std: 8 },
         { grade: 85, mean: 90, std: 5 },
         { grade: 90, mean: 85, std: 3 }
      ]
   }
] )
```

In the following example, the :update:`$` operator updates the value of the `std` field in the first embedded document that has a `grade` field with a value less than or equal to `90` and a `mean` field with a value greater than `80`:

```javascript
db.students.updateOne(
   {
     _id: 5,
     grades: { $elemMatch: { grade: { $lte: 90 }, mean: { $gt: 80 } } }
   },
   { $set: { "grades.$.std" : 6 } }
)
```

This operation updates the first embedded document that matches the criteria, namely the second embedded document in the array:

```javascript
{
  _id: 5,
  grades: [
    { grade: 80, mean: 75, std: 8 },
    { grade: 85, mean: 90, std: 6 },
    { grade: 90, mean: 85, std: 3 }
  ]
}
```

### Update with Multiple Array Matches

The positional :update:`$` update operator behaves ambiguously when the query has multiple array fields to filter documents in the collection.

Consider a document in the `students_deans_list` collection, which holds arrays of student information:

```javascript
db.students_deans_list.insertMany( [
   {
      _id: 8,
      activity_ids: [ 1, 2 ],
      grades: [ 90, 95 ],
      deans_list: [ 2021, 2020 ]
   }
] )
```

In the following example, the user attempts to modify the `deans_list` field. The example filters documents using the `activity_ids`, `deans_list`, and `grades` fields, and updates the 2021 value in the `deans_list` field to 2022:

```javascript
db.students_deans_list.updateOne(
   { activity_ids: 1, grades: 95, deans_list: 2021 },
   { $set: { "deans_list.$": 2022 } }
)
```

When the server executes the preceding `updateOne` method, it filters the available documents using values in the supplied array fields. Although the `deans_list` field is used in the filter, it is not the field used by the positional :update:`$` update operator to determine which position in the array to update:

```javascript
db.students_deans_list.find( { _id: 8 } )
```

Example output:

```javascript
{
   _id: 8,
   activity_ids: [ 1, 2 ],
   grades: [ 90, 95 ],
   deans_list: [ 2021, 2022 ]
}
```

The `updateOne` method matched the `deans_list` field on 2021, but the positional :update:`$` update operator instead changed the 2020 value to 2022.

To avoid unexpected results when matching on multiple arrays, use the filtered positional operator :update:`$[<identifier>]`.

> **Seealso:** - :method:`db.collection.updateMany()`
- :method:`db.collection.findAndModify()`
- :query:`$elemMatch`

## Learn More

For examples that use the :update:`$` operator to update arrays, see `array-updates-mql`.
