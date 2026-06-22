---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/list-users.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# List Users in Self-Managed Deployments

To list all users, use :binary:`~bin.mongosh` to query the `system.users <system-users>` collection:

## Before You Begin

.. include:: /includes/dSO-role-intro.rst

.. include:: /includes/dSO-warning.rst

## Steps

```sh
use admin
db.system.users.find()
```

> **Important:** Do not modify the :doc:`system.users
</reference/system-users-collection>` collection directly. To manage
users, use the designated :ref:`user management commands
<user-management-commands>`.

To list all users of a `sharded cluster <sharding-sharded-cluster>` that were created through a :binary:`~bin.mongos`, connect to a :binary:`~bin.mongos` and run the preceding command. MongoDB stores users that are created through a :binary:`~bin.mongos` in the `admin` database of the `config servers <config server>`.

To list all `shard local users <shard-local-users>`, connect to the respective shard directly and run the preceding command. MongoDB stores shard local users in the `admin` database of the shard itself. These shard local users are independent from the users added to the sharded cluster through a :binary:`~bin.mongos`. Shard local users are local to the shard and are inaccessible to :binary:`~bin.mongos`.
