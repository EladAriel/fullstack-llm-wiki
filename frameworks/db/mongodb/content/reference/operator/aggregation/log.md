---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/log.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $log (expression operator)

## Definition

## Behavior

.. include:: /includes/agg-expression-double-unless-decimal-behavior.rst

.. include:: /includes/extracts/agg-expression-null-operand-log.rst

## Example

A collection `integers` contains the following documents:

```javascript
db.integers.insertMany( [
   { _id: 1, int: 5 },
   { _id: 2, int: 2 },
   { _id: 3, int: 23 },
   { _id: 4, int: 10 }
] )
```

The following example uses log\ :sub:`2` in its calculation to determine the number of bits required to represent the value of `int`.

```javascript
db.integers.aggregate([
   { $project: { bitsNeeded:
      {
         $floor: { $add: [ 1, { $log: [ "$int", 2 ] } ] } } }
      }
])
```

The operation returns the following results:

```javascript
{ "_id" : 1, "bitsNeeded" : 3 }
{ "_id" : 2, "bitsNeeded" : 2 }
{ "_id" : 3, "bitsNeeded" : 5 }
{ "_id" : 4, "bitsNeeded" : 4 }
```

> **Seealso:** - :expression:`$log10`
- :expression:`$ln`
