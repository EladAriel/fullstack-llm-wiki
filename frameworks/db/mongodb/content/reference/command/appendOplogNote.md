---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/appendOplogNote.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.010015Z"
---
# appendOplogNote (database command)

**meta:** :description: Append a non-operational entry to the oplog using the `appendOplogNote` command on the `admin` database.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** appendOplogNote

   Writes a non-operational entry to the :term:`oplog`.

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst

## Syntax

You can only run the ``appendOplogNote`` command on the ``admin``
database.

The command has this syntax:

.. code-block:: javascript
   :copyable: false

   db.adminCommand(
      {
         appendOplogNote: 1,
         data: <document>
      }
   )

### Command Fields

.. list-table::
   :header-rows: 1
   :widths: 20 20 80

   * - Field
     - Type
     - Description

   * - ``appendOplogNote``
     - any
     - Set to any value.

       You can use ``appendOplogNote`` to advance the change stream 
       highwatermark token timestamp on idle shards with infrequent writes. To 
       learn more about resume token types, see 
       :ref:`change-stream-resume-token`. 

   * - ``data``
     - document
     - The document to append to the :term:`oplog`.

## Example

To append a non-operational entry to the :term:`oplog`, use the
:method:`db.adminCommand` method:

.. code-block:: javascript

   db.adminCommand(
      {
         appendOplogNote: 1,
         data: {
            msg: "Appending test message to oplog"
         }
      }
   )

Example ``oplog`` entry:

.. code-block:: json
   :copyable: false

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