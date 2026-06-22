---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/serializeEJSON.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# $serializeEJSON (expression operator)

## Definition

## Syntax

```javascript
{
   $serializeEJSON: {
      input: <expression>,
      relaxed: <boolean>,
      onError: <expression>
   }
}
```

`$serializeEJSON` takes a document with the following fields:

## Behavior

### Comparison of Canonical and Relaxed Formats

The following table shows how common BSON types are converted to Extended JSON:

### Null and Missing Values

If the `input` value is null or missing, `$serializeEJSON` returns null.

## Examples

.. include:: /includes/sample-data-usage.rst

### Canonical Extended JSON Example

The following example converts a movie document to Canonical Extended JSON format:

### Relaxed Extended JSON Example

The following example uses the `relaxed` option for more readable output:

### Convert to JSON String

To convert the EJSON result to a JSON string, combine `$serializeEJSON` with :expression:`$toString`:

> **Note:** The `jsonString` field in the previous example is reformatted
for readability. In actual output, the JSON string is a single
line without whitespace.

### Serialize Specific Fields

You can serialize specific fields rather than entire documents:

### Use onError for Error Handling

The following example uses `onError` to provide a fallback value if serialization fails:

```javascript
db.movies.aggregate([
  {
    $project: {
      title: 1,
      ejson: { 
        $serializeEJSON: { 
          input: "$customField",
          onError: { error: "Serialization failed" }
        }
      }
    }
  }
])
```

## Learn More

- :expression:`$deserializeEJSON`
- :expression:`$convert`
- :expression:`$toString`
- The MongoDB Shell provides built-in methods to help work with
Extended JSON. To learn more, see `mongosh-ejson`.
