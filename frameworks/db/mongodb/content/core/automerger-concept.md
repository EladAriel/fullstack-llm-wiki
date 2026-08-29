---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/automerger-concept.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.529909Z"
---
.. _automerger-concept:

# The {+auto-merge-upper+}

**meta:** :description: Enable automatic merging of chunks in MongoDB 7.0 to optimize shard balancing operations.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

Starting in MongoDB 7.0, the balancer can automatically merge chunks
that meet the :ref:`mergeability requirements <mergeability-concept>`.

## Behavior

The {+auto-merge-upper+} runs in the background as part of balancing
operations. For most use cases, the default settings perform well. For 
details on which settings to customize for your deployment, see 
:ref:`{+auto-merge-upper+} Policy <automerge-policy-settings>`.

When the {+auto-merge-upper+} runs, it squashes together all sequences
of mergeable chunks for each shard of each collection.

### {+auto-merge-upper+} Policy

.. _automerge-policy-settings:

Unless explicitly disabled, the {+auto-merge-upper+} starts the first 
time the balancer is enabled and pauses for the next 
:parameter:`autoMergerIntervalSecs` after the routine drains.

When {+auto-merge-upper+} is enabled, {+auto-merge-action+} happens 
every :parameter:`autoMergerIntervalSecs` seconds.

For a given collection, {+auto-merge-upper+} guarantees that subsequent 
merges are delayed at least the amount specified by 
:parameter:`autoMergerThrottlingMS`.

If a :ref:`balancing window <sharding-schedule-balancing-window>` is 
set, {+auto-merge-upper+} only runs during the window.

### Balancing Settings Precedence
{+auto-merge-action-upper+} happens as part of balancing operations. 
In order to decide if and when to execute {+auto-merge-lower-plural+}, 
the settings are taken into account in this order:

#. Global :ref:`balancing settings <balancer-sharding-params>`
#. Per-collection balancing settings (configured by :dbcommand:`configureCollectionBalancing`)
#. Global :ref:`{+auto-merge-upper+} settings <automerger-params>`
#. Per-collection {+auto-merge-upper+} settings (configured by :dbcommand:`configureCollectionBalancing`)

## Details

.. _mergeability-concept:

**include:** /includes/mergeability.rst

## Example

**include:** /includes/mergeAllChunksOnShard-example.rst