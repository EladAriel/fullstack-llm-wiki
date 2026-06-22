---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/median.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $median (accumulator operator)

## Definition

## Syntax

The syntax for |operatorName| is:

```javascript
{
   $median: {
      input: <number>,
      method: <string>
   }
}
```

## Command Fields

|operatorName| takes the following fields:

## Behavior

.. include:: /includes/aggregation/fact-behavior-percent-median.rst

### Type of Operation

.. include:: /includes/aggregation/fact-type-of-operation.rst

### Calculation Considerations

.. include:: /includes/aggregation/fact-calc-considerations.rst

### Array Input

If you use |operatorName| as an aggregation expression in a :pipeline:`$project <$project>` stage, you can use an array as input. |operatorName| ignores non-numeric array values.

The syntax is:

```javascript
{
   $median:
      {
         input: [ <expression1, <expression2>, ..., <expressionN> ], 
         method: <string>
      }
}
```

### Window Functions

.. include:: /includes/aggregation/fact-setwindowfield.rst

## Examples

.. include:: /includes/aggregation/example-setup-01.rst

### Use |operatorName| as an Accumulator

Create an accumulator that calculates the median value:

```javascript
db.testScores.aggregate( [
   {
      $group: {
         _id: null,
         test01_median: {
            $median: {
               input: "$test01",
               method: 'approximate'
            }
         }
      }
   }
] )
```

Output:

```javascript
{ _id: null, test01_median: 62 }
```

The `_id` field value is `null` so `$group` selects all the documents in the collection.

The |operatorName| accumulator takes its input from the `test01` field. |operatorName| calculates the median value for the field, `62` in this example.

### Use |operatorName| in a `$project` Stage

In a `$group` stage, |operatorName| is an accumulator and calculates a single value for all documents. In a `$project` stage, |operatorName| is an aggregation expression and calculates values for each document.

You can use a field name or an array as input in a `$project` stage.

```javascript
db.testScores.aggregate( [
   {
      $project: {
         _id: 0,
         studentId: 1,
         testMedians: {
            $median: {
               input: [ "$test01", "$test02", "$test03" ],
               method: 'approximate'
            }
         }
      }
   }
] )
```

Output:

```javascript
{ studentId: '2345', testMedians: 80 },
{ studentId: '2356', testMedians: 79 },
{ studentId: '2358', testMedians: 78 },
{ studentId: '2367', testMedians: 72 },
{ studentId: '2369', testMedians: 60 }
```

When |operatorName| is an aggregation expression there is a result for each `studentId`.

### Use |operatorName| in a `$setWindowField` Stage

To base your percentile values on local data trends, use |operatorName| in a `$setWindowField` aggregation pipeline stage.

This example creates a window to filter scores:

```javascript
db.testScores.aggregate( [
   {
      $setWindowFields: {
         sortBy: { test01: 1 },
         output: {
            test01_median: {
               $median: {
                  input: "$test01",
                  method: 'approximate'
               },
               window: {
                  range: [ -3, 3 ]
               }
            }
         }
      }
   },
   {
      $project: {
         _id: 0,
         studentId: 1,
         test01_median: 1
      }
   }
] )
```

Output:

```javascript
{ studentId: '2356', test01_median: 60 },
{ studentId: '2369', test01_median: 60 },
{ studentId: '2345', test01_median: 60 },
{ studentId: '2367', test01_median: 64 },
{ studentId: '2358', test01_median: 64 }
```

In this example, the median calculation for each document also incorporates data from the three documents before and after it.

## Learn More

The :group:`$percentile <$percentile>` operator is a more general version of the |operatorName| operator that allows you to set one or more percentile values.

For more information on window functions, see: :pipeline:`$setWindowFields`.
