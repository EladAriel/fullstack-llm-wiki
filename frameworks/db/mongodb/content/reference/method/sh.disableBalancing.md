---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.disableBalancing.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.917434Z"
---
# sh.disableBalancing() (mongosh method)

**meta:** :description: Disable the balancer for a specific sharded collection using `sh.disableBalancing()` on a `mongos` instance.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Description

**method:** sh.disableBalancing(namespace)

   Disables the balancer for the
   specified sharded collection. This does not affect the balancing of
   :term:`chunks <chunk>` for other sharded collections in the same cluster.

   .. important::

      You can only run :method:`sh.disableBalancing()` on a
      :binary:`~bin.mongos` instance. :method:`sh.disableBalancing()`
      errors if run on :binary:`~bin.mongod` instance.

   The :method:`sh.disableBalancing()` method has the following
   parameter:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``namespace``
   
        - string
   
        - The :term:`namespace` of the collection.
          
          
   


   For more information on the balancing process, see
   :doc:`/tutorial/manage-sharded-cluster-balancer` and
   :ref:`sharding-balancing`.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-onprem-only.rst