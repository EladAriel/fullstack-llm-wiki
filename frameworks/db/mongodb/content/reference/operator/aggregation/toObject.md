---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toObject.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# $toObject (expression operator)

## Definition

## Behavior

### Input Type Expectations

The following table describes the behavior of `$toObject` for different input types:

.. include:: /includes/table-toObject-input-types.rst

### Parsing Rules

When converting a string to an object, `$toObject`:

- Requires valid `JSON` syntax. Comments and trailing commas are
not allowed.

- Requires the top-level value to be an object. If the string
does not represent an object, `$toObject` errors.

- Does not interpret Extended JSON type wrappers such as `$oid`,
`$date`, or `Timestamp(...)`. These remain strings or nested objects in the result.

- Preserves the last value when the object contains duplicate field
names. Earlier values for the same field are discarded.

### Numeric Type Mapping

`$toObject` converts numeric types based on their value and format:

.. include:: /includes/fact-string-conversion-numeric-type-mapping.rst

## Examples

The following table shows examples of using `$toObject` to convert strings to objects:

### Convert String to Object

Create a collection with strings stored in a field:

```javascript
db.jsonStrings.insertOne({
  _id: 1,
  config: '{"feature": true, "threshold": 10}'
})
```

The following aggregation converts the string in `config` to an object:

```javascript
db.jsonStrings.aggregate([
  {
    $project: {
      _id: 0,
      parsedConfig: { $toObject: "$config" }
    }
  }
])
```

This operation returns a document where `parsedConfig` is a nested document with a boolean and an integer value:

```javascript
{ parsedConfig: { feature: true, threshold: 10 } }
```

.. include:: /includes/note-conversion-error-use-convert.rst
