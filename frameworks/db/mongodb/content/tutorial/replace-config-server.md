---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/replace-config-server.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# Replace a Self-Managed Config Server

> **Important:** The following procedure applies to {+latest-lts-version+} config
servers. For earlier versions of MongoDB, refer to the corresponding
version of the MongoDB Manual.

## Overview

If the config server replica set becomes read only, i.e. does not have a primary, the sharded cluster cannot support operations that change the cluster metadata, such as chunk splits and migrations. Although no chunks can be split or migrated, applications will be able to write data to the sharded cluster.

If one of the config servers is unavailable or inoperable, repair or replace it as soon as possible. The following procedure replaces a member of a `config server replica set <sharding-config-server>` with a new member.

The tutorial is specific to MongoDB {+latest-lts-version+}. For earlier versions of MongoDB, refer to the corresponding version of the MongoDB Manual.

## Considerations

.. include:: /includes/fact-config-server-replica-set-restrictions.rst

## Procedure

.. include:: /includes/steps/replace-disabled-config-server.rst
