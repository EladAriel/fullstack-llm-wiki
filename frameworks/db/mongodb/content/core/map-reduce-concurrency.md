---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/map-reduce-concurrency.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.538262Z"
---
.. _map-reduce-concurrency:

# Map-Reduce Concurrency

**meta:** :description: Use aggregation pipelines instead of map-reduce for better performance and usability in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**note:** Aggregation Pipeline as an Alternative to Map-Reduce

   .. include:: /includes/fact-use-aggregation-not-map-reduce.rst

The map-reduce operation is composed of many tasks, including reads
from the input collection, executions of the ``map`` function,
executions of the ``reduce`` function, writes to a temporary collection
during processing, and writes to the output collection.

During the operation, map-reduce takes the following locks:

- The read phase takes a read lock.  It yields every 100 documents.

- The insert into the temporary collection takes a write lock for a
  single write.

- If the output collection does not exist, the creation of the output
  collection takes a write lock.

- If the output collection exists, then the output actions (i.e.
  ``merge``, ``replace``, ``reduce``) take a write lock. This write
  lock is *global*, and blocks all operations on the :binary:`~bin.mongod`
  instance.
