---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.hasNext.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.937115Z"
---
# cursor.hasNext() (mongosh method)

**meta:** :description: Determine if a cursor from a `db.collection.find()` query can iterate further using `cursor.hasNext()`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** cursor.hasNext()


   .. include:: /includes/fact-mongosh-shell-method.rst


   :returns: Boolean.

   :method:`cursor.hasNext()` returns ``true`` if the cursor returned by
   the :method:`db.collection.find()` query can iterate further to
   return more documents. If the client-side cursor batch is empty and the
   server has more data, ``hasNext()`` fetches the next batch from the server.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst