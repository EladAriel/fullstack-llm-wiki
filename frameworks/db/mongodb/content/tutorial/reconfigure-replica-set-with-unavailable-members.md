---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/reconfigure-replica-set-with-unavailable-members.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================================

# Reconfigure Self-Managed Replica Set for Unavailable Members

To reconfigure a `replica set` when a **majority** of members are available, use the :method:`rs.reconfig()` operation on the current `primary`, following the example in the `Replica Set Reconfiguration Procedure <replica-set-reconfiguration-usage>`.

This document provides steps for re-configuring a replica set when only a **minority** of members are accessible.

You may need to use the procedure, for example, in a geographically distributed replica set, where no local group of members can reach a majority. See `replica-set-elections` for more information on this situation.

## Reconfigure by Forcing the Reconfiguration

This procedure lets you recover while a majority of `replica set` members are down or unreachable. You connect to any surviving member and use the `force` option to the :method:`rs.reconfig()`  method.

The `force` option forces a new configuration onto the member. Use this procedure only to recover from catastrophic interruptions. Do not use `force` every time you reconfigure. Also, do not use the `force` option in any automatic scripts and do not use `force` when there is still a `primary`.

> **Warning:** .. include:: /includes/force-reconfiguration-warning.rst

To force reconfiguration:

1. Back up a surviving member.
#. Connect to a surviving member and save the current configuration. Consider the following example commands for saving the configuration:

```javascript
   cfg = rs.conf()

   printjson(cfg)
```

#. On the same member, remove the down and unreachable members of the replica set from the :rsconf:`members` array by setting the array equal to the surviving members alone. Consider the following example, which uses the `cfg` variable created in the previous step:

```javascript
   cfg.members = [cfg.members[0] , cfg.members[4] , cfg.members[7]]
```

#. On the same member, reconfigure the set by using the :method:`rs.reconfig()` command with the `force` option set to `true`:

```javascript
   rs.reconfig(cfg, {force : true})

This operation forces the secondary to use the new configuration. The
configuration is then propagated to all the surviving members listed
in the ``members`` array. The replica set then elects a new primary.

.. note::

   When you use ``force : true``, the version number in the replica
   set configuration increases significantly, by tens or hundreds
   of thousands. This is normal and designed to prevent set version
   collisions if you accidentally force re-configurations on both
   sides of a network partition and then the network partitioning
   ends.
```

#. If the failure or partition was only temporary, shut down or decommission the removed members as soon as possible.

> **Seealso:** `/tutorial/resync-replica-set-member`
