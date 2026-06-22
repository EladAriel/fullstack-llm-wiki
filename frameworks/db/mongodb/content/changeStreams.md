---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/changeStreams.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============

# Change Streams

Change streams allow applications to access real-time data changes without the prior complexity and risk of manually tailing the `oplog`. Applications can use change streams to subscribe to all data changes on a single collection, a database, or an entire deployment, and immediately react to them. Because change streams use the aggregation framework, applications can also filter for specific changes or transform the notifications at will.

> **Note:** Change streams are restricted to database events. Atlas Stream
Processing has extended functionality, including managing multiple
data event types and processing streams of complex data using the
same query API as Atlas databases. For more information, see
`Atlas Stream Processing <atlas-sp>`.

.. include:: /includes/change-streams-optimization.rst

## Availability

Change streams are available for `replica sets <replication>` and `sharded clusters <sharding-background>`:

- **Storage Engine.**
The replica sets and sharded clusters must use the `WiredTiger <storage-wiredtiger>` storage engine. Change streams can also be used on deployments that use the `encryption-at-rest<encrypted-storage-engine>` feature.

- **Replica Set Protocol Version.**
The replica sets and sharded clusters must use replica set protocol version 1 (:rsconf:`pv1 <protocolVersion>`).

- **Read Concern "majority" Enablement.**
.. include:: /includes/extracts/changestream-rc-majority-4.2.rst

> **Note:** Time series collections do not support change streams because time
series collections use an optimized storage format instead of
tracking changes at the document level. You cannot use
time series collections as a source for {+atlas-sp+}.

> **Tip:** See `manual-timeseries-collection-limitations` for more information.

### Stable API Support

.. include:: /includes/stable-api/change-stream-support.rst

## Connect

Connections for a change stream can either use DNS seed lists with the `+srv` connection option or by listing the servers individually in the connection string.

If the driver loses the connection to a change stream or the connection goes down, it attempts to reestablish a connection to the change stream through another node in the cluster that has a matching `read preference <connections-read-preference>`. If the driver cannot find a node with the correct read preference, it throws an exception.

For more information, see `Connection String URI Format <mongodb-uri>`.

## Watch a Collection, Database, or Deployment

You can open change streams against:

## Change Stream Performance Considerations

If the amount of active change streams opened against a database exceeds the `connection pool size <connection-pool-overview>`, you may experience notification latency. Each change stream holds a connection open with a `getMore <manual-reference-commands-getMore>` operation while waiting for the next event. To avoid latency, ensure that the pool size is greater than the number of open change streams. For details, see the `maxPoolSize<maxpoolsize-cp-setting>` setting.

### Sharded Cluster Considerations

When a change stream is opened on a sharded cluster:

- The :binary:`mongos` creates individual change streams on **each
shard**. This behavior occurs regardless of whether the change stream targets a particular shard key range.

- When the `mongos` receives change stream results, it sorts and
filters those results. If needed, the `mongos` also performs a `fullDocument` lookup.

For best performance, limit the use of :pipeline:`$lookup` queries in change streams.

## Open a Change Stream

To open a change stream:

- For a replica set, open the change stream from any
data-bearing member.

- For a sharded cluster, open the change stream from the
:binary:`~bin.mongos`.

