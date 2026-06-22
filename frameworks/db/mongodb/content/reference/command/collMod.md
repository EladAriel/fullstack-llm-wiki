---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/collMod.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# collMod (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     collMod: <collection or view>, 
     <option1>: <value1>, 
     <option2>: <value2>,
     ... 
   } 
)
```

For the `<collection or view>`, specify the name of a collection or view in the current database.

## Options

### Change Index Properties

To change index options, specify either the key pattern or name of the existing index options you want to change:

```javascript
db.runCommand( {
   collMod: <collection>,
   index: {
      keyPattern: <index_spec> | name: <index_name>,
      expireAfterSeconds: <number>,  // Set the TTL expiration threshold
      hidden: <boolean>,             // Change index visibility in the query planner
      prepareUnique: <boolean>,      // Reject new duplicate index entries 
      unique: <boolean>              // Convert an index to a unique index
   },
   dryRun: <boolean>
} )
```

If the index does not exist, the command errors with the message `"cannot find index <name|keyPattern> for ns <db.collection>"`.

### Validate Documents

### Modify Views

> **Note:** The view modified by this command does not refer to materialized
views. For discussion of on-demand materialized views, see
:pipeline:`$merge` instead.

```javascript
db.runCommand( {
   collMod: "myView",
   viewOn: "activities",
   pipeline: [
     { $match: { status: "Q" } },
     { $project: { user: 1, date: 1, description: 1} } ]
} )
```

### Modify Time Series Collections

> **Note:** If you specify a modification in the `timeseries` parameter of your
`collMod` operation, you cannot use other modification options in the
same command. You must perform time series modifications in a dedicated
command that is separate from other collection modifications.

> **Seealso:** `manual-timeseries-automatic-removal`

### Resize a Capped Collection

.. versionadded:: 6.0

Starting in MongoDB 6.0, you can resize a capped collection. To change a `capped collection's <manual-capped-collection>` maximum size in bytes, use the `cappedSize` option. To change the maximum number of documents in an existing capped collection, use the `cappedMax` option.

> **Note:** You can't use these commands to resize the oplog. Use
:dbcommand:`replSetResizeOplog` instead.

For example, the following command sets the maximum size of a capped collection to 100000 bytes and sets the maximum number of documents in the collection to 500:

```javascript
db.runCommand( {
   collMod: <collection>,
   cappedSize: 100000,
   cappedMax: 500
} )
```

### Change Streams with Document Pre- and Post-Images

.. versionadded:: 6.0

.. include:: /includes/change-stream-pre-and-post-images-introduction.rst

To use `collMod` to enable change stream pre- and post-images for a collection, use the `changeStreamPreAndPostImages` field:

```javascript
db.runCommand( {
   collMod: <collection>,
   changeStreamPreAndPostImages: { enabled: <boolean> }
} )
```

To enable change stream pre- and post-images for a collection, set `changeStreamPreAndPostImages` to `true`. For example:

```javascript
db.runCommand( {
   collMod: "orders",
   changeStreamPreAndPostImages: { enabled: true }
} )
```

To disable change stream pre- and post-images for a collection, set `changeStreamPreAndPostImages` to `false`. For example:

```javascript
db.runCommand( {
   collMod: "orders",
   changeStreamPreAndPostImages: { enabled: false }
} )
```

.. include:: /includes/change-stream-pre-and-post-images-additional-information.rst

### Attach Comment

Optional. You can attach a comment to this command. The comment must be a top-level field and can be any valid `BSON type <bson-types>`. The comment that you specify appears alongside records of this command in the following locations:

- `mongod log messages <log-messages-ref>`, in the
`attr.command.cursor.comment` field.

- `Database profiler <profiler>` output, in the
`command.comment <system.profile.command>` field.

- :dbcommand:`currentOp` output, in the :data:`command.comment
<currentOp.command>` field.

### Write Concern

Optional. A document expressing the `write concern <write-concern>` of the `collMod` command.

Omit to use the default write concern.

## Access Control

If the deployment enforces authentication/authorization, you must have the following privilege to run the `collMod` command:

The built-in role :authrole:`dbAdmin` provides the required privileges.

## Behavior

### Resource Locking

.. include:: /includes/extracts/collMod-resource-lock.rst

## Examples

### Change Expiration Value for Indexes

The following example updates the `expireAfterSeconds` property of an existing TTL index `{ lastAccess: 1 }` on a collection named `user_log`. The current `expireAfterSeconds` property for the index is set to `1800` seconds (or 30 minutes) and the example changes the value to `3600` seconds (or 60 minutes).

```javascript
db.runCommand({ 
   collMod: "user_log",
   index: { 
      keyPattern: { lastAccess: 1 },
      expireAfterSeconds: 3600 
   }
})
```

If successful, the operation returns a document that includes both the old and new value for the changed property:

```javascript
{ "expireAfterSeconds_old" : 1800, "expireAfterSeconds_new" : 3600, "ok" : 1 }
```

### Hide an Index from the Query Planner

> **Note:** To hide an index, you must have :ref:`featureCompatibilityVersion
<view-fcv>` set to `{+minimum-lts-version+}` or greater.

The following example `hides <index-type-hidden>` an existing index on the `orders` collection. Specifically, the operation hides the index with the specification `{ shippedDate: 1 }` from the query planner.

```javascript
db.runCommand( {
   collMod: "orders",
   index: {
      keyPattern: { shippedDate: 1 },
      hidden: true
   }
} )
```

If successful, the operation returns a document that includes both the old and new value for the changed property:

```javascript
{ "hidden_old" : false, "hidden_new" : true, "ok" : 1 }
```

> **Note:** If the operation is successful but the `hidden` value has not
changed (specifically, hiding an already hidden index or unhiding an already
unhidden index), the command omits the `hidden_old` and
`hidden_new` fields from the output.

To hide a text index, you must specify the index by `name` and not by `keyPattern`.

> **Seealso:** - `index-type-hidden`
- :method:`db.collection.hideIndex()`
- :method:`db.collection.unhideIndex()`
