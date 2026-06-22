---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/schedule-backup-window-for-sharded-clusters.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================================

# Schedule Backup Window for a Self-Managed Sharded Cluster

## Overview

In a `sharded cluster`, the balancer process is responsible for distributing sharded data around the cluster, so that each `shard` has roughly the same amount of data.

However, when creating backups from a sharded cluster it is important that you disable the balancer while taking backups to ensure that no chunk migrations affect the content of the backup captured by the backup procedure.

.. include:: /includes/fact-backup-shard

Using the procedure outlined in the section `sharding-balancing-disable-temporarily` you can manually stop the balancer process temporarily. As an alternative, you can use the following procedure to define a balancing window so that the balancer is always disabled during your automated backup operation.

> **Tip:** .. include:: /includes/extracts/sharded-clusters-backup-restore-mongodump-mongorestore-restriction.rst

## Procedure

If you have an automated backup schedule, you can disable all balancing operations for a period of time. For instance, consider the following command:

```javascript
use config
db.settings.updateOne(
   { _id : "balancer" }, 
   { $set : { activeWindow : { start : "06:00", stop : "23:00" } } }, 
   true
)
```

This operation configures the balancer to run between 6:00am and 11:00pm, server time. Schedule your backup operation to run and complete outside of this time. Ensure that the backup can complete outside the window when the balancer is running and that the balancer can effectively balance the collection among the shards in the window allotted to each.
