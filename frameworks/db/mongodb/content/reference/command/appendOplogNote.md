---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/appendOplogNote.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# appendOplogNote (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

You can only run the `appendOplogNote` command on the `admin` database.

The command has this syntax:

```javascript
db.adminCommand(
   {
      appendOplogNote: 1,
      data: <document>
   }
)
```

### Command Fields

## Example

To append a non-operational entry to the `oplog`, use the :method:`db.adminCommand` method:

```javascript
db.adminCommand(
   {
      appendOplogNote: 1,
      data: {
         msg: "Appending test message to oplog"
      }
   }
)
```

Example `oplog` entry:

```json
{
   op: "n",
   ns: "",
   o: { 
      msg: "Appending test message to oplog"
   }, 
   ts: Timestamp({ t: 1689177321, i: 1 }), 
   t: Long("1"), 
   v: Long("2"),
   wall: ISODate("2023-07-12T15:55:21.180Z")
}
```
