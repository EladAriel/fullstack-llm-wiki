---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.getReadPrefTagSet.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.990349Z"
---
# Mongo.getReadPrefTagSet() (mongosh method)

**meta:** :description: Retrieve the current read preference tag set for a MongoDB connection using `getReadPrefTagSet()`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** Mongo.getReadPrefTagSet()

   :returns: The current :term:`read preference` tag set for the
             :method:`Mongo() <db.getMongo()>` connection object.

   See :doc:`/core/read-preference` for an introduction to read
   preferences and tag sets in MongoDB. Use
   :method:`~Mongo.getReadPrefTagSet()` to return the current read
   preference tag set, as in the following example:

   .. code-block:: javascript

      db.getMongo().getReadPrefTagSet()

   Use the following operation to return and print the current read
   preference tag set:

   .. code-block:: javascript

      printjson(db.getMongo().getReadPrefTagSet());

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-onprem-only.rst

   .. seealso::

      - :doc:`/core/read-preference`
      - :method:`~cursor.readPref()`
      - :method:`~Mongo.setReadPref()`
      - :method:`~Mongo.getReadPrefTagSet()`