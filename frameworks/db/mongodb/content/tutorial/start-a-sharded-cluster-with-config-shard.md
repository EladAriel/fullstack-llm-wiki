---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/start-a-sharded-cluster-with-config-shard.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
