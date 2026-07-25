---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.setProfilingLevel.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================================

# db.setProfilingLevel() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`db.setProfilingLevel()` method has the following form:

```javascript
db.setProfilingLevel(<level>, <options>)
```

## Parameters

## Returns

The method returns a document that contains the **previous** values of the settings.

Where:

- `was` is the **previous** `level <set-profiling-level-level>`
setting.

- `slowms` is the **previous** :ref:`slowms
<set-profiling-level-options-slowms>` setting.

- `sampleRate` is the **previous** :ref:`sampleRate
<set-profiling-level-options-sampleRate>` setting.

- `filter` is the **previous** :ref:`filter
<set-profiling-level-options-filter>` setting.

- `note` is a string explaining the behavior of `filter`. This field
only appears in the output when `filter` is also present.

> **Note:** The `filter` and `note` fields only appear in the output if
they were present in the previous :ref:`level
<set-profiling-level-level>` setting.

To view the current profiling level, see :method:`db.getProfilingStatus()`.

## Behavior

.. include:: /includes/warning-profiler-performance.rst

## Examples

### Enable Profiler and Set Slow Operation Threshold and Sample Rate

The following example sets for a :binary:`~bin.mongod` instance:

- the `profiling level <set-profiling-level-level>` to `1`,
- the slow operation threshold :ref:`slowms
<set-profiling-level-options-slowms>` to `20` milliseconds, and

- the `sampleRate <set-profiling-level-options-sampleRate>` to
`0.42`.

```javascript
db.setProfilingLevel(1, { slowms: 20, sampleRate: 0.42 })
```

.. include:: /includes/reference/return-set-profile.rst

### Disable Profiler and Set Slow Operation Threshold and Sample Rate

The following example sets for a :binary:`~bin.mongod` or :binary:`~bin.mongos` instance:

- the `profiling level <set-profiling-level-level>` to `0`,
- the slow operation threshold :ref:`slowms
<set-profiling-level-options-slowms>` to `20` milliseconds, and

- the `sampleRate <set-profiling-level-options-sampleRate>` to
`0.42`.

```javascript
db.setProfilingLevel(0, { slowms: 20, sampleRate: 0.42 })
```

.. include:: /includes/reference/return-set-profile.rst

### Set a Filter to Determine Profiled Operations

The following example sets for a :binary:`~bin.mongod` instance:

- the `profiling level <set-profiling-level-level>` to `1`,
- a `filter <set-profiling-level-options-filter>` of
`{ op: "query", millis: { $gt: 2000 } }`, which causes the profiler to only record `query` operations that took longer than 2 seconds.

```javascript
db.setProfilingLevel( 1, { filter: { op: "query", millis: { $gt: 2000 } } } )
```

.. include:: /includes/reference/return-set-profile.rst

### Set a Filter Without Enabling the Profiler

You can set a `filter` without enabling the database profiler. The following example uses a filter with a `profiling level <set-profiling-level-level>` of `0`.

```javascript
db.setProfilingLevel( 0, { filter: { op: "query", millis: { $gt: 2000 } } } )
```

Because the profiling level is `0`, the profiler is disabled and does not record matching operations to the profiler collection. The filter still applies to the diagnostic log.

.. include:: /includes/reference/return-set-profile.rst

### Unset a Filter

To clear a profile filter, run `db.setProfilingLevel()` with the `filter: "unset"` option.

```javascript
db.setProfilingLevel( 1, { filter: "unset" } )
```

.. include:: /includes/reference/return-set-profile.rst
