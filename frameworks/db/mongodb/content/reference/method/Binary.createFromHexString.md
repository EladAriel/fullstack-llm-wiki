---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Binary.createFromHexString.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================

# Binary.createFromHexString() (mongosh method)

## Definition

Creates a binary object from a hexadecimal value.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The `hexadecimalString` field specifies a string that contains a hexadecimal value. For example, `"64c13ab08edf48a008793cac"`.

## Examples

The following examples show how to add a binary object to a document using `Binary.createFromHexString()` and how the binary object appears in the output when retrieved.

### Create Collection Containing Document with Binary Object

The following example creates a collection named `binaryObjectsFromHexString`:

```javascript
db.binaryObjectsFromHexString.insertOne( {
   _id: 0,
   binaryObject: Binary.createFromHexString( "64c13ab08edf48a008793cac" )
} )
```

The `binaryObject` field contains the binary object created from the string specified in `Binary.createFromHexString()`.

### Retrieve Document from Collection with Binary Object

The following example retrieves the document:

```javascript
db.binaryObjectsFromHexString.findOne( { _id: 0 } )
```

> **Note:** Starting in :binary:`mongosh` 2.0.0, binary values are shown as
`Binary.createFromBase64( <base64String> )` values instead of
`Binary( Buffer.from( <base64String> ) )` values. This only changes
the display of binary values.

Example output, which shows the number in base64:

```javascript
{
   _id: 0,
   binaryObject: Binary.createFromBase64("ZME6sI7fSKAIeTys")
}
```
