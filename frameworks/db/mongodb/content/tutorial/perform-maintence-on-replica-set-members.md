---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/perform-maintence-on-replica-set-members.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================================================

# Perform Maintenance on Self-Managed Replica Set Members

## Overview

`Replica sets <replica set>` allow a MongoDB deployment to remain available during the majority of a maintenance window.

This document outlines the basic procedure for performing maintenance on each of the members of a replica set. Furthermore, this particular sequence strives to minimize the amount of time that the `primary` is unavailable and control the impact on the entire deployment.

Use these steps as the basis for common replica set operations, particularly for procedures such as upgrading to the latest version of MongoDB.

## Procedure

For each member of a replica set, starting with a secondary member, perform the following sequence of events, ending with the primary:

- Restart the :binary:`~bin.mongod` instance as a standalone.
- Perform the task on the standalone instance.
- Restart the :binary:`~bin.mongod` instance as a member of the replica
set.

.. include:: /includes/steps/perform-maintenance-task-on-replica-set-members.rst
