---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.splitFind.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.981113Z"
---
# sh.splitFind() (mongosh method)

**meta:** :description: Use `sh.splitFind()` to split a chunk containing a specified shard key value at its median point, creating two roughly equal chunks.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** sh.splitFind(namespace, query)

   Splits the chunk that contains the shard key value specified by the
   ``query`` at the chunk's median point. :method:`sh.splitFind()`
   creates two roughly equal chunks. To split a chunk at a specific
   point instead, see :method:`sh.splitAt()`.

   .. |dbcommand| replace:: :dbcommand:`split` command
   .. include:: /includes/fact-mongosh-shell-method-alt.rst

   The method takes the following arguments:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``namespace``
   
        - string
   
        - The namespace (i.e. ``<database>.<collection>``) of the sharded
          collection that contains the chunk to split.
          
          
   
      * - ``query``
   
        - document
   
        - A query document that specifies the :term:`shard key` value 
          that determines the chunk to split.
          
          
   


   The :method:`sh.splitFind()` method wraps the :dbcommand:`split`
   command.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst

## Consideration

In most circumstances, you should leave chunk splitting to the
automated processes within MongoDB.

To use :method:`sh.splitFind()`, the sharded collection must be
populated.

## Example

For the sharded collection ``test.foo``, the following example splits,
at the median point, a chunk that contains the shard key value ``x:
70``.

.. code-block:: javascript

   sh.splitFind( "test.foo", { x: 70 } )