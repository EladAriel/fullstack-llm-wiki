---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-secondary-only-replica-set-member.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================================

# Prevent a Self-Managed Secondary from Becoming Primary

## Overview

In a replica set, by default all `secondary` members are eligible to become primary through the election process. You can use the :rsconf:`priority <members[n].priority>` to affect the outcome of these elections by making some members more likely to become primary and other members less likely or unable to become primary.

Secondaries that cannot become primary are also unable to trigger elections. In all other respects these secondaries are identical to other secondaries.

To prevent a `secondary` member from ever becoming a `primary` in a `failover`, assign the secondary a priority of `0`, as described here. For a detailed description of secondary-only members and their purposes, see `/core/replica-set-priority-0-member`.

## Considerations

.. include:: /includes/fact-rs-conf-array-index.rst

> **Note:** MongoDB does not permit the current `primary` to have a priority
of `0`. To prevent the current primary from again becoming a primary,
you must first step down the current primary using
:method:`rs.stepDown()`.

## Procedure

This tutorial uses a sample replica set with 5 members.

.. include:: /includes/warning-rs-reconfig.rst

.. include:: /includes/steps/configure-secondary-only-rs-member.rst

## Related Documents

- :rsconf:`members[n].priority`
- `/tutorial/adjust-replica-set-member-priority`
- `Replica Set Reconfiguration <replica-set-reconfiguration-usage>`
- `/core/replica-set-elections`
