---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/unsharded-collections.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.554808Z"
---
.. _unsharded-collections-concept:

# Unsharded Collections

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

Starting in MongoDB 8.0, you can unshard a sharded collection by using the 
:dbcommand:`unshardCollection` command. When you unshard a collection,
MongoDB moves the collection data onto a single shard and updates the metadata 
to reflect the unsharded state. 

## Command Syntax

To unshard a collection, use the :dbcommand:`unshardCollection` command:

.. code-block:: javascript

   db.adminCommand({
      unshardCollection : "<database>.<collection>",
      toShard : "<recipient shard ID>"
   })

## Use Cases

A user can unshard a collection if: 

- You can store the collection entirely on a single shard.

- The collection requires resource isolation, and access patterns are better 
  supported if the collection lives on a single shard. To meet the same 
  requirements on a sharded collection, see :ref:`Zone Sharding 
  <zone-sharding>`.

- The collection was previously sharded but no longer needs to be sharded.

## Get Started

- :ref:`unshard-collection-task`

## Access Control

**include:** /includes/access-control-unshardCollection.rst

## Details

An unsharded collection's data only lives on one shard and the :term:`shard key` 
is removed. Collections that you manually unshard behave the same as newly 
created collections that were never sharded.

You can specify the destination shard with the optional ``toShard`` field. If 
you don't specify a destination shard, MongoDB automatically selects the shard
with the least amount of data.

## Learn More

- :ref:`moveable-collections`
- :dbcommand:`unshardCollection`

**toctree:** :titlesonly: 

   Unshard a Collection </tutorial/unshard-collection>
   Stop Unsharding a Collection </tutorial/stop-unsharding-collection>