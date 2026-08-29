---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.totalSize.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.886301Z"
---
# db.collection.totalSize() (mongosh method)

**meta:** :description: Calculate the total size in bytes of a collection's data and indexes, including compressed sizes for WiredTiger storage.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol


**include:** /includes/fact-mongosh-shell-method-alt

## Definition

**method:** db.collection.totalSize()

   .. |dbcommand| replace:: :data:`~collStats.totalSize` field returned by the
      :dbcommand:`collStats` command

   :returns: The total size in bytes of the data in the collection plus
             the size of every index on the collection.
             
             If collection data is compressed (which is the
             :option:`default for WiredTiger <mongod
             --wiredTigerCollectionBlockCompressor>`), the returned
             size reflects the compressed size of the collection data.

             If an index uses prefix compression (which is the
             :option:`default for WiredTiger <mongod
             --wiredTigerIndexPrefixCompression>`), the returned size
             reflects the compressed size of the index.

   The value returned is the sum of
   :method:`db.collection.storageSize()` and
   :method:`db.collection.totalIndexSize()` in bytes.

   .. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

   .. |operations| replace:: :dbcommand:`collStats`

## Compatibility

This method is available in deployments hosted in the following environments:

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst