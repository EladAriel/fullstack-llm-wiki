---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/read-concern-available.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

============================

# Read Concern `"available"`

A query with read concern `"available"` returns data from the instance with no guarantee that the data has been written to a majority of the replica set members (i.e. may be rolled back).

- **For a sharded cluster**, :readconcern:`"available"` read concern
provides greater tolerance for partitions.

Queries with the :readconcern:`"available"` read concern don't require a check to ensure that the correct shard received the query.

In the event of network partitions, these queries route to the shard considered appropriate before the network partition occurred.  They do not wait for consistency guarantees from servers that may be unavailable.  If the shard was undergoing chunk migration, queries with :readconcern:`"available"` can return `orphaned documents <orphaned document>`.

> **Warning:**   :program:`mongos` does not guarantee that queries with read concern
  :readconcern:`"available"` route to the correct shards.  The shard that
  receives the query returns data, but this shard may not be the
  authoritative owner of the requested data.
  This can cause queries to return incorrect or unexpected results.

- **For unsharded collections** (including collections in a standalone
deployment or a replica set deployment), :readconcern:`"local"` and :readconcern:`"available"` read concerns behave identically.

.. include:: /includes/fact-readConcern-most-recent-data-in-node.rst

> **Seealso:** :parameter:`orphanCleanupDelaySecs`

## Availability

Read concern :readconcern:`"available"` is :red:`unavailable for use` with causally consistent sessions and transactions.

## Example

.. include:: /includes/fact-read-concern-write-timeline.rst

Then, the following tables summarizes the state of the data that a read operation with :readconcern:`"available"` read concern would see at time `T`.

.. figure:: /images/read-concern-write-timeline.svg
