---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/troubleshooting/frequent-elections.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# Troubleshoot Frequent Elections

Replica sets occasionally run `elections <replica-set-elections>` when a primary steps down or becomes unavailable. During an election, the replica set cannot accept writes until it successfully elects a new primary, though most reads can continue on secondaries if configured.

Expect this behavior during rare failovers or planned maintenance. However, frequent elections, where the primary changes often during normal operation, cause repeated write interruptions and, in some cases, rollbacks of uncommitted data.

This page contains common issues and resolutions for frequent elections to ensure fast diagnosis and avoid application write interruptions. If you need additional support after reviewing the following sections, contact `technical-support`.

## Prerequisite Checks

Healthy clusters see elections only during infrequent, expected events. Elections normally happen during the following scenarios:

- Initial setup
- Maintenance operations, such as :method:`rs.stepDown()` or
:method:`rs.reconfig()`

- New member additions with :method:`rs.add()`
- Primary unavailability for more than the configured
`timeout`, where the default is 10 seconds

Verify that your deployment experiences frequent elections outside of these scenarios by running the :dbcommand:`replSetGetStatus` or :method:`rs.status() method multiple times over a set period, such as within an hour or throughout the day. Compare the reported primary's id` value each time to track if and when the primary node changes, meaning an election occurred.

> **Note:** If you see a `TOO_MANY_ELECTIONS`
alert in Ops Manager, you are
likely experiencing frequent elections.

### Check Log Messages

You can also refer to your deployment's `log messages <log-messages-ref>` for entries where the component (`"c"`) value is `ELECTION`. If your logs display multiple occurrences of the following messages over short intervals, such as multiple times per hour or day without planned maintenance, this typically indicates an unhealthy replica set caused by network instability, unhealthy hosts, or misconfiguration:

## Common Issues and Resolutions

The following section describes common issues that can cause a replica set to perform unexpected frequent elections. Before you contact support, check if the following pitfalls cause frequent elections in your replica set.

### Resource Exhaustion

Intensive queries, large aggregations, and background tasks like index builds or backups can lead to high CPU usage, disk latency or failures, and memory pressure. Resource exhaustion can cause frequent elections because the primary can become unresponsive or unable to process heartbeats on time.

Inefficient Queries ```````````````````

To check if your deployment experiences resource exhaustion due to inefficient queries:

1. Look for entries in your logs where the component ("c")
value is `COMMAND`. #. For each entry, the `bytesRead` field indicates how many bytes a given command reads. Pay attention to commands with large `bytesRead` values. #. If the timestamps for your inefficient queries occur near the timestamps for multiple elections, inefficient queries are likely causing your frequent elections.

Use the following resources to optimize your queries:

- Handle your workload more efficiently using `index-type-compound`.
- Review our `ESR Guideline <esr-indexing-rule>` to create new indexes.
- In Atlas, review your `performance advisor <performance-advisor>`
regularly for index suggestions based on your latest workload.

### Replica Set Misconfiguration

Node Priority `````````````

Replica sets continuously call elections until they elect the member with the highest `priority <rs-election-priority>`. If you do not set member priorities appropriately, elections can occur more often, with unexpected members becoming primary.

To check the priority values of each member, run the :dbcommand:`replSetGetConfig` command or :method:`rs.conf()` method. The following example shows the output of the :method:`rs.conf()` method for a replica set with incorrectly configured priorities:

In the above example, the current primary has lower priority than the three other members. If a high-priority secondary is healthy and in SECONDARY state, it can trigger an election to take over as primary.

Ensure you configure the priorities for your replica set members appropriately:

- Assign the highest priority to the server you want to
consistently serve as the primary

- Assign default or lower priorities to other members to reduce
their likelihood of becoming primary

- Assign nodes with high replication lag low priority
Replica Set Settings ````````````````````

To check your replica set configuration settings, run the :dbcommand:`replSetGetConfig` command or :method:`rs.conf()` method. The following example shows a replica set with `electionTimeoutMillis` configured too low:

Ensure your value for :rsconf:`settings.electionTimeoutMillis` is not too low. In the above example, the :rsconf:`settings.electionTimeoutMillis` value is lower than :rsconf:`settings.heartbeatIntervalMillis`. This means a node can declare the primary "down" before a full heartbeat interval completes, causing unnecessary elections.

### Network Partitioning or Latency

If your deployment experiences `network partition` or your nodes experience delayed heartbeat messages, secondaries can incorrectly view the primary as unavailable and initiate elections.

To verify that you are experiencing network partitions:

1. Check for common occurrences of the following messages in
your logs:

#. Run :method:`rs.status()` or :dbcommand:`replSetGetStatus` from different nodes to show differing views of which members are reachable, which indicates a split between subsets of nodes.

To help restore connectivity after a partition:

- Check your firewalls configurations for any rules that can
block communication between members.

- Check DNS hostnames.
- Ensure that you add your IP address to your IP Access List.
## Verify Resolution

After you address the root cause, confirm that frequent elections no longer occur by re-running `rs.status()`. The output shows exactly one member in the primary state, and that the primary remains stable over your normal observation window without unplanned changes.

You can also consult your deployment logs. Look for the log messages listed above in your deployment logs to ensure that elections do not occur multiple times over short intervals.

## Diagnostics to Collect for More Support

If you still aren't able to resolve your issue, contact Technical Support with the following diagnostic information:

- Relevant log messages over the affected time period
- `rs.config()` output
- `rs.status()` output
## Related Issues

- `manual-troubleshooting-replica-set-no-primary`
- `manual-troubleshooting-replication-lag`
## Learn More

- `replica-set-elections`
- `self-managed-replset-configuration`
