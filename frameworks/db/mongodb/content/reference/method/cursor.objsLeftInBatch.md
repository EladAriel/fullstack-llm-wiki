---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.objsLeftInBatch.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.994973Z"
---
# cursor.objsLeftInBatch() (mongosh method)

**meta:** :description: Determine the number of documents left in the current batch using `cursor.objsLeftInBatch()` in `mongosh`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** cursor.objsLeftInBatch()


   .. include:: /includes/fact-mongosh-shell-method.rst


   :method:`cursor.objsLeftInBatch()` returns the number of
   documents remaining in the current batch.

   The MongoDB instance returns response in batches. To retrieve
   all the documents from a cursor may require multiple batch
   responses from the MongoDB instance. When there are no more
   documents remaining in the current batch, the cursor will retrieve
   another batch to get more documents until the cursor exhausts.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst