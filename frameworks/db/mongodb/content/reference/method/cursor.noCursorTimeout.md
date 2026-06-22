---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.noCursorTimeout.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# cursor.noCursorTimeout() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Session Idle Timeout Overrides `noCursorTimeout`

.. include:: /includes/extracts/sessions-cursor-timeout.rst

Consider an application that issues a :method:`db.collection.find()` with :method:`cursor.noCursorTimeout`. The server returns a cursor along with a batch of documents defined by the :method:`cursor.batchSize()` of the :method:`~db.collection.find()`. The session refreshes each time the application requests a new batch of documents from the server. However, if the application takes longer than 30 minutes to process the current batch of documents, the session is marked as expired and closed. When the server closes the session, it also kills the cursor despite the cursor being configured with :method:`~cursor.noCursorTimeout`. When the application requests the next batch of documents, the server returns an error.

### Refresh a Cursor with `refreshSessions`

For operations that return a cursor, if the cursor may be idle for longer than 30 minutes, issue the operation within an explicit session using :method:`Mongo.startSession()` and periodically refresh the session using the :dbcommand:`refreshSessions` command. For example:

```bash
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

In the example operation, the :method:`db.collection.find()` method is associated with an explicit session. The cursor is configured with :method:`cursor.noCursorTimeout()` to prevent the server from closing the cursor if idle. The `while` loop includes a block that uses :dbcommand:`refreshSessions` to refresh the session every 5 minutes. Since the session will never exceed the 30 minute idle timeout, the cursor can remain open indefinitely.

For MongoDB drivers, defer to the :driver:`driver documentation </>` for instructions and syntax for creating sessions.
