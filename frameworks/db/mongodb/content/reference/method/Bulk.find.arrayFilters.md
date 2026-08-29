---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.find.arrayFilters.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.898630Z"
---
# Bulk.find.arrayFilters() (mongosh method)

**meta:** :description: Specify array filters for update operations using `Bulk.find.arrayFilters()` to determine which array elements to modify in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Description

**method:** Bulk.find.arrayFilters(<array of filter documents>)

   Determines which array elements to modify for an update operation on
   an array field:

   .. code-block:: javascript

      Bulk.find(<query>).arrayFilters([ <filter1>, ... ]).updateOne(<update>);
      Bulk.find(<query>).arrayFilters([ <filter1>, ... ]).update(<update>);

   .. include:: /includes/extracts/arrayFilters-details.rst

   Append to :method:`Bulk.find()` method to specify the array filters
   for the :method:`~Bulk.find.updateOne()` and
   :method:`~Bulk.find.update()` operations.

## Compatibility

This command is available in deployments hosted in the following
environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst
   
## Example

.. code-block:: javascript

   var bulk = db.coll.initializeUnorderedBulkOp();
   bulk.find({}).arrayFilters( [ { "elem.grade": { $gt: 85 } } ] ).updateOne( { $set: { "grades.$[elem].mean" : 70 } } );
   bulk.execute();

**seealso:** - :method:`db.collection.initializeUnorderedBulkOp()`
   - :method:`db.collection.initializeOrderedBulkOp()`
   - :method:`Bulk.find.update()`
   - :method:`Bulk.find.updateOne()`
   - :method:`Bulk.execute()`
   - :ref:`All Bulk Methods <bulk-methods>`