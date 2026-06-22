---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/replica-set-architectures.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# Replica Set Deployment Architectures

The architecture of a `replica set <replica set>` affects the set's capacity and capability. This document provides strategies for replica set deployments and describes common architectures.

The standard replica set deployment for a production system is a three-member replica set. These sets provide redundancy and fault tolerance. Avoid complexity when possible, but let your application requirements dictate the architecture.

.. include:: /includes/replication/note-replica-set-major-versions.rst

## Strategies

### Determine the Number of Members

Add members in a replica set according to these strategies.

Maximum Number of Voting Members ````````````````````````````````

A replica set can have up to :limit:`50 members <Number of Members of a Replica Set>`, but only :limit:`7 voting members <Number of Voting Members of a Replica Set>`. If the replica set already has 7 voting members, additional members must be `non-voting members <replica-set-non-voting-members>`.

Deploy an Odd Number of Members ```````````````````````````````

Ensure that the replica set has an odd number of voting members. A replica set can have up to 7 voting members. If you have an even number of voting members, deploy another data bearing voting member or, if constraints prohibit against another data bearing voting member, an `arbiter <replica-set-arbiters>`.

An `arbiter <arbiter>` does not store a copy of the data and requires fewer resources. As a result, you may run an arbiter on an application server or other shared resource. With no copy of the data, it may be possible to place an arbiter into environments that you would not place other members of the replica set. Consult your security policies.

.. include:: /includes/admonition-multiple-arbiters.rst

Consider Fault Tolerance ````````````````````````

Fault tolerance for a replica set is the number of members that can become unavailable and still leave enough members in the set to elect a primary. In other words, it is the difference between the number of members in the set and the `majority <replSetGetStatus.majorityVoteCount>` of voting members needed to elect a primary. Without a primary, a replica set cannot accept write operations. Fault tolerance is an effect of replica set size, but the relationship is not direct. See the following table:

Adding a member to the replica set does not always increase the fault tolerance. However, in these cases, additional members can provide support for dedicated functions, such as backups or reporting.

:method:`rs.status()` returns `replSetGetStatus.majorityVoteCount` for the replica set.

Use Hidden and Delayed Members for Dedicated Functions ``````````````````````````````````````````````````````

Add `hidden <replica-set-hidden-members>` or `delayed <replica-set-delayed-members>` members to support dedicated functions, such as backup or reporting.

Read-Heavy Applications ```````````````````````

A replica set is designed for high availability and redundancy. In most cases secondary members operate under similar loads as the primary. You should not direct reads to secondaries.

If you have a read-heavy application, consider using `c2c-index` to replicate data to another cluster for reading.

For more information on secondary read modes, see: :readmode:`secondary` and :readmode:`secondaryPreferred`.

Add Capacity Ahead of Demand ````````````````````````````

The existing members of a replica set must have spare capacity to support adding a new member. Always add new members before the current demand saturates the capacity of the set.

### Distribute Members Geographically

To protect your data in case of a data center failure, keep at least one member in an alternate data center. If possible, use an odd number of data centers, and choose a distribution of members that maximizes the likelihood that even with a loss of a data center, the remaining replica set members can form a majority or at minimum, provide a copy of your data.

.. include:: /includes/note-csrs-distribution.rst

To ensure that the members in your main data center be elected primary before the members in the alternate data center, set the :rsconf:`members[n].priority` of the members in the alternate data center to be lower than that of the members in the primary data center.

For more information, see `/core/replica-set-architecture-geographically-distributed`

### Target Operations with Tag Sets

Use `replica set tag sets <replica-set-configuration-tag-sets>` to target read operations to specific members or to customize write concern to request acknowledgment from specific members.

> **Seealso:** - `/data-center-awareness`
- `/core/workload-isolation`

### Use Journaling to Protect Against Power Failures

MongoDB enables `journaling <journaling-internals>` by default. Journaling protects against data loss in the event of service interruptions, such as power failures and unexpected reboots.

### Hostnames

.. include:: /includes/important-hostnames.rst

## Replica Set Naming

.. include:: /includes/fact-unique-replica-set-names.rst

## Deployment Patterns

The following documents describe common replica set deployment patterns. Other patterns are possible and effective depending on the application's requirements. If needed, combine features of each architecture in your own deployment:

`/core/replica-set-architecture-three-members` Three-member replica sets provide the minimum recommended architecture for a replica set.

`/core/replica-set-architecture-geographically-distributed` Geographically distributed sets include members in multiple locations to protect against facility-specific failures, such as power outages.

## Contents

- Three Members </core/replica-set-architecture-three-members>
- Distributed Data Centers </core/replica-set-architecture-geographically-distributed>
