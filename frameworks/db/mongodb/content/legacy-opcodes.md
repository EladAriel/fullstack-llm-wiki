---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/legacy-opcodes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============

# Legacy Opcodes

This page describes legacy opcodes that are no longer supported by MongoDB. These legacy opcodes are:

- Deprecated as of MongoDB 5.0.
- Unsupported as of MongoDB 5.1.
Starting in MongoDB 5.1, `OP_MSG <wire-op-msg>` and `OP_COMPRESSED <wire-op-compressed>` are the only supported opcodes to send requests to a MongoDB server.

## OP_DELETE

The OP_DELETE message is used to remove one or more documents from a collection. The format of the OP_DELETE message is:

```c
struct {
    MsgHeader header;             // standard message header
    int32     ZERO;               // 0 - reserved for future use
    cstring   fullCollectionName; // "dbname.collectionname"
    int32     flags;              // bit values - see below for details.
    document  selector;           // query object.  See below for details.
}
```

There is no response to an OP_DELETE message.

## OP_GET_MORE

The OP_GET_MORE message is used to query the database for documents in a collection. The format of the OP_GET_MORE message is:

```c
struct {
    MsgHeader header;             // standard message header
    int32     ZERO;               // 0 - reserved for future use
    cstring   fullCollectionName; // "dbname.collectionname"
    int32     numberToReturn;     // number of documents to return
    int64     cursorID;           // cursorID from the OP_REPLY
}
```

The database will respond to an OP_GET_MORE message with an `OP_REPLY <wire-op-reply>` message.

## OP_INSERT

The OP_INSERT message is used to insert one or more documents into a collection. The format of the OP_INSERT message is:

```c
struct {
    MsgHeader header;             // standard message header
    int32     flags;              // bit values - see below
    cstring   fullCollectionName; // "dbname.collectionname"
    document* documents;          // one or more documents to insert into the collection
}
```

There is no response to an OP_INSERT message.

## OP_KILL_CURSORS

The OP_KILL_CURSORS message is used to close an active cursor in the database. This is necessary to ensure that database resources are reclaimed at the end of the query. The format of the OP_KILL_CURSORS message is:

```bash
struct {
    MsgHeader header;            // standard message header
    int32     ZERO;              // 0 - reserved for future use
    int32     numberOfCursorIDs; // number of cursorIDs in message
    int64*    cursorIDs;         // sequence of cursorIDs to close
}
```

If a cursor is read until exhausted (read until `OP_QUERY <wire-op-query>` or `OP_GET_MORE <wire-op-get-more>` returns zero for the cursor id), there is no need to kill the cursor.

## OP_QUERY

The OP_QUERY message is used to query the database for documents in a collection. The format of the OP_QUERY message is:

```c
struct OP_QUERY {
    MsgHeader header;                 // standard message header
    int32     flags;                  // bit values of query options.  See below for details.
    cstring   fullCollectionName ;    // "dbname.collectionname"
    int32     numberToSkip;           // number of documents to skip
    int32     numberToReturn;         // number of documents to return
                                      //  in the first OP_REPLY batch
    document  query;                  // query object.  See below for details.
  [ document  returnFieldsSelector; ] // Optional. Selector indicating the fields
                                      //  to return.  See below for details.
}
```

The database will respond to an OP_QUERY message with an `OP_REPLY <wire-op-reply>` message.

> **Note:** MongoDB 5.1 removes support for both `OP_QUERY` find operations
and `OP_QUERY` commands. As an exception, `OP_QUERY` is still
supported for running the :dbcommand:`hello` and `isMaster`
commands as part of the connection handshake.

## OP_REPLY

The `OP_REPLY` message is sent by the database in response to an `OP_QUERY <wire-op-query>` or `OP_GET_MORE <wire-op-get-more>` message. The format of an OP_REPLY message is:

```bash
struct {
    MsgHeader header;         // standard message header
    int32     responseFlags;  // bit values - see details below
    int64     cursorID;       // cursor ID if client needs to do get more's
    int32     startingFrom;   // where in the cursor this reply is starting
    int32     numberReturned; // number of documents in the reply
    document* documents;      // documents
}
```

## OP_UPDATE

The OP_UPDATE message is used to update a document in a collection. The format of a OP_UPDATE message is the following:

```c
struct OP_UPDATE {
    MsgHeader header;             // standard message header
    int32     ZERO;               // 0 - reserved for future use
    cstring   fullCollectionName; // "dbname.collectionname"
    int32     flags;              // bit values. see below
    document  selector;           // the query to select the document
    document  update;             // specification of the update to perform
}
```

There is no response to an OP_UPDATE message.
