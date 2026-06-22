---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/replica-set-architecture-three-members.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# Three Member Replica Sets

The minimum number of replica set members needed to obtain the benefits of a replica set is three members. A three member replica set can have either three data-bearing members (Primary-Secondary-Secondary) (Recommended) or if circumstances (such as cost) prohibit adding a third data bearing member, two data-bearing members and an arbiter (Primary-Secondary-Arbiter). [#arbiter-considerations]_

For considerations when using an arbiter, see `/core/replica-set-arbiter`.

## Primary with Two Secondary Members (P-S-S)

A replica set with three members that store data has:

- One `primary <replica-set-primary>`.
- Two `secondary <replica-set-secondary-members-ref>` members. Both
secondaries can become the primary in an `election <replica-set-election-internals>`.

.. include:: /images/replica-set-primary-with-two-secondaries.rst

These deployments provide two complete copies of the data set at all times in addition to the primary. These replica sets provide additional fault tolerance and `high availability <replica-set-failover>`. If the primary is unavailable, the replica set elects a secondary to be primary and continues normal operation. The old primary rejoins the set when available.

.. include:: /images/replica-set-trigger-election.rst

## Primary with a Secondary and an Arbiter (PSA)

> **Note:** For considerations when using an arbiter, see
`/core/replica-set-arbiter`.

A three member replica set with a two members that store data has:

- One `primary <replica-set-primary>`.
- One `secondary <replica-set-secondary-members-ref>` member. The
secondary can become primary in an `election <replica-set-election-internals>`.

- One `arbiter <replica-set-arbiter-configuration>`. The arbiter only
votes in elections.

.. include:: /images/replica-set-primary-with-secondary-and-arbiter.rst

Since the arbiter does not hold a copy of the data, these deployments provides only one complete copy of the data. Arbiters require fewer resources, but at the expense of more limited redundancy and fault tolerance.

However, a deployment with a primary, secondary, and an arbiter ensures that a replica set remains available if the primary or the secondary is unavailable. If the primary is unavailable, the replica set will elect the secondary to be primary.

.. include:: /images/replica-set-w-arbiter-trigger-election.rst

> **Seealso:** `/tutorial/deploy-replica-set`
