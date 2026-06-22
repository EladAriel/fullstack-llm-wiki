---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/troubleshooting/replica-set-no-primary.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# Troubleshoot Replica Sets with No Primary

Replica sets can occasionally enter a state where no primary exists, typically during elections. However, when no primary exists for an extended period, the replica set cannot accept writes.

This page contains common issues and resolutions for troubleshooting replica sets that have no primary for an extended period. If you need additional support after going through the following sections, contact `technical-support`.

## Prerequisite Checks

Verify that your deployment does not have a primary by running the :dbcommand:`replSetGetStatus` or :method:`rs.status()` method. The following example shows the output of the :method:`rs.status()` method for a replica set with no primary:

> **Note:** In some cases, you may see that the `rs.status()` output shows some
members' `stateStr` value as :replstate:`UNKNOWN` or :replstate:`DOWN`.

### Check Log Messages

Check your deployment's `log messages <log-messages-ref>` for entries where the component (`"c"`) value is `ELECTION`. Here, you might find repeated attempts to start elections that fail with the following messages in the `"msg"` field:

## Common Issues and Resolutions

The following section describes common issues that may cause a replica set to have difficulty electing a new primary and how to resolve them. Before you contact support, check whether the following issues prevent your deployment from electing a primary.

### Network Partition

If your deployment experiences a `network partition`, the nodes can't communicate with each other, preventing them from electing a primary.

To verify whether your deployment is affected by a network partition, run the :dbcommand:`replSetGetStatus` or :method:`rs.status()` method from different nodes. Based on the output from each node, identify which nodes are on each side of the partition.

To help restore connectivity after a partition:

- Check your firewall configurations for any rules that block
communication between members.

- Check DNS hostnames.
- Ensure that you add your IP address to your IP Access List.
> **Seealso:** - `considerations-when-deploying-rs`
- `replica-set-troubleshooting-check-connection`

Once a majority of nodes can reach each other, MongoDB automatically elects a primary and writes resume normally.

### No Eligible Secondary to Promote

Ensure that your main data center contains both a quorum of voting members and members that are eligible to be primary. If your replica set's primary goes down and none of the secondaries are elected to become the primary, check that your remaining nodes aren't all `priority 0 <replica-set-secondary-only-members>` members.

To check the priority values of each member, run the :dbcommand:`replSetGetConfig` command or :method:`rs.conf()` method:

If no secondaries are eligible to become primary due to their priority, update the :rsconf:`members[n].priority` value of one or more secondaries. For detailed instructions, see `replica-set-adjust-priority`.

### Resource Exhaustion

If your deployment has write-heavy workloads, too many indexes, or maintenance processes that take up significant disk space, you might overwhelm your nodes and cause them to crash.

To reclaim disk space, consider:

- Dropping unused collections or databases.
- Removing duplicate or unused indexes.
- If you have a scheduled `maintenance window <configure-maintenance-window>`,
consider enabling background compaction with the :dbcommand:`autoCompact`.

> **Warning:**   Run `autoCompact` only during periods of low traffic, such as a
  maintenance window. On high-traffic databases, background compaction can
  potentially delay or prevent operational tasks such as taking backups. To
  learn more about performance impact and other considerations before
  enabling background compaction, see
  `autoCompact Behavior <autocompact-behavior>`.

To monitor disk usage:

- On Atlas, you can view the :guilabel:`Disk Usage` chart, available in
`cluster monitoring <monitor-cluster-metrics>`.

- On self-managed deployments, run the :dbcommand:`dbStats` command or
:method:`db.stats()` method.

### Loss of Majority

If multiple voting members go down and the replica set loses its majority, `rs.status()` output may show that all members are in the `SECONDARY` or `RECOVERING` state. The following scenarios can cause loss of majority:

Incorrectly Performed Rolling Maintenance `````````````````````````````````````````

For example, consider a three-member replica set where you take two members down for maintenance at the same time. In this scenario, the replica set loses its majority and can't elect a new primary until the third member is back up.

To avoid this scenario, ensure that you perform rolling maintenance serially, starting with secondary members and ending with the primary. This ensures that a primary is always available. For guidance on replica set maintenance, see `perform-maint-on-replica-set`.

Underprovisioned Cluster Topology `````````````````````````````````

For example, consider a deployment with two data-bearing members and one hidden non-voting node. If one data-bearing member fails, the remaining members can't form a majority.

In a primary-secondary-arbiter (PSA) topology that uses :writeconcern:`"majority"` write concern, if the secondary goes down for maintenance, writes stall. The primary cannot get majority acknowledgment because only one of the two data-bearing voting members is available. Without `wtimeout <wc-wtimeout>` set on write operations, writes block indefinitely. To mitigate this:

- Throttle write operations during the maintenance window to limit
the volume of stalled writes.

- Set the `wtimeout` parameter on write operations that use
`"majority"` write concern to prevent writes from blocking indefinitely.

For more details on mitigating performance issues in PSA topologies, see `performance-issues-psa`.

In a primary-secondary-secondary-secondary-arbiter (PSSSA) topology, placing a majority of voting members in a single data center or disaster recovery (DR) site creates a risk of majority loss. If that region goes down completely, the remaining members cannot form a majority and cannot elect a primary. Distribute voting members across regions so that a majority remains available after a single-region failure. For guidance, see `data-center-awareness`.

## Verify Resolution

Once your deployment is restored and a new primary is elected, the `rs.status()` output shows that one of your members is in the `PRIMARY` state.

## Diagnostics to Collect for More Support

If you can't resolve your issue, contact `technical-support` with the following diagnostic information:

- Relevant log messages
- `rs.config()` output
- `rs.status()` output
## Related Issues

- `manual-troubleshooting-server-selection-timeout`
- `manual-troubleshooting-replication-lag`
## Learn More

- `monitoring-for-mdb`
- `reconfigure-replica-set-with-unavailable-members`
- `replica-set-architecture`
