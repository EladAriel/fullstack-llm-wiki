---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/localhost-exception.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# Localhost Exception in Self-Managed Deployments

> **Important:** On a :binary:`~bin.mongod` instance, the localhost exception only
applies when there are **no users or roles** created in the MongoDB
instance.

The localhost exception allows you to create the first user or role in the system after enabling access control. You can also use it to initiate a replica set.

## Initiating a Replica Set

You can use the localhost exception to initiate a replica set, following the steps in `server-replica-set-deploy`. You must wait until the replica set elects a primary before you can add the first user.

## Creating the First User or Role

> **Warning:** Connections using the localhost exception have access to create
only the **first user OR role**. Only create a role first if you are
authorizing users with LDAP. See :ref:`LDAP Authorization
<security-ldap-external>` for more information.

After you enable access control, connect to the localhost interface and `create the first user <create-user-admin>` in the `admin` database. The first user must have privileges to create other users. The :authrole:`userAdmin` or :authrole:`userAdminAnyDatabase` role both confer the privilege to create other users.

### Localhost Exception for Sharded Clusters

> **Important:** - On a :binary:`~bin.mongos`, the localhost exception only applies
  when there are no `sharded cluster users <sharding-localhost>`
  or roles created.
- In a sharded cluster, the localhost exception applies to each shard
  individually as well as to the cluster as a whole.

Once you create a sharded cluster and add a `user administrator <create-user-admin>` through the :binary:`~bin.mongos` instance, you **must** still prevent unauthorized access to the individual shards. To prevent unauthorized access to individual shards, follow one of the following steps for each shard in your cluster:

- `Create a user administrator <create-user-admin>` on the shard's
primary.

- Disable the localhost exception at startup. To disable the localhost
exception, set the :parameter:`enableLocalhostAuthBypass` parameter to `0`.

## All Localhost Exception Permissions

While the localhost exception applies, you can:

- Run the :dbcommand:`createUser` command or :method:`db.createUser()` method.
This ends the localhost exception.

- Run the :dbcommand:`createRole` command or :method:`db.createRole()` method.
This ends the localhost exception.

- Use the :authaction:`grantRole` action to grant a role to a user on an
external authentication system, such as LDAP.

- Run :dbcommand:`replSetInitiate` to initiate a new replica set
- Run :dbcommand:`replSetGetStatus` to get the status of the current member's
replica set

- Run :dbcommand:`replSetReconfig` on the primary member to modify replica set
configuration.

- On a :binary:`~bin.mongos` instance, if the cluster is hosted on
`localhost`, you can run :dbcommand:`addShard` to add a shard to the cluster.
