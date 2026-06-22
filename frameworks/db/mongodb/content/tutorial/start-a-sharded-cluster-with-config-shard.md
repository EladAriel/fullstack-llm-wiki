---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/start-a-sharded-cluster-with-config-shard.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# Start a Sharded Cluster with a Config Shard

.. include:: /includes/config-shard-intro.rst

## About this Task

You can consider using a config shard if your cluster has three or fewer shards.

For details, see `Config Shard Use Cases <config-shard-use-cases>`.

### Compatibility

You can perform this task on deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

> **Note:** This task is not available on the {+atlas+} Free or Flex Tiers.

.. include:: /includes/fact-environments-onprem-only.rst

..

## Access Control

TBD. Checking in with Tech re Access Control: https://docs.google.com/document/d/1Q2R01EArSVZ86pilDnjFJNrgRZVNjQ77dGN99oGk1Gk/edit

## Steps

## Learn More

- `config-shard-concept`
- :dbcommand:`addShard`
- :dbcommand:`transitionFromDedicatedConfigServer`
