---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/upgrade-to-enterprise-sharded-cluster.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===============================================

# Upgrade to MongoDB Enterprise (Sharded Cluster)

.. include:: /includes/minor-release.rst

.. include:: /includes/extracts/enterprise-additional-features.rst

The following steps outline the procedure to upgrade a sharded cluster from the MongoDB Community Edition to the MongoDB Enterprise Edition. For example, the steps can be used to upgrade MongoDB 7.0 Community to MongoDB 7.0 Enterprise.

## Consideration

> **Warning:** .. include:: /includes/extracts/enterprise-upgrade-edition-only.rst

## Download Enterprise Binaries

.. include:: /includes/extracts/enterprise-install-binaries.rst

## Procedure

To minimize downtime, you can upgrade from MongoDB Community to Enterprise Edition using a "rolling" upgrade by upgrading the members individually while the other members are available.

.. include:: /includes/steps/upgrade-enterprise-sharded-cluster.rst

> **Important:** Before using any Enterprise features, ensure that all members have
been upgraded to Enterprise edition.
