---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/PlanCache.help.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.998164Z"
---
# PlanCache.help() (mongosh method)

**meta:** :description: Access methods to view and modify a collection's query plan cache using `PlanCache.help()`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** PlanCache.help()

   Displays the methods available to view and modify a collection's
   query plan cache.

   The method is only available from the :method:`plan cache object
   <db.collection.getPlanCache()>` of a specific collection; i.e.

   .. code-block:: javascript

      db.collection.getPlanCache().help()

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-onprem-only.rst

**seealso:** :method:`db.collection.getPlanCache()`