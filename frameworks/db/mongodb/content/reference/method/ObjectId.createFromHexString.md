---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/ObjectId.createFromHexString.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===============================================

# ObjectId.createFromHexString() (mongosh method)

## Definition

Creates an `ObjectId` from a hexadecimal value.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The `hexadecimalString` field specifies a string that contains a 24 character hexadecimal value. For example, `"64c13ab08edf48a008793cac"`.

## Examples

The following examples show how to add an object identifier to a document using `ObjectId.createFromHexString()` and how the object identifier appears in the output when retrieved.

### Create Collection Containing Document with Object Identifier

The following example creates a collection named `objectIdentifierValuesFromHex`:

```javascript
db.objectIdentifierValuesFromHex.insertOne( {
   _id: 0,
   objectIdentifierValue: ObjectId.createFromHexString( "64c13ab08edf48a008793cac" )
} )
```

The `objectIdentifierValue` field contains the object identifier created from the hexadecimal string specified in `ObjectId.createFromHexString()`.

### Retrieve Document from Collection with Object Identifier

The following example retrieves the document:

```javascript
db.objectIdentifierValuesFromHex.findOne( { _id: 0 } )
```

Example output:

```javascript
{
   _id: 0,
   objectIdentifierValue: ObjectId("64c13ab08edf48a008793cac")
}
```
