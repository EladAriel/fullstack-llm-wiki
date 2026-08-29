---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.removeShardTag.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.891417Z"
---
# sh.removeShardTag() (mongosh method)

**meta:** :description: Remove a tag from a shard using `sh.removeShardTag()` when connected to a `mongos` instance.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** sh.removeShardTag(shard, tag)

   .. |method| replace:: :method:`sh.removeShardFromZone()`

   .. include:: /includes/fact-zone-sharding-alias.rst
   
   Removes the association between a tag and a shard. Only issue
   :method:`sh.removeShardTag()` when connected to a :binary:`~bin.mongos`
   instance.

   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``shard``
   
        - string
   
        - The name of the shard from which to remove a tag.
          
          
   
      * - ``tag``
   
        - string
   
        - The name of the tag to remove from the shard.

   .. seealso::

      :method:`sh.addShardTag()`
      :method:`sh.addTagRange()`

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst