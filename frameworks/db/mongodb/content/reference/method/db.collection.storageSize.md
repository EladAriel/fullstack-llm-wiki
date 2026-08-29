---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.storageSize.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.953890Z"
---
# db.collection.storageSize() (mongosh method)

**meta:** :description: Determine the total storage size in bytes allocated for document storage in a MongoDB collection, reflecting compressed size if applicable.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol


**include:** /includes/fact-mongosh-shell-method-alt

## Definition

**method:** db.collection.storageSize()

   .. |dbcommand| replace:: :data:`~collStats.storageSize` field returned
      by the :dbcommand:`collStats` command

   :returns: The total amount of storage in bytes allocated to this 
             collection for document storage.

             If collection data is compressed (which is the
             :option:`default for WiredTiger <mongod
             --wiredTigerCollectionBlockCompressor>`), the storage size
             reflects the compressed size and may be smaller than the
             value returned by :method:`db.collection.dataSize()`.

   .. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

   .. |operations| replace:: :dbcommand:`collStats`

## Compatibility

This method is available in deployments hosted in the following environments:

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst