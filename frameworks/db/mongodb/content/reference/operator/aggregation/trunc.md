---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/trunc.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# $trunc  (expression operator)

## Definition

## Syntax

The `$trunc` operator has the following syntax:

```javascript
{ $trunc : [ <number>, <place> ] }
```

The `<number>` expression can be any valid `expression <aggregation-expressions>` as long as it resolves to a number. For more information on expressions, see `aggregation-expressions`.

## Behavior

:expression:`$trunc` does not round the truncated data. To round input values to a specified place, use the :expression:`$round` expression.

### Returned Data Type

The returned data type matches the data type of the input expression or value.

### Truncation Precision with Floating Point Numbers

If you print a double-precision floating point number `4.56` with 20 digits after the decimal separator, you will see `4.55999999999999960920`, which is slightly less than `4.56` and is truncated to `4.55`.

.. include:: /includes/precision.rst

### `null`, `NaN`, and `+/- Infinity`

- If the argument resolves to a value of `null` or refers to a field
that is  missing, :expression:`$trunc` returns `null`.

- If the argument resolves to `NaN`, :expression:`$trunc` returns
`NaN`.

- If the argument resolves to negative or positive infinity,
:expression:`$trunc` returns negative or positive infinity respectively.

## Example

Create a collection named `samples` with the following documents:

```javascript
db.samples.insertMany(
   [
      { _id: 1, value: 19.25 },
      { _id: 2, value: 28.73 },
      { _id: 3, value: 34.32 },
      { _id: 4, value: -45.34 }
   ]
)
```

- The following aggregation returns `value` truncated to the first
decimal place:

```javascript
  db.samples.aggregate([
     { $project: { truncatedValue: { $trunc: [ "$value", 1 ] } } }
  ])

The operation returns the following results:

.. code-block:: javascript

  { "_id" : 1, "truncatedValue" : 19.2 }
  { "_id" : 2, "truncatedValue" : 28.7 }
  { "_id" : 3, "truncatedValue" : 34.3 }
  { "_id" : 4, "truncatedValue" : -45.3 }
```

- The following aggregation returns `value` truncated to the first
place:

```javascript
  db.samples.aggregate([
     { $project: { truncatedValue: { $trunc: [ "$value", -1 ] } } }
  ])

The operation returns the following results:

.. code-block:: javascript

  { "_id" : 1, "truncatedValue" : 10 }
  { "_id" : 2, "truncatedValue" : 20 }
  { "_id" : 3, "truncatedValue" : 30 }
  { "_id" : 4, "truncatedValue" : -40 }
```

- The following aggregation returns`value` truncated to the whole
integer:

```javascript
  db.samples.aggregate([
     { $project: { truncatedValue: { $trunc: [ "$value", 0 ] } } }
  ])

The operation returns the following results:

.. code-block:: javascript

  { "_id" : 1, "truncatedValue" : 19 }
  { "_id" : 2, "truncatedValue" : 28 }
  { "_id" : 3, "truncatedValue" : 34 }
  { "_id" : 4, "truncatedValue" : -45 }
```
