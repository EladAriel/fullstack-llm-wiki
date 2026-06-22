---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Binary.createFromBase64.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# Binary.createFromBase64() (mongosh method)

## Definition

Creates a binary object from a base64 value.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

### Method Fields

The method accepts the following fields:

## Examples

The following examples show how to add a binary object to a document using `Binary.createFromBase64()` and how the binary object appears in the output when retrieved.

### Create Collection Containing Document with Binary Object

The following example creates a collection named `binaryObjectsFromBase64`:

```javascript
db.binaryObjectsFromBase64.insertOne( {
   _id: 0,
   binaryObject: Binary.createFromBase64( "SGVsbG8gV29ybGQhCg==" )
} )
```

The `binaryObject` field contains the binary object created from the string specified in `Binary.createFromBase64()`.

### Retrieve Document from Collection with Binary Object

The following example retrieves the document:

```javascript
db.binaryObjectsFromBase64.findOne( { _id: 0 } )
```

> **Note:** Starting in :binary:`mongosh` 2.0.0, binary objects are shown
as `Binary.createFromBase64( <base64String> )` values instead of
`Binary( Buffer.from( <base64String> ) )` values. This only changes
the display of binary values.

Example output, starting in `mongosh` 2.0.0:

```javascript
{
   _id: 0,
   binaryObject: Binary.createFromBase64("SGVsbG8gV29ybGQhCg==")
}
```
