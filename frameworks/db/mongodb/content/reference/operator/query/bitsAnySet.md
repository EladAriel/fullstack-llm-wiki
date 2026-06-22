---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/bitsAnySet.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# $bitsAnySet (query predicate operator)

## Behavior

.. include:: /includes/fact-bindata-endian.rst

### Indexes

.. include:: /includes/extracts/fact-query-bitwise-indexes-bitsAnySet.rst

### Floating Point Values

.. include:: /includes/extracts/fact-query-bitsanyset-floating-point.rst

### Sign Extension

.. include:: /includes/extracts/fact-query-bitsanyset-sign-extension.rst

## Examples

.. include:: /includes/extracts/fact-query-bitwise-example-collection.rst

### Bit Position Array

The following query uses the :query:`$bitsAnySet` operator to test whether field `a` has either bit position `1` or bit position `5` set, where the least significant bit is position `0`.

```javascript
db.collection.find( { a: { $bitsAnySet: [ 1, 5 ] } } )
```

The query matches the following documents:

```javascript
{ "_id" : 1, "a" : 54, "binaryValueofA" : "00110110" }
{ "_id" : 4, "a" : BinData(0,"Zg=="), "binaryValueofA" : "01100110" }
```

### Integer Bitmask

The following query uses the :query:`$bitsAnySet` operator to test whether field `a` has any bits set at positions `0`, `1`, and `5` (the binary representation of the bitmask `35` is `00100011`).

```javascript
db.collection.find( { a: { $bitsAnySet: 35 } } )
```

The query matches the following documents:

```javascript
{ "_id" : 1, "a" : 54, "binaryValueofA" : "00110110" }
{ "_id" : 4, "a" : BinData(0,"Zg=="), "binaryValueofA" : "01100110" }
```

### BinData Bitmask

The following query uses the :query:`$bitsAnySet` operator to test whether field `a` has any bits set at positions `4`, and `5` (the binary representation of `BinData(0, "MA==")` is `00110000`).

```javascript
db.collection.find( { a: { $bitsAnySet: BinData(0, "MA==") } } )
```

The query matches the following documents:

```javascript
{ "_id" : 1, "a" : 54, "binaryValueofA" : "00110110" }
{ "_id" : 2, "a" : 20, "binaryValueofA" : "00010100" }
{ "_id" : 3, "a" : 20.0, "binaryValueofA" : "00010100" }
{ "_id" : 4, "a" : BinData(0,"Zg=="), "binaryValueofA" : "01100110" }
```
