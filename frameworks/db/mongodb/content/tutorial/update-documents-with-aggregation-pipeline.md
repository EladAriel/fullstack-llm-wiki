---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/update-documents-with-aggregation-pipeline.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# Updates with Aggregation Pipeline

Use aggregation pipelines to perform update operations. You can build and execute these pipelines in:

- [{+atlas+}](https://www.mongodb.com/docs/atlas)_
- [MongoDB Compass](https://www.mongodb.com/docs/compass/)_
- [MongoDB Shell](https://www.mongodb.com/docs/mongodb-shell/)_
- [Drivers](https://www.mongodb.com/docs/drivers/)_
Aggregation pipelines for updates support these stages:

.. include:: /includes/aggregation/update-aggregation-stages.rst

Aggregation pipelines enable expressive updates, such as:

- Conditional updates based on current field values
- Setting field values from other fields
.. include:: /includes/aggregation/agg-dollar-sign.rst

## Create an Update Aggregation Pipeline in Atlas

You can build aggregation pipelines to perform updates in the {+atlas+} UI. Requires :authrole:`Project Data Access Read Only` role or higher.

## Examples

The following examples demonstrate how to use the aggregation pipeline stages `$set`, `$replaceRoot`, and `$addFields` to perform updates.

### updateOne with $set

Create the `students` collection:

```javascript
db.students.insertMany( [
   { _id: 1, test1: 95, test2: 92, test3: 90, modified: new Date("01/05/2020") },
   { _id: 2, test1: 98, test2: 100, test3: 102, modified: new Date("01/05/2020") },
   { _id: 3, test1: 95, test2: 110, modified: new Date("01/04/2020") }
] )
```

To verify, query the collection:

```javascript
db.students.find()
```

The following :method:`db.collection.updateOne() operation uses an aggregation pipeline to update the document with id: 3`:

```javascript
db.students.updateOne( { _id: 3 }, [ { $set: { "test3": 98, modified: "$$NOW"} } ] )
```

The pipeline consists of a :pipeline:`$set` stage which adds the `test3` field (and sets its value to `98`) to the document and sets the `modified` field to the current datetime. The operation uses the aggregation variable :variable:`NOW` for the current datetime. To access the variable, prefix with  `$$` and enclose in quotes.

To verify, query the collection:

```javascript
db.students.find().pretty()
```

### updateMany with $replaceRoot and $set

Create the `students2` collection:

```javascript
db.students2.insertMany( [
   { "_id" : 1, quiz1: 8, test2: 100, quiz2: 9, modified: new Date("01/05/2020") },
   { "_id" : 2, quiz2: 5, test1: 80, test2: 89, modified: new Date("01/05/2020") },
] )
```

To verify, query the collection:

```javascript
db.students2.find()
```

The following :method:`db.collection.updateMany()` operation uses an aggregation pipeline to standardize the fields for the documents (i.e. documents in the collection should have the same fields) and update the `modified` field:

```javascript
db.students2.updateMany( {}, 
  [
    { $replaceRoot: { newRoot: 
       { $mergeObjects: [ { quiz1: 0, quiz2: 0, test1: 0, test2: 0 }, "$$ROOT" ] }
    } },
    { $set: { modified: "$$NOW"}  }
  ]
)
```

This pipeline consists of:

- a :pipeline:`$replaceRoot` stage with a
:expression:`$mergeObjects` expression to set default values for the `quiz1`, `quiz2`, `test1` and `test2` fields. The aggregation variable :variable:`ROOT` refers to the current document being modified. To access the variable, prefix with `$$` and enclose in quotes. The current document fields will override the default values.

- a :pipeline:`$set` stage to update the `modified` field to the
current datetime. The operation uses the aggregation variable :variable:`NOW` for the current datetime. To access the variable, prefix with `$$` and enclose in quotes.

To verify, query the collection:

```javascript
db.students2.find()
```

### updateMany with $set

Create the `students3` collection:

```javascript
db.students3.insertMany( [
   { "_id" : 1, "tests" : [ 95, 92, 90 ], "modified" : ISODate("2019-01-01T00:00:00Z") },
   { "_id" : 2, "tests" : [ 94, 88, 90 ], "modified" : ISODate("2019-01-01T00:00:00Z") },
   { "_id" : 3, "tests" : [ 70, 75, 82 ], "modified" : ISODate("2019-01-01T00:00:00Z") }
] );
```

To verify, query the collection:

```javascript
db.students3.find()
```

The following :method:`db.collection.updateMany()` operation uses an aggregation pipeline to update the documents with the calculated grade average and letter grade.

```javascript
db.students3.updateMany(
   { },
   [
     { $set: { average : { $trunc: [ { $avg: "$tests" }, 0 ] }, modified: "$$NOW" } },
     { $set: { grade: { $switch: {
                           branches: [
                               { case: { $gte: [ "$average", 90 ] }, then: "A" },
                               { case: { $gte: [ "$average", 80 ] }, then: "B" },
                               { case: { $gte: [ "$average", 70 ] }, then: "C" },
                               { case: { $gte: [ "$average", 60 ] }, then: "D" }
                           ],
                           default: "F"
     } } } }
   ]
)
```

This pipeline consists of:

- a :pipeline:`$set` stage to calculate the truncated average value
of the `tests` array elements and to update the `modified` field to the current datetime. To calculate the truncated average, the stage uses the :group:`$avg` and :expression:`$trunc` expressions. The operation uses the aggregation variable :variable:`NOW` for the current datetime. To access the variable, prefix with `$$` and enclose in quotes.

- a :pipeline:`$set` stage to add the `grade` field based on the
`average` using the :expression:`$switch` expression.

To verify, query the collection:

```javascript
db.students3.find()
```

### updateOne with $set

Create the `students4` collection:

```javascript
db.students4.insertMany( [
  { "_id" : 1, "quizzes" : [ 4, 6, 7 ] },
  { "_id" : 2, "quizzes" : [ 5 ] },
  { "_id" : 3, "quizzes" : [ 10, 10, 10 ] }
] )
```

To verify, query the collection:

```javascript
db.students4.find()
```

The following :method:`db.collection.updateOne() operation uses an aggregation pipeline to add quiz scores to the document with id: 2`:

```javascript
db.students4.updateOne( { _id: 2 }, 
  [ { $set: { quizzes: { $concatArrays: [ "$quizzes", [ 8, 6 ]  ] } } } ]
)
```

To verify, query the collection:

```javascript
db.students4.find()
```

### updateMany with $addFields

Create the `temperatures` collection using tempatures in Celsius:

```javascript
db.temperatures.insertMany( [
  { "_id" : 1, "date" : ISODate("2019-06-23"), "tempsC" : [ 4, 12, 17 ] },
  { "_id" : 2, "date" : ISODate("2019-07-07"), "tempsC" : [ 14, 24, 11 ] },
  { "_id" : 3, "date" : ISODate("2019-10-30"), "tempsC" : [ 18, 6, 8 ] }
] )
```

To verify, query the collection:

```javascript
db.temperatures.find()
```

The following :method:`db.collection.updateMany()` operation uses an aggregation pipeline to update the documents with the corresponding temperatures in Fahrenheit:

```javascript
db.temperatures.updateMany( { },
  [
    { $addFields: { "tempsF": {
          $map: {
             input: "$tempsC",
             as: "celsius",
             in: { $add: [ { $multiply: ["$$celsius", 9/5 ] }, 32 ] }
          }
    } } }
  ]
)
```

The pipeline consists of an :pipeline:`$addFields` stage to add a new array field `tempsF` that contains the temperatures in Fahrenheit. To convert each celsius temperature in the `tempsC` array to Fahrenheit, the stage uses the :expression:`$map` expression with :expression:`$add` and :expression:`$multiply` expressions.

To verify, query the collection:

```javascript
db.temperatures.find()
```

### Update with let Variables

.. include:: /includes/let-example-introduction.rst

.. include:: /includes/let-example-create-flavors.rst

The following `updateOne` command uses variables set with the `let` option:

- The `targetFlavor` variable is set to `cherry`. This variable is
used in the `$eq` expression to specify the match filter.

- The `newFlavor` variable is set to `orange`. This variable is used
in the `$set` operator to specify the updated `flavor` value for the matched document.

```javascript
db.cakeFlavors.updateOne(
   { 
      $expr: { $eq: [ "$flavor", "$$targetFlavor" ] }
   },
   [
      { 
         $set: { flavor: "$$newFlavor" }
      }
   ],
   { 
      let: { targetFlavor: "cherry", newFlavor: "orange" }
   }
)
```

After you run the preceding update operation, the `cakeFlavors` collection contains these documents:

```javascript
[
   { _id: 1, flavor: 'chocolate' },
   { _id: 2, flavor: 'strawberry' },
   { _id: 3, flavor: 'orange' }
]
```

### Additional Examples

See the following pages for more examples:

- `db.collection.updateOne <updateOne-example-agg>`
- `db.collection.updateMany <updateMany-example-agg>`
- `db.collection.findOneAndUpdate() <findOneAndUpdate-agg-pipeline>`
- `db.collection.findAndModify() <findAndModify-agg-pipeline>`
- `Bulk.find.update() <example-bulk-find-update-agg>`
- `Bulk.find.updateOne() <example-bulk-find-update-one-agg>`
- `Bulk.find.upsert() <bulk-find-upsert-update-agg-example>`
