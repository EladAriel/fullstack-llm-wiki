---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.printCollectionStats.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.993854Z"
---
# db.printCollectionStats() (mongosh method)

**meta:** :description: Use `db.printCollectionStats()` to manually inspect collection statistics in `mongosh`, not suitable for JSON output in scripts.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** db.printCollectionStats()

   Provides a wrapper around the :method:`db.collection.stats()`
   method. Returns statistics from every collection separated by three
   hyphen characters.

   .. |method| replace:: :method:`db.printCollectionStats()`
   .. |method-alternative| replace:: :method:`db.collection.stats()`

   .. include:: /includes/note-method-does-not-return-json.rst


   .. seealso::

      :doc:`/reference/command/collStats`

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst