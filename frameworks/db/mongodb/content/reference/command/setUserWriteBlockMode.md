---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/setUserWriteBlockMode.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# setUserWriteBlockMode (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   {
     setUserWriteBlockMode: 1,
     global: <boolean>,
     reason: <string>  // Optional
   }
)
```

## Command Fields

The command takes the following fields:

## Required Access

To execute the `setUserWriteBlockMode` command, the user must have the :authaction:`setUserWriteBlockMode` privilege.

## Example

#. Enable user write block mode:

```javascript
   db.adminCommand( {
      setUserWriteBlockMode: 1,
      global: true
   } )
```

#. Add a record to the collection:

```javascript
   db.names.insertOne( { name: "George Washington Cable" } )

The server blocks the write because the user write block is enabled.

Example  Output:

.. code-block:: text

   MongoServerError: User writes blocked
```

#. Disable user write block mode:

```javascript
   db.adminCommand( {
      setUserWriteBlockMode: 1,
      global: false 
   } )
```

#. Add a record to the collection:

```javascript
   db.names.insertOne( { name: "George Washington Cable" } )

The :method:`~db.collection.insertOne()` method writes to a collection.  The
server allows the write because the user write block is disabled. 
```
