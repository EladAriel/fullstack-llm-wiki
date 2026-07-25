---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/bitNot.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
