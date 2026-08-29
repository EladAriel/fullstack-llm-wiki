---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.isClosed.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.952129Z"
---
# cursor.isClosed() (mongosh method)

**meta:** :description: Check if a cursor is closed in `mongosh` using `cursor.isClosed()`, which returns `true` if the server has closed the cursor.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** cursor.isClosed()


   .. include:: /includes/fact-mongosh-shell-method.rst


   :returns: Boolean.

   :method:`cursor.isClosed()` returns ``true`` if the server has
   closed the cursor. 

   A closed cursor may still have documents remaining in the last
   received batch. Use :method:`cursor.isExhausted()` or 
   :method:`cursor.hasNext()` to check if the cursor is fully
   exhausted.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst