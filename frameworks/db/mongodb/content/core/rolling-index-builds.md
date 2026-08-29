---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/rolling-index-builds.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.515471Z"
---
.. _rolling-index-build:

# Rolling Index Builds

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

Rolling index builds are an alternative to :ref:`the default index
builds <index-operations>`. Rolling indexes build indexes on the
applicable nodes sequentially and may reduce the performance impact of
an index build if your deployment matches one of the following cases:

- If your average CPU utilization exceeds (N-1)/N-10% where N is the
  number of CPU threads available to mongod
- If the WiredTiger cache fill ratio regularly exceeds 90%

If your deployment does not meet this criteria, use the
:ref:`default index build <index-operations>`. 

**include:** /includes/warning-simultaneous-index-builds.rst

## Considerations

- Rolling index builds hide at most one replica set member at a time,
  starting with the secondary members, and build the index on that member
  as a standalone. 

- Rolling index builds require at least one replica set
  election.

- Rolling index builds lower the resiliency of your cluster and increases build
  duration.

**include:** /includes/note-atlas-index-docs.rst

## Tutorials

To create rolling index builds, use the following tutorials:

- :ref:`index-building-replica-sets`
- :ref:`index-build-on-sharded-clusters`

**toctree:** :titlesonly:
   :hidden:

   Create on Replica Sets </tutorial/build-indexes-on-replica-sets>
   Create on Sharded Clusters </tutorial/build-indexes-on-sharded-clusters>