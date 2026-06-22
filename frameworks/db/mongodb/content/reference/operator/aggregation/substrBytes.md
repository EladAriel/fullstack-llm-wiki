---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/substrBytes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# $substrBytes (expression operator)

## Definition

## Behavior

The :expression:`$substrBytes` operator uses the indexes of UTF-8 encoded bytes where each code point, or character, may use between one and four bytes to encode.

.. include:: /includes/fact-utf8-char-byte-sizes.rst

It is important to be mindful of the content in the `string expression` because providing a `byte index` or `byte count` located in the middle of a UTF-8 character will result in an error.

:expression:`$substrBytes` differs from :expression:`$substrCP` in that :expression:`$substrBytes` counts the bytes of each character, whereas :expression:`$substrCP` counts the code points, or characters, regardless of how many bytes a character uses.

## Example

### Single-Byte Character Set

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "ABC1", quarter: "13Q1", description: "product 1" },
   { _id: 2, item: "ABC2", quarter: "13Q4", description: "product 2" },
   { _id: 3, item: "XYZ1", quarter: "14Q2", description: null }
] )
```

The following operation uses the :expression:`$substrBytes` operator separate the `quarter` value (containing only single byte US-ASCII characters) into a `yearSubstring` and a `quarterSubstring`. The `quarterSubstring` field represents the rest of the string from the specified `byte index` following the `yearSubstring`. It is calculated by subtracting the `byte index` from the length of the string using :expression:`$strLenBytes`.

```javascript
db.inventory.aggregate(
  [
    {
      $project: {
        item: 1,
        yearSubstring: { $substrBytes: [ "$quarter", 0, 2 ] },
        quarterSubstring: { 
          $substrBytes: [ 
            "$quarter", 2, { $subtract: [ { $strLenBytes: "$quarter" }, 2 ] }
          ]
        }
      }
    }
  ]
)
```

The operation returns the following results:

```javascript
{ _id: 1, item: "ABC1", yearSubstring: "13", quarterSubstring: "Q1" }
{ _id: 2, item: "ABC2", yearSubstring: "13", quarterSubstring: "Q4" }
{ _id: 3, item: "XYZ1", yearSubstring: "14", quarterSubstring: "Q2" }
```

### Single-Byte and Multibyte Character Set

Create a `food` collection with the following documents:

```javascript
db.food.insertMany(
 [
    { _id: 1, name: "apple" },
    { _id: 2, name: "banana" },
    { _id: 3, name: "éclair" },
    { _id: 4, name: "hamburger" },
    { _id: 5, name: "jalapeño" },
    { _id: 6, name: "pizza" },
    { _id: 7, name: "tacos" },
    { _id: 8, name: "寿司sushi" }
 ]
)
```

The following operation uses the `$substrBytes` operator to create a three byte `menuCode` from the `name` value:

```javascript
db.food.aggregate(
  [
    {
      $project: {
        "name": 1,
        "menuCode": { $substrBytes: [ "$name", 0, 3 ] }
      }
    }
  ]
)
```

The operation returns the following results:

```javascript
{ _id: 1, name: "apple", menuCode: "app" }
{ _id: 2, name: "banana", menuCode: "ban" }
{ _id: 3, name: "éclair", menuCode: "éc" }
{ _id: 4, name: "hamburger", menuCode: "ham" }
{ _id: 5, name: "jalapeño", menuCode: "jal" }
{ _id: 6, name: "pizza", menuCode: "piz" }
{ _id: 7, name: "tacos", menuCode: "tac" }
{ _id: 8, name: "寿司sushi", menuCode: "寿" }
```

> **Seealso:** :expression:`$substrCP`
