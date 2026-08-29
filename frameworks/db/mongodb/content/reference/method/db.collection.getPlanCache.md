---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.getPlanCache.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.967608Z"
---
# db.collection.getPlanCache() (mongosh method)

**meta:** :description: Access and manage the query plan cache for a collection using `db.collection.getPlanCache()` with methods to view and clear cached query plans.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** db.collection.getPlanCache()


   .. include:: /includes/fact-mongosh-shell-method.rst


   Returns an interface to access the query plan cache for a
   collection. The interface provides methods to view and clear the
   query plan cache.

   :returns: Interface to access the query plan cache.

   .. include:: /includes/fact-query-optimizer-cache-behavior.rst


## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-onprem-only.rst

### Query Settings

**include:** /includes/persistent-query-settings-avoid-index-filters-intro.rst

## Methods

The following methods are available through the interface:

.. list-table::
   :widths: 30,70
   :header-rows: 1

   * - Name

     - Description

   * - :method:`PlanCache.help()`

     - Displays the methods available for a collection's query plan cache.
       Accessible through the plan cache object of a specific collection,
       i.e. ``db.collection.getPlanCache().help()``.
   

   * - :method:`PlanCache.clearPlansByQuery()`

     - Clears the cached query plans for the specified :term:`plan cache query shape`.
       Accessible through the plan cache object of a specific collection,
       i.e. ``db.collection.getPlanCache().clearPlansByQuery()``
   

   * - :method:`PlanCache.clear()`

     - Clears all the cached query plans for a collection.
       Accessible through the plan cache object of a specific collection,
       i.e. ``db.collection.getPlanCache().clear()``.
   
   * - :method:`PlanCache.list()`

     - Returns the plan cache information for a collection. Accessible
       through the plan cache object of a specific collection, i.e.
       ``db.collection.getPlanCache().list()``.