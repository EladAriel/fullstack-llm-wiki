---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.distinct.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# db.collection.distinct() (mongosh method)

.. include:: includes/wayfinding/mongosh-method-distinct.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

This method takes the following parameters:

.. include:: /includes/note-distinct-bson-limit-agg-alternative.rst

The following diagram shows an example `distinct()` call.

.. include:: /images/distinct.rst

## Options

```javascript
{ collation: <document> }
```

## Behavior

In a `sharded cluster`, the :dbcommand:`distinct` command may return `orphaned documents <orphaned document>`.

For `time series collections <manual-timeseries-landing>`, the `distinct` command can't make efficient use of indexes. Instead, use a :pipeline:`$group` aggregation to group documents by distinct values. For details, see `Time Series Limitations <timeseries-limitation-distinct>`.

### Array Fields

.. include:: /includes/extracts/fact-distinct-method-array-field.rst

For an example, see `distinct-method-array`.

### Index Use

.. include:: /includes/extracts/fact-distinct-method-index-use.rst

### Transactions

.. include:: /includes/extracts/transactions-distinct-support.rst

.. include:: /includes/extracts/transactions-usage.rst

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

### Replica Set Member State Restriction

.. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

### Query Settings

.. include:: /includes/persistent-query-settings-info-for-queries.rst

## Examples

The examples use the `inventory` collection that contains the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, dept: "A", item: { sku: "111", color: "red" }, sizes: [ "S", "M" ] },
   { _id: 2, dept: "A", item: { sku: "111", color: "blue" }, sizes: [ "M", "L" ] },
   { _id: 3, dept: "B", item: { sku: "222", color: "blue" }, sizes: "S" },
   { _id: 4, dept: "A", item: { sku: "333", color: "black" }, sizes: [ "S" ] }
] )
```

### Return Distinct Values for a Field

The following example returns distinct values for the `dept` field:

```javascript
db.inventory.distinct( "dept" )
```

The operation returns:

```javascript
[ "A", "B" ]
```

### Return Distinct Values for an Embedded Field

The following example returns distinct values for the embedded `item.sku` field:

```javascript
db.inventory.distinct( "item.sku" )
```

The operation returns:

```javascript
[ "111", "222", "333" ]
```

> **Seealso:** `document-dot-notation` for information on accessing fields
within embedded documents

### Return Distinct Values for an Array Field

The following example returns distinct values for the `sizes` array field:

```javascript
db.inventory.distinct( "sizes" )
```

The operation returns:

```javascript
[ "M", "S", "L" ]
```

For information on `distinct()` and array fields, see the `Behavior <distinct-method-behavior-array>` section.

### Specify Query with `distinct`

The following example returns distinct values for the embedded `item.sku` field where `dept` equals `"A"`:

```javascript
db.inventory.distinct( "item.sku", { dept: "A" } )
```

The operation returns:

```javascript
[ "111", "333" ]
```

### Specify a Collation

.. include:: /includes/extracts/collation-description.rst

A collection `myColl` has the following documents:

```javascript
db.myColl.insertMany( [
   { _id: 1, category: "café", status: "A" },
   { _id: 2, category: "cafe", status: "a" },
   { _id: 3, category: "cafE", status: "a" }
] )
```

The following aggregation operation includes the `collation` option:

```javascript
db.myColl.distinct( "category", {}, { collation: { locale: "fr", strength: 1 } } )
```

For descriptions on the collation fields, see `collation-document-fields`.
