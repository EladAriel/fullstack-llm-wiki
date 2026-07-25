---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.configureQueryAnalyzer.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================================================

# db.collection.configureQueryAnalyzer() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The method has the following syntax:

```javascript
db.collection.configureQueryAnalyzer( 
   {
     mode: <string>,
     samplesPerSecond: <double>
   } 
)
```

### Fields

|CQA| has the following fields:

## Access Control

For details, see `configureQueryAnalyzer Access Control <cqa-access-control>`.

## Behavior

For behavior, see `configureQueryAnalyzer Behavior <cqa-behavior>`.

## Output

For details, see `configureQueryAnalyzer Output <cqa-output>`.

## Examples

For examples, see `configureQueryAnalyzer Examples <cqa-examples>`.

## Learn More

- :dbcommand:`analyzeShardKey`
- :dbcommand:`configureQueryAnalyzer`
- :pipeline:`$listSampledQueries`
