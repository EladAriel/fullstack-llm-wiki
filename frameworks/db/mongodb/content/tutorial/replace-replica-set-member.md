---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/replace-replica-set-member.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.610347Z"
---
.. _server-replica-set-replace-member:

# Replace a Self-Managed Replica Set Member

**meta:** :keywords: on-prem
   :description: Learn how to change the hostname of a replica set member without altering its configuration using a specific operation.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

If you need to change the hostname of a replica set member without
changing the configuration of that member or the set, you can use the
operation outlined in this tutorial. For example if you must
re-provision systems or rename hosts, you can use this pattern to
minimize the scope of that change.

## Operation

To change the hostname for a replica set member modify the
:rsconf:`members[n].host` field. The value of
:rsconf:`members[n]._id` field will not change
when you reconfigure the set.

See :doc:`/reference/replica-configuration` and
:method:`rs.reconfig()` for more information.

**note:** Any replica set configuration change can trigger the current
   :term:`primary` to step down, which forces an :ref:`election
   <replica-set-elections>`. During the election, the current shell
   session and clients connected to this replica set disconnect,
   which produces an error even when the operation succeeds.

## Example

To change the hostname to ``mongo2.example.net`` for the replica set
member configured at ``members[0]``, issue the following sequence of
commands:

.. code-block:: javascript

   cfg = rs.conf()
   cfg.members[0].host = "mongo2.example.net"
   rs.reconfig(cfg)