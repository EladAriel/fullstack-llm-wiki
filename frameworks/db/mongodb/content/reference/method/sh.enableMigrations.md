---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.enableMigrations.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.926250Z"
---
# sh.enableMigrations() (mongosh method)

**meta:** :description: Enable migrations for a specified sharded collection namespace using `sh.enableMigrations()` on a `mongos` instance.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** sh.enableMigrations(namespace)

   Enables migrations for the specified namespace of the sharded collection, 
   but does not start chunk migrations. The balancer includes the collection you pass to 
   :method:`sh.enableMigrations()` in migration operations the next time it runs.
   For more information on chunk migrations, see :ref:`sharded-cluster-balancer`.

   .. important::

      You can only run :method:`sh.enableMigrations()` on a
      :binary:`~bin.mongos` instance. If you run :method:`sh.enableMigrations()` 
      on a :binary:`~bin.mongod` instance, the method returns an error. 

   The :method:`sh.enableMigrations()` method has the following parameter:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``namespace``
   
        - string
   
        - The :term:`namespace` of the collection.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-onprem-only.rst

**note:** You can verify migration status using :method:`sh.status()`, which displays 
   the ``allowMigrations`` field for each collection.