---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.size.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.917164Z"
---
# cursor.size() (mongosh method)

**meta:** :description: Count the number of documents matching a query after applying `skip` and `limit` methods using `cursor.size()`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** cursor.size()


   .. include:: /includes/fact-mongosh-shell-method.rst


   :returns: A count of the number of documents that match the
             :method:`db.collection.find()` query after applying any
             :method:`cursor.skip()` and :method:`cursor.limit()` methods.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst