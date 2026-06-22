---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/upgrade-to-enterprise-sharded-cluster.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
