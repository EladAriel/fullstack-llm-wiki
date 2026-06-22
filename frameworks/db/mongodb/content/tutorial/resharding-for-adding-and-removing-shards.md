---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/resharding-for-adding-and-removing-shards.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# Resharding for Adding and Removing Shards

## About this Task

You can use resharding to distribute your sharded collections to new shards. You can also use it to remove shards faster than chunk migrations.

.. include:: /includes/resharding-operation-phases.rst

## Before you Begin

Before you reshard, you must calculate your cluster's `<resharding-storage-req>`, `<resharding-latency-req>`, and any `<resharding-addl-reqs>`.

### Storage Requirements

.. include:: /includes/reshard-to-same-key/storage.rst

### Latency Requirements

.. include:: /includes/reshard-to-same-key/latency.rst

### Reshard Limitations

.. include:: /includes/fact-reshard-limitations.rst

### Additional Resource Requirements

.. include:: /includes/reshard-to-same-key/addl-resource-reqs.rst

## Steps

## Learn More

- `<reshard-to-same-key>`
- `<sharding-resharding>`
- :method:`sh.reshardCollection()`
