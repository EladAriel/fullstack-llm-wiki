---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.tryNext.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.914773Z"
---
# cursor.tryNext() (mongosh method)

**meta:** :description: Access the next document in a cursor using `cursor.tryNext()`, which returns the document or `null` if unavailable.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** cursor.tryNext()


   .. include:: /includes/fact-mongosh-shell-method.rst


   :returns: The next document in the cursor returned by the
             :method:`db.collection.find()` method or ``null``.
             
## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst

## Behavior

``cursor.tryNext()`` is a special case of the :method:`cursor.next()`
method that returns the next element in the iteration if available or
else ``null``.