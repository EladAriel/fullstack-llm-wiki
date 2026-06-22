---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/unshard-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# Unshard a Collection

You can unshard a sharded collection with the :dbcommand:`unshardCollection` command. When you unshard a collection, the collection cannot be partitioned across multiple `shards <shard>` and the `shard key` is removed.

By default, when you unshard a collection, MongoDB moves the collection's data to the shard with the least amount of data. Alternatively, you can specify which shard to place the data on.

## About this Task

### Compatibility

You can perform this task on deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

> **Note:** This task is not available on the {+atlas+} Free or Flex Tiers.

.. include:: /includes/fact-environments-onprem-only.rst

### Restrictions

.. include:: /includes/uc-considerations.rst

## Access Control

.. include:: /includes/access-control-unshardCollection.rst

## Before you Begin

.. include:: /includes/uc-reqs.rst

## Steps

## Learn More

- :method:`sh.abortUnshardCollection()`
- `remove-shards-from-cluster-tutorial`
- `shard-key-refine`
