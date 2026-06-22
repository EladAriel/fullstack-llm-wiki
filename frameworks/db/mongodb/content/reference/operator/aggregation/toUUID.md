---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toUUID.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $toUUID  (expression operator)

## Definition

.. versionadded:: 8.0

## Syntax

```javascript
{
   $toUUID: <expression>
}
```

The `$toUUID` expression is shorthand for the following :expression:`$convert` expression:

```javascript
{
   $convert: {
      input: <expression>,
      to: {
         type: "binData",
         subtype: 4 // UUID
      },
      format: "uuid"
   }
}
```

## Example

Create a `products` collection with the following document:

```javascript
db.products.insertOne(
   {
      name: "laptop",
      price: 400,
      UUID: "0e3b9063-8abd-4eb3-9f9f-f4c59fd30a60"
   }
)
```

In the example document, the `UUID` field is a string. To convert the `UUID` field to a UUID value, run the following `$toUUID` operation:

```javascript
db.products.aggregate( [
   {
      $project: {
         name: 1,
         price: 1,
         UUID: {
            $toUUID: "$UUID"
         }
      }
   }
] )
```

Output:

```javascript
[
   {
      _id: ObjectId('669945ab610b080391a8e2f5'),
      name: 'laptop',
      price: 400,
      UUID: UUID('0e3b9063-8abd-4eb3-9f9f-f4c59fd30a60')
   }
]
```
