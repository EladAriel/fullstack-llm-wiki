---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.totalIndexSize.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.978339Z"
---
# db.collection.totalIndexSize() (mongosh method)

**meta:** :description: Retrieve the total size of all indexes for a collection using `db.collection.totalIndexSize()`, reflecting compressed size if prefix compression is used.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol


**include:** /includes/fact-mongosh-shell-method-alt

## Definition

**method:** db.collection.totalIndexSize()

   .. |dbcommand| replace:: :data:`~collStats.totalIndexSize` field returned
      by the :dbcommand:`collStats` command

   :returns: The total size of all indexes for the collection.  
   
             If an index uses prefix compression (which is the
             :option:`default for WiredTiger <mongod
             --wiredTigerIndexPrefixCompression>`), the returned size
             reflects the compressed size.

   .. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

   .. |operations| replace:: :dbcommand:`collStats`

## Compatibility

This method is available in deployments hosted in the following environments:

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst