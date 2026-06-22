---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/automerger-concept.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# The {+auto-merge-upper+}

Starting in MongoDB 7.0, the balancer can automatically merge chunks that meet the `mergeability requirements <mergeability-concept>`.

## Behavior

The {+auto-merge-upper+} runs in the background as part of balancing operations. For most use cases, the default settings perform well. For details on which settings to customize for your deployment, see `{+auto-merge-upper+} Policy <automerge-policy-settings>`.

When the {+auto-merge-upper+} runs, it squashes together all sequences of mergeable chunks for each shard of each collection.

{+auto-merge-upper+} Policy ```````````````````````````

Unless explicitly disabled, the {+auto-merge-upper+} starts the first time the balancer is enabled and pauses for the next :parameter:`autoMergerIntervalSecs` after the routine drains.

When {+auto-merge-upper+} is enabled, {+auto-merge-action+} happens every :parameter:`autoMergerIntervalSecs` seconds.

For a given collection, {+auto-merge-upper+} guarantees that subsequent merges are delayed at least the amount specified by :parameter:`autoMergerThrottlingMS`.

If a `balancing window <sharding-schedule-balancing-window>` is set, {+auto-merge-upper+} only runs during the window.

Balancing Settings Precedence ````````````````````````````` {+auto-merge-action-upper+} happens as part of balancing operations. In order to decide if and when to execute {+auto-merge-lower-plural+}, the settings are taken into account in this order:

#. Global `balancing settings <balancer-sharding-params>` #. Per-collection balancing settings (configured by :dbcommand:`configureCollectionBalancing`) #. Global `{+auto-merge-upper+} settings <automerger-params>` #. Per-collection {+auto-merge-upper+} settings (configured by :dbcommand:`configureCollectionBalancing`)

## Details

.. include:: /includes/mergeability.rst

## Example

.. include:: /includes/mergeAllChunksOnShard-example.rst
