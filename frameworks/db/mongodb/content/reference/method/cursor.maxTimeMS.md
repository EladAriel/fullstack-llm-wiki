---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.maxTimeMS.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# cursor.maxTimeMS() (mongosh method)

## Definition

> **Important:** :method:`~cursor.maxTimeMS()` is not related to the
`NoCursorTimeout` query flag. :method:`~cursor.maxTimeMS()`
relates to processing time, while `NoCursorTimeout` relates
to idle time. A cursor's idle time does not contribute towards its
processing time.
The :method:`~cursor.maxAwaitTimeMS()` method sets a limit on how
long a `tailable cursor <tailable-cursors-landing-page>` waits
for the next response. It does not set a limit on total processing
time.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behaviors

MongoDB targets operations for termination if the associated cursor exceeds its allotted time limit. MongoDB terminates operations that exceed their allotted time limit using the same mechanism as :method:`db.killOp()`. MongoDB only terminates an operation at one of its designated `interrupt points <interrupt point>`.

MongoDB does not count network latency between the client and the server towards a cursor's time limit. For a sharded cluster, however, MongoDB does include the latency between the :binary:`~bin.mongos` and :binary:`~bin.mongod` instances towards this time limit.

Queries that generate multiple batches of results continue to return batches until the cursor exceeds its allotted time limit.

### Session Idle Timeout Overrides `maxTimeMS`

.. include:: /includes/extracts/sessions-cursor-timeout.rst

For example, consider a :method:`~db.collection.find()` operation with the :method:`~cursor.maxTimeMS` configured for a timeout of 31 minutes. The server returns a cursor along with a batch of documents defined by the :method:`cursor.batchSize()` of the :method:`~db.collection.find()`. The session refreshes each time the application requests a new batch of documents from the server. However, if the application takes longer than 30 minutes to process the current batch of documents, the session is marked as expired and closed. When the server closes the session, it also kills the cursor despite the cursor being configured with :method:`~cursor.maxTimeMS` greater than 30 minutes. When the application requests the next batch of documents, the server returns an error.

For operations that return a cursor, if the cursor may be idle for longer than 30 minutes, issue the operation within an explicit session using :method:`Mongo.startSession()` and periodically refresh the session using the :dbcommand:`refreshSessions` command. For example:

```javascript
var session = db.getMongo().startSession()
var sessionId = session
sessionId  // show the sessionId

var cursor = session.getDatabase("examples").getCollection("data").find().noCursorTimeout()
var refreshTimestamp = new Date() // take note of time at operation start

while (cursor.hasNext()) {

  // Check if more than 5 minutes have passed since the last refresh
  if ( (new Date()-refreshTimestamp)/1000 > 300 ) { 
    print("refreshing session")
    db.adminCommand({"refreshSessions" : [sessionId]})
    refreshTimestamp = new Date()
  }

  // process cursor normally

}
```

In the example operation, the :method:`db.collection.find()` method is associated with an explicit session. The cursor is configured with :method:`cursor.maxTimeMS()` to keep the cursor open for at least 31 minutes. The `while` loop includes a block that uses :dbcommand:`refreshSessions` to refresh the session every 5 minutes. Since the session will never exceed the 30 minute idle timeout, the cursor can remain open up to the configured :method:`~cursor.maxTimeMS()`.

For MongoDB drivers, defer to the :driver:`driver documentation </>` for instructions and syntax for creating sessions.

> **Seealso:** :limit:`Session Idle Timeout`

### Default Timeout for All Operations

Starting in MongoDB 8.0, you can use the :parameter:`defaultMaxTimeMS` cluster parameter to specify a default time limit for individual read operations to complete. If a query specifies a :method:`~cursor.maxTimeMS()` option, that value overrides the `defaultMaxTimeMS` value.

## Examples
