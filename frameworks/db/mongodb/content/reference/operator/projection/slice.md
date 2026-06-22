---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/projection/slice.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# $slice (projection operator)

## Definition

## Syntax

The :projection:`$slice` has one of the following syntax forms:

```javascript
db.collection.find( 
   <query>, 
   { <arrayField>: { $slice: <number> } } 
);
```

or

```javascript
db.collection.find( 
   <query>, 
   { <arrayField>: { $slice: [ <number>, <number> ] } } 
);
```

## Behavior

### `$slice` of Embedded Array

.. include:: /includes/extracts/projection-slice-operator-inclusion.rst

### View Restriction

.. include:: /includes/extracts/views-unsupported-projection-$slice.rst

### `$` Positional Operator and `$slice` Restriction

.. include:: /includes/extracts/projection-positional-operator-slice-full.rst

### Path Collision: `$slice` of an Array and Embedded Fields

.. include:: /includes/extracts/projection-path-collision-slice-embedded-field-full.rst

> **Seealso:** `find-projection`

## Examples

Create an example collection `posts` with the following documents:

```javascript
db.posts.insertMany([
   {
     _id: 1, 
     title: "Bagels are not croissants.", 
     comments: [ { comment: "0. true" }, { comment: "1. croissants aren't bagels."} ]
   },
   {
     _id: 2, 
     title: "Coffee please.", 
     comments: [ { comment: "0. fooey" }, { comment: "1. tea please" }, { comment: "2. iced coffee" }, { comment: "3. cappuccino" }, { comment: "4. whatever" } ]
   }
])
```

### Return an Array with Its First 3 Elements

The following operation uses the :projection:`$slice` projection operator on the `comments` array to return the array with its first three elements. If the array has less than three elements, all elements in the array are returned.

```javascript
db.posts.find( {}, { comments: { $slice: 3 } } )
```

The operation returns the following documents:

```javascript
{
   "_id" : 1, 
   "title" : "Bagels are not croissants.", 
   "comments" : [ { "comment" : "0. true" }, { "comment" : "1. croissants aren't bagels." } ] 
}
{ 
   "_id" : 2,
   "title" : "Coffee please.",
   "comments" : [ { "comment" : "0. fooey" }, { "comment" : "1. tea please" }, { "comment" : "2. iced coffee" } ]
}
```

### Return an Array with Its Last 3 Elements

The following operation uses the :projection:`$slice` projection operator on the `comments` array to return the array with its last three elements. If the array has less than three elements, all elements in the array are returned.

```javascript
db.posts.find( {}, { comments: { $slice: -3 } } )
```

The operation returns the following documents:

```javascript
{ 
   "_id" : 1, 
   "title" : "Bagels are not croissants.",
   "comments" : [ { "comment" : "0. true" }, { "comment" : "1. croissants aren't bagels." } ]
}
{ 
   "_id" : 2,
   "title" : "Coffee please.",
   "comments" : [ { "comment" : "2. iced coffee" }, { "comment" : "3. cappuccino" }, { "comment" : "4. whatever" } ]
}
```

### Return an Array with 3 Elements After Skipping the First Element

The following operation uses the :projection:`$slice` projection operator on the `comments` array to:

- Skip the first element such that the second element is the starting
point.

- Then, return three elements from the starting point.
If the array has less than three elements after the skip, all remaining elements are returned.

```javascript
db.posts.find( {}, { comments: { $slice: [ 1, 3 ] } } )
```

The operation returns the following documents:

```javascript
{
   "_id" : 1,
   "title" : "Bagels are not croissants.",
   "comments" : [ { "comment" : "1. croissants aren't bagels." } ]
}

{
   "_id" : 2,
   "title" : "Coffee please.",
   "comments" : [ { "comment" : "1. tea please" }, { "comment" : "2. iced coffee" }, { "comment" : "3. cappuccino" } ]
}
```

### Return an Array with 3 Elements After Skipping the Last Element

The following operation uses the :projection:`$slice` projection operator on the `comments` array to

- Skip backwards from the first element such that the last element is
the starting point.

- Then, return three elements from the starting point.
If the array has less than three elements after the skip, all remaining elements in the array are returned.

```javascript
db.posts.find( {}, { comments: { $slice: [ -1, 3 ] } } )
```

The operation returns the following documents:

```javascript
{
   "_id" : 1,
   "title" : "Bagels are not croissants.",
   "comments" : [ { "comment" : "1. croissants aren't bagels." } ]
}
{
   "_id" : 2,
   "title" : "Coffee please.",
   "comments" : [ { "comment" : "4. whatever" } ]
}
```
