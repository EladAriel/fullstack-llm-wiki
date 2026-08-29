---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.close.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.898887Z"
---
# cursor.close() (mongosh method)

**meta:** :description: Close a cursor in MongoDB to free server resources, applicable in Atlas, Enterprise, and Community environments.

.. default-domain:: mongodb

## Definition

**method:** cursor.close()


   .. include:: /includes/fact-mongosh-shell-method.rst


   Instructs the server to close a :ref:`cursor <cursors>`
   and free associated server resources. The server will automatically close
   cursors that have no remaining results, as well as cursors that have been
   idle for a period of time and lack the :method:`cursor.noCursorTimeout()`
   option.

   The :method:`~cursor.close()` method has the following
   prototype form:

   .. code-block:: javascript

      db.collection.find(<query>).close()

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst