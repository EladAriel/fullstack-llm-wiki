---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/slice.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# $slice (update operator)

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

The order in which the modifiers appear is immaterial. Previous versions required the :update:`$each` modifier to appear as the first modifier if used in conjunction with :update:`$slice`. For a list of modifiers available for :update:`$push`, see `push-modifiers`.

Trying to use the :update:`$slice` modifier without the :update:`$each` modifier results in an error.

## Examples

### Slice from the End of the Array

A collection `students` contains the following document:

```javascript
db.students.insertOne([
   { _id : 1, "scores" : [ 40, 50, 60 ] }
] )
```

The following operation adds new elements to the `scores` array, and then uses the :update:`$slice` modifier to trim the array to the last five elements:

```javascript
db.students.updateOne(
   { _id: 1 },
   {
     $push: {
       scores: {
         $each: [ 80, 78, 86 ],
         $slice: -5
       }
     }
   }
)
```

The result of the operation is slice the elements of the updated `scores` array to the last five elements:

```javascript
{ "_id" : 1, "scores" : [  50,  60,  80,  78,  86 ] }
```

### Slice from the Front of the Array

A collection `students` contains the following document:

```javascript
db.students.insertOne( [
   { _id : 2, "scores" : [ 89, 90 ] }
] )
```

The following operation adds new elements to the `scores` array, and then uses the :update:`$slice` modifier to trim the array to the first three elements.

```javascript
db.students.updateOne(
   { _id: 2 },
   {
     $push: {
       scores: {
         $each: [ 100, 20 ],
         $slice: 3
       }
     }
   }
)
```

The result of the operation is to slice the elements of the updated `scores` array to the first three elements:

```javascript
{ "_id" : 2, "scores" : [  89,  90,  100 ] }
```

### Update Array Using Slice Only

A collection `students` contains the following document:

```javascript
db.students.insertOne( [
   { _id : 3, "scores" : [  89,  70,  100,  20 ] }
] )
```

To update the `scores` field with just the effects of the :update:`$slice` modifier, specify the number of elements to slice (e.g. `-3`) for the :update:`$slice` modifier and an empty array `[]` for the :update:`$each` modifier, as in the following:

```javascript
db.students.updateOne(
  { _id: 3 },
  {
    $push: {
      scores: {
         $each: [ ],
         $slice: -3
      }
    }
  }
)
```

The result of the operation is to slice the elements of the `scores` array to the last three elements:

```javascript
{ "_id" : 3, "scores" : [  70,  100,  20 ] }
```

### Use `$slice` with Other `$push` Modifiers

.. include:: /includes/example-push-with-multiple-modifiers.rst

The order of the modifiers is immaterial to the order in which the modifiers are processed. See `push-modifiers` for details.
