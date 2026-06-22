---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.createCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# db.createCollection() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The `db.createCollection()` method has the following prototype form:

```javascript
db.createCollection( <name>,
    {
      capped: <boolean>,
      timeseries: {                  // Added in MongoDB 5.0
         timeField: <string>,        // required for time series collections
         metaField: <string>,
         granularity: <string>,
         bucketMaxSpanSeconds: <number>,  // Added in MongoDB 6.3
         bucketRoundingSeconds: <number>  // Added in MongoDB 6.3
      },
      expireAfterSeconds: <number>,
      clusteredIndex: <document>,  // Added in MongoDB 5.3
      changeStreamPreAndPostImages: <document>,  // Added in MongoDB 6.0
      size: <number>,
      max: <number>,
      storageEngine: <document>,
      validator: <document>,
      validationLevel: <string>,
      validationAction: <string>,
      indexOptionDefaults: <document>,
      viewOn: <string>,
      pipeline: <pipeline>,
      collation: <document>,
      writeConcern: <document>,
      encryptedFields: <document>
    }
  )
```

The `db.createCollection()` method has the following parameters:

The `options` document contains the following fields:

## Access Control

.. include:: /includes/extracts/access-control-createCollection.rst

## Behavior

`db.createCollection()` has the following behavior:

### Resource Locking

.. include:: /includes/extracts/createCollection-resource-lock.rst

### Transactions

.. include:: /includes/extracts/transactions-explicit-ddl.rst

### Collection or View with Same Name and Options

.. include:: /includes/createCollection-idempotence.rst

## Examples

### Create a Capped Collection

Capped collections have maximum size or document counts that prevent them from growing beyond maximum thresholds. All capped collections must specify a maximum size and may also specify a maximum document count. MongoDB removes older documents if a collection reaches the maximum size limit before it reaches the maximum document count. Consider the following example:

```javascript
db.createCollection("log", { capped : true, size : 5242880, max : 5000 } )
```

This command creates a collection named `log` with a maximum size of 5 megabytes and a maximum of 5000 documents.

See `manual-capped-collection` for more information about capped collections.

### Create a Time Series Collection

To create a `time series collection` that captures weather data for the past 24 hours, issue this command:

```javascript
db.createCollection(
    "weather24h",
    {
       timeseries: {
          timeField: "timestamp",
          metaField: "data",
          granularity: "hours"
       },
       expireAfterSeconds: 86400
    }
)
```

Alternately, to create the same collection but limit each bucket to timestamp values within the same hour, issue this command:

```javascript
db.createCollection(
    "weather24h",
    {
       timeseries: {
          timeField: "timestamp",
          metaField: "data",
          bucketMaxSpanSeconds: 3600,
          bucketRoundingSeconds: 3600
       },
       expireAfterSeconds: 86400
    }
)
```

### Create a Clustered Collection

.. include:: /includes/db-create-clustered-collection-example.rst

### Create a Collection with Change Stream Pre- and Post-Images for Documents

.. include:: /includes/change-stream-pre-and-post-images-introduction.rst

The following example creates a collection that has `changeStreamPreAndPostImages <db.createCollection.changeStreamPreAndPostImages>` enabled:

```javascript
db.createCollection(
   "temperatureSensor",
   { changeStreamPreAndPostImages: { enabled: true } }
);
```

.. include:: /includes/change-stream-pre-and-post-images-additional-information.rst

### Specify Collation

.. include:: /includes/extracts/collation-description.rst

You can specify `collation <collation>` at the collection or `view <views-landing-page>` level. For example, the following operation creates a collection, specifying a collation for the collection (See `collation-document-fields` for descriptions of the collation fields):

```javascript
db.createCollection( "myColl", { collation: { locale: "fr" } } );
```

This collation will be used by indexes and operations that support collation unless they explicitly specify a different collation. For example, insert the following documents into `myColl`:

```javascript
{ _id: 1, category: "café" }
{ _id: 2, category: "cafe" }
{ _id: 3, category: "cafE" }
```

The following operation uses the collection's collation:

```javascript
db.myColl.find().sort( { category: 1 } )
```

The operation returns documents in the following order:

```javascript
{ "_id" : 2, "category" : "cafe" }
{ "_id" : 3, "category" : "cafE" }
{ "_id" : 1, "category" : "café" }
```

The same operation on a collection that uses simple binary collation (i.e. no specific collation set) returns documents in the following order:

```javascript
{ "_id" : 3, "category" : "cafE" }
{ "_id" : 2, "category" : "cafe" }
{ "_id" : 1, "category" : "café" }
```

> **Seealso:** `create-view-w-collation`

### Specify Storage Engine Options

You can specify collection-specific storage engine configuration options when you create a collection with `db.createCollection()`. Consider the following operation:

```javascript
db.createCollection(
   "users",
   { storageEngine: { wiredTiger: { configString: "<option>=<setting>" } } }
)
```

This operation creates a new collection named `users` with a specific configuration string that MongoDB will pass to the `wiredTiger` storage engine.

For example, to specify the `zlib` compressor for file blocks in the `users` collection, set the `block_compressor` option with the following command:

```javascript
db.createCollection(
   "users",
   { storageEngine: { wiredTiger: { configString: "block_compressor=zlib" } } }
)
```

.. include:: /includes/fact-encryption-options-create-collection.rst
