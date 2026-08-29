---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.toArray.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.940854Z"
---
# cursor.toArray() (mongosh method)

**meta:** :description: Use `cursor.toArray()` to convert a cursor's documents into an array, iterating through and exhausting the cursor.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** cursor.toArray()


   .. include:: /includes/fact-mongosh-shell-method.rst


   The :method:`~cursor.toArray()` method returns an array that
   contains all the documents from a cursor. The method iterates
   completely the cursor, loading all the documents into RAM and
   exhausting the cursor.

   :returns: An array of documents.

Consider the following example that applies :method:`~cursor.toArray()`
to the cursor returned from the :method:`~db.collection.find()` method:

.. code-block:: javascript

   var allProductsArray = db.products.find().toArray();

   if (allProductsArray.length > 0) { printjson (allProductsArray[0]); }

The variable ``allProductsArray`` holds the array of documents returned by
:method:`~cursor.toArray()`.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst