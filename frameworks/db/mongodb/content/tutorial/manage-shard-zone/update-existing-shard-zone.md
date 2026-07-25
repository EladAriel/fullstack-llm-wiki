---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/manage-shard-zone/update-existing-shard-zone.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================

# Update an Existing Shard Zone

After you specify a range of values for a shard zone, you can update the shard zone range if your application's requirements change.

To update an existing shard zone, perform these steps:

#. Stop the `balancer`.

#. Remove the old range from the zone.

#. Update the zone's range.

#. Restart the balancer.

## About this Task

- Zone ranges are inclusive of the lower boundary and exclusive of the
upper boundary.

- After you modify a zone, the balancer must migrate chunks to the
appropriate zones based on the new range of values. Until balancing completes, some chunks may reside on the wrong shard given the configured zones for the sharded cluster.

## Before you Begin

To complete this tutorial, you must `deploy a sharded cluster <sharding-procedure-setup>` with a sharded collection and create a zone to modify.

This example uses a sharded collection named `users` in the `records` database, sharded by the `zipcode` field.

## Steps

The following procedure modifies the range of `zipcode` values for the `NYC` zone to be `11201` through `11240`.

## Learn More

- :method:`sh.removeRangeFromZone()`
- :method:`sh.updateZoneKeyRange()`
- `workload-isolation`
