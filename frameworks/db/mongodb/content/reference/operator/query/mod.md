---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/mod.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $mod (query predicate operator)

## Definition

## Syntax

To specify a `$mod` expression, use the following syntax:

```javascript
{ field: { $mod: [ divisor, remainder ] } }
```

## Behavior

`$mod` returns an error if the `[ divisor, remainder ]` array doesn't contain two elements. For examples, see `mod-not-enough-elements` and `mod-too-many-elements` respectively.

Also, starting in MongoDB 5.1 (and 5.0.4), `$mod` returns an error if the `divisor` or `remainder` values evaluate to:

- `NaN` (not a number).
- `Infinity`.
- A value that can't be represented using a 64-bit integer.
If a document in the collection contains a field where the value is  `NaN` (not a number) or `Infinity`, `$mod` doesn't include the document in the output.

### Negative Dividend

.. include:: /includes/negative-dividend.rst

For an example, see `<mod-qo-negative-dividend-example>`.

## Examples

### Use `$mod` to Select Documents

Create an `inventory` collection:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "abc123", qty: 0 },
   { _id: 2, item: "xyz123", qty: 5 },
   { _id: 3, item: "ijk123", qty: 12 }
] )
```

Then, the following query selects those documents in the `inventory` collection where value of the `qty` field modulo `4` equals `0`:

```javascript
db.inventory.find( { qty: { $mod: [ 4, 0 ] } } )
```

The query returns the following documents:

```json
[
  { _id: 1, item: 'abc123', qty: 0 },
  { _id: 3, item: 'ijk123', qty: 12 }
]
```

### Not Enough Elements Error

The :query:`$mod` operator errors when passed an array with fewer than two elements.

Array with Single Element `````````````````````````

The following operation incorrectly passes the :query:`$mod` operator an array that contains a single element:

```javascript
db.inventory.find( { qty: { $mod: [ 4 ] } } )
```

The statement results in the following error:

```javascript
MongoServerError: malformed mod, not enough elements
```

Empty Array ```````````

The following operation incorrectly passes the :query:`$mod` operator an empty array:

```javascript
db.inventory.find( { qty: { $mod: [ ] } } )
```

The statement results in the following error:

```javascript
MongoServerError: malformed mod, not enough elements
```

### Too Many Elements Error

The :query:`$mod` operator errors when passed an array with more than two elements.

For example, the following operation attempts to use the :query:`$mod` operator with an array that contains four elements:

```javascript
db.inventory.find( { qty: { $mod: [ 4, 1, 2, 3 ] } } )
```

The statement results in the following error:

```javascript
MongoServerError: malformed mod, too many elements
```

### Floating Point Arguments

The `$mod` expression rounds decimal input towards zero.

The following examples demonstrate this behavior:

Each query applies `4` to the `$mod` expression regardless of decimal points, resulting in the same result set.

### Negative Dividend

The `$mod` expression produces a negative result when the dividend is negative.

The following example demonstrates this behavior:
