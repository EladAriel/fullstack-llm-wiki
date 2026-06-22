---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/add-member-to-shard.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# Add a Member to a Shard

You can add members to an existing shard in a `sharded cluster`. You might want to add a member to a shard for the same reasons you'd want to add a member to any `replica set <replica set>`. For example, increasing the number of members provides additional candidates to replace a primary in the event of a `failover <replication-auto-failover>`. Additional members also increase data redundancy and replica set availability.

For more information, refer to `replica-set-architecture`.

## About This Task

.. include:: /includes/tip-repl-set-add-members.rst

## Before You Begin

To add a member to a shard replica set, you need:

#. An active sharded cluster replica set.

#. A new host server for the new member. The new host server must be able to support your sharded data set and be accessible by the active replica set through the network.

.. include:: /includes/dSO-role-intro.rst

.. include:: /includes/dSO-warning.rst

## Steps

## Next Steps

Once the newly added member has transitioned into :replstate:`SECONDARY` state, use :method:`rs.reconfig()` to update the newly added member's :rsconf:`~members[n].priority` and :rsconf:`~members[n].votes` if needed.

.. include:: /includes/warning-rs-reconfig.rst

### Example

If :method:`rs.conf()` returns the configuration document for `mongodb3.example.net:27017` as the fifth element in the :rsconf:`members` array, to update its priority and votes to `1`, use the following sequence of operations:

```javascript
var cfg = rs.conf();
cfg.members[4].priority = 1
cfg.members[4].votes = 1
rs.reconfig(cfg)
```
