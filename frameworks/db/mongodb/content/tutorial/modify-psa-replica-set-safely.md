---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/modify-psa-replica-set-safely.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

============================================

# Modify a Self-Managed PSA Replica Set Safely

## Overview

When reconfiguring primary-secondary-arbiter (PSA) replica sets or changing to a PSA architecture, you need to take special care in the following cases:

- You want to reconfigure a secondary in an existing three-member
replica set with a PSA architecture to become a voting, data-bearing node with a non-zero priority.

- You want to add a new voting, data-bearing node with a non-zero
priority to an existing two-member replica set that contains one primary and one arbiter.

> **Warning:** If the secondary you are adding is lagged and the resulting replica
set is a PSA configuration, the first configuration change will
change the number of nodes that need to commit a change with
:writeconcern:`"majority"`. In this case, your commit point will lag
until the secondary has caught up.

This document outlines the procedure for reconfiguring your replica set in these specific cases **without** using the designated helper method :method:`rs.reconfigForPSASet`.

## Procedure

If you are performing one of the preceding operations, it is necessary to reconfigure your replica set in two steps:

1. Reconfigure the replica set to add or modify a secondary with
`{ votes: 1, priority: 0 }`.

2. Once the added or modified secondary has caught up with all
committed writes, reconfigure the secondary to have a non-zero priority `{ votes: 1, priority: <num> }`.

The two-step approach avoids the possibility of rolling back committed writes in the case of a failover to the new secondary before the new secondary has all committed writes from the previous primary.

To run the :method:`rs.reconfigForPSASet()` method, you must connect to the `primary` of the replica set.

.. include:: /includes/steps/modify-psa-replica-set-safely.rst