The following example opens a change stream for a collection and iterates over the cursor to retrieve the change stream documents. [#start-time]_

----------

|arrow| Use the **Select your language** drop-down menu in the upper-right to set the language of the examples on this page.

----------

Iterate the change stream cursor to retrieve change events. See `change-stream-output` for the change stream document format.

.. include:: /includes/extracts/changestream-cursor-open.rst

> **Note:** The lifecycle of an unclosed cursor is language-dependent.

You can specify a `startAtOperationTime` to open the cursor at a particular point in time. If the specified starting point is in the past, it must be in the time range of the oplog.

## Modify Change Stream Output

----------

|arrow| Use the **Select your language** drop-down menu in the upper-right to set the language of the examples on this page.

----------

> **Tip:** The `_id <change-stream-event-id>` field of the change stream
event document act as the :ref:`resume token
<change-stream-resume>`. Do not use the pipeline to modify or remove
the change stream event's `_id` field.
.. include:: /includes/extracts/4.2-changes-change-stream-modification-error.rst
See `change-stream-output` for more information on the change stream
response document format.

## Lookup Full Document for Update Operations

By default, change streams only return the delta of fields during the update operation. However, you can configure the change stream to return the most current majority-committed version of the updated document.

The `updateLookup` operation reads the document identified by its shard key and document identifier from the collection. The collection is identified by its name and uses the collection data as it exists at the time the change stream is processed. Consider these scenarios:

- If the collection is renamed, no document is returned.
- If the collection is renamed and a new collection is created with the
old name, then the lookup operation is performed on the new collection. If a matching document is found, it is returned.

.. include:: /includes/change-stream/warning_fullDocument_match.rst

----------

|arrow| Use the **Select your language** drop-down menu in the upper-right to set the language of the examples on this page.

----------

> **Note:** If there are one or more majority-committed operations that modified
the updated document after the update operation but before the
lookup, the full document returned may differ significantly from the
document at the time of the update operation.
However, the deltas included in the change stream document always
correctly describe the watched collection changes that applied to
that change stream event.
The `fullDocument` field for an update event may be missing if one
of the following is true:
- If the document is deleted or if the collection is dropped in
  between the update and the lookup.
- If the update changes the values for at least one of the fields in
  that collection's shard key.
See `change-stream-output` for more information on the change
stream response document format.

## Resume a Change Stream

Change streams are resumable by specifying a resume token to either `resumeAfter <change-stream-resume-after>` or `startAfter <change-stream-start-after>` when opening the cursor.

> **Warning:** When you resume a change stream with a resume token, use the
same pipeline and options as when you originally generated the token.
If you use a different change stream pipeline or different options, it might
lead to unpredictable behavior, negatively impact data consistency, or
prevent the change stream from resuming.

### `resumeAfter` for Change Streams

You can resume a change stream after a specific event by passing a resume token to `resumeAfter` when opening the cursor.

See `change-stream-resume-token` for more information on the resume token.

> **Important:** - The oplog must have enough history to locate the operation
  associated with the token or the timestamp, if the timestamp is in
  the past.
- .. include:: /includes/extracts/changestream-invalid-events.rst

### `startAfter` for Change Streams

You can start a new change stream after a specific event by passing a resume token to `startAfter` when opening the cursor. Unlike `resumeAfter <change-stream-resume-after>`, `startAfter` can resume notifications after an `invalidate event <change-event-invalidate>` by creating a new change stream.

See `change-stream-resume-token` for more information on the resume token.

> **Important:** - The oplog must have enough history to locate the operation
  associated with the token or the timestamp, if the timestamp is in
  the past.

### Resume Tokens

There are two types of resume tokens:

- **Event token**: Identifies a specific change event. The change stream
cursor generates an event token each time a change event occurs.

- **Highwatermark token**: Represents a point in time without an
associated change event. The server periodically generates highwatermark tokens to indicate that cluster time has advanced, even when no change events occur.

> **Tip:** .. include:: /includes/change-stream/highwatermark-tip-idle-shards.rst

You can find resume tokens in multiple sources:

.. include:: /includes/extracts/4.2-changes-change-stream-modification-error.rst

> **Tip:** .. include:: /includes/note-decode-resume-tokens.rst

#### Resume Tokens from Change Events

Change event notifications include a resume token on the `_id` field:

```json
{
   "_id": {
      "_data": "82635019A0000000012B042C0100296E5A1004AB1154ACACD849A48C61756D70D3B21F463C6F7065726174696F6E54797065003C696E736572740046646F63756D656E744B65790046645F69640064635019A078BE67426D7CF4D2000004"
    },
    "operationType": "insert",
    "clusterTime": Timestamp({ "t": 1666193824, "i": 1 }),
    "collectionUUID": new UUID("ab1154ac-acd8-49a4-8c61-756d70d3b21f"),
    "wallTime": ISODate("2022-10-19T15:37:04.604Z"),
    "fullDocument": {
       "_id": ObjectId("635019a078be67426d7cf4d2"'),
       "name": "Giovanni Verga"
    },
    "ns": { 
       "db": "test", 
       "coll": "names" 
    },
    "documentKey": { 
       "_id": ObjectId("635019a078be67426d7cf4d2") 
    }
}
```

#### Resume Tokens from `aggregate`

When using the :dbcommand:`aggregate` command, the :pipeline:`$changeStream` aggregation stage includes a resume token on the `cursor.postBatchResumeToken` field:

```json
{
   "cursor": {
      "firstBatch": [],
      "postBatchResumeToken": { 
         "_data": "8263515EAC000000022B0429296E1404" 
      },
      "id": Long("4309380460777152828"),
      "ns": "test.names"
   },
   "ok": 1,
   "$clusterTime": {
      "clusterTime": Timestamp({ "t": 1666277036, "i": 1 }),
      "signature": {
         "hash": Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
         "keyId": Long("0")
      }
   },
   "operationTime": Timestamp({ "t": 1666277036, "i": 1 })
}
```

#### Resume Tokens from `getMore`

The :dbcommand:`getMore` command also includes a resume token on the `cursor.postBatchResumeToken` field:

```json
{
   "cursor": {
      "nextBatch": [],
      "postBatchResumeToken": { 
         "_data": "8263515979000000022B0429296E1404"
      },
      "id": Long("7049907285270685005"),
      "ns": "test.names"
   }, 
   "ok": 1,
   "$clusterTime": {
      "clusterTime": Timestamp( { "t": 1666275705, "i": 1 } ),
      "signature": {
         "hash": Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
         "keyId": Long("0")
      }
   },
   "operationTime": Timestamp({ "t": 1666275705, "i": 1 })
}
```

## Use Cases

Change streams can benefit architectures with reliant business systems, informing downstream systems once data changes are durable. For example, change streams can save time for developers when implementing Extract, Transform, and Load (ETL) services, cross-platform synchronization, collaboration functionality, and notification services.

## Access Control

For deployments enforcing `authentication` and `authorization <authorization>`:

- To open a change stream against specific collection, applications
must have privileges that grant :authaction:`changeStream` and :authaction:`find` actions on the corresponding collection.

```javascript
  { resource: { db: <dbname>, collection: <collection> }, actions: [ "find", "changeStream" ] }
```

- To open a change stream on a single database, applications must have
privileges that grant :authaction:`changeStream` and :authaction:`find` actions on all non-`system` collections in the database.

```javascript
  { resource: { db: <dbname>, collection: "" }, actions: [ "find", "changeStream" ] }
```

- To open a change stream on an entire deployment, applications must
have privileges that grant :authaction:`changeStream` and :authaction:`find` actions on all non-`system` collections for all databases in the deployment.

```javascript
  { resource: { db: "", collection: "" }, actions: [ "find", "changeStream" ] }
```

## Event Notification

Change streams only notify on data changes that have persisted to a majority of data-bearing members in the replica set. Change streams ensure that notifications trigger only for majority-committed changes that are durable in failure scenarios.

For example, consider a 3-member `replica set` with a change stream cursor opened against the `primary`. If a client issues an insert operation, the change stream only notifies the application of the data change once that insert has persisted to a majority of data-bearing members.

If an operation is associated with a `transaction <transactions>`, the change event document includes the `txnNumber` and the `lsid`.

## Collation

Change streams use `simple` binary comparisons unless an explicit collation is provided.

## Change Streams and Orphan Documents

.. include:: /includes/change-streams-and-orphans.rst

## Change Streams with Document Pre- and Post-Images

.. include:: /includes/change-stream-pre-and-post-images-introduction.rst

.. include:: /includes/change-stream-pre-and-post-images-additional-information.rst

For complete examples with the change stream output, see `db.collection.watch-change-streams-pre-and-post-images-example`.

.. include:: /includes/initial-sync-change-streams.rst

## Contents

- Production Recommendations </administration/change-streams-production-recommendations>
- Change Events </reference/change-events>
