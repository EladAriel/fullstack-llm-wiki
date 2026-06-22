---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/strLenCP.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $strLenCP (expression operator)

## Definition

## Behavior

The :expression:`$strLenCP` operator counts the number of code points in the specified string. This behavior differs from the :expression:`$strLenBytes` operator that counts the number of bytes in the string, where each character uses between one and four bytes.

## Example

### Single-Byte and Multibyte Character Set

Create a `food` collection:

```javascript
db.food.insertMany( [
   { _id: 1, name: "apple" },
   { _id: 2, name: "banana" },
   { _id: 3, name: "éclair" },
   { _id: 4, name: "hamburger" },
   { _id: 5, name: "jalapeño" },
   { _id: 6, name: "pizza" },
   { _id: 7, name: "tacos" },
   { _id: 8, name: "寿司" }
] )
```

The following example uses the `$strLenCP` operator to calculate the `length` of each `name` value:

```javascript
db.food.aggregate( [
   {
      $project: {
         name: 1,
         length: { $strLenCP: "$name" }
      }
   }
] )
```

Example output:

```javascript
[
   { _id: 1, name: 'apple', length: 5 },
   { _id: 2, name: 'banana', length: 6 },
   { _id: 3, name: 'éclair', length: 6 },
   { _id: 4, name: 'hamburger', length: 9 },
   { _id: 5, name: 'jalapeño', length: 8 },
   { _id: 6, name: 'pizza', length: 5 },
   { _id: 7, name: 'tacos', length: 5 },
   { _id: 8, name: '寿司', length: 2 }
]
```

> **Seealso:** :expression:`$strLenBytes`
