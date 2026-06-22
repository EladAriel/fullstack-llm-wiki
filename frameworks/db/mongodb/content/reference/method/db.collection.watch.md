---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.watch.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# db.collection.watch() (mongosh method)

.. include:: /includes/fact-mongosh-shell-method-alt

## Definition

### Parameters

## Fields

The `options` document can contain the following fields and values:

> **Seealso:** :method:`db.watch()` and :method:`Mongo.watch()`

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Availability

### Deployment

:method:`db.collection.watch()` is available for replica set and sharded cluster deployments :

- For a replica set, you can issue :method:`db.collection.watch()` on
any data-bearing member.

- For a sharded cluster, you must issue :method:`db.collection.watch()`
on a :binary:`~bin.mongos` instance.

### Storage Engine

You can only use :method:`db.collection.watch()` with the `Wired Tiger storage engine <storage-wiredtiger>`.

### Read Concern `majority` Support

.. include:: /includes/extracts/changestream-rc-majority-4.2.rst

## Behavior

- :method:`db.collection.watch()` only notifies on data changes that have
persisted to a majority of data-bearing members.

- .. include:: /includes/extracts/changestream-cursor-open.rst
### Resumability

.. include:: /includes/extracts/changestream-resume.rst

.. include:: /includes/change-stream/resume-after

### Full Document Lookup of Update Operations

.. include:: /includes/extracts/changestream-full-document-lookup.rst

## Access Control

When running with access control, the user must have the :authaction:`find` and :authaction:`changeStream` privilege actions on the `collection resource <resource-document>`. That is, a user must have a `role <roles>` that grants the following `privilege <privileges>`:

```javascript
{ resource: { db: <dbname>, collection: <collection> }, actions: [ "find", "changeStream" ] }
```

The built-in :authrole:`read` role provides the appropriate privileges.

## Cursor Iteration

.. include:: /includes/fact-multiple-cursor-monitors.rst

## Examples

### Open a Change Stream

The following operation opens a change stream cursor against the `data.sensors` collection:

```javascript
watchCursor = db.getSiblingDB("data").sensors.watch()
```

Iterate the cursor to check for new events. Use the :method:`cursor.isClosed()` method with the :method:`cursor.tryNext()` method to ensure the loop only exits if the change stream cursor is closed and there are no objects remaining in the latest batch:

```javascript
while (!watchCursor.isClosed()) {
  let next = watchCursor.tryNext()
  while (next !== null) {
    printjson(next);
    next = watchCursor.tryNext()
  }
}
```

For complete documentation on change stream output, see `change-stream-output`.

.. include:: /includes/isExhausted-no-change-streams.rst

### Change Stream with Full Document Update Lookup

.. include:: /includes/change-stream/warning_fullDocument_match.rst

Set the `fullDocument` option to `"updateLookup"` to direct the change stream cursor to lookup the most current majority-committed version of the document associated to an update change stream event.

The following operation opens a change stream cursor against the `data.sensors` collection using the `fullDocument : "updateLookup"` option.

```javascript
watchCursor = db.getSiblingDB("data").sensors.watch(
   [],
   { fullDocument : "updateLookup" }
)
```

Iterate the cursor to check for new events. Use the :method:`cursor.isClosed()` method with the :method:`cursor.tryNext()` method to ensure the loop only exits if the change stream cursor is closed and there are no objects remaining in the latest batch:

```javascript
while (!watchCursor.isClosed()) {
  let next = watchCursor.tryNext()
  while (next !== null) {
    printjson(next);
    next = watchCursor.tryNext()
  }
}
```

For any update operation, the change event returns the result of the document lookup in the `fullDocument` field.

For an example of the full document update output, see  `change stream update event <change-streams-update-event>`.

For complete documentation on change stream output, see `change-stream-output`.

### Change Streams with Document Pre- and Post-Images

.. include:: /includes/change-stream-pre-and-post-images-introduction.rst

.. include:: /includes/change-stream-pre-and-post-images-additional-information.rst

Create Collection `````````````````

Create a `temperatureSensor` collection that has `changeStreamPreAndPostImages <db.createCollection.changeStreamPreAndPostImages>` enabled:

```javascript
db.createCollection(
   "temperatureSensor",
   { changeStreamPreAndPostImages: { enabled: true } }
)
```

Populate the `temperatureSensor` collection with temperature readings:

```javascript
db.temperatureSensor.insertMany( [
   { "_id" : 0, "reading" : 26.1 },
   { "_id" : 1, "reading" : 25.9 },
   { "_id" : 2, "reading" : 24.3 },
   { "_id" : 3, "reading" : 22.4 },
   { "_id" : 4, "reading" : 24.6 }
] )
```

The following sections show change stream examples for document pre- and post-images that use the `temperatureSensor` collection.

Change Stream with Document Pre-Image `````````````````````````````````````

You use the `fullDocumentBeforeChange: "whenAvailable"` setting to output the document pre-image, if available. The pre-image is the document before it was replaced, updated, or deleted. There is no pre-image for an inserted document.

The following example creates a change stream cursor for the `temperatureSensor` collection using `fullDocumentBeforeChange: "whenAvailable"`:

```javascript
watchCursorFullDocumentBeforeChange = db.temperatureSensor.watch(
   [],
   { fullDocumentBeforeChange: "whenAvailable" }
)
```

The following example uses the cursor to check for new change stream events:

