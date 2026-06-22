---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/force-member-to-be-primary.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================================

# Force a Self-Managed Replica Set Member to Become Primary

## Overview

You can force a `replica set` member to become `primary` by giving it a higher :rsconf:`members[n].priority` value than any other member in the set.

Optionally, you also can force a member never to become primary by setting its :rsconf:`members[n].priority` value to `0`, which means the member can never seek `election <replica-set-elections>` as primary. For more information, see `replica-set-secondary-only-members`.

For more information on priorities, see :rsconf:`members[n].priority`.

## Consideration

A majority of the configured members of a replica set must be available for a set to reconfigure a set or elect a primary. See `/core/replica-set-elections` for more information.

## Procedures

> **Note:** .. include:: /includes/extracts/rs-stepdown-election-handoff.rst

### Force a Member to be Primary by Setting its Priority High

This procedure assumes your current `primary` is `m1.example.net` and that you'd like to instead make `m3.example.net` primary. The procedure also assumes you have a three-member `replica set` with the configuration below. For more information on configurations, see `Replica Set Configuration Use <replica-set-reconfiguration-usage>`.

This procedure assumes this configuration:

```javascript
{
    "_id" : "rs",
    "version" : 7,
    "members" : [
        {
            "_id" : 0,
            "host" : "m1.example.net:27017"
        },
        {
            "_id" : 1,
            "host" : "m2.example.net:27017"
        },
        {
            "_id" : 2,
            "host" : "m3.example.net:27017"
        }
    ]
}
```

1. In a :binary:`~bin.mongosh` session that is connected to the primary,
use the following sequence of operations to make `m3.example.net` the primary:

```javascript
   cfg = rs.conf()
   cfg.members[0].priority = 0.5
   cfg.members[1].priority = 0.5
   cfg.members[2].priority = 1
   rs.reconfig(cfg)

The last statement calls :method:`rs.reconfig()` with the modified
configuration document to configure ``m3.example.net`` to have a higher
:rsconf:`members[n].priority` value than the other
:binary:`~bin.mongod` instances.

The following sequence of events occur:

- ``m3.example.net`` and ``m2.example.net`` sync with
  ``m1.example.net`` (typically within 10 seconds).

- ``m1.example.net`` sees that it no longer has highest priority and,
  in most cases, steps down. ``m1.example.net`` *does not* step down
  if ``m3.example.net``'s sync is far behind. In that case,
  ``m1.example.net`` waits until ``m3.example.net`` is within 10
  seconds of its optime and then steps down. This minimizes the
  amount of time with no primary following failover.

- The step down forces an election in which ``m3.example.net``
  becomes primary based on its
  :rsconf:`priority <members[n].priority>` setting.
```

#. Optionally, if `m3.example.net` is more than 10 seconds behind `m1.example.net`'s optime, and if you don't need to have a primary designated within 10 seconds, you can force `m1.example.net` to step down by running:

```javascript
   db.adminCommand({replSetStepDown: 86400, force: 1})

This prevents ``m1.example.net`` from being primary for 86,400
seconds (24 hours), even if there is no other member that can become primary.
When ``m3.example.net`` catches up with ``m1.example.net`` it will
become primary.

If you later want to make ``m1.example.net``
primary again while it waits for ``m3.example.net`` to catch up,
issue the following command to make ``m1.example.net`` seek election
again:

.. code-block:: javascript

   rs.freeze()

The :method:`rs.freeze()` provides a wrapper around the
:dbcommand:`replSetFreeze` database command.
```

### Force a Member to be Primary Using Database Commands

Consider a `replica set` with the following members:

- `mdb0.example.net` - the  current `primary`.
- `mdb1.example.net` - a `secondary`.
- `mdb2.example.net` - a secondary .
To force a member to become primary use the following procedure:

1. In :binary:`~bin.mongosh`, run :method:`rs.status()` to ensure your
replica set is running as expected.

#. In a :binary:`~bin.mongosh` session that is connected to the :binary:`~bin.mongod` instance running on `mdb2.example.net`, freeze `mdb2.example.net` so that it does not attempt to become primary for 120 seconds.

```javascript
   rs.freeze(120)
```

#. In a :binary:`~bin.mongosh` session that is connected to the :binary:`~bin.mongod` running on `mdb0.example.net`, step down this instance that the :binary:`~bin.mongod` is not eligible to become primary for 120 seconds:

```javascript
   rs.stepDown(120)

``mdb1.example.net`` becomes primary.

.. note:: During the transition, there is a short window where
   the set does not have a primary.
```

For more information, consider the :method:`rs.freeze()` and :method:`rs.stepDown()` methods that wrap the :dbcommand:`replSetFreeze` and :dbcommand:`replSetStepDown` commands.
