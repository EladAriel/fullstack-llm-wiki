---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.next.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.976693Z"
---
# cursor.next() (mongosh method)

**meta:** :description: Retrieve the next document in a cursor using the `cursor.next()` method in `mongosh`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** cursor.next()


   .. include:: /includes/fact-mongosh-shell-method.rst


   :returns: The next document in the cursor returned by the
             :method:`db.collection.find()` method. See
             :method:`cursor.hasNext()` related functionality.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst