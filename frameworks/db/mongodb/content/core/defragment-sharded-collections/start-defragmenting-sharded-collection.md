---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/defragment-sharded-collections/start-defragmenting-sharded-collection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
