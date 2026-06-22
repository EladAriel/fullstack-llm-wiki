---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/defragment-sharded-collections/start-defragmenting-sharded-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# Start Defragmenting a Sharded Collection

To start defragmenting a sharded collection, use the :dbcommand:`configureCollectionBalancing` command with the `defragmentCollection` option set to `true`.

## About this Task

.. include:: /includes/defragment-sharded-collections-conditions.rst

.. include:: /includes/defragment-sharded-collections-example.rst

## Before you Begin

Connect to :binary:`~bin.mongos`.

## Procedure

## Next Steps

You can monitor the collection's defragmentation progress. For details, see `monitor-defragmentation-sharded-collection`.

## Learn More

.. include:: /includes/defragment-sharded-collections-learn-more.rst
