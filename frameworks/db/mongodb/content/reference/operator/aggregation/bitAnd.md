---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/bitAnd.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================

# $bitAnd (expression operator)

## Definition

.. versionadded:: 6.3

## Syntax

The :expression:`$bitAnd` operator has the following syntax:

```javascript
   { $bitAnd: [ <expression1>, <expression2>, ... ] }
```

## Behavior

.. include:: /includes/fact-bitwise-integer-long-results.rst

.. include:: /includes/fact-mongosh-integer-long-constructors.rst

.. include:: /includes/fact-bitwise-type-error.rst

If the argument is an empty array, the operation returns `Int32(-1)`.

If any of the operands equate to `null`, the operation returns `null`.

## Examples

The examples on this page use the `switches` collection, which contains the following documents:

```javascript
 db.switches.insertMany( [
     { _id: 0, a: Int32(0), b: Int32(127) },
     { _id: 1, a: Int32(2), b: Int32(3) },
     { _id: 2, a: Int32(3), b: Int32(5) }
 ] )
```

### Bitwise `AND` with Two Integers

The following aggregation uses the :expression:`$bitAnd` operator in the :pipeline:`$project` stage:

```javascript
 db.switches.aggregate( [
   { 
     $project: { 
       result: { 
         $bitAnd: [ "$a", "$b" ]
       }
     }
   }
 ])
```

The operation returns the following results:

```javascript
 [
   { _id: 0, result: 0 }
   { _id: 1, result: 2 }
   { _id: 2, result: 1 }
 ]
```

### Bitwise `AND` with a Long and Integer

The following aggregation uses the :expression:`$bitAnd` operator in the :pipeline:`$project` stage:

```javascript
 db.switches.aggregate( [
   { 
     $project: { 
       result: { 
         $bitAnd: [ "$a", Long("63") ]
       }
     }
   }
 ])
```

The operation returns the following results:

```javascript
 [
   { _id: 0, result: Long("0") }
   { _id: 1, result: Long("2") }
   { _id: 2, result: Long("3") }
 ]
```

## Learn More

- `aggregation-pipeline-operators`
- `update-bit`
