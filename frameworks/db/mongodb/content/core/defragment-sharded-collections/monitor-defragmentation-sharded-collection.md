---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/defragment-sharded-collections/monitor-defragmentation-sharded-collection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===============================================

# Monitor Defragmentation of a Sharded Collection

To monitor defragmentation of a sharded collection, use the :dbcommand:`balancerCollectionStatus` command.

You can see the current defragmentation state and the number of remaining chunks to process. This shows you the defragmentation progress.

## About this Task

.. include:: /includes/defragment-sharded-collections-status.rst

.. include:: /includes/defragment-sharded-collections-example.rst

In the procedure for this task, you monitor the phases and see the defragmentation progress.

## Before you Begin

- Start defragmenting a sharded collection. For details, see
`start-defragmenting-sharded-collection`.

- Connect to :binary:`~bin.mongos`.
## Procedure

## Next Steps

If defragmentation has not yet completed, you can stop it. For details, see `stop-defragmenting-sharded-collection`.

## Learn More

- :ref:`Start defragmenting a sharded collection
<start-defragmenting-sharded-collection>`

- :ref:`Stop defragmenting a sharded collection
<stop-defragmenting-sharded-collection>`

- To view the balancer collection status output document, see
`Balancer collection status output document <cmd-balancer-CollectionStatus-output>`

.. include:: /includes/defragment-sharded-collections-learn-more.rst
