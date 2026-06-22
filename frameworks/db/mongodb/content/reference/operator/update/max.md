---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/max.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================

# $max (update operator)

## Definition

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

If the field does not exists, the :update:`$max` operator sets the field to the specified value.

.. include:: /includes/extracts/update-operation-empty-operand-expressions-max.rst

## Examples

### Use `$max` to Compare Numbers

Create the `scores` collection:

```javascript
db.scores.insertOne( { _id: 1, highScore: 800, lowScore: 200 } )
```

The `highScore` for the document currently has the value 800. The following operation:

- Compares the `highscore`, 800, to the specified value, 950
- Updates `highScore` to 950 since 950 is greater than 800
```javascript
db.scores.updateOne( { _id: 1 }, { $max: { highScore: 950 } } )
```

The `scores` collection now contains the following modified document:

```javascript
{ _id: 1, highScore: 950, lowScore: 200 }
```

The next operation has no effect since the value of `highScore`, 950, is greater than 870:

```javascript
db.scores.updateOne( { _id: 1 }, { $max: { highScore: 870 } } )
```

The document remains unchanged in the `scores` collection:

```javascript
{ _id: 1, highScore: 950, lowScore: 200 }
```

### Use `$max` to Compare Dates

Create the `tags` collection:

```javascript
db.tags.insertOne(
   {
     _id: 1,
     desc: "crafts",
     dateEntered: ISODate("2013-10-01T05:00:00Z"),
     dateExpired: ISODate("2013-10-01T16:38:16.163Z")
   }
)
```

The following operation compares the current value of the `dateExpired` field, `ISODate("2013-10-01T16:38:16.163Z")`, with the specified date `new Date("2013-09-30")` to determine whether to update the field:

```javascript
db.tags.updateOne(
   { _id: 1 },
   { $max: { dateExpired: new Date("2013-09-30") } }
)
```

`new Date("2013-09-30")` is not the newest date, so the operation does not update the `dateExpired` field:

```javascript
{
   _id: 1,
   desc: "decorative arts",
   dateEntered: ISODate("2013-10-01T05:00:00Z"),
   dateExpired: ISODate("2013-10-01T16:38:16.163Z")
}
```

> **Seealso:** - :method:`db.collection.updateMany()`
- :method:`db.collection.findAndModify()`
