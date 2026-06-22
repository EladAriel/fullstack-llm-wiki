---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/deploy-replica-set.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# Deploy a Self-Managed Replica Set

.. include:: /includes/introduction-deploy-replica-set.rst

.. include:: /includes/fact-self-managed.rst

.. include:: /includes/fact-atlas-link.rst

## Requirements

For production deployments, you should maintain as much separation between members as possible by hosting the :binary:`~bin.mongod` instances on separate machines. When using virtual machines for production deployments, you should place each :binary:`~bin.mongod` instance on a separate host server serviced by redundant power circuits and redundant network paths.

Before you can deploy a replica set, you must install MongoDB on each system that will be part of your `replica set`. If you have not already installed MongoDB, see the `installation tutorials <tutorial-installation>`.

## Considerations When Deploying a Replica Set

.. include:: /includes/considerations-deploying-replica-set.rst

## Deploy a Replica Set in the Terminal

This tutorial describes how to create a three-member `replica set` from three existing :binary:`~bin.mongod` instances running with `access control <authorization>` disabled.

To deploy a replica set with enabled `access control <authorization>`, see `deploy-repl-set-with-auth`. If you wish to deploy a replica set from a single MongoDB instance, see `server-replica-set-deploy-convert`. For more information on replica set deployments, see the `replication` and `replica-set-architecture` documentation.

.. include:: /includes/steps/deploy-replica-set.rst

> **Seealso:** `deploy-repl-set-with-auth`
