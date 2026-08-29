---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.dataSize.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.972350Z"
---
# db.collection.dataSize() (mongosh method)

**meta:** :description: Determine the size in bytes of a MongoDB collection using the `db.collection.dataSize()` method.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol


**include:** /includes/fact-mongosh-shell-method-alt

## Definition

**method:** db.collection.dataSize()

   .. |dbcommand| replace:: :data:`~collStats.size` field returned by the
      :dbcommand:`collStats` command

   :returns: The size in bytes of the collection.
   
             :option:`Data compression <mongod
             --wiredTigerCollectionBlockCompressor>` does not affect
             this value.

   .. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

   .. |operations| replace:: :dbcommand:`collStats`

## Compatibility

.. |command| replace:: method

This method is available in deployments hosted in the following environments:

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst