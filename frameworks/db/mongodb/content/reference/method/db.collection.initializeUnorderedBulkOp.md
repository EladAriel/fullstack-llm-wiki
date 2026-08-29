---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.initializeUnorderedBulkOp.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.928015Z"
---
# db.collection.initializeUnorderedBulkOp() (mongosh method)

**meta:** :description: Initialize and execute unordered bulk write operations in MongoDB using `initializeUnorderedBulkOp()`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**include:** /includes/fact-bulkwrite.rst

## Definition

**method:** db.collection.initializeUnorderedBulkOp()


   .. include:: /includes/fact-mongosh-shell-method.rst

   Initializes and returns a new :method:`Bulk()` operations builder
   for a collection. The builder constructs an *unordered* list of
   write operations that MongoDB executes in bulk.

## Compatibility

This command is available in deployments hosted in the following
environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst
   
## Behavior

### Order of Operation

With an *unordered* operations list, MongoDB can execute in parallel
the write operations in the list and in any order. If the order of
operations matter, use
:method:`db.collection.initializeOrderedBulkOp()` instead.

### Execution of Operations

**include:** /includes/fact-bulk-operation-unordered-list.rst

**include:** /includes/fact-bulk-operation-batches.rst

### Error Handling

If an error occurs during the processing of one of the write
operations, MongoDB will continue to process remaining write operations
in the list.

## Example

The following initializes a :method:`Bulk()` operations builder and
adds a series of insert operations to add multiple documents:

.. code-block:: javascript

   var bulk = db.users.initializeUnorderedBulkOp();
   bulk.insert( { user: "abc123", status: "A", points: 0 } );
   bulk.insert( { user: "ijk123", status: "A", points: 0 } );
   bulk.insert( { user: "mop123", status: "P", points: 0 } );
   bulk.execute();

**seealso:** - :method:`db.collection.initializeOrderedBulkOp()`
   - :method:`Bulk()`
   - :method:`Bulk.insert()`
   - :method:`Bulk.execute()`