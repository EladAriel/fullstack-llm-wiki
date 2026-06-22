---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.configureQueryAnalyzer.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
