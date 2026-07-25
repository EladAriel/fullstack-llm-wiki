---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/BinData.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================

# BinData() (mongosh method)

## Definition

Creates a binary data object.

`BinData` has the following syntax:

### Binary Subtypes

Specify one of the following values for `sub_type`:

.. include:: /includes/binary-subtypes.rst

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

.. include:: /includes/fact-bindata-endian.rst

## Examples

### Insert a `BinData()` Object

Use the `BinData()` constructor to create the `bdata` variable.

```javascript
var bdata = BinData(0, "gf1UcxdHTJ2HQ/EGQrO7mQ==")
```

Insert the object into the `testbin` collection.

```javascript
db.testbin.insertOne( { _id : 1, bin_data: bdata } )
```

Query the `testbin` collection for the inserted document.

```javascript
db.testbin.find()
```

You can see the binary `buffer` stored in the collection.

```javascript
{
  _id: 1,
  bin_data: Binary(Buffer.from("81fd547317474c9d8743f10642b3bb99", "hex"), 0) 
}
```

### Get the Length of `BinData()` Object

Use the `BinData()` constructor to create the `bdata` variable.

```javascript
var bdata = BinData(0, "gf1UcxdHTJ2HQ/EGQrO7mQ==")
```

Use `.length()` to return the bit length of the object.

```javascript
bdata.length()
```

The returned value is:

```javascript
16
```
