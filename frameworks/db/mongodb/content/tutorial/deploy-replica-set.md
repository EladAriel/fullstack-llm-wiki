---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/deploy-replica-set.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================================

# Deploy a Self-Managed Replica Set

.. include:: /includes/introduction-deploy-replica-set.rst

.. include:: /includes/fact-self-managed.rst

.. include:: /includes/fact-atlas-link.rst

## Requirements

For production deployments, host each :binary:`~bin.mongod` instance on a separate machine serviced by redundant power circuits and redundant network paths. This includes instances running on virtual machines.

Before you can deploy a replica set, you must install MongoDB on each system that will be part of your `replica set`. If you have not already installed MongoDB, see the `installation tutorials <tutorial-installation>`.

## Considerations When Deploying a Replica Set

.. include:: /includes/considerations-deploying-replica-set.rst

## Deploy a Replica Set in the Terminal

Use the following steps to create a three-member `replica set` from three existing :binary:`~bin.mongod` instances running with `access control <authorization>` disabled.

To deploy a replica set with enabled `access control <authorization>`, see `deploy-repl-set-with-auth`. If you want to deploy a replica set from a single MongoDB instance, see `server-replica-set-deploy-convert`. For more information on replica set deployments, see the `replication` and `replica-set-architecture` documentation.

.. include:: /includes/steps/deploy-replica-set.rst

> **Seealso:** `deploy-repl-set-with-auth`
