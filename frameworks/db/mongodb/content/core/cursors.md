---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/cursors.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======

# Cursors

A `cursor` points to the results of a `query <read-operations-queries>`. Cursors let you iterate over database results one batch at a time.

## Use Cases

The `find()` and `aggregate()` methods return a cursor with a batch of results. Iterate the cursor manually or use :method:`~cursor.toArray()` to access documents. For more information, see `<read-operations-cursors>`.

For `capped collections <manual-capped-collection>`, use a tailable cursor to retrieve documents as they are inserted. For more information, see `<tailable-cursors-landing-page>`.

## Behavior

MongoDB closes cursors created within a `client session <read-isolation-consistency-recency>` when:

- The client exhausts the cursor.
- You manually close the cursor.
- You manually terminate the session.
- The `session <server-sessions>` times out.
:parameter:`cursorTimeoutMillis` sets the timeout for idle cursors (default: 10 minutes). MongoDB closes idle cursors outside sessions after this time. Returning a batch extends the timeout. Use :dbcommand:`killCursors` to close cursors manually.

:parameter:`localLogicalSessionTimeoutMinutes` sets the session timeout (default: 30 minutes). Use :dbcommand:`refreshSessions` to extend a session and :dbcommand:`killSessions` to end it.

Drivers and :binary:`~bin.mongosh` create implicit sessions for cursors opened outside explicit sessions.

### Concurrent Updates While Using a Cursor

.. include:: /includes/fact-concurrent-updates-cursor.rst

### Cursor Results for Non-Existent `mongos` Databases

.. include:: /includes/fact-mongos-db-agg-validation.rst

## Get Started

- `<read-operations-cursors>`
- `<tailable-cursors-landing-page>`
- :driver:`MongoDB Drivers </>`
## Details

:dbcommand:`find` and :dbcommand:`aggregate` operations execute until they fill a `batch <cursor-batches>`. The query then pauses. This paused query is a cursor, identified by a cursor ID.

The database returns the batch and cursor ID. Drivers and `mongosh` store this in a client-side cursor. If more documents exist, the cursor retrieves the next batch via :dbcommand:`getMore`. Use :method:`cursor.objsLeftInBatch()` to check remaining batch results and :method:`cursor.hasNext()` to check for more results.

### Cursor Batches

Cursors return results in batches, limited by the 16 MiB `maximum BSON document size <limit-bson-document-size>`. Use :method:`cursor.batchSize()` to set the document limit. `find()` and `aggregate()` default to a batch size of `101`. Subsequent :dbcommand:`getMore` operations have no default limit, only the 16 MiB message size.

### Sorting

Queries with a sort operation without an index must load all documents into memory before returning results.

### Cursor Information

:method:`db.serverStatus()` returns cursor metrics in the `metrics.cursor` field. See :serverstatus:`metrics.cursor`.

## Learn More

- :driver:`MongoDB Drivers </>`
- `<doc-cursor-methods>`
## Contents

- Iterate a Cursor </tutorial/iterate-a-cursor/>
- Tailable Cursors </core/tailable-cursors>
