---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/jsonSchema.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# $jsonSchema (query predicate operator)

## Definition

## Syntax

The `$jsonSchema` operator expression has the following syntax:

```javascript
{ $jsonSchema: <JSON Schema object> }
```

Where the JSON Schema object is formatted according to [draft 4 of the JSON Schema standard](https://tools.ietf.org/html/draft-zyp-json-schema-04).

```javascript
{ <keyword1>: <value1>, ... }
```

For example:

```javascript
{
  $jsonSchema: {
     required: [ "name", "major", "gpa", "address" ],
     properties: {
        name: {
           bsonType: "string",
           description: "must be a string and is required"
        },
        address: {
           bsonType: "object",
           required: [ "zipcode" ],
           properties: {
               "street": { bsonType: "string" },
               "zipcode": { bsonType: "string" } 
           }
        }
     }
  }
}
```

## JSON Schema

.. include:: /includes/schema-validation/json-schema-intro.rst

### Available Keywords

You can specify the following keywords in your JSON Schema.

> **Note:** MongoDB implements a subset of keywords available in JSON Schema.
For a complete list of omissions, see `json-schema-omission`.

### Extensions

MongoDB's implementation of JSON Schema includes the addition of the `bsonType` keyword, which allows you to use all `BSON` types in the `$jsonSchema` operator. `bsonType` accepts the same string aliases used for the :query:`$type` operator.

### Omissions

The following are not supported in MongoDB's implementation of JSON Schema:

- [Hypertext definitions](https://tools.ietf.org/html/draft-luff-json-hyper-schema-00)
in draft 4 of the JSON Schema spec.

- The keywords:
- `$ref`
- `$schema`
- `default`
- `definitions`
- `format`
- `id`
- The `integer` type. You must use the `BSON` type `int` or `long`
with the `bsonType` keyword.

- Hypermedia and linking properties of JSON Schema, including the use of
JSON References and JSON Pointers.

- Unknown keywords.
## Examples

For examples using `$jsonSchema`, see the following pages:

- `schema-validation-json`
- `use-json-schema-query-conditions`
