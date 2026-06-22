---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/troubleshooting/backup-restore-failures.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# Troubleshoot Backup and Restore Failures

Backup and restore operations for deployments managed by Ops Manager can fail for a variety of reasons, including agent connectivity issues, disk space constraints, or oplog inconsistencies.

This page describes how to confirm backup and restore failures, outlines common causes and resolutions, and provides guidance on what to collect before contacting support. If the issue persists after you complete the steps below, contact `technical-support`.

## Prerequisite Checks

Before you investigate the root cause of a backup or restore failure, confirm that a failure has occurred by checking the relevant status indicators in the Ops Manager UI or API.

### Check for Backup Failures

Use the following methods to confirm that a backup job or snapshot has failed.

Check Snapshot Status `````````````````````

To confirm whether a snapshot failed:

You can also click :guilabel:`JSON` next to a snapshot to view additional fields, including:

- `status`
- `createdDate`
- `completedDate`
- `totalDuration`
- `transferSpeed`
These fields help confirm whether the backup completed successfully.

For a description of all snapshot states, see :opsmgr:`Backup Overview </core/backup-overview/#backup-definition-and-operational-states>`.

Check the Backup Jobs Page ``````````````````````````

To check for issues with ongoing backup jobs:

For more information, see :opsmgr:`Jobs </admin/backup/jobs-page/#jobs>`.

Check Backup Logs `````````````````

To review error messages from backup jobs:

The logs display error messages grouped by time, which can help diagnose why a backup job failed.

Check Alerts ````````````

Ops Manager generates alerts that indicate failures or issues with backup jobs, including:

- "Backup has reached a high number of retries"
- "Backup is in an unexpected state"
- "Replica set has a late snapshot"
For a full list of backup-related alert conditions, see :opsmgr:`Alert Conditions </reference/alerts>`.

Query the API for Incomplete Snapshots ``````````````````````````````````````

To retrieve snapshots that have not completed, query the Ops Manager API using the `completed=false` query parameter:

```bash
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/snapshots?completed=false"
```

The response includes a `results` array where each object represents a snapshot. The `complete` field indicates whether the snapshot finished successfully.

> **Note:** The snapshot API does not provide a named failure status. A snapshot
with `complete: false` may still be in progress or may have failed.

For more information, see :opsmgr:`Get All Snapshots for One Cluster </reference/api/snapshots/get-all-snapshots-for-one-cluster/>`.

### Check for Restore Failures

Use the following methods to confirm that a restore job has failed.

Check the Restores Page ```````````````````````

To view the status of restore jobs in the Ops Manager UI:

The :guilabel:`Restores` page shows a table of the last 300 restore jobs. Check the :guilabel:`Status` column to identify jobs with the following states:

- `FAILED`
- `CANCELED`
- `IN_PROGRESS`
- `FINISHED`
Click a row to view more details about that specific restore operation.

For more information, see :opsmgr:`Restores </admin/backup/restores-page>`.

Query the API for Failed Restore Jobs ``````````````````````````````````````

To retrieve restore jobs programmatically, query the Ops Manager API:

```bash
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs"
```

The response includes a `results` array where each object represents a restore job. The `statusName` field indicates the job state. Possible values include:

- `FINISHED`
- `IN_PROGRESS`
- `BROKEN`
- `KILLED`
Restore jobs with a `statusName` of `BROKEN` or `KILLED` are considered failed.

To filter for failed jobs using `jq`:

```bash
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
  --header "Accept: application/json" \
  "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs" \
  | jq '.results[] | select(.statusName=="BROKEN" or .statusName=="KILLED")'
```

For more information, see :opsmgr:`Get All Restore Jobs for One Cluster </reference/api/restorejobs/get-all-restore-jobs-for-one-cluster/>`.

## Common Issues and Resolutions

The following sections describe common causes of backup and restore failures and how to resolve them.

### Backup Failures

The following sections describe common causes of backup failures and how to resolve them.

