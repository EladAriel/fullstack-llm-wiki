---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/ObjectId.createFromBase64.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================

# ObjectId.createFromBase64() (mongosh method)

## Definition

Creates an `ObjectId` from a base64 value.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

### Method Fields

The method accepts the following fields:

## Examples

The following examples show how to add an object identifier to a document using `ObjectId.createFromBase64()` and how the object identifier appears in the output when retrieved.

### Create Collection Containing Document with Base64 Number

The following example creates a collection named `objectIdentifierValuesFromBase64`:

```javascript
db.objectIdentifierValuesFromBase64.insertOne( {
   _id: 0,
   objectIdentifierValue: ObjectId.createFromBase64( "SGVsbG8gV29ybGQh" )
} )
```

The `objectIdentifierValue` field contains the object identifier created from the base64 string specified in `ObjectId.createFromBase64()`.

### Retrieve Document from Collection with Object Identifier

The following example retrieves the document:

```javascript
db.objectIdentifierValuesFromBase64.findOne( { _id: 0 } )
```

Example output:

```javascript
{
   _id: 0,
   objectIdentifierValue: ObjectId("48656c6c6f20576f726c6421")
}
```
