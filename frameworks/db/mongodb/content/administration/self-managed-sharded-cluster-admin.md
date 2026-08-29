---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/self-managed-sharded-cluster-admin.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.759242Z"
---
.. _self-managed-sharded-cluster-admin:

# Self-Managed Sharded Cluster Administration

**meta:** :keywords: on-prem
   :robots: noindex, nosnippet

.. default-domain:: mongodb

**facet:** :name: genre
   :values: reference

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

These documents provide instructions on how to administer a 
self-managed sharded cluster.

:ref:`replace-self-managed-config-server`
   Replace a config server in a replica set.

:ref:`restart-sharded-cluster`
   Stop and restart a sharded cluster.

:ref:`migrate-cluster-to-different-hardware`
   Migrate a sharded cluster to a different hardware system, for
   example, when moving a pre-production environment to production.

:ref:`back-up-sharded-cluster-metadata`
   Create a backup of a sharded cluster's metadata while keeping the
   cluster operational.

:ref:`convert-sharded-cluster-to-replica-set`
   Convert a sharded cluster into a single replica set.

:ref:`manual-convert-replica-set-to-sharded-cluster`
   Deploy a sharded cluster for an existing replica set.

**toctree:** :titlesonly:
   :hidden:

   Replace </tutorial/replace-config-server.txt>
   Restart </tutorial/restart-sharded-cluster>
   Migrate </tutorial/migrate-sharded-cluster-to-new-hardware>
   Back Up Cluster Metadata </tutorial/backup-sharded-cluster-metadata>
   Convert Sharded Cluster to Replica Set </tutorial/convert-sharded-cluster-to-replica-set>
   Convert a Replica Set to a Sharded Cluster </tutorial/convert-replica-set-to-replicated-shard-cluster>