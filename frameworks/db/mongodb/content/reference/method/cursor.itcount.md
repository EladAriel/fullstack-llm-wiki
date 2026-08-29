---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.itcount.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.910242Z"
---
# cursor.itcount() (mongosh method)

**meta:** :description: Count the number of documents remaining in a cursor using `itcount()`, which exhausts the cursor's contents.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** cursor.itcount()


   .. include:: /includes/fact-mongosh-shell-method.rst


   Counts the number of documents remaining in a cursor.

   :method:`~cursor.itcount()` is similar to :method:`cursor.count()`, but
   actually executes the query on an existing iterator, exhausting its contents
   in the process.

   The :method:`~cursor.itcount()` method has the following
   prototype form:

   .. code-block:: javascript

      db.collection.find(<query>).itcount()

   .. seealso::

      :method:`cursor.count()`

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst