---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/map-reduce-sharded-collections.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.514625Z"
---
.. _map-reduce-sharded-collections:

# Map-Reduce and Sharded Collections

**meta:** :description: Use aggregation pipelines instead of map-reduce for better performance and usability, especially with sharded collections.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**note:** Aggregation Pipeline as an Alternative to Map-Reduce

   .. include:: /includes/fact-use-aggregation-not-map-reduce.rst

Map-reduce supports operations on sharded collections, both as an input
and as an output. This section describes the behaviors of
:dbcommand:`mapReduce` specific to sharded collections.

.. _map-reduce-sharded-cluster:

## Sharded Collection as Input

When using sharded collection as the input for a map-reduce operation,
:binary:`~bin.mongos` will automatically dispatch the map-reduce job to
each shard in parallel. There is no special option
required. :binary:`~bin.mongos` will wait for jobs on all shards to
finish.

## Sharded Collection as Output

If the ``out`` field for :dbcommand:`mapReduce` has the ``sharded``
value, MongoDB shards the output collection using the ``_id`` field as
the shard key.
   
To output to a sharded collection:

- If the output collection does not exist, create the sharded
  collection first.
  
- If the output collection already exists but is not sharded, map-reduce fails.

- For a new or an empty sharded collection, MongoDB uses the results of
  the first stage of the map-reduce operation to create the initial
  :term:`chunks <chunk>` distributed among the shards.

- :binary:`~bin.mongos` dispatches, in parallel, a map-reduce
  post-processing job to every shard that owns a chunk. During the
  post-processing, each shard will pull the results
  for its own chunks from the other shards, run the final
  reduce/finalize, and write locally to the output collection.

**note:** - During later map-reduce jobs, MongoDB splits chunks as needed.

   - Balancing of chunks for the output collection is automatically
     prevented during post-processing to avoid concurrency issues.