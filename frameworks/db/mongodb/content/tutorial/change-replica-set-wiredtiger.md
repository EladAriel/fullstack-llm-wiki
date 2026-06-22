---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/change-replica-set-wiredtiger.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# Change a Self-Managed Replica Set to WiredTiger

> **Note:** - .. include:: /includes/collMod-note.rst
- You must upgrade to WiredTiger. MongoDB removed the deprecated MMAPv1
  storage engine in version 4.2.

Use this tutorial to update a replica set to use `WiredTiger <storage-wiredtiger>`. The procedure updates the replica set in a rolling fashion to avoid downtime.

## Considerations

Replica sets can have members with different storage engines. As such, you can update members to use the WiredTiger storage engine in a rolling fashion.

### PSA 3-member Architecture

The :readconcern:`"majority"` read concern, available for WiredTiger, is enabled by default. However, in three-member replica sets with a primary-secondary-arbiter (PSA) architecture, you can disable the :readconcern:`"majority"` read concern. Disabling the :readconcern:`"majority"` read concern for a three-member PSA architecture avoids possible cache-pressure build up.

The `procedure <change-replica-set-wiredtiger-procedure>` below disables :readconcern:`"majority"` read concern for PSA architecture by including :option:`--enableMajorityReadConcern false <mongod --enableMajorityReadConcern>`.

> **Note:** .. include:: /includes/extracts/changestream-disable-rc-majority.rst

For more information on PSA architecture and read concern :readconcern:`"majority"`, see `disable-read-concern-majority`.

### Default Bind to Localhost

.. include:: /includes/fact-default-bind-ip-change.rst

### XFS and WiredTiger

With the WiredTiger storage engine, using XFS for data bearing nodes is recommended on Linux. For more information, see `prod-notes-linux-file-system`.

### MMAPv1 Only Restrictions

.. include:: /includes/fact-mmapv1-only-restrictions.rst

## Procedure

The following procedure updates the replica set in a rolling fashion. The procedure updates the `secondary` members first, then steps down the `primary`, and updates the stepped-down member.

To update a member to WiredTiger, the procedure removes a member's data, starts :binary:`~bin.mongod` with WiredTiger, and performs an `initial sync <resync-replica-member>`.

### A. Update the secondary members to WiredTiger.

Update the secondary members one at a time:

.. include:: /includes/steps/change-replica-set-wiredtiger.rst

Repeat the steps for the remaining secondary members, updating them one at a time.

### B. Step down the primary.

> **Important:** If updating all members of the replica set to use WiredTiger, ensure
that all secondary members have been updated first before updating
the primary.

Once all the secondary members have been upgraded to WiredTiger, connect :binary:`~bin.mongosh` to the primary and use :method:`rs.stepDown()` to step down the primary and force an election of a new primary.

```javascript
rs.stepDown()
```

### C. Update the stepped down primary.

When the primary has stepped down and become a secondary, update the secondary to use WiredTiger as before:

.. include:: /includes/steps/change-replica-set-wiredtiger.rst
