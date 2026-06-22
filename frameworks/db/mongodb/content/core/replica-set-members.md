---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/replica-set-members.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================

# Replica Set Members

A replica set in MongoDB is a group of :binary:`~bin.mongod` processes that provide redundancy and high availability. The members of a replica set are:

`replica-set-primary-member` The primary receives all write operations.

`replica-set-secondary-members` Secondaries replicate operations from the primary to maintain an identical data set. Secondaries may have additional configurations for special usage profiles. For example, secondaries may be `non-voting <replica-set-non-voting-members>` or `priority 0 <replica-set-secondary-only-members>`.

The minimum recommended configuration for a replica set is a three member replica set with three data-bearing members: one `primary <replica-set-primary-member>` and two `secondary <replica-set-secondary-members>` members. In some circumstances (such as you have a primary and a secondary but cost constraints prohibit adding another secondary), you may choose to include an `arbiter <replica-set-arbiters>`. An arbiter participates in `elections <replica-set-elections>` but does not hold data (i.e. does not provide data redundancy).

A replica set can have up to 50 members but only 7 voting members.

> **Seealso:** - `replSetGetStatus.votingMembersCount`
- `replSetGetStatus.writableVotingMembersCount`

## Primary

.. include:: /core/replica-set-primary.txt

## Contents

- Primary </core/replica-set-primary>

## Secondaries

.. include:: /core/replica-set-secondary.txt

.. include:: /core/replica-set-secondary.txt

## Contents

- Secondary </core/replica-set-secondary>

## Arbiter

.. include:: /core/replica-set-arbiter.txt

For considerations when using an arbiter, see `/core/replica-set-arbiter`.

## Contents

- Arbiter </core/replica-set-arbiter>

.. include:: /includes/footnote-two-primaries-edge-cases.rst
