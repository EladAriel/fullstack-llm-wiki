---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.find.removeOne.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.941360Z"
---
# Bulk.find.removeOne() (mongosh method)

**meta:** :description: Perform bulk write operations using `Bulk.find.removeOne()` to delete a single document matching a query in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**include:** /includes/fact-bulkwrite.rst

## Description

**method:** Bulk.find.removeOne()

 
   Starting in ``mongosh`` 0.12.2, ``Bulk.find.removeOne()`` is an alias
   for :method:`Bulk.find.deleteOne()`.

**note:** Use ``Bulk.find.deleteOne()`` instead of ``Bulk.find.removeOne()``.