---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/schema-validation/specify-json-schema/json-schema-tips.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# Tips for JSON Schema Validation

This page describes best practices for JSON schema validation to help avoid common issues.

## `_id` Field and `additionalProperties: false`

When you specify `additionalProperties: false` in your JSON schema, MongoDB rejects documents that contain fields not included in your schema's `properties` object.

Because all objects contain an automatically-generated `_id` field, when you set `additionalProperties: false, you must include the id` field in your `properties` object. If you don't, all documents are rejected.

For example, with this validation, no documents are valid:

```javascript
{
  "$jsonSchema": {
    "required": [ "_id", "storeLocation" ],
    "properties": {
      "storeLocation": { "bsonType": "string" }
    },
    "additionalProperties": false
  }
}
```

This validation ensures that `storeLocation` is a string. However, the `properties object does not contain an id` field.

To allow documents in the collection, you must update the `properties object to include an id` field:

```javascript
{
  "$jsonSchema": {
    "required": [ "_id", "storeLocation" ],
    "properties": {
      "_id": { "bsonType": "objectId" },
      "storeLocation": { "bsonType": "string" }
    },
    "additionalProperties": false
  }
}
```

## Validation for `null` Field Values

Your application may be configured to set missing field values to `null`, instead of not including those fields in the object sent to the collection.

If your schema validates data types for a field, to insert documents with a `null` value for that field, you must explicitly allow `null` as a valid BSON type.

For example, this schema validation does not allow documents where `storeLocation` is `null`:

```javascript
db.createCollection("sales",
   {
      validator:
         {
            "$jsonSchema": {
               "properties": {
                  "storeLocation": { "bsonType": "string" }
               }
            }
         }
    }
 )
```

With the preceding validation, this document is rejected:

```javascript
db.store.insertOne( { storeLocation: null } )
```

Alternatively, this schema validation allows `null` values for `storeLocation`:

```javascript
db.createCollection("store",
   {
      validator:
         {
            "$jsonSchema": {
               "properties": {
                  "storeLocation": { "bsonType": [ "null", "string" ] }
               }
            }
         }
    }
 )
```

With the preceding validation, this document is allowed:

```javascript
db.store.insertOne( { storeLocation: null } )
```

> **Note:** `null` field values are not the same as missing fields. If a field
is missing from a document, MongoDB does not validate that field.

## Validation with Encrypted Fields

.. include:: /includes/queryable-encryption/qe-csfle-schema-validation.rst
