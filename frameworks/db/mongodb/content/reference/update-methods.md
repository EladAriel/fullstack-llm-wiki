---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/update-methods.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.675351Z"
---
.. _update-methods:

# Update Methods

**meta:** :description: Explore methods for updating documents in MongoDB, including updateOne, updateMany, and replaceOne.

.. default-domain:: mongodb

MongoDB provides the following methods for updating documents in a
collection:

.. list-table::
   :widths: 35 65

   * - :method:`db.collection.updateOne()`
     - Updates at most a single document that match a specified filter
       even though multiple documents may match the specified filter.

   * - :method:`db.collection.updateMany()`
     - Update all documents that match a specified filter.

   * - :method:`db.collection.replaceOne()`
     - Replaces at most a single document that match a specified filter
       even though multiple documents may match the specified filter.

.. _additional-updates:

## Additional Methods

The following methods can also update documents from a collection:

- :method:`db.collection.findOneAndReplace()`.
- :method:`db.collection.findOneAndUpdate()`.
- :method:`db.collection.findAndModify()`.
- :method:`db.collection.bulkWrite()`.

See the individual reference pages for the methods for more information
and examples.