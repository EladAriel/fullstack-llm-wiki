---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-shard-collection.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.796717Z"
---
.. _manual-timeseries-shard-collection:

# Shard a Time Series Collection

**meta:** :description: Learn how to shard new or existing time series collections in MongoDB, including prerequisites and step-by-step procedures.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

Use this tutorial to shard a new or existing time series collection.

**important:** Before completing this tutorial, review the :ref:`sharding
   limitations <time-series-limitations-sharding>` for time series
   collections.

## Prerequisites

To shard a time series collection, you must :ref:`deploy a sharded
cluster <sharding-procedure-setup>` to host the database that contains
your time series collection.

**note:** .. include:: /includes/time-series/reshard-timeseries.rst

## Procedures

### Create a Sharded Time Series Collection

**include:** /includes/steps/shard-new-tsc.rst

**include:** /includes/steps/shard-new-tsc.rst

### Shard an Existing Time Series Collection

**include:** /includes/steps/shard-existing-tsc.rst

## Additional Information

- :ref:`manual-timeseries-collection`

- :method:`sh.shardCollection()`

- :dbcommand:`shardCollection`