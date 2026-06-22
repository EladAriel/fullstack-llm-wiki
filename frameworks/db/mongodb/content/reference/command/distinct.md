---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/distinct.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# distinct (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-limited-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
     distinct: "<collection>",
     key: "<field>",
     query: <query>,
     readConcern: <read concern document>,
     collation: <collation document>,
     comment: <any>,
     hint: <string or document>
   }
)
```

## Command Fields

The command takes the following fields:

.. include:: /includes/note-distinct-bson-limit-agg-alternative.rst

MongoDB also provides the shell wrapper method :method:`db.collection.distinct()` for the :dbcommand:`distinct` command. Additionally, many MongoDB `drivers <driver>` provide a wrapper method. Refer to the specific driver documentation.

## Behavior

In a `sharded cluster`, the :dbcommand:`distinct` command may return `orphaned documents <orphaned document>`.

For `time series collections <manual-timeseries-landing>`, the `distinct` command can't make efficient use of indexes. Instead, use a :pipeline:`$group` aggregation to group documents by distinct values. For details, see `Time Series Limitations <timeseries-limitation-distinct>`.

### Array Fields

.. include:: /includes/extracts/fact-distinct-command-array-field.rst

.. include:: /includes/distinct-arrays-in-collections-and-views.rst

For examples, see:

- `distinct-command-array`
- `distinct-arrays-in-collections-and-views`
### Index Use

.. include:: /includes/extracts/fact-distinct-command-index-use.rst

### Transactions

.. include:: /includes/extracts/transactions-distinct-support.rst

.. include:: /includes/extracts/transactions-usage.rst

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

### Replica Set Member State Restriction

.. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

### Index Filters and Collations

.. include:: /includes/index-filters-and-collations.rst

### Query Settings

.. include:: /includes/persistent-query-settings-info-for-queries.rst

## Examples

The examples use the `inventory` collection that contains the following documents:

```javascript
{ "_id": 1, "dept": "A", "item": { "sku": "111", "color": "red" }, "sizes": [ "S", "M" ] }
{ "_id": 2, "dept": "A", "item": { "sku": "111", "color": "blue" }, "sizes": [ "M", "L" ] }
{ "_id": 3, "dept": "B", "item": { "sku": "222", "color": "blue" }, "sizes": "S" }
{ "_id": 4, "dept": "A", "item": { "sku": "333", "color": "black" }, "sizes": [ "S" ] }
```

### Return Distinct Values for a Field

The following example returns the distinct values for the field `dept` from all documents in the `inventory` collection:

```javascript
db.runCommand ( { distinct: "inventory", key: "dept" } )
```

The command returns a document with a field named `values` that contains the distinct `dept` values:

```javascript
{
   "values" : [ "A", "B" ],
   "ok" : 1
}
```

### Return Distinct Values for an Embedded Field

The following example returns the distinct values for the field `sku`, embedded in the `item` field, from all documents in the `inventory` collection:

```javascript
db.runCommand ( { distinct: "inventory", key: "item.sku" } )
```

The command returns a document with a field named `values` that contains the distinct `sku` values:

```javascript
{
  "values" : [ "111", "222", "333" ],
  "ok" : 1
}
```

> **Seealso:** `document-dot-notation` for information on accessing fields
within embedded documents

### Return Distinct Values for an Array Field

The following example returns the distinct values for the field `sizes` from all documents in the `inventory` collection:

```javascript
db.runCommand ( { distinct: "inventory", key: "sizes" } )
```

The command returns a document with a field named `values` that contains the distinct `sizes` values:

```javascript
{
  "values" : [ "M", "S", "L" ],
  "ok" : 1
}
```

For information on :dbcommand:`distinct` and array fields, see the `Behavior <distinct-command-array-behavior>` section.

### Arrays in Collections and Views

.. include:: /includes/distinct-arrays-in-collections-and-views.rst

The following example creates a collection named `sensor` with an array of temperature values for each document:

```javascript
db.sensor.insertMany( [
   { _id: 0, temperatures: [ { value: 1 }, { value: 4 } ] },
   { _id: 1, temperatures: [ { value: 2 }, { value: 8 } ] },
   { _id: 2, temperatures: [ { value: 3 }, { value: 12 } ] },
   { _id: 3, temperatures: [ { value: 1 }, { value: 4 } ] }
] )
```

The following example creates a view named `sensorView` from the `sensor` collection:

```javascript
db.createView( "sensorView", "sensor", [] )
```

The following example uses :dbcommand:`distinct` to return the unique values from the `temperatures` array in the `sensor` collection:

```javascript
db.sensor.distinct( "temperatures.1.value" )
```

The `1` in `temperatures.1.value` specifies the `temperatures` array index.

Example output:

```javascript
[ 4, 8, 12 ]
```

Example for `sensorView`:

```javascript
db.sensorView.distinct( "temperatures.1.value" )
```

Example output:

- `[ 4, 8, 12 ]` starting in MongoDB 6.0 (identical to result
returned from the `sensor` collection).

- `[]` in MongoDB versions earlier than 6.0.
### Specify Query with `distinct`

The following example returns the distinct values for the field `sku`, embedded in the `item` field, from the documents whose `dept` is equal to `"A"`:

```javascript
db.runCommand ( { distinct: "inventory", key: "item.sku", query: { dept: "A"} } )
```

The command returns a document with a field named `values` that contains the distinct `sku` values:

```javascript
{
  "values" : [ "111", "333" ],
  "ok" : 1
}
```

### Specify a Collation

.. include:: /includes/extracts/collation-description.rst

A collection `myColl` has the following documents:

```javascript
{ _id: 1, category: "café", status: "A" }
{ _id: 2, category: "cafe", status: "a" }
{ _id: 3, category: "cafE", status: "a" }
```

The following aggregation operation includes the `collation` option:

```javascript
db.runCommand( 
   { 
      distinct: "myColl",
      key: "category",
      collation: { locale: "fr", strength: 1 } 
   }
)
```

For descriptions on the collation fields, see `collation-document-fields`.

### Override Default Read Concern

To override the default read concern level of :readconcern:`"local"`, use the `readConcern` option.

The following operation on a replica set specifies a `/reference/read-concern` of :readconcern:`"majority"` to read the most recent copy of the data confirmed as having been written to a majority of the nodes.

> **Note:** .. include:: /includes/fact-readConcern-most-recent-data-in-node.rst

```javascript
db.runCommand(
   {
     distinct: "restaurants",
     key: "rating",
     query: { cuisine: "italian" },
     readConcern: { level: "majority" }
   }
)
```

.. include:: /includes/usage-read-concern-majority.rst

### Specify an Index

You can specify an index name or pattern using the hint option.

To specify a hint based on an index name:

```javascript
db.runCommand ( { distinct: "inventory", key: "dept", hint: "sizes" } )
```

To specify a hint based on an index pattern:

```javascript
db.runCommand ( { distinct: "inventory", key: "dept", hint: { sizes: 1 } } )
```
