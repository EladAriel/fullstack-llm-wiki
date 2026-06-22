---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/validate.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# validate (database command)

## Definition

.. versionchanged:: 6.2

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     validate: <string>,  // Collection name
     full: <boolean>,  // Optional
     repair: <boolean>,  // Optional, added in MongoDB 5.0
     metadata: <boolean>,  // Optional, added in MongoDB 5.0.4
     checkBSONConformance: <boolean>  // Optional, added in MongoDB 6.2
     background: <boolean> // Optional
   } 
)
```

## Command Fields

The command takes the following fields:

## Behavior

### Performance

The :dbcommand:`validate` command can be slow, particularly on larger data sets.

The :dbcommand:`validate` command obtains an exclusive lock `W` on the collection. This will block all reads and writes on the collection until the operation finishes. When run on a secondary, the :dbcommand:`validate` operation can block all other operations on that secondary until it finishes.

> **Warning:** Due to the performance impact of validation, consider running
:dbcommand:`validate` only on `secondary` replica set nodes.
You can use :method:`rs.stepDown()` to instruct the current
`primary` node to become a secondary to avoid impacting a live
primary node.

### Data Throughput Metrics

.. include:: /includes/extracts/4.4-validate-data-throughput.rst

### Collection Validation Improvements

.. include:: /includes/validate-improvements-introduction.rst

### Restrictions

The :dbcommand:`validate` command no longer supports `afterClusterTime <afterClusterTime>`. As such, :dbcommand:`validate` cannot be associated with `causally consistent sessions <causal-consistency>`.

Time series collections were introduced in MongoDB 5.0. Starting in v5.2, the default internal format for storing time series measurements changed. Due to this change:

- Time series collections created before v5.2 might contain documents in both the
old and new format. Internally, such collections are flagged as `timeseriesBucketsMayHaveMixedSchemaData: true`.

- Time series collections created in v5.2 or later will always contain documents
in the new format. Internally, such collections are flagged as `timeseriesBucketsMayHaveMixedSchemaData: false` or not flagged at all.

When the flag is `true`, time series queries take both the new and the old format into account. When the flag is `false` or missing, time series queries take only the new format into account.

Due to a bug described in [SERVER-91194](https://jira.mongodb.org/browse/SERVER-91194), under some conditions the flag might be lost. When this happens for time series collections created before v5.2, read query results may be incomplete. That is, some documents may be missed, even though they are still stored on the disk.

To determine if you are impacted by this, run :dbcommand:`validate` on your time series collection. The command returns an error if the collection is affected by the bug. Your read query results may be incorrect if this is the case.

If affected, upgrade to a fixed version and set `timeseriesBucketsMayHaveMixedSchemaData` to `true` for each affected collection to ensure that future queries on the collection return correct results. The full steps for this process are located [here](https://github.com/mongodb/support-tools/tree/master/timeseries-mixed-schema).

### Index Key Format

Starting in MongoDB 6.0, the `validate` command returns a message if a `unique index <index-type-unique>` has a key format that is incompatible. The message indicates an old format is used.

### Count and Data Size Statistics

The :dbcommand:`validate` command updates the collection's count and data size statistics in the :dbcommand:`collStats` `output <collStats-output>` with their correct values.

> **Note:** In the event of an :ref:`unclean shutdown
<estimated-document-count-unclean-shutdown>`, the count and data size
statistics might be inaccurate.

## Examples

- To validate a collection `myCollection` using the default validation
setting (specifically, `full: false <cmd-validate-full>`):

```javascript
  db.runCommand( { validate: "myCollection" } )
```

- To perform a full validation of collection `myCollection`, specify
`full: true <cmd-validate-full>`:

```javascript
  db.runCommand( { validate: "myCollection", full: true } )
```

- To repair collection `myCollection`, specify
`repair: true <cmd-validate-repair>`:

```javascript
 db.runCommand( { validate: "myCollection", repair: true } )
```

- To validate the metadata in the `myCollection` collection,
specify `metadata: true <cmd-validate-metadata>`:

```javascript
 db.runCommand( { validate: "myCollection", metadata: true } )
```

- To perform additional BSON conformance checks in `myCollection`,
specify `checkBSONConformance: true <cmd-validate-checkBSONConformance>`:

```javascript
 db.runCommand( { validate: "myCollection", checkBSONConformance: true } )
```

## Validate Output

.. include:: /includes/note-output-may-vary.rst

Specify `full: true <cmd-validate-full>` for more detailed output.
