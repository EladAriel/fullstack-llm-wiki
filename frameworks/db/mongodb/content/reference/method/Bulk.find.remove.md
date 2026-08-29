---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.find.remove.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.990090Z"
---
# Bulk.find.remove() (mongosh method)

**meta:** :description: Perform bulk write operations using `Bulk.find.remove()` to delete documents matching a specified query.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**include:** /includes/fact-bulkwrite.rst

## Description

**method:** Bulk.find.remove()

   Starting in ``mongosh`` 0.12.2, ``Bulk.find.remove()`` is an alias
   for :method:`Bulk.find.delete()`.

**note:** Use ``Bulk.find.delete()`` instead of ``Bulk.find.remove()``.