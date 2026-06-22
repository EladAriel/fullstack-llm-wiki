---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/split.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# split (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     split: <database>.<collection>, <find|middle|bounds> 
   } 
)
```

## Command Fields

The command takes the following fields:

## Considerations

When used with either the `find` or the `bounds` option, the :dbcommand:`split` command splits the chunk along the median. As such, the command cannot use the `find` or the `bounds` option to split an empty chunk since an empty chunk has no median.

To create splits in empty chunks, use either the `middle` option with the :dbcommand:`split` command or use the :method:`sh.splitAt()` command.

## Command Formats

To create a chunk split, connect to a :binary:`~bin.mongos` instance, and issue the following command to the `admin` database:

```javascript
db.adminCommand( { split: <database>.<collection>,
                   find: <document> } )
```

Or:

```javascript
db.adminCommand( { split: <database>.<collection>,
                   middle: <document> } )
```

Or:

```javascript
db.adminCommand( { split: <database>.<collection>,
                   bounds: [ <lower>, <upper> ] } )
```

To create a split for a collection that uses a `hashed shard key`, use the `bounds` parameter. Do not use the `middle` parameter for this purpose.

.. include:: /includes/warning-splitting-chunks.rst

> **Seealso:** - :dbcommand:`moveChunk`
- :dbcommand:`moveRange`
- :method:`sh.moveChunk()`
- :method:`sh.splitAt()`
- :method:`sh.splitFind()`
- :dbcommand:`split`

## Examples

The following sections provide examples of the :dbcommand:`split` command.

### Split a Chunk in Half

```javascript
db.adminCommand( { split : "test.people", find : { _id : 99 } } )
```

The :dbcommand:`split` command identifies the chunk in the `people` collection of the `test` database, that holds documents that match `{ _id : 99 }`. :dbcommand:`split` does not require that a match exist, in order to identify the appropriate chunk. Then the command splits it into two chunks of equal size.

> **Note:** :dbcommand:`split` creates two equal chunks by range as
opposed to size, and does not use the selected point as a boundary for
the new chunks.

### Define an Arbitrary Split Point

To define an arbitrary split point, use the following form:

```javascript
db.adminCommand( { split : "test.people", middle : { _id : 99 } } )
```

The :dbcommand:`split` command identifies the chunk in the `people` collection of the `test` database, that would hold documents matching the query `{ _id : 99 }`. :dbcommand:`split` does not require that a match exist, in order to identify the appropriate chunk. Then the command splits it into two chunks, with the matching document as the lower bound of one of the split chunks.

This form is typically used when `pre-splitting` data in a collection.

### Split a Chunk Using Values of a Hashed Shard Key

This example uses the `hashed shard key` `userid` in a `people` collection of a `test` database. The following command uses an array holding two single-field documents to represent the minimum and maximum values of the hashed shard key to split the chunk:

```javascript
db.adminCommand( { split: "test.people",
                  bounds : [ { userid: Long("-5838464104018346494") },
                             { userid: Long("-5557153028469814163") }
             ] } )
```

> **Note:** type to represent the hashed value.

Use :method:`sh.status()` to see the existing bounds of the shard keys.

## Metadata Lock Error

If another process, such as a balancer process, changes metadata while :dbcommand:`split` is running, you may see a `metadata lock error`.

```none
errmsg: "The collection's metadata lock is already taken."
```

This message indicates that the split has failed with no side effects. Retry the :dbcommand:`split` command.
