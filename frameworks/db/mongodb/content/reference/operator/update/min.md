---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/min.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================

# $min (update operator)

## Definition

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

If the field does not exist, the :update:`$min` operator sets the field to the specified value.

For comparisons between values of different types, such as a number and a null, :update:`$min` uses the `BSON comparison order <faq-dev-compare-order-for-BSON-types>`.

.. include:: /includes/extracts/update-operation-empty-operand-expressions-min.rst

## Examples

### Use `$min` to Compare Numbers

Create the `scores` collection:

```javascript
db.scores.insertOne( { _id: 1, highScore: 800, lowScore: 200 } )
```

The `lowScore` for the document currently has the value `200`. The following operation uses :update:`$min` to compare `200` to the specified value `150` and updates the value of `lowScore` to `150` since `150` is less than `200`:

```javascript
db.scores.updateOne( { _id: 1 }, { $min: { lowScore: 150 } } )
```

The `scores` collection now contains the following modified document:

```javascript
{ _id: 1, highScore: 800, lowScore: 150 }
```

The next operation has no effect since the current value of the field `lowScore`, i.e `150`, is less than `250`:

```javascript
db.scores.updateOne( { _id: 1 }, { $min: { lowScore: 250 } } )
```

The document remains unchanged in the `scores` collection:

```javascript
{ _id: 1, highScore: 800, lowScore: 150 }
```

### Use `$min` to Compare Dates

Create the `tags` collection:

```javascript
db.tags.insertOne(
   {
     _id: 1,
     desc: "crafts",
     dateEntered: ISODate("2013-10-01T05:00:00Z"),
     dateExpired: ISODate("2013-10-01T16:38:16Z")
   }
)
```

The following operation compares the current value of the `dateEntered` field, i.e. `ISODate("2013-10-01T05:00:00Z")`, with the specified date `new Date("2013-09-25")` to determine whether to update the field:

```javascript
db.tags.updateOne(
   { _id: 1 },
   { $min: { dateEntered: new Date("2013-09-25") } }
)
```

The operation updates the `dateEntered` field:

```javascript
{
  _id: 1,
  desc: "crafts",
  dateEntered: ISODate("2013-09-25T00:00:00Z"),
  dateExpired: ISODate("2013-10-01T16:38:16Z")
}
```

> **Seealso:** - :method:`db.collection.updateMany()`
- :method:`db.collection.findAndModify()`
