---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/replica-set-primary.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:orphan:

===================

# Replica Set Primary

The primary is the only member in the replica set that receives write operations. MongoDB applies write operations on the `primary` and then records the operations on the primary's `oplog </core/replica-set-oplog>`. `Secondary <replica-set-secondary-members>` members replicate this log and apply the operations to their data sets.

In the following three-member replica set, the primary accepts all write operations. Then the secondaries replicate the oplog to apply to their data sets.

.. include:: /images/replica-set-read-write-operations-primary.rst

All members of the replica set can accept read operations. However, by default, an application directs its read operations to the primary member. See `/core/read-preference` for details on changing the default read behavior.

The replica set can have at most one primary. [#edge-cases-2-primaries]_ If the current primary becomes unavailable, an election determines the new primary. See `/core/replica-set-elections` for more details.

In the following 3-member replica set, the primary becomes unavailable. This triggers an election which selects one of the remaining secondaries as the new primary.

.. include:: /images/replica-set-trigger-election.rst

.. include:: /includes/footnote-two-primaries-edge-cases.rst
