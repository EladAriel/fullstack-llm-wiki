---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/percentile.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# $percentile (accumulator operator)

## Definition

## Syntax

The syntax for |operatorName| is:

```javascript
{
   $percentile: {
      input: <expression>,
      p: [ <expression1>, <expression2>, ... ],
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

|operatorName| returns the minimum value for `p = 0.0`.

|operatorName| returns the maximum value for `p = 1.0`.

### Array Input

If you use |operatorName| as an aggregation expression in a :pipeline:`$project <$project>` stage, you can use an array as input. The syntax is:

```javascript
{
   $percentile: {
      input: [ <expression1, <expression2>, .., <expressionN> ],
      p: [ <expression1>, <expression2>, ... ],
      method: <string>
   }
}
```

### Window Functions

.. include:: /includes/aggregation/fact-setwindowfield.rst

## Examples

.. include:: /includes/aggregation/example-setup-01.rst

### Calculate a Single Value as an Accumulator

Create an accumulator that calculates a single percentile value:

```javascript
db.testScores.aggregate( [
   {
      $group: {
         _id: null,
         test01_percentiles: {
            $percentile: {
               input: "$test01",
               p: [ 0.95 ],
               method: 'approximate'
            }
         },
      }
   }
] )
```

Output:

```javascript
{ _id: null, test01_percentiles: [ 67 ] }
```

The `_id` field value is `null` so `$group` selects all the documents in the collection.

The `percentile` accumulator takes its input data from the `test01` field.

In this example, the percentiles array, `p`, has one value so the `$percentile` operator only calculates one term for the `test01` data. The 95th percentile value is `67`.

### Calculate Multiple Values as an Accumulator

Create an accumulator that calculates multiple percentile values:

```javascript
db.testScores.aggregate( [
   {
       $group: {
          _id: null,
          test01_percentiles: {
             $percentile: {
                input: "$test01",
                p: [ 0.5, 0.75, 0.9, 0.95 ],
                method: 'approximate'
             }
          },
          test02_percentiles: {
             $percentile: {
                input: "$test02",
                p: [ 0.5, 0.75, 0.9, 0.95 ],
                method: 'approximate'
             }
          },
          test03_percentiles: {
             $percentile: {
                input: "$test03",
                p: [ 0.5, 0.75, 0.9, 0.95 ],
                method: 'approximate'
             }
          },
          test03_percent_alt: {
             $percentile: {
                input: "$test03",
                p: [ 0.9, 0.5, 0.75, 0.95 ],
                method: 'approximate'
             }
          },
       }
    }
] )
```

Output:

```javascript
{
   _id: null,
  test01_percentiles: [ 62, 64, 67, 67 ],
  test02_percentiles: [ 81, 82, 83, 83 ],
  test03_percentiles: [ 78, 79, 80, 80 ],
  test03_percent_alt: [ 80, 78, 79, 80 ]
}
```

The `_id` field value is `null` so `$group` selects all the documents in the collection.

The `percentile` accumulator calculates values for three fields, `test01`, `test02`, and `test03`.

The accumulator calculates the 50th, 75th, 90th, and 95th percentile values for each input field.

The percentile values are returned in the same order as the elements of `p`. The values in `test03_percentiles` and `test03_percent_alt` are the same, but their order is different. The order of elements in each result array matches the corresponding order of elements in `p`.

### Use |operatorName| in a `$project` Stage

In a `$project` stage, |operatorName| is an aggregation expression and calculates values for each document.

You can use a field name or an array as input in a `$project` stage.

```javascript
db.testScores.aggregate( [
   {
      $project: {
         _id: 0,
         studentId: 1,
         testPercentiles: {
            $percentile: {
               input: [ "$test01", "$test02", "$test03" ],
               p: [ 0.5, 0.95 ],
               method: 'approximate'
            }
         }
      }
   }
] )
```

Output:

```javascript
{ studentId: '2345', testPercentiles: [ 80, 81 ] },
{ studentId: '2356', testPercentiles: [ 79, 83 ] },
{ studentId: '2358', testPercentiles: [ 78, 82 ] },
{ studentId: '2367', testPercentiles: [ 72, 77 ] },
{ studentId: '2369', testPercentiles: [ 60, 72 ] }
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
            test01_95percentile: {
               $percentile: {
                  input: "$test01",
                  p: [ 0.95 ],
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
         test01_95percentile: 1
      }
   }
] )
```

Output:

```javascript
{ studentId: '2356', test01_95percentile: [ 62 ] },
{ studentId: '2369', test01_95percentile: [ 62 ] },
{ studentId: '2345', test01_95percentile: [ 64 ] },
{ studentId: '2367', test01_95percentile: [ 67 ] },
{ studentId: '2358', test01_95percentile: [ 67 ] }
```

In this example, the percentile calculation for each document also incorporates data from the three documents before and after it.

## Learn More

The :group:`$median <$median>` operator is a special case of the |operatorName| operator that uses a fixed value of `p: [ 0.5 ]`.

For more information on window functions, see: :pipeline:`$setWindowFields`.
