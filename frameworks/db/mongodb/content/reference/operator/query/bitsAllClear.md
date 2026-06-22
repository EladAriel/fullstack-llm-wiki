---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/bitsAllClear.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# $bitsAllClear (query predicate operator)

## Behavior

.. include:: /includes/fact-bindata-endian.rst

### Indexes

.. include:: /includes/extracts/fact-query-bitwise-indexes-bitsAllClear.rst

### Floating Point Values

.. include:: /includes/extracts/fact-query-bitsallclear-floating-point.rst

### Sign Extension

.. include:: /includes/extracts/fact-query-bitsallclear-sign-extension.rst

## Examples

.. include:: /includes/extracts/fact-query-bitwise-example-collection.rst

### Bit Position Array

The following query uses the :query:`$bitsAllClear` operator to test whether field `a` has bits clear at position `1` and position `5`, where the least significant bit is position `0`.

```javascript
db.collection.find( { a: { $bitsAllClear: [ 1, 5 ] } } )
```

The query matches the following documents:

```javascript
{ "_id" : 2, "a" : 20, "binaryValueofA" : "00010100" }
{ "_id" : 3, "a" : 20, "binaryValueofA" : "00010100" }
```

### Integer Bitmask

The following query uses the :query:`$bitsAllClear` operator to test whether field `a` has bits clear at positions `0`, `1`, and `5` (the binary representation of the bitmask `35` is `00100011`).

```javascript
db.collection.find( { a: { $bitsAllClear: 35 } } )
```

The query matches the following documents:

```javascript
{ "_id" : 2, "a" : 20, "binaryValueofA" : "00010100" }
{ "_id" : 3, "a" : 20, "binaryValueofA" : "00010100" }
```

### BinData Bitmask

The following query uses the :query:`$bitsAllClear` operator:

```javascript
db.collection.find( { a: { $bitsAllClear: BinData(0, "IA==") } } )
```

The query:

- Specifies `0` as the first value for :bsontype:`BinData
<data_binary>`, which indicates `IA==` should be interpreted as binary. The base-64 value `IA==` in binary is `00100000`, which has `1` in position 5.

- Uses :query:`$bitsAllClear` to return documents where the `a` field
has a clear bit `0` in position 5 of the binary value.

The query returns the following documents:

```javascript
{ "_id" : 2, "a" : 20, "binaryValueofA" : "00010100" }
{ "_id" : 3, "a" : 20, "binaryValueofA" : "00010100" }
```
