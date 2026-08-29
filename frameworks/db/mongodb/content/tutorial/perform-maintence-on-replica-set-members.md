---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/perform-maintence-on-replica-set-members.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.631675Z"
---
.. _perform-maint-on-replica-set:

# Perform Maintenance on Self-Managed Replica Set Members

**meta:** :keywords: on-prem
   :description: Perform maintenance on replica set members by restarting each as a standalone, completing tasks, and reintegrating them into the set, starting with secondaries.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Overview

:term:`Replica sets <replica set>` allow a MongoDB deployment to
remain available during the majority of a maintenance window.

This document outlines the basic procedure for performing maintenance on
each of the members of a replica set. Furthermore, this particular
sequence strives to minimize the amount of time that the
:term:`primary` is unavailable and control the impact on the
entire deployment.

Use these steps as the basis for common replica set operations,
particularly for procedures such as upgrading to the latest
version of MongoDB. 

## Procedure

For each member of a replica set, starting with a secondary member,
perform the following sequence of events, ending with the primary:

- Restart the :binary:`~bin.mongod` instance as a standalone.

- Perform the task on the standalone instance.

- Restart the :binary:`~bin.mongod` instance as a member of the replica
  set.

**include:** /includes/steps/perform-maintenance-task-on-replica-set-members.rst