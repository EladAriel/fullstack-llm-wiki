---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/rand.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# $rand (expression operator)

## Definition

## Behavior

Each time `$rand` is called it will return a floating point value that has up to 17 digits after the decimal point. Trailing 0s are dropped so the actual number of digits may vary.

## Examples

### Generate Random Data Points

This example models charitable donations. The collection starts with a list of donors.

```javascript
db.donors.insertMany(
   [
     { donorId: 1000, amount: 0, frequency: 1 },
     { donorId: 1001, amount: 0, frequency: 2 },
     { donorId: 1002, amount: 0, frequency: 1 },
     { donorId: 1003, amount: 0, frequency: 2 },
     { donorId: 1004, amount: 0, frequency: 1 }
   ]
)
```

We use an aggregation pipeline to update each document with a random donation amount.

```javascript
db.donors.aggregate(
   [
      { $set: { amount: { $multiply: [ { $rand: {} }, 100 ] } } },
      { $set: { amount: { $floor: "$amount" } } },
      { $merge: "donors" }
   ]
)
```

The first :pipeline:`$set` stage updates the `amount` field. An initial value between 0 and 1 is generated using `$rand`. Then :expression:`$multiply` scales it upward 100 times.

The :expression:`$floor` operator in the second `$set` stage removes the decimal portion from the `amount` to leave an integer value.

Finally, :pipeline:`$merge` writes the random value created in the previous steps to the `amount` field, updating it for each document in the `donors` collection.

You can view the results with a projection stage:

```javascript
db.donors.aggregate(
   [
      { $project: {_id: 0, donorId: 1, amount: 1 } }
   ]
)
```

The projection shows the scaled amounts are now random values in the range from 0 to 99.

```javascript
{ "donorId" : 1000, "amount" : 27 }
{ "donorId" : 1001, "amount" : 10 }
{ "donorId" : 1002, "amount" : 88 }
{ "donorId" : 1003, "amount" : 73 }
{ "donorId" : 1004, "amount" : 5 }
```

### Select Random Items From a Collection

You can use `$rand` in an aggregation pipeline to select random documents from a collection. Consider a collection of voter records:

```javascript
db.voters.insertMany(
   [
     { name: "Archibald", voterId: 4321, district: 3, registered: true },
     { name: "Beckham", voterId: 4331, district: 3, registered: true },
     { name: "Carolin", voterId: 5321, district: 4, registered: true },
     { name: "Debarge", voterId: 4343, district: 3, registered: false },
     { name: "Eckhard", voterId: 4161, district: 3, registered: false },
     { name: "Faberge", voterId: 4300, district: 1, registered: true },
     { name: "Grimwald", voterId: 4111, district: 3, registered: true },
     { name: "Humphrey", voterId: 2021, district: 3, registered: true },
     { name: "Idelfon", voterId: 1021, district: 4, registered: true },
     { name: "Justo", voterId: 9891, district: 3, registered: false }
   ]
)
```

Imagine you want to select about half of the voters in District 3 to do some polling.

```javascript
db.voters.aggregate(
   [
      { $match: { district: 3 } },
      { $match: { $expr: { $lt: [0.5, {$rand: {} } ] } } },
      { $project: { _id: 0, name: 1, registered: 1 } }
   ]
)
```

The first pipeline stage matches all documents where the voter is from district 3.

The second :pipeline:`$match` stage uses `$rand` in a match expression to further refine the selection. For each document, `$rand` generates a value between 0 and 1. The threshold of `0.5` in the less than :expression:`($lt)<$lt>` comparison means that :query:`$expr` will be true for about half the documents.

In the :pipeline:`$project` stage the selected documents are filtered to return the `name` and `registered` fields. There are 7 voters in District 3, running the code selects about half of them.

```javascript
{ "name" : "Archibald", "registered" : true }
{ "name" : "Debarge", "registered" : false }
{ "name" : "Humphrey", "registered" : true }
```

> **Note:** The number of documents selected is different each time. If you need
to select an exact number of documents, consider using
:pipeline:`$sample` instead of `$rand`.

> **Seealso:** - :pipeline:`$sample`
- :expression:`$round`
