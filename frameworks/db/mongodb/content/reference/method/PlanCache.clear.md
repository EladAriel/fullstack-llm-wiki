---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/PlanCache.clear.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.977404Z"
---
# PlanCache.clear() (mongosh method)

**meta:** :description: Clear all cached query plans for a collection using the `PlanCache.clear()` method in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** PlanCache.clear()

   Removes all cached query plans for a collection.

   .. |dbcommand| replace:: :dbcommand:`planCacheClear` command
   .. include:: /includes/fact-mongosh-shell-method-alt

   The method is only available from the :method:`plan cache object
   <db.collection.getPlanCache()>` of a specific collection; i.e.

   .. code-block:: javascript

      db.collection.getPlanCache().clear()

   For example, to clear the cache for the ``orders`` collection:

   .. code-block:: javascript

      db.orders.getPlanCache().clear()

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-onprem-only.rst

## Required Access

On systems running with :setting:`~security.authorization`, a user must have access that
includes the :authaction:`planCacheWrite` action.

**seealso:** - :method:`db.collection.getPlanCache()`
   - :method:`PlanCache.clearPlansByQuery()`