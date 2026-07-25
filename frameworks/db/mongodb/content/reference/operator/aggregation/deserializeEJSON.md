---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/deserializeEJSON.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================================

# $deserializeEJSON (expression operator)

## Definition

## Syntax

```javascript
{
   $deserializeEJSON: {
      input: <expression>,
      onError: <expression>
   }
}
```

`$deserializeEJSON` takes a document with the following fields:

## Behavior

### Type Wrapper Parsing

`$deserializeEJSON` converts Extended JSON type wrappers to their corresponding BSON types:

### Null and Missing Values

If the `input` value is null or missing, `$deserializeEJSON` returns null.

## Examples

.. include:: /includes/sample-data-usage.rst

### Deserialize Extended JSON Document

The following example deserializes an Extended JSON document back to native BSON types:

### Parse JSON String and Deserialize

The following example combines :expression:`$convert` with `$deserializeEJSON` to parse a JSON string and convert EJSON type wrappers to BSON:

### Deserialize Specific Fields

You can deserialize specific fields containing EJSON type wrappers:

### Use onError for Error Handling

The following example uses `onError` to provide a fallback value if deserialization fails:

```javascript
db.data.aggregate([
  {
    $project: {
      result: { 
        $deserializeEJSON: { 
          input: "$ejsonField",
          onError: { error: "Invalid EJSON format" }
        }
      }
    }
  }
])
```

## Learn More

- :expression:`$serializeEJSON`
- :expression:`$convert`
- :expression:`$toString`
- The MongoDB Shell provides built-in methods to help work with
Extended JSON. To learn more, see `mongosh-ejson`.
