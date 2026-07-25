---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/resharding-back-to-same-key.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===============================================

# Reshard a Collection back to the Same Shard Key

## About this Task

Resharding to the same shard key lets you use resharding as a data movement mechanism. This enables you to:

.. include:: /includes/resharding-about.rst

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
