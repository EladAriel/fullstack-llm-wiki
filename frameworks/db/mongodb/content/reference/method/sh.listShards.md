---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.listShards.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.909097Z"
---
# sh.listShards() (mongosh method)

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** sh.listShards()

``sh.listShards()`` returns a list of the 
configured shards in a sharded cluster. This
information matches the ``shards`` field
returned by the :dbcommand:`listShards` database command.

## Syntax

``sh.listShards()`` has the following syntax:

.. code-block:: javascript

   sh.listShards()

## Behavior

The output for ``sh.listShards()`` returns an array of documents,
each describing one shard. Each document may contain the 
following fields:

**include:** /includes/list-shards-output.rst

## Example

The following code runs
``sh.listShards()`` and provides
an example output array:

.. io-code-block::
   
   .. input::
      :language: javascript

      sh.listShards()

   .. output::
      :visible: true
      :language: javascript
       
      [
        {
            "_id": "shard01",
            "host": "shard01/host1:27018,host2:27018,host3:27018",
            "state": 1
        },
        {
            "_id": "shard02",
            "host": "shard02/host4:27018,host5:27018,host6:27018",
            "tags": [ "NYC" ],
            "state": 1
        },
        {
            "_id": "shard03",
            "host": "shard03/host7:27018,host8:27018,host9:27018",
            "state": 1
        }
      ]