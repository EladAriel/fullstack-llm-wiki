---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/list-users.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.582896Z"
---
.. _list-users:

# List Users in Self-Managed Deployments

.. default-domain:: mongodb

**meta:** :keywords: on-prem
   :description: Query the system.users collection using `mongosh` to list all users in self-managed MongoDB deployments.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 3
   :class: singlecol

To list all users, use :binary:`~bin.mongosh` to query the
:ref:`system.users <system-users>` collection:

## Before You Begin

**include:** /includes/dSO-role-intro.rst

**include:** /includes/dSO-warning.rst

## Steps

.. code-block:: sh

   use admin
   db.system.users.find()

**important:** Do not modify the :doc:`system.users
   </reference/system-users-collection>` collection directly. To manage
   users, use the designated :ref:`user management commands
   <user-management-commands>`.

To list all users of a :ref:`sharded cluster <sharding-sharded-cluster>` that were
created through a :binary:`~bin.mongos`, connect to a
:binary:`~bin.mongos` and run the preceding command. MongoDB stores
users that are created through a :binary:`~bin.mongos` in the ``admin``
database of the :term:`config servers <config server>`.

To list all :ref:`shard local users
<shard-local-users>`, connect to the respective shard directly and run
the preceding command. MongoDB stores *shard local* users in the
``admin`` database of the shard itself. These *shard local* users are
independent from the users added to the sharded cluster through a
:binary:`~bin.mongos`. *Shard local* users are local to the shard and
are inaccessible to :binary:`~bin.mongos`.