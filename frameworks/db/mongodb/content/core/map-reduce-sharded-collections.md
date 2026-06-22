---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/map-reduce-sharded-collections.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# Map-Reduce and Sharded Collections

> **Note:** .. include:: /includes/fact-use-aggregation-not-map-reduce.rst

Map-reduce supports operations on sharded collections, both as an input and as an output. This section describes the behaviors of :dbcommand:`mapReduce` specific to sharded collections.

## Sharded Collection as Input

When using sharded collection as the input for a map-reduce operation, :binary:`~bin.mongos` will automatically dispatch the map-reduce job to each shard in parallel. There is no special option required. :binary:`~bin.mongos` will wait for jobs on all shards to finish.

## Sharded Collection as Output

If the `out` field for :dbcommand:`mapReduce` has the `sharded value, MongoDB shards the output collection using the id` field as the shard key.

To output to a sharded collection:

- If the output collection does not exist, create the sharded
collection first.

- If the output collection already exists but is not sharded, map-reduce fails.
- For a new or an empty sharded collection, MongoDB uses the results of
the first stage of the map-reduce operation to create the initial `chunks <chunk>` distributed among the shards.

- :binary:`~bin.mongos` dispatches, in parallel, a map-reduce
post-processing job to every shard that owns a chunk. During the post-processing, each shard will pull the results for its own chunks from the other shards, run the final reduce/finalize, and write locally to the output collection.

> **Note:** - During later map-reduce jobs, MongoDB splits chunks as needed.
- Balancing of chunks for the output collection is automatically
  prevented during post-processing to avoid concurrency issues.
