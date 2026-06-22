---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/bitNot.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# $bitNot (expression operator)

## Definition

.. versionadded:: 6.3

## Syntax

The `$bitNot` operator has the following syntax:

```javascript
   { $bitNot: <expression> }
```

The expression can be a single argument or an array with one `int` or `long` element.

## Behavior

.. include:: /includes/fact-mongosh-integer-long-constructors.rst

.. include:: /includes/fact-bitwise-type-error.rst

If the expression evalutates to `null`, the operation returns `null`.

## Example

The example on this page uses the `switches` collection:

```javascript
 db.switches.insertMany( [
     { _id: 0, a: Int32(0), b: Int32(127) },
     { _id: 1, a: Int32(2), b: Int32(3) },
     { _id: 2, a: Int32(3), b: Int32(5) }
 ] )
```

The following aggregation uses the `$bitNot` operator in the :pipeline:`$project` stage:

```javascript
 db.switches.aggregate( [
   { 
     $project: { 
       result: { 
         $bitNot: "$a"
       }
     }
   }
 ])
```

The operation returns the following results:

```javascript
 [
   { _id: 0, result: -1 },
   { _id: 1, result: -3 },
   { _id: 2, result: -4 }
 ]
```

## Learn More

- `aggregation-pipeline-operators`
- `update-bit`
