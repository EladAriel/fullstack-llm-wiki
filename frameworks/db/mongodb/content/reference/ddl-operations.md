---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/ddl-operations.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.701027Z"
---
.. _ddl-operations:

# DDL Operations

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

DDL (Data Description Language) operations change the properties of a 
database or collection. MongoDB supports both 
:ref:`<explicit-ddl-operations>` and :ref:`<implicit-ddl-operations>`. 
Explicit DDL operations directly run an operation like creating or 
dropping a collection or index. Implicit DDL operations create 
collections by referencing a non-existent collection, like inserting 
data into a non-existent collection.

.. _explicit-ddl-operations:

## Explicit DDL Operations

MongoDB supports the following explicit :term:`DDL <DDL (Data Definition 
Language)>` operations:

- ``cleanupStructuredEncryptionData``
- :dbcommand:`cloneCollectionAsCapped`
- :dbcommand:`collMod`
- :dbcommand:`compactStructuredEncryptionData`
- :dbcommand:`convertToCapped`
- :dbcommand:`create`
- :dbcommand:`createIndexes`
- :dbcommand:`drop`
- :dbcommand:`dropDatabase`
- :dbcommand:`dropIndexes`
- :dbcommand:`enableSharding`
- :dbcommand:`moveCollection`
- :dbcommand:`movePrimary`
- :dbcommand:`renameCollection`
- :dbcommand:`refineCollectionShardKey`
- :dbcommand:`reshardCollection`
- :dbcommand:`shardCollection`
- :dbcommand:`unshardCollection`

.. _implicit-ddl-operations:

## Implicit DDL Operations

MongoDB also supports write operations such as :dbcommand:`insert` or 
:dbcommand:`update` with ``upsert:true``. Any command that writes to a
non-existing collection creates that collection. 

.. _implicit-ddl-ops-examples:

### Examples

For example, this ``insert`` command creates the ``users`` collection
if it does not already exist.

.. code-block:: javascript
   
   db.runCommand(
      {
         insert: "users",
         documents: [ { _id: 1, user: "abc123", status: "A" } ]
      }
   )

This ``update`` command with ``upsert: true`` creates the ``people``
collection if it does not already exist.

.. code-block:: javascript

   db.runCommand(
      {
         update: "people",
         updates: [
           { q: { name: "Andy" }, u: { $inc: { score: 1 } }, upsert: true }
         ]
      }
   )