---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/create.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# create (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The `create` command has the following syntax:

> **Note:** MongoDB 6.3 adds the `bucketMaxSpanSeconds` and
`bucketRoundingSeconds` parameters. To downgrade below 6.3, you
must either drop all collections with these parameters, or modify
them to use the corresponding `granularity`, if possible. For
details see :dbcommand:`collMod`.

```javascript
db.runCommand(
   {
     create: <collection or view name>,
     capped: <true|false>,
     timeseries: {
        timeField: <string>,
        metaField: <string>,
        granularity: <string>,
        bucketMaxSpanSeconds: <timespan>,  // Added in MongoDB 6.3
        bucketRoundingSeconds: <timespan>  // Added in MongoDB 6.3
     },
     expireAfterSeconds: <number>,
     clusteredIndex: <document>,  // Added in MongoDB 5.3
     changeStreamPreAndPostImages: <document>,  // Added in MongoDB 6.0
     autoIndexId: <true|false>,
     size: <max_size>,
     max: <max_documents>,
     storageEngine: <document>,
     validator: <document>,
     validationLevel: <string>,
     validationAction: <string>,
     indexOptionDefaults: <document>,
     viewOn: <source>,
     pipeline: <pipeline>,
     collation: <document>,
     writeConcern: <document>,
     encryptedFields: <document>,
     comment: <any>
   }
```

### Command Fields

The `create` command has the following fields:

The :method:`db.createCollection()` method and the :method:`db.createView()` method wrap the `create` command.

## Behavior

`create` has the following behavior:

### Resource Locking

.. include:: /includes/extracts/create-resource-lock.rst

### Transactions

.. include:: /includes/extracts/transactions-explicit-ddl.rst

### Collection or View with Same Name and Options

.. include:: /includes/createCollection-idempotence.rst

### Stable API

.. versionchanged:: 5.0

When using `Stable API <stable-api>` V1, you cannot specify the following fields in a `create` command:

- `autoIndexId`
- `capped`
- `indexOptionDefaults`
- `max`
- `size`
- `storageEngine`
## Access Control

.. include:: /includes/extracts/access-control-create-cmd.rst

## Examples

### Create a Capped Collection

To create a `capped collection` limited to 64 kilobytes, issue the command in the following form:

```javascript
db.runCommand( { create: "collection", capped: true, size: 64 * 1024 } )
```

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

> **Note:** In this example `expireAfterSeconds` is specified as `86400`
which means documents expire `86400` seconds after the
`timestamp` value. See `manual-timeseries-automatic-removal`.

### Create a Clustered Collection

.. include:: /includes/create-clustered-collection-example.rst

### Create a Collection with Change Stream Pre- and Post-Images for Documents

.. include:: /includes/change-stream-pre-and-post-images-introduction.rst

The following example creates a collection that has `changeStreamPreAndPostImages <create.changeStreamPreAndPostImages>` enabled:

```javascript
db.runCommand( {
   create: "temperatureSensor",
   changeStreamPreAndPostImages: { enabled: true }
} )
```

.. include:: /includes/change-stream-pre-and-post-images-additional-information.rst

### Create a View

> **Note:** The view created by this command does not refer to materialized
views. For discussion of on-demand materialized views, see
:pipeline:`$merge` instead.

.. include:: /includes/extracts/views-restriction-output-to-disk.rst

To create a `view <views-landing-page>` using the `create` command, use the following syntax:

```javascript
db.runCommand( { create: <view>, viewOn: <source>, pipeline: <pipeline> } )
```

or if specifying a collation:

```javascript
db.runCommand( { create: <view>, viewOn: <source>, pipeline: <pipeline>, collation: <collation> } )
```

For example, create a `survey` collection with the following documents:

```javascript
db.survey.insertMany(
   [
      { _id: 1, empNumber: "abc123", feedback: { management: 3, environment: 3 }, department: "A" },
      { _id: 2, empNumber: "xyz987", feedback: { management: 2, environment: 3 }, department: "B" },
      { _id: 3, empNumber: "ijk555", feedback: { management: 3, environment: 4 }, department: "A" }
   ]
)
```

The following operation creates a `managementRatings view with the id`, `feedback.management`, and `department` fields:

```javascript
db.runCommand ( {
   create: "managementFeedback",
   viewOn: "survey",
   pipeline: [ { $project: { "management": "$feedback.management", department: 1 } } ]
} )
```

> **Important:** .. include:: /includes/extracts/views-public-definition.rst

> **Seealso:** :method:`db.createView()`

### Specify Collation

You can specify `collation <collation>` at the collection or `view <views-landing-page>` level. For example, the following operation creates a collection, specifying a collation for the collection (See `collation-document-fields` for descriptions of the collation fields):

```javascript
db.runCommand ( {
   create: "myColl",
   collation: { locale: "fr" }
});
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

> **Seealso:** - `create-view-w-collation`
- `ref-collation-and-views`

### Specify Storage Engine Options

You can specify collection-specific storage engine configuration options when you create a collection with :method:`db.createCollection()`. Consider the following operation:

```javascript
db.runCommand( {
    create: "users",
    storageEngine: { wiredTiger: { configString: "<option>=<setting>" } }
} )
```

This operation creates a new collection named `users` with a specific configuration string that MongoDB will pass to the `wiredTiger` storage engine. See the :wtdocs-v5.0:`WiredTiger documentation of collection level options </struct_w_t___s_e_s_s_i_o_n.html>` for specific `wiredTiger` options.

.. include:: /includes/fact-encryption-options-create-collection.rst
