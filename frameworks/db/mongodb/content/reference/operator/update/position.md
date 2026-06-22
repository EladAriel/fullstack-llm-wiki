---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/position.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# $position (update operator)

## Definition

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

## Examples

### Add Elements at the Start of the Array

Create the `students` collection:

```javascript
db.students.insertOne( { "_id" : 1, "scores" : [ 100 ] } )
```

The following operation updates the `scores` field to add the elements `50`, `60` and `70` to the beginning of the array:

```javascript
db.students.updateOne(
   { _id: 1 },
   {
     $push: {
        scores: {
           $each: [ 50, 60, 70 ],
           $position: 0
        }
     }
   }
)
```

The operation results in the following updated document:

```javascript
{ "_id" : 1, "scores" : [  50,  60,  70,  100 ] }
```

### Add Elements to the Middle of the Array

Add a document to the `students` collection:

```javascript
db.students.insertOne( { "_id" : 2, "scores" : [  50,  60,  70,  100 ] } )
```

The following operation updates the `scores` field to add the elements `20` and `30` at the array index (position) of `2`:

```javascript
db.students.updateOne(
   { _id: 2 },
   {
     $push: {
        scores: {
           $each: [ 20, 30 ],
           $position: 2
        }
     }
   }
)
```

The operation results in the following updated document:

```javascript
{ "_id" : 2, "scores" : [  50,  60,  20,  30,  70,  100 ] }
```

### Use a Negative Array Index (Position) to Add Elements to the Array

:update:`$position` can accept a negative array index (position) value to indicate the position starting from the end, counting from (but not including) the last element of the array. For example, `-1` indicates the position just before the last element in the array.

Add the following document to the `students` collection:

```javascript
db.students.insertOne(
   { "_id" : 3, "scores" : [  50,  60,  20,  30,  70,  100 ] }
)
```

The following operation specifies `-2` for the :update:`$position` to add `90` at the position two places before the last element, and then `80` at the position two places before the last element.

> **Important:** With a negative array index (position), if you specify multiple
elements in the :update:`$each` array, the last added element is in
the specified position from the end.

```javascript
db.students.updateOne(
   { _id: 3 },
   {
     $push: {
        scores: {
           $each: [ 90, 80 ],
           $position: -2
        }
     }
   }
)
```

The operation results in the following updated document:

```javascript
{ "_id" : 3, "scores" : [ 50, 60, 20, 30, 90, 80, 70, 100 ] }
```
