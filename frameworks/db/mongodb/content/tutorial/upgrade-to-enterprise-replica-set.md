---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/upgrade-to-enterprise-replica-set.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.581119Z"
---
.. _upgrade_to_enterprise_rs:

# Upgrade to MongoDB Enterprise (Replica Set)

**meta:** :keywords: on-prem
   :description: Upgrade a replica set from MongoDB Community to Enterprise Edition with minimal downtime using rolling upgrades and primary step-down.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**include:** /includes/minor-release.rst

**include:** /includes/extracts/enterprise-additional-features.rst

The following steps outline the procedure to upgrade a replica set from
the MongoDB Community Edition to the MongoDB Enterprise Edition. For
example, the steps can be used to upgrade MongoDB 7.0 Community to
MongoDB 7.0 Enterprise.

## Consideration

**warning:** .. include:: /includes/extracts/enterprise-upgrade-edition-only.rst


## Download Enterprise Binaries

**include:** /includes/extracts/enterprise-install-binaries.rst

## Procedure

To minimize downtime, you can upgrade from MongoDB Community to
Enterprise Edition using a "rolling" upgrade by upgrading the members
individually while the other members are available.

**include:** /includes/steps/upgrade-enterprise-replica-set.rst

**important:** Before using any Enterprise features, ensure that all members have
   been upgraded to Enterprise edition.