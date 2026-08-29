---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.enableBalancing.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.911515Z"
---
# sh.enableBalancing() (mongosh method)

**meta:** :description: Enable the balancer for a specified sharded collection namespace using `sh.enableBalancing()` on a `mongos` instance.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Description

**method:** sh.enableBalancing(namespace)

   Enables the balancer for the specified namespace of the sharded collection.

   .. important::

      You can only run :method:`sh.enableBalancing()` on a
      :binary:`~bin.mongos` instance. :method:`sh.enableBalancing()`
      errors if run on :binary:`~bin.mongod` instance.

   The :method:`sh.enableBalancing()` method has the following parameter:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``namespace``
   
        - string
   
        - The :term:`namespace` of the collection.


   .. important:: 

      :method:`sh.enableBalancing()` does not *start*
      balancing. Rather, it allows balancing of this collection the
      next time the balancer runs.

   For more information on the balancing process, see
   :doc:`/tutorial/manage-sharded-cluster-balancer` and
   :ref:`sharding-balancing`.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-onprem-only.rst