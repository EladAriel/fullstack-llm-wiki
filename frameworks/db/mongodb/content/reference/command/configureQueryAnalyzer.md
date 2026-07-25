---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/configureQueryAnalyzer.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=========================================

# configureQueryAnalyzer (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   {
     configureQueryAnalyzer: <string>,
     mode: <string>,
     samplesPerSecond: <double>
   } 
)
```

### Command Fields

|CQA| has the following fields:

## Access Control

|CQA| requires one of the following roles:

- :authrole:`dbAdmin` role against the database that contains the
collection being analyzed

- :authrole:`clusterManager` role against the cluster
## Behavior

Consider the following behavior when running |CQA|:

.. include:: /includes/cqa-behavior-colls.rst

### Conversion to Sharded Cluster

.. include:: /includes/fact-convert-shard-query-analysis.rst

.. include:: /includes/cqa-samplesPerSecond-limit.rst

.. include:: /includes/cqa-queryAnalysisSampleExpirationSecs.rst

.. include:: /includes/cqa-currentOp.rst

### View Sampled Queries

To see sampled queries for all collections or a specific collection, use the :pipeline:`$listSampledQueries` aggregation stage.

To see the count of every command type captured by the query analyzer, use:

When you have enough samples, you can disable the query analyzer.

### Limitations

.. include:: /includes/cqa-limitations.rst

## Output

.. include:: /includes/cqa-output.rst

## Examples

### Enable Query Sampling

To enable query sampling on the `test.students` collection at a rate of five samples per second, use the following command:

```javascript
db.adminCommand(
   {
     configureQueryAnalyzer: "test.students",
     mode: "full",
     samplesPerSecond: 5
   } 
)
```

### Disable Query Sampling

To disable query sampling on the `test.students` collection, use the following command:

```javascript
db.adminCommand(
   {
     configureQueryAnalyzer: "test.students",
     mode: "off"
   } 
)
```

## Learn More

- :method:`db.collection.configureQueryAnalyzer()`
- :ref:`currentOp Query Sampling Metrics
<currentOp-agg-query-sampling-fields>`

- :pipeline:`$listSampledQueries`
