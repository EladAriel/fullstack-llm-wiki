---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/round.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# $round  (expression operator)

## Definition

## Behavior

### Rounding to Even Values

When rounding on a value of `5`, :expression:`$round` rounds to the nearest even value. For example, consider the following sample documents:

```javascript
{_id : 1, "value" : 10.5},
{_id : 2, "value" : 11.5},
{_id : 3, "value" : 12.5},
{_id : 4, "value" : 13.5}
```

:expression:`$round : [ "$value", 0] <$round>` returns the following:

```javascript
{_id : 1, "value" : 10},
{_id : 2, "value" : 12},
{_id : 3, "value" : 12},
{_id : 4, "value" : 14}
```

The value `10.5` is closest to the even value `10`, while the values `11.5` and `12.5` are closest to the even value `12`. Rounding to the nearest even value supports more even distribution of rounded data than always rounding up or down.

### Rounding Precision with Floating Point Numbers

If you print a double-precision floating point number `0.05` with 20 digits after the decimal separator, you will see `0.05000000000000000278`, which is slightly greater than `0.05` and is rounded to `0.1`.

.. include:: /includes/precision.rst

### Returned Data Type

The returned data type matches the data type of the input expression or value.

### `null`, `NaN`, and `+/- Infinity`

- If the first argument resolves to a value of `null` or
refers to a field that is  missing, :expression:`$round` returns `null`.

- If the first argument resolves to `NaN`, :expression:`$round`
returns `NaN`.

- If the first argument resolves to negative or positive infinity,
:expression:`$round` returns negative or positive infinity respectively.

## Example

Create a collection named `samples` with the following documents:

```javascript
db.samples.insertMany(
   [
     { _id: 1, value: 19.25 },
     { _id: 2, value: 28.73 },
     { _id: 3, value: 34.32 },
     { _id: 4, value: -45.39 }
   ]
)
```

- The following aggregation returns `value` rounded to the
first decimal place:

```javascript
  db.samples.aggregate([
     { $project: { roundedValue: { $round: [ "$value", 1 ] } } }
  ])

The operation returns the following results:

.. code-block:: javascript

  { "_id" : 1, "roundedValue" : 19.2 }
  { "_id" : 2, "roundedValue" : 28.7 }
  { "_id" : 3, "roundedValue" : 34.3 }
  { "_id" : 4, "roundedValue" : -45.4 }
```

- The following aggregation returns `value`
rounded using the first digit to the left of the decimal:

```javascript
  db.samples.aggregate([
     { $project: { roundedValue: { $round: [ "$value", -1 ] } } }
  ])

The operation returns the following results:

.. code-block:: javascript

  { "_id" : 1, "roundedValue" : 10 }
  { "_id" : 2, "roundedValue" : 20 }
  { "_id" : 3, "roundedValue" : 30 }
  { "_id" : 4, "roundedValue" : -50 }
```

- The following aggregation returns `value` rounded to the
whole integer:

```javascript
  db.samples.aggregate([
     { $project: { roundedValue: { $round: [ "$value", 0 ] } } }
  ])

The operation returns the following results:

.. code-block:: javascript

  { "_id" : 1, "roundedValue" : 19 }
  { "_id" : 2, "roundedValue" : 29 }
  { "_id" : 3, "roundedValue" : 34 }
  { "_id" : 4, "roundedValue" : -45 }
```
