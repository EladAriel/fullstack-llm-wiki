---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/fsyncUnlock.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# fsyncUnlock (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   {
     fsyncUnlock: 1,
     comment: <any>
   }
)
```

The `comment` field is optional and may contain a comment of any data type.

## Results

The operation returns a document with the following fields:

## Examples

Consider a situation where :method:`db.fsyncLock()` has been issued two times. The following :dbcommand:`fsyncUnlock` operation reduces the locks taken by :method:`db.fsyncLock()` by 1:

```javascript
db.adminCommand( { fsyncUnlock: 1 } )
```

The operation returns the following document:

```javascript
{ "info" : "fsyncUnlock completed", "lockCount" : Long(1), "ok" : 1 }
```

As the `lockCount` is greater than 0, the :binary:`~bin.mongod` instance is locked against writes. To unlock the instance for writes, run the unlock operation again:

```javascript
db.adminCommand( { fsyncUnlock: 1 } )
```

The operation returns the following document:

```javascript
{ "info" : "fsyncUnlock completed", "lockCount" : Long(0), "ok" : 1 }
```

The :binary:`~bin.mongod` instance is unlocked for writes.
