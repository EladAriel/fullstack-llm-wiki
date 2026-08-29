---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.addShardTag.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.943941Z"
---
.. _sharding-add-shard-tag:

# sh.addShardTag() (mongosh method)

**meta:** :description: Associate shards with tags using `sh.addShardTag()` to direct chunks within tagged ranges to specific shards.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** sh.addShardTag(shard, tag)

   .. |method| replace:: :method:`sh.addShardToZone()`
   
   .. include:: /includes/fact-zone-sharding-alias.rst
   
   Associates a shard with a tag or identifier. MongoDB uses these
   identifiers to direct :term:`chunks <chunk>` that fall within a
   tagged range to specific shards. :method:`sh.addTagRange()`
   associates chunk ranges with tag ranges.


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``shard``
   
        - string
   
        - The name of the shard to which to give a specific tag.
          
          
   
      * - ``tag``
   
        - string
   
        - The name of the tag to add to the shard.
          
          
   


   Only issue :method:`sh.addShardTag()` when connected to a
   :binary:`~bin.mongos` instance.

   .. tip::
   
      .. include:: /includes/extracts/zoned-sharding-pre-define-zone.rst

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst

## Example

The following example adds three tags, ``NYC``, ``LAX``, and ``NRT``, to
three shards:

.. code-block:: javascript

   sh.addShardTag("shard0000", "NYC")
   sh.addShardTag("shard0001", "LAX")
   sh.addShardTag("shard0002", "NRT")

**seealso:** - :method:`sh.addTagRange()`
   - :method:`sh.removeShardTag()`