```javascript
while ( !watchCursorFullDocumentBeforeChange.isClosed() ) {
   if ( watchCursorFullDocumentBeforeChange.hasNext() ) {
      printjson( watchCursorFullDocumentBeforeChange.next() );
   }
}
```

.. include:: /includes/change-stream-pre-and-post-images-example-cursor-methods.rst

The following example updates the `reading` field for a `temperatureSensor` document:

```javascript
db.temperatureSensor.updateOne(
   { _id: 2 },
   { $set: { reading: 22.1 } }
)
```

After the `temperatureSensor` document is updated, the change event outputs the document pre-image in the `fullDocumentBeforeChange` field. The pre-image contains the `temperatureSensor` document `reading` field before it was updated. For example:

```javascript
{
   "_id" : {
      "_data" : "82624B21...",
      "_typeBits" : BinData(0,"QA==")
   },
   "operationType" : "update",
   "clusterTime" : Timestamp(1649090957, 1),
   "ns" : {
      "db" : "test",
      "coll" : "temperatureSensor"
   },
   "documentKey" : {
      "_id" : 2
   },
   "updateDescription" : {
      "updatedFields" : {
         "reading" : 22.1
      },
      "removedFields" : [ ],
      "truncatedArrays" : [ ]
   },
   "fullDocumentBeforeChange" : {
      "_id" : 2,
      "reading" : 24.3
   }
}
```

.. include:: /includes/change-stream-pre-and-post-images-output.rst

Change Stream with Document Post-Image ``````````````````````````````````````

You use the `fullDocument: "whenAvailable"` setting to output the document post-image, if available. The post-image is the document after it was inserted, replaced, or updated. There is no post-image for a deleted document.

The following example creates a change stream cursor for the `temperatureSensor` collection using `fullDocument: "whenAvailable"`:

```javascript
watchCursorFullDocument = db.temperatureSensor.watch(
   [],
   { fullDocument: "whenAvailable" }
)
```

The following example uses the cursor to check for new change stream events:

```javascript
while ( !watchCursorFullDocument.isClosed() ) {
   if ( watchCursorFullDocument.hasNext() ) {
      printjson( watchCursorFullDocument.next() );
   }
}
```

.. include:: /includes/change-stream-pre-and-post-images-example-cursor-methods.rst

The following example updates the `reading` field for a `temperatureSensor` document:

```javascript
db.temperatureSensor.updateOne(
   { _id: 1 },
   { $set: { reading: 29.5 } }
)
```

After the `temperatureSensor` document is updated, the change event outputs the document post-image in the `fullDocument` field. The post-image contains the `temperatureSensor` document `reading` field after it was updated. For example:

```javascript
{
   "_id" : {
      "_data" : "8262474D...",
      "_typeBits" : BinData(0,"QA==")
   },
   "operationType" : "update",
   "clusterTime" : Timestamp(1648840090, 1),
   "fullDocument" : {
      "_id" : 1,
      "reading" : 29.5
   },
   "ns" : {
      "db" : "test",
      "coll" : "temperatureSensor"
   },
   "documentKey" : {
      "_id" : 1
   },
   "updateDescription" : {
      "updatedFields" : {
         "reading" : 29.5
      },
      "removedFields" : [ ],
      "truncatedArrays" : [ ]
   }
}
```

.. include:: /includes/change-stream-pre-and-post-images-output.rst

### Change Stream with Aggregation Pipeline Filter

> **Note:** .. include:: /includes/extracts/4.2-changes-change-stream-modification-error.rst

The following operation opens a change stream cursor against the `data.sensors` collection using an aggregation pipeline to filter only `insert` events:

```javascript
watchCursor = db.getSiblingDB("data").sensors.watch(
   [
      { $match : {"operationType" : "insert" } }
   ]
)
```

Iterate the cursor to check for new events. Use the :method:`cursor.isClosed()` method with the :method:`cursor.hasNext()` method to ensure the loop only exits if the change stream cursor is closed and there are no objects remaining in the latest batch:

```javascript
while (!watchCursor.isClosed()){
   if (watchCursor.hasNext()){
      printjson(watchCursor.next());
   }
}
```

The change stream cursor only returns change events where the `operationType` is `insert`. For complete documentation on change stream output, see `change-stream-output`.

### Resuming a Change Stream

Every  document returned by a change stream cursor includes a resume token as the `_id field. To resume a change stream, pass the entire id` document of the change event you want to resume from to either the `resumeAfter` or `startAfter` option of :method:`~db.collection.watch()`.

The following operation resumes a change stream cursor against the `data.sensors` collection using a resume token. This assumes that the operation that generated the resume token has not rolled off the cluster's oplog.

```javascript
let watchCursor = db.getSiblingDB("data").sensors.watch();
let firstChange;

while (!watchCursor.isClosed()) {
   if (watchCursor.hasNext()) {
     firstChange = watchCursor.next();
     break;
   }
}

watchCursor.close();

let resumeToken = firstChange._id;

resumedWatchCursor = db.getSiblingDB("data").sensors.watch(
[],
   { resumeAfter : resumeToken }
)
```

Iterate the cursor to check for new events. Use the :method:`cursor.isClosed()` method with the :method:`cursor.hasNext()` method to ensure the loop only exits if the change stream cursor is closed and there are no objects remaining in the latest batch:

```javascript
while (!resumedWatchCursor.isClosed()){
   if (resumedWatchCursor.hasNext()){
      print(resumedWatchCursor.next());
   }
}
```

See `change-stream-resume` for complete documentation on resuming a change stream.
