---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/bitsAllSet.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# $bitsAllSet (query predicate operator)

## Behavior

.. include:: /includes/fact-bindata-endian.rst

### Indexes

.. include:: /includes/extracts/fact-query-bitwise-indexes-bitsAllSet.rst

### Floating Point Values

.. include:: /includes/extracts/fact-query-bitsallset-floating-point.rst

### Sign Extension

.. include:: /includes/extracts/fact-query-bitsallset-sign-extension.rst

## Examples

.. include:: /includes/extracts/fact-query-bitwise-example-collection.rst

### Bit Position Array

The following query uses the :query:`$bitsAllSet` operator to test whether field `a` has bits set at position `1` and position `5`, where the least significant bit is position `0`.

```javascript
db.collection.find( { a: { $bitsAllSet: [ 1, 5 ] } } )
```

The query matches the following documents:

```javascript
{ "_id" : 1, "a" : 54, "binaryValueofA" : "00110110" }
{ "_id" : 4, "a" : BinData(0,"Zg=="), "binaryValueofA" : "01100110" }
```

### Integer Bitmask

The following query uses the :query:`$bitsAllSet` operator to test whether field `a` has bits set at positions `1`, `4`, and `5` (the binary representation of the bitmask `50` is `00110010`).

```javascript
db.collection.find( { a: { $bitsAllSet: 50 } } )
```

The query matches the following document:

```javascript
{ "_id" : 1, "a" : 54, "binaryValueofA" : "00110110" }
```

### BinData Bitmask

The following query uses the :query:`$bitsAllSet` operator to test whether field `a` has bits set at positions `4` and `5` (the binary representation of `BinData(0, "MA==")` is `00110000`).

```javascript
db.collection.find( { a: { $bitsAllSet: BinData(0, "MA==") } } )
```

The query matches the following document:

```javascript
{ _id: 1, a: 54, binaryValueofA: "00110110" }
```
