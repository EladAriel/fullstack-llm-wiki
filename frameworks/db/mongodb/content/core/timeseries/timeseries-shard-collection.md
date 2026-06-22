---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-shard-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# Shard a Time Series Collection

Use this tutorial to shard a new or existing time series collection.

> **Important:** Before completing this tutorial, review the :ref:`sharding
limitations <time-series-limitations-sharding>` for time series
collections.

## Prerequisites

To shard a time series collection, you must `deploy a sharded cluster <sharding-procedure-setup>` to host the database that contains your time series collection.

> **Note:** .. include:: /includes/time-series/reshard-timeseries.rst

## Procedures

### Create a Sharded Time Series Collection

.. include:: /includes/steps/shard-new-tsc.rst

.. include:: /includes/steps/shard-new-tsc.rst

### Shard an Existing Time Series Collection

.. include:: /includes/steps/shard-existing-tsc.rst

## Additional Information

- `manual-timeseries-collection`
- :method:`sh.shardCollection()`
- :dbcommand:`shardCollection`
