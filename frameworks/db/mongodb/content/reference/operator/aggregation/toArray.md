---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toArray.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $toArray (expression operator)

## Definition

## Behavior

### Input Type Expectations

The following table describes the behavior of `$toArray` for different input types:

.. include:: /includes/table-toArray-input-types.rst

### Parsing Rules

When converting a string to an array, `$toArray`:

- Requires valid `JSON` syntax. Comments and trailing commas are
not allowed.

- Requires the top-level value to be an array. If the string
does not represent an array, `$toArray` errors.

- Does not interpret Extended JSON type wrappers such as `$oid`,
`$date`, or `Timestamp(...)`. These remain strings or nested objects in the result.

### binData Conversion

When converting binData to an array, `$toArray`:

- Accepts binData with subtype 9 values.
- Converts `PACKED_BIT` vectors to `boolean` arrays.
- Converts `INT8` vectors to `integer` arrays.
- Converts `FLOAT32` vectors to `double` arrays.
### Numeric Type Mapping

`$toArray` converts numeric types based on their value and format:

.. include:: /includes/fact-string-conversion-numeric-type-mapping.rst

## Examples

The following table shows examples of using `$toArray` to convert strings to arrays:

### Convert String to Array

Insert a document into the `jsonStrings` collection:

```javascript
db.jsonStrings.insertOne({_id: 1})
```

The following operation converts strings to arrays:

```javascript
db.jsonStrings.aggregate([
  {
    $project: {
      _id: 0,
      numbers: { $toArray: "[1, 2, 3]" },
      documents: { $toArray: '[{"a": 1}, {"b": 2}]' }
    }
  }
])
```

The `numbers` field in the result is an array of integers, and `documents` is an array of embedded documents:

```json
{
  numbers: [ 1, 2, 3 ],
  documents: [ { a: 1 }, { b: 2 } ]
}
```

### Convert binData to Array

The following operation converts binData vectors to arrays:

```javascript
db.t.aggregate([
  {
    $project: {
      _id: 0,
      original: "$v",
      asArray: { $toArray: "$v" }
    }
  }
])
```

The operation returns:

.. include:: /includes/note-conversion-error-use-convert.rst