Insufficient Disk Space ```````````````````````

A lack of free disk space on the replica set member nodes can cause the cluster to enter an unhealthy state, leading to backup failures.

To resolve this issue, increase the available storage capacity on the `dbPath` of the affected nodes. Monitor disk usage regularly to prevent recurrence.

MongoDB Agent Is Down or Unstable ``````````````````````````````````

The backup process depends on the MongoDB Agent running continuously. If the agent stops or keeps restarting, backups fail.

Symptoms include:

- Alerts such as "Backup oplog is behind"
- No oplog slices received for an hour
To resolve this issue:

For more information, see :opsmgr:`Fix Backup Oplog Issues </reference/alerts/backup-oplog-is-behind/>`.

Agent Cannot Reach the Replica Set ```````````````````````````````````

The backup agent must maintain a connection to the replica set. Failures can occur due to network connectivity issues, an unavailable MongoDB node, or an authentication failure.

Symptoms in the agent logs include:

- `server selection timeout`
- `Authentication failed`
To resolve this issue:

For more information, see :opsmgr:`Fix Backup Oplog Issues </reference/alerts/backup-oplog-is-behind/>`.

Oplog Issues ````````````

If the oplog is too small or the backup agent cannot keep up with write activity, the backup falls behind and eventually fails.

Symptoms include the following alerts:

- "Backup requires a resync"
- "Backup oplog is behind"
To resolve this issue:

- Increase the oplog size so the oplog window covers enough history (a minimum
of 24 hours is recommended).

- If the backup has fallen too far behind, resync the backup.
Backup Job Fails to Bind to a Backup Daemon ````````````````````````````````````````````

A backup job requires a Backup Daemon with enough space to store a local copy of the backed-up replica set. If no daemon has sufficient space, the job fails to bind. To resolve this issue, add an additional Backup Daemon to increase capacity.

This issue can also occur when no primary is detected in the replica set. To resolve this, ensure the replica set is healthy and has a primary before you retry the backup.

For more information, see :opsmgr:`Backup FAQ </reference/faq/faq-backup/>`.

### Restore Failures

The following sections describe common causes of restore failures and how to resolve them.

Attempting to Restore a Single Shard in a Sharded Cluster ``````````````````````````````````````````````````````````

When you restore a sharded cluster, you must restore all shards. The restore process fails if you attempt to restore a single shard in isolation.

For more information, see :opsmgr:`Restore Limitations </tutorial/nav/restore-overview/#limitations>`.

Mismatched Settings Between Backup and Target Database ```````````````````````````````````````````````````````

An automated restore can fail when certain storage settings of the source backup and the target database do not match. If a restore attempt fails, Ops Manager displays any mismatched settings.

For a list of settings that must match, see :opsmgr:`Potential Causes for Automated Restore Failure </tutorial/nav/restore-overview/#potential-causes-for-automated-restore-failure>`.

Oplog Gaps During Point-in-Time Restore ````````````````````````````````````````

Point-in-time restores require a continuous oplog history. If there is a gap in the oplog, the restore fails.

Common causes of oplog gaps include:

- The backup agent stopped tailing the oplog.
- The oplog rolled over before the agent processed it.
- Cluster topology changes occurred.
- A Feature Compatibility Version (FCV) change occurred.
- A restore was attempted across MongoDB version changes.
To resolve this issue:

- Restore from the latest valid snapshot taken before the oplog gap, or
- Wait until a new snapshot is created, then perform the restore again.
For more information, see :opsmgr:`Restore from a Specific Point in Time </tutorial/restore-pit-snapshot-http/>`.

Insufficient Disk Space on the Restore Host ````````````````````````````````````````````

If the target host does not have enough storage for the snapshot files and restored database, the restore fails.

To resolve this issue:

For more information about the `dbStats` command, see :dbcommand:`dbStats`.

## Diagnostics to Collect for More Support

If the issue persists, collect the following information before contacting `technical-support`:

- Complete error messages from the Ops Manager UI or API
- Backup agent log files
- MongoDB server version
- Ops Manager version
- Relevant MongoDB server logs
- Output from the Restores page or API restore job query
## Related Issues

- `manual-troubleshooting-replica-set-no-primary`
- `manual-troubleshooting-replication-lag`
## Learn More

- :opsmgr:`Backup Overview </core/backup-overview/>`
- :opsmgr:`Restore Overview </tutorial/nav/restore-overview/>`
- :opsmgr:`Fix Backup Oplog Issues </reference/alerts/backup-oplog-is-behind/>`